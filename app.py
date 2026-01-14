import io
from datetime import date

import streamlit as st
import pandas as pd

from batch_writer import escribir_batch
# Barquito es opcional: si el archivo de config está desactualizado, evitamos que la app falle
try:
    from config import CONFIG_POTRERILLOS, CONFIG_CALETONES, CONFIG_TBA, CONFIG_SAN_ANTONIO, CONFIG_RT, CONFIG_CHUQUICAMATA, CONFIG_DMH, CONFIG_BARQUITO
except ImportError:
    from config import CONFIG_POTRERILLOS, CONFIG_CALETONES, CONFIG_TBA, CONFIG_SAN_ANTONIO, CONFIG_RT, CONFIG_CHUQUICAMATA, CONFIG_DMH
    CONFIG_BARQUITO = {}
from extractor import extraer_movimientos, extraer_siregad
from validator import validar_inventario

st.set_page_config(
    page_title="Carga SIREGAD",
    page_icon="📦",
    layout="wide",
)

st.title("📦 Generador Batch SIREGAD")

# Mapeo de palabras clave en nombres de archivo a configuraciones
DIVISIONES_CONFIG = {
    "Potrerillos": CONFIG_POTRERILLOS,
    "Caletones": CONFIG_CALETONES,
    "TBA": CONFIG_TBA,
    "San Antonio": CONFIG_SAN_ANTONIO,
    "Radomiro Tomic": CONFIG_RT,
    "Chuquicamata": CONFIG_CHUQUICAMATA,
    "Ministro Hales": CONFIG_DMH,
    "Barquito": CONFIG_BARQUITO,
}

# Mapeo de palabras clave para detectar división en nombre de archivo
# IMPORTANTE: El orden importa - las más específicas deben ir primero
KEYWORDS_DIVISION = {
    "san antonio": "San Antonio",    # Más específico
    "sanantonio": "San Antonio",
    "rt -": "Radomiro Tomic",        # Más específico que solo "rt"
    "dmh": "Ministro Hales",         # Antes de "dch" para evitar conflictos
    "dch": "Chuquicamata",
    "salvador": "Salvador",
    "potrerillos": "Potrerillos",
    "potre": "Potrerillos",
    "caletones": "Caletones",
    "calet": "Caletones",
    "calpo": "Caletones",
    "teca": "Caletones",
    "tba": "TBA",
    "tbape": "TBA",
    "chuquicamata": "Chuquicamata",
    "chuqui": "Chuquicamata",
    "radomiro": "Radomiro Tomic",
    "tomic": "Radomiro Tomic",
    "rt": "Radomiro Tomic",
    "gabriela": "Gabriela Mistral",
    "mistral": "Gabriela Mistral",
    "ministro": "Ministro Hales",
    "hales": "Ministro Hales",
    "ventana": "Ventana",
    "barquito": "Barquito",
    "tas": "Barquito",
}

# Nota: Caletones, TBA y San Antonio usan el mismo Excel (hoja "Balance") con columnas diferentes


def detectar_division(nombre_archivo):
    """Detecta la división basándose en el nombre del archivo"""
    nombre_lower = nombre_archivo.lower()
    for keyword, division in KEYWORDS_DIVISION.items():
        if keyword in nombre_lower:
            return division
    return None


fecha = st.date_input(
    "Fecha de los movimientos",
    value=date.today(),
)

st.subheader("📂 Paso 1: Cargar Balances de Divisiones")

# Mostrar convenciones de nombres
with st.expander("ℹ️ Convención de nombres de archivos", expanded=False):
    st.markdown("""
    **El nombre del archivo debe contener una de estas palabras clave:**
    
    - `Salvador` o `SALPO` → División Salvador
    - `Potrerillos` o `Potre` → División Potrerillos  
    - `Caletones` o `CALPO` o `TECA` → División Caletones
    - `TBA` o `TBAPE` → División TBA
    - `Chuquicamata` o `Chuqui` → División Chuquicamata
    - `Radomiro` o `Tomic` → División Radomiro Tomic
    - `Gabriela` o `Mistral` → División Gabriela Mistral
    - `Ministro` o `Hales` → División Ministro Hales
    - `Ventana` → División Ventana
    """)

# Cargar múltiples archivos a la vez
archivos = st.file_uploader(
    "Sube todos los Excel de las divisiones",
    type=["xlsx"],
    accept_multiple_files=True,
    key="balances"
)

st.subheader("📋 Paso 2: Cargar Respaldo SIREGAD (Opcional)")

archivo_siregad = st.file_uploader(
    "Sube el archivo SIREGAD Noviembre para auditoría",
    type=["xlsx"],
    key="siregad"
)

# Botón para procesar
if st.button("🚀 Cargar y Procesar", type="primary", use_container_width=True):
    if not archivos:
        st.error("Por favor sube al menos un archivo de Balance")
        st.stop()
    # Mostrar archivos detectados
    st.subheader("📋 Archivos cargados")
    archivos_por_division = {}
    
    for archivo in archivos:
        division = detectar_division(archivo.name)
        if division:
            # Si es Caletones, agregar también TBA y San Antonio (mismo Excel, diferentes columnas)
            if division == "Caletones":
                archivos_por_division["Caletones"] = archivo
                archivos_por_division["TBA"] = archivo
                archivos_por_division["San Antonio"] = archivo
                st.success(f"✅ {archivo.name} → **Caletones, TBA y San Antonio**")
            else:
                archivos_por_division[division] = archivo
                st.success(f"✅ {archivo.name} → **{division}**")
        else:
            st.warning(f"⚠️ {archivo.name} → No se pudo detectar la división")
    
    if not archivos_por_division:
        st.error("No se detectó ninguna división. Verifica los nombres de los archivos.")
        st.stop()
    
    # Extraer datos de todas las divisiones
    todos_los_datos = []
    
    with st.spinner("Leyendo archivos…"):
        for division, archivo in archivos_por_division.items():
            try:
                config = DIVISIONES_CONFIG.get(division)
                if not config:
                    st.warning(f"No hay configuración para {division}")
                    continue
                    
                df = extraer_movimientos(
                    archivo,
                    config,
                    fecha,
                    division
                )
                if not df.empty:
                    todos_los_datos.append(df)
            except Exception as exc:
                st.error(f"Error en {division} ({archivo.name}): {exc}")
                import traceback
                st.code(traceback.format_exc())
    
    # Combinar todos los DataFrames
    df_completo = pd.concat(todos_los_datos, ignore_index=True)
    
    if df_completo.empty:
        st.warning("No se encontraron movimientos en los archivos.")
        st.stop()

    st.subheader("📊 Datos extraídos")
    st.dataframe(df_completo, use_container_width=True)
    
    # Cargar SIREGAD si se proporcionó
    df_siregad = None
    if archivo_siregad:
        try:
            with st.spinner("Leyendo respaldo SIREGAD…"):
                df_siregad = extraer_siregad(archivo_siregad)
            st.success(f"✅ Respaldo SIREGAD cargado: {len(df_siregad)} registros")
        except Exception as exc:
            st.warning(f"⚠️ No se pudo leer el respaldo SIREGAD: {exc}")
            import traceback
            st.code(traceback.format_exc())
    
    # Botón para descargar Excel intermedio con formato
    from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
    
    buffer_intermedio = io.BytesIO()
    
    with pd.ExcelWriter(buffer_intermedio, engine='openpyxl') as writer:
        # Crear la hoja "Datos" una sola vez
        df_dummy = pd.DataFrame()
        df_dummy.to_excel(writer, sheet_name='Datos', index=False)
        ws = writer.sheets['Datos']
        
        row_actual = 1
        
        # Colores por división
        colores_division = {
            "Salvador": "FFFF99",      # Amarillo
            "Caletones": "FFA500",     # Naranja
            "Potrerillos": "90EE90",   # Verde claro
            "TBA": "87CEEB",           # Azul cielo
            "San Antonio": "F0E68C",   # Caqui
            "Chuquicamata": "DDA0DD",  # Púrpura claro
            "Radomiro Tomic": "FFB6C1", # Rosa
            "Gabriela Mistral": "D8BFD8", # Lavanda
            "Ministro Hales": "98FB98" # Verde pálido
        }
        
        # Header de columnas
        columnas = ["Número Factura", "Id. Bodega", "SQC CAS/Nombre Mezcla", "Concentración", 
                   "Ingreso/Egreso", "Tipo de Movimiento", "Cantidad", "Unidad Medida", "Fecha"]
        
        for division in df_completo["Division"].unique():
            df_div = df_completo[df_completo["Division"] == division].copy()
            
            # Calcular totales simplificados
            inv_inicial = df_div[df_div["Concepto"].str.contains("inventario_inicial", na=False)]["Cantidad"].sum()
            ingresos_total = df_div[df_div["Movimiento"] == "I"]["Cantidad"].sum()
            egresos_total = df_div[df_div["Movimiento"] == "E"]["Cantidad"].sum()
            inv_final_calculado = inv_inicial + ingresos_total - egresos_total
            
            # Extraer el inventario final del Excel
            inv_final_extraido = df_div[df_div["Concepto"].str.contains("inventario_final", na=False)]["Cantidad"].sum()
            
            # Calcular diferencia
            diferencia = inv_final_extraido - inv_final_calculado
            
            color = colores_division.get(division, "FFFFFF")
            
            # ===== HEADER DE DIVISIÓN =====
            ws.merge_cells(f'A{row_actual}:I{row_actual}')
            cell_header = ws[f'A{row_actual}']
            cell_header.value = division.upper()
            cell_header.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
            cell_header.font = Font(bold=True, size=12)
            cell_header.alignment = Alignment(horizontal="left", vertical="center")
            
            # Agregar INV INICIAL en la misma fila a la derecha
            ws.merge_cells(f'J{row_actual}:K{row_actual}')
            cell_inv_ini_label = ws[f'J{row_actual}']
            cell_inv_ini_label.value = "INV INICIAL"
            cell_inv_ini_label.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
            cell_inv_ini_label.font = Font(bold=True)
            cell_inv_ini_label.alignment = Alignment(horizontal="right")
            
            ws.merge_cells(f'L{row_actual}:M{row_actual}')
            cell_inv_ini_valor = ws[f'L{row_actual}']
            cell_inv_ini_valor.value = inv_inicial
            cell_inv_ini_valor.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
            cell_inv_ini_valor.font = Font(bold=True)
            cell_inv_ini_valor.alignment = Alignment(horizontal="right")
            cell_inv_ini_valor.number_format = '#,##0.000'
            
            row_actual += 1
            
            # ===== HEADER DE COLUMNAS =====
            for col_idx, col_name in enumerate(columnas, 1):
                cell = ws.cell(row=row_actual, column=col_idx)
                cell.value = col_name
                cell.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
                cell.font = Font(bold=True, color="FFFFFF")
                cell.alignment = Alignment(horizontal="center", wrap_text=True)
            
            row_actual += 1
            
            # ===== DATOS DE MOVIMIENTOS =====
            df_batch = df_div[df_div["IncludeBatch"] == True].copy()
            
            # Agrupar por "Grupo" (suma celdas con mismo grupo), sumando las cantidades
            df_batch_agrupado = df_batch.groupby("Grupo", as_index=False).agg({
                "Cantidad": "sum",
                "Bodega": "first",
                "Material": "first",
                "Tipo Movimiento": "first",
                "Movimiento": "first",
                "Unidad": "first"
            }).copy()
            
            for idx, row in df_batch_agrupado.iterrows():
                ws.cell(row=row_actual, column=1).value = row.get("Grupo", "")
                ws.cell(row=row_actual, column=2).value = row.get("Bodega", "")
                ws.cell(row=row_actual, column=3).value = row.get("Material", "")
                ws.cell(row=row_actual, column=4).value = "Ácido Sulfúrico (Conc: 96)"
                ws.cell(row=row_actual, column=5).value = row.get("Movimiento", "")
                ws.cell(row=row_actual, column=6).value = row.get("Tipo Movimiento", "")
                ws.cell(row=row_actual, column=7).value = row.get("Cantidad", 0)
                ws.cell(row=row_actual, column=8).value = row.get("Unidad", "TN")
                ws.cell(row=row_actual, column=9).value = fecha
                
                # Aplicar color
                for col in range(1, 10):
                    cell = ws.cell(row=row_actual, column=col)
                    cell.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
                    if col == 7:
                        cell.number_format = '#,##0.000'
                
                row_actual += 1
            
            # ===== FOOTER INV FINAL =====
            ws.merge_cells(f'A{row_actual}:I{row_actual}')
            cell_footer = ws[f'A{row_actual}']
            cell_footer.value = ""
            cell_footer.fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            
            # INV FINAL CALCULADO
            ws.merge_cells(f'J{row_actual}:K{row_actual}')
            cell_inv_calc_label = ws[f'J{row_actual}']
            cell_inv_calc_label.value = "INV FINAL (CALCULADO)"
            cell_inv_calc_label.fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            cell_inv_calc_label.font = Font(bold=True)
            cell_inv_calc_label.alignment = Alignment(horizontal="right")
            
            ws.merge_cells(f'L{row_actual}:M{row_actual}')
            cell_inv_calc_valor = ws[f'L{row_actual}']
            cell_inv_calc_valor.value = inv_final_calculado
            cell_inv_calc_valor.fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            cell_inv_calc_valor.font = Font(bold=True)
            cell_inv_calc_valor.alignment = Alignment(horizontal="right")
            cell_inv_calc_valor.number_format = '#,##0.000'
            
            # INV FINAL EXTRAIDO
            ws.merge_cells(f'N{row_actual}:O{row_actual}')
            cell_inv_ext_label = ws[f'N{row_actual}']
            cell_inv_ext_label.value = "INV FINAL (EXTRAÍDO)"
            cell_inv_ext_label.fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            cell_inv_ext_label.font = Font(bold=True)
            cell_inv_ext_label.alignment = Alignment(horizontal="right")
            
            ws.merge_cells(f'P{row_actual}:Q{row_actual}')
            cell_inv_ext_valor = ws[f'P{row_actual}']
            cell_inv_ext_valor.value = inv_final_extraido
            cell_inv_ext_valor.fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            cell_inv_ext_valor.font = Font(bold=True)
            cell_inv_ext_valor.alignment = Alignment(horizontal="right")
            cell_inv_ext_valor.number_format = '#,##0.000'
            
            # DIFERENCIA
            ws.merge_cells(f'R{row_actual}:S{row_actual}')
            cell_dif_label = ws[f'R{row_actual}']
            cell_dif_label.value = "DIFERENCIA"
            cell_dif_label.fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            cell_dif_label.font = Font(bold=True)
            cell_dif_label.alignment = Alignment(horizontal="right")
            
            ws.merge_cells(f'T{row_actual}:U{row_actual}')
            cell_dif_valor = ws[f'T{row_actual}']
            cell_dif_valor.value = diferencia
            # Color rojo si hay diferencia, verde si cuadra
            color_dif = "FF0000" if abs(diferencia) > 0.001 else "00B050"  # Rojo si diferencia, verde si cuadra
            cell_dif_valor.fill = PatternFill(start_color=color_dif, end_color=color_dif, fill_type="solid")
            cell_dif_valor.font = Font(bold=True, color="FFFFFF")
            cell_dif_valor.alignment = Alignment(horizontal="right")
            cell_dif_valor.number_format = '#,##0.000'
            
            row_actual += 3  # Espacio entre divisiones
        
        # Ajustar anchos de columna
        ws = writer.sheets['Datos']
        anchos = [20, 15, 15, 25, 15, 20, 15, 15, 15]
        for col_idx, ancho in enumerate(anchos, 1):
            ws.column_dimensions[get_column_letter(col_idx)].width = ancho
        
        # Agregar pestaña de respaldo SIREGAD si se proporcionó
        if df_siregad is not None and not df_siregad.empty:
            df_siregad.to_excel(writer, sheet_name='Respaldo SIREGAD', index=False)
            ws_respaldo = writer.sheets['Respaldo SIREGAD']
            
            # Formatear headers
            for col_idx in range(1, len(df_siregad.columns) + 1):
                cell = ws_respaldo.cell(row=1, column=col_idx)
                cell.fill = PatternFill(start_color="D3D3D3", end_color="D3D3D3", fill_type="solid")
                cell.font = Font(bold=True)
                cell.alignment = Alignment(horizontal="center", wrap_text=True)
            
            # Ajustar anchos
            for col_idx in range(1, len(df_siregad.columns) + 1):
                ws_respaldo.column_dimensions[get_column_letter(col_idx)].width = 18
    
    buffer_intermedio.seek(0)
    
    st.download_button(
        "📥 Descargar Excel Intermedio",
        buffer_intermedio,
        file_name=f"Intermedio_SIREGAD_{fecha}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    # Validación
    validacion = validar_inventario(df_completo)

    st.subheader("🔎 Validación por División")
    for resultado in validacion["por_division"]:
        with st.expander(f"División: {resultado['division']}", expanded=True):
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Inv. Inicial", f"{resultado['inventario_inicial']:.2f} TN")
            col2.metric("Ingresos", f"{resultado['ingresos']:.2f} TN")
            col3.metric("Egresos", f"{resultado['egresos']:.2f} TN")
            col4.metric("Inv. Final", f"{resultado['inventario_final_calculado']:.2f} TN")
            
            if resultado["cuadra"]:
                st.success("✅ Inventario válido")
            else:
                st.error("❌ Inventario NO cuadra")

    if not validacion["cuadra"]:
        st.error("❌ Hay divisiones con inventario negativo. Revisa los datos.")
        st.stop()

    # Generar Batch SIREGAD
    if st.button("🚀 Generar Batch SIREGAD"):
        # Filtrar solo registros que van al batch
        df_batch = df_completo[df_completo["IncludeBatch"] == True].copy()
        
        if df_batch.empty:
            st.warning("No hay registros para incluir en el batch.")
            st.stop()
        
        buffer = io.BytesIO()

        try:
            escribir_batch(
                df_batch,
                "templates/PlantillaCargaInventarioBatch_CODELCO.xlsx",
                buffer,
            )
        except FileNotFoundError:
            st.error("No se encontró la plantilla en templates/PlantillaCargaInventarioBatch_CODELCO.xlsx")
            st.stop()
        except Exception as exc:
            st.error(f"No se pudo generar el batch: {exc}")
            st.stop()

        st.download_button(
            "📥 Descargar Batch SIREGAD",
            buffer,
            file_name=f"Batch_SIREGAD_{fecha}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
