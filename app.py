import io
from datetime import date

import streamlit as st
import pandas as pd

from batch_writer import escribir_batch
# Barquito es opcional: si el archivo de config está desactualizado, evitamos que la app falle
try:
    from config import CONFIG_POTRERILLOS, CONFIG_CALETONES, CONFIG_TBA, CONFIG_SAN_ANTONIO, CONFIG_RT, CONFIG_CHUQUICAMATA, CONFIG_DMH, CONFIG_BARQUITO, CONFIG_DGM
except ImportError:
    from config import CONFIG_POTRERILLOS, CONFIG_CALETONES, CONFIG_TBA, CONFIG_SAN_ANTONIO, CONFIG_RT, CONFIG_CHUQUICAMATA, CONFIG_DMH
    CONFIG_BARQUITO = {}
    CONFIG_DGM = {}
from config_programacion import COLUMNA_MES, MES_ALIAS, DIVISION_A_GRUPO_PROGRA, TOLERANCIA_DIFERENCIA
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
    "Gabriela Mistral": CONFIG_DGM,
}

# Mapeo de palabras clave para detectar división en nombre de archivo
# IMPORTANTE: El orden importa - las más específicas deben ir primero
KEYWORDS_DIVISION = {
    "san antonio": "San Antonio",    # Más específico
    "sanantonio": "San Antonio",
    "rt -": "Radomiro Tomic",        # Más específico que solo "rt"
    "dgm": "Gabriela Mistral",       # DGM = Gabriela Mistral
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
    - `Barquito` o `TAS` → División Barquito
    - `DGM` → División Gabriela Mistral
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

# ===== PASO 2.5: IMPORTAR FACTURAS DESDE EXCEL CM =====
st.subheader("📑 Paso 2.5: Importar Facturas CM (Ventas/Compras)")

with st.expander("📤 Importar desde Excel Casa Matriz (CM)", expanded=False):
    st.markdown("""
    **Este importador lee el Excel de CM con las hojas:**
    - **Ventas**: Egresos (VENT, CL) - columnas I-U con formato batch
    - **Compras**: Ingresos (CL, IM) - columnas I-U con formato batch
    
    Las columnas I-U deben tener: `Número Fact | Id. Bodega | SQC CAS | Concentración | Ingreso/Egreso | Tipo de Mov | Cantidad | Unidad Med | Expediente | Rut | Nombre`
    """)
    
    archivo_cm = st.file_uploader(
        "Sube Excel de Casa Matriz (con hojas Ventas y Compras)",
        type=["xlsx"],
        key="cm_import"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        importar_ventas = st.checkbox("Importar Ventas (Egresos)", value=True)
    with col2:
        importar_compras = st.checkbox("Importar Compras (Ingresos)", value=True)
    
    # División para los datos importados
    division_cm = st.selectbox(
        "División para estos datos",
        ["San Antonio", "Ministro Hales"],
        key="div_cm",
        help="CM = Casa Matriz, puede ser San Antonio o Ministro Hales"
    )
    
    if archivo_cm and st.button("📥 Importar desde CM"):
        try:
            import openpyxl
            wb = openpyxl.load_workbook(archivo_cm, data_only=True)
            hojas_disponibles = wb.sheetnames
            st.write(f"📋 Hojas encontradas: {hojas_disponibles}")
            
            registros_importados = []
            
            # Función para leer hoja con formato CM
            def leer_hoja_cm(wb, nombre_hoja, division):
                registros = []
                if nombre_hoja not in wb.sheetnames:
                    st.warning(f"⚠️ Hoja '{nombre_hoja}' no encontrada")
                    return registros
                
                ws = wb[nombre_hoja]
                
                # Las columnas I-U contienen los datos del batch (columnas 9-21)
                # I=9: Número Fact, J=10: Id. Bodega, K=11: SQC CAS, L=12: Concentración
                # M=13: Ingreso/Egreso, N=14: Tipo de Mov, O=15: Cantidad, P=16: Unidad Med
                # Q=17: Expediente, R=18: Rut, S=19: Nombre
                
                for row in range(2, ws.max_row + 1):  # Empezar desde fila 2 (saltando header)
                    num_factura = ws.cell(row=row, column=9).value  # Columna I
                    cantidad = ws.cell(row=row, column=15).value    # Columna O
                    
                    # Convertir cantidad a número
                    try:
                        cantidad_num = float(str(cantidad).replace(",", ".").replace(" ", "")) if cantidad else 0
                    except:
                        cantidad_num = 0
                    
                    # Solo importar si hay factura y cantidad > 0
                    if num_factura and cantidad_num > 0:
                        registro = {
                            "Division": division,
                            "Concepto": str(num_factura),
                            "Grupo": str(num_factura),
                            "Bodega": ws.cell(row=row, column=10).value or "CM",  # J
                            "Material": ws.cell(row=row, column=11).value or "7664-93-9",  # K
                            "Concentracion": ws.cell(row=row, column=12).value or "Ácido Sulfúrico (Conc: 96)",  # L
                            "Movimiento": ws.cell(row=row, column=13).value or "",  # M (I/E)
                            "Tipo Movimiento": ws.cell(row=row, column=14).value or "",  # N
                            "Cantidad": cantidad_num,
                            "Unidad": ws.cell(row=row, column=16).value or "TN",  # P
                            "Expediente": ws.cell(row=row, column=17).value or "",  # Q
                            "Rut": ws.cell(row=row, column=18).value or "",  # R
                            "Nombre": ws.cell(row=row, column=19).value or "",  # S
                            "IncludeBatch": True,
                            "Fecha": fecha,
                        }
                        registros.append(registro)
                
                return registros
            
            # Importar Ventas (Egresos)
            if importar_ventas:
                ventas = leer_hoja_cm(wb, "Ventas", division_cm)
                if ventas:
                    registros_importados.extend(ventas)
                    st.success(f"✅ Ventas: {len(ventas)} registros importados")
            
            # Importar Compras (Ingresos)
            if importar_compras:
                compras = leer_hoja_cm(wb, "Compras", division_cm)
                if compras:
                    registros_importados.extend(compras)
                    st.success(f"✅ Compras: {len(compras)} registros importados")
            
            wb.close()
            
            if registros_importados:
                # Guardar en session_state
                if "facturas_importadas" not in st.session_state:
                    st.session_state.facturas_importadas = []
                
                st.session_state.facturas_importadas.extend(registros_importados)
                
                # Mostrar resumen
                df_preview = pd.DataFrame(registros_importados)
                st.write("**📊 Resumen de importación:**")
                resumen = df_preview.groupby(["Tipo Movimiento", "Movimiento"]).agg({
                    "Cantidad": ["count", "sum"]
                }).reset_index()
                resumen.columns = ["Tipo Mov", "I/E", "Registros", "Total TN"]
                st.dataframe(resumen, use_container_width=True)
                
                st.rerun()
            else:
                st.warning("No se encontraron registros válidos para importar.")
                
        except Exception as e:
            st.error(f"Error al importar: {e}")
            import traceback
            st.code(traceback.format_exc())

# Mostrar facturas importadas
if "facturas_importadas" in st.session_state and st.session_state.facturas_importadas:
    st.write(f"**📑 Facturas/Movimientos importados: {len(st.session_state.facturas_importadas)} registros**")
    
    # Resumen por división y tipo
    df_resumen = pd.DataFrame(st.session_state.facturas_importadas)
    resumen = df_resumen.groupby(["Division", "Tipo Movimiento", "Movimiento"]).agg({
        "Cantidad": ["count", "sum"]
    }).reset_index()
    resumen.columns = ["División", "Tipo Mov", "I/E", "Registros", "Total TN"]
    st.dataframe(resumen, use_container_width=True)
    
    if st.button("🗑️ Limpiar facturas importadas"):
        st.session_state.facturas_importadas = []
        st.rerun()

# ===== PASO 2.6: CUADRE CON PROGRAMACIÓN =====
st.subheader("📊 Paso 2.6: Cuadre con Programación AS 2025")

with st.expander("🔍 Validar datos vs Programación", expanded=False):
    st.markdown("""
    **Este módulo compara los datos extraídos de las divisiones con el Excel de Programación AS 2025.**
    
    📌 **Correspondencias:**
    - **Salvador (SALV)** → Potrerillos + Barquito
    - **Teniente (TTE)** → Caletones + TBA + San Antonio  
    - **DMH** → Ministro Hales
    - **Chuqui** → Chuquicamata + RT + GM
    """)
    
    archivo_progra = st.file_uploader(
        "Sube el Excel PROGRAMACIÓN AS 2025",
        type=["xlsx"],
        key="progra_import"
    )
    
    # Seleccionar mes a comparar
    mes_progra = st.selectbox(
        "Mes a comparar",
        ["noviembre", "octubre", "septiembre", "agosto", "julio", "junio", 
         "mayo", "abril", "marzo", "febrero", "enero", "diciembre"],
        key="mes_progra"
    )
    
    if archivo_progra and st.button("📊 Extraer y Comparar"):
        try:
            import openpyxl
            wb_progra = openpyxl.load_workbook(archivo_progra, data_only=True)
            hojas = wb_progra.sheetnames
            st.write(f"📋 Hojas encontradas: {hojas}")
            
            col_mes = COLUMNA_MES.get(mes_progra.lower(), 12)  # Default noviembre
            
            datos_progra = {}
            
            # ========== EXTRAER DATOS DE HOJA "Cuadrar" ==========
            if "Cuadrar" in hojas:
                ws_cuadrar = wb_progra["Cuadrar"]
                
                # Salvador (filas aproximadas basadas en la imagen)
                datos_progra["Salvador"] = {
                    "produccion": ws_cuadrar.cell(row=17, column=col_mes).value or 0,
                    "consumo_interno": ws_cuadrar.cell(row=18, column=col_mes).value or 0,
                    "consumo_lixiviacion": ws_cuadrar.cell(row=19, column=col_mes).value or 0,
                    "consumo_refineria": ws_cuadrar.cell(row=20, column=col_mes).value or 0,
                    "otros": ws_cuadrar.cell(row=21, column=col_mes).value or 0,
                }
                
                # Teniente/Caletones (filas 34-44)
                datos_progra["Teniente"] = {
                    "saldo_inicial": ws_cuadrar.cell(row=35, column=col_mes).value or 0,
                    "produccion": ws_cuadrar.cell(row=36, column=col_mes).value or 0,
                    "consumo_interno": ws_cuadrar.cell(row=38, column=col_mes).value or 0,
                    "entregas_caletones": ws_cuadrar.cell(row=39, column=col_mes).value or 0,
                    "despachos_los_lirios": ws_cuadrar.cell(row=40, column=col_mes).value or 0,
                    "ajuste_inventario": ws_cuadrar.cell(row=43, column=col_mes).value or 0,
                    "saldo_final": ws_cuadrar.cell(row=44, column=col_mes).value or 0,
                }
                
                # Los Lirios (filas 47-55)
                datos_progra["Los_Lirios"] = {
                    "saldo_inicial": ws_cuadrar.cell(row=48, column=col_mes).value or 0,
                    "recepcion": ws_cuadrar.cell(row=49, column=col_mes).value or 0,
                    "entregas": ws_cuadrar.cell(row=51, column=col_mes).value or 0,
                    "despachos_terquim": ws_cuadrar.cell(row=52, column=col_mes).value or 0,
                    "ajuste": ws_cuadrar.cell(row=54, column=col_mes).value or 0,
                    "saldo_final": ws_cuadrar.cell(row=55, column=col_mes).value or 0,
                }
                
                # Terquim San Antonio (filas 57-65)
                datos_progra["Terquim_SA"] = {
                    "saldo_inicial": ws_cuadrar.cell(row=58, column=col_mes).value or 0,
                    "recepcion_los_lirios": ws_cuadrar.cell(row=59, column=col_mes).value or 0,
                    "recepcion_caletones": ws_cuadrar.cell(row=60, column=col_mes).value or 0,
                    "despachos": ws_cuadrar.cell(row=62, column=col_mes).value or 0,
                    "ajuste": ws_cuadrar.cell(row=64, column=col_mes).value or 0,
                    "saldo_final": ws_cuadrar.cell(row=65, column=col_mes).value or 0,
                }
            
            wb_progra.close()
            
            # Guardar datos extraídos en session_state
            st.session_state.datos_progra = datos_progra
            st.session_state.mes_progra = mes_progra
            
            # Mostrar datos extraídos
            st.success(f"✅ Datos de Programación extraídos para {mes_progra.upper()}")
            
            for grupo, valores in datos_progra.items():
                with st.expander(f"📁 {grupo}", expanded=True):
                    df_grupo = pd.DataFrame([
                        {"Concepto": k.replace("_", " ").title(), "Valor (TN)": v}
                        for k, v in valores.items() if v != 0
                    ])
                    st.dataframe(df_grupo, use_container_width=True)
            
        except Exception as e:
            st.error(f"Error al extraer datos de Programación: {e}")
            import traceback
            st.code(traceback.format_exc())

# Mostrar comparación si hay datos de ambas fuentes
if "datos_progra" in st.session_state and "df_completo" in st.session_state:
    st.write("---")
    st.subheader("📈 Comparación: Programación vs Divisiones")
    
    df_completo = st.session_state.df_completo
    datos_progra = st.session_state.datos_progra
    
    # Agregar datos de divisiones por grupo
    comparaciones = []
    
    # Salvador = Potrerillos + Barquito
    if "Salvador" in datos_progra:
        df_salvador = df_completo[df_completo["Division"].isin(["Potrerillos", "Barquito"])]
        prod_div = df_salvador[df_salvador["Tipo Movimiento"] == "MPRO"]["Cantidad"].sum()
        
        comparaciones.append({
            "Grupo": "Salvador",
            "Concepto": "Producción",
            "Programación": datos_progra["Salvador"].get("produccion", 0),
            "Divisiones": prod_div,
        })
    
    # Teniente = Caletones + TBA + San Antonio
    if "Teniente" in datos_progra:
        df_teniente = df_completo[df_completo["Division"].isin(["Caletones", "TBA", "San Antonio"])]
        
        prod_div = df_teniente[df_teniente["Tipo Movimiento"] == "MPRO"]["Cantidad"].sum()
        comparaciones.append({
            "Grupo": "Teniente",
            "Concepto": "Producción",
            "Programación": datos_progra["Teniente"].get("produccion", 0),
            "Divisiones": prod_div,
        })
        
        # TIEB (entregas internas)
        tieb_div = df_teniente[df_teniente["Tipo Movimiento"] == "TIEB"]["Cantidad"].sum()
        comparaciones.append({
            "Grupo": "Teniente",
            "Concepto": "Entregas TIEB",
            "Programación": datos_progra["Teniente"].get("despachos_los_lirios", 0),
            "Divisiones": tieb_div,
        })
    
    if comparaciones:
        df_comp = pd.DataFrame(comparaciones)
        df_comp["Diferencia"] = df_comp["Programación"] - df_comp["Divisiones"]
        df_comp["Estado"] = df_comp["Diferencia"].apply(
            lambda x: "✅" if abs(x) <= TOLERANCIA_DIFERENCIA else ("⚠️" if abs(x) <= 10 else "❌")
        )
        
        st.dataframe(
            df_comp.style.applymap(
                lambda x: "background-color: #90EE90" if x == "✅" else 
                         ("background-color: #FFD700" if x == "⚠️" else 
                          ("background-color: #FF6B6B" if x == "❌" else "")),
                subset=["Estado"]
            ),
            use_container_width=True
        )
    else:
        st.info("No hay datos suficientes para comparar. Procesa los archivos de Balance primero.")

# ===== PASO 3: AJUSTES MANUALES POR DIVISIÓN =====
st.subheader("🔧 Paso 3: Ajustes Manuales (Opcional)")

# Lista de divisiones disponibles para ajustes
DIVISIONES_AJUSTES = ["Salvador", "Caletones", "TBA", "San Antonio", "Potrerillos", "Chuquicamata", 
                      "Radomiro Tomic", "Gabriela Mistral", "Ministro Hales", "Barquito"]

# Códigos de bodega por división
BODEGAS_DIVISION = {
    "Salvador": "SALVA",
    "Caletones": "TECA",
    "TBA": "TETBA", 
    "San Antonio": "CM",
    "Potrerillos": "SALPO",
    "Chuquicamata": "CH",
    "Radomiro Tomic": "RT",
    "Gabriela Mistral": "DGM",
    "Ministro Hales": "CM",
    "Barquito": "BARQUITO",
}

# Tipos de movimiento disponibles
TIPOS_MOVIMIENTO = ["MDEV", "EDEV", "MPRO", "ECIP", "TIEB", "TIPB", "VENT", "AJUSTE"]

# Inicializar lista de ajustes en session_state
if "ajustes_manuales" not in st.session_state:
    st.session_state.ajustes_manuales = []

with st.expander("➕ Agregar Ajuste Manual", expanded=False):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        ajuste_division = st.selectbox("División", DIVISIONES_AJUSTES, key="ajuste_div")
        ajuste_bodega = st.text_input("Id. Bodega", value=BODEGAS_DIVISION.get(DIVISIONES_AJUSTES[0], ""), key="ajuste_bodega")
        ajuste_rut = st.text_input("Rut", value="61.704.000-K", key="ajuste_rut")
    
    with col2:
        ajuste_num_factura = st.text_input("Número Factura", key="ajuste_factura")
        ajuste_tipo_mov = st.selectbox("Tipo Movimiento", TIPOS_MOVIMIENTO, key="ajuste_tipo")
        ajuste_nombre = st.text_input("Nombre", value="Corporación Nacional del Cobre de Chile (Codelco)", key="ajuste_nombre")
    
    with col3:
        ajuste_movimiento = st.selectbox("Ingreso/Egreso", ["I", "E"], key="ajuste_ie")
        ajuste_cantidad = st.number_input("Cantidad (TN)", min_value=0.0, step=0.001, format="%.3f", key="ajuste_cant")
        ajuste_expediente = st.text_input("Expediente Com. Anticipada", key="ajuste_expediente")
    
    with col4:
        ajuste_material = st.text_input("SQC CAS/Nombre Mezcla", value="7664-93-9", key="ajuste_material")
        ajuste_concentracion = st.text_input("Concentración", value="Ácido Sulfúrico (Conc: 96)", key="ajuste_conc")
        ajuste_unidad = st.selectbox("Unidad Medida", ["TN", "KG", "LT"], key="ajuste_unidad")
    
    if st.button("➕ Agregar Ajuste"):
        if ajuste_cantidad > 0:
            mes_nombre = fecha.strftime("%b").upper()  # NOV, DIC, etc.
            nuevo_ajuste = {
                "Division": ajuste_division,
                "Concepto": ajuste_num_factura if ajuste_num_factura else f"K.{ajuste_movimiento}.Ajuste.{mes_nombre}",
                "Grupo": ajuste_num_factura if ajuste_num_factura else f"ajuste_{ajuste_division.lower()}_{len(st.session_state.ajustes_manuales)}",
                "Fecha": fecha,
                "Cantidad": ajuste_cantidad,
                "Unidad": ajuste_unidad,
                "IncludeBatch": True,
                "Bodega": ajuste_bodega if ajuste_bodega else BODEGAS_DIVISION.get(ajuste_division, ""),
                "Material": ajuste_material,
                "Tipo Movimiento": ajuste_tipo_mov,
                "Movimiento": ajuste_movimiento,
                "Concentracion": ajuste_concentracion,
                "Expediente": ajuste_expediente,
                "Rut": ajuste_rut,
                "Nombre": ajuste_nombre,
            }
            st.session_state.ajustes_manuales.append(nuevo_ajuste)
            
            # Si ya se procesaron datos, actualizar df_completo con el nuevo ajuste
            if "df_base" in st.session_state and st.session_state.df_base is not None:
                df_ajustes = pd.DataFrame(st.session_state.ajustes_manuales)
                if st.session_state.df_base.empty:
                    st.session_state.df_completo = df_ajustes.copy()
                else:
                    st.session_state.df_completo = pd.concat([st.session_state.df_base, df_ajustes], ignore_index=True)
            
            st.success(f"✅ Ajuste agregado: {ajuste_division} - {ajuste_tipo_mov} {ajuste_movimiento} {ajuste_cantidad} TN")
            st.rerun()

# Mostrar ajustes agregados
if st.session_state.ajustes_manuales:
    st.write("**Ajustes agregados:**")
    for i, ajuste in enumerate(st.session_state.ajustes_manuales):
        col1, col2 = st.columns([4, 1])
        with col1:
            factura_txt = f"[{ajuste.get('Concepto', '')}] " if ajuste.get('Concepto') else ""
            st.write(f"• {ajuste['Division']}: {factura_txt}{ajuste['Tipo Movimiento']} {ajuste['Movimiento']} {ajuste['Cantidad']:.3f} {ajuste.get('Unidad', 'TN')} - {ajuste.get('Rut', '')} {ajuste.get('Nombre', '')[:30]}...")
        with col2:
            if st.button("🗑️", key=f"del_ajuste_{i}"):
                st.session_state.ajustes_manuales.pop(i)
                # También actualizar df_completo al eliminar
                if "df_base" in st.session_state and st.session_state.df_base is not None:
                    if st.session_state.ajustes_manuales:
                        df_ajustes = pd.DataFrame(st.session_state.ajustes_manuales)
                        st.session_state.df_completo = pd.concat([st.session_state.df_base, df_ajustes], ignore_index=True)
                    else:
                        st.session_state.df_completo = st.session_state.df_base.copy()
                st.rerun()
    
    if st.button("🗑️ Limpiar todos los ajustes"):
        st.session_state.ajustes_manuales = []
        if "df_base" in st.session_state and st.session_state.df_base is not None:
            st.session_state.df_completo = st.session_state.df_base.copy()
        st.rerun()
    
    # Mensaje informativo
    if "df_base" in st.session_state:
        st.info("💡 Los ajustes se actualizarán automáticamente en los datos procesados.")

# Verificar si hay facturas importadas
facturas_importadas = st.session_state.get("facturas_importadas", [])

# Botón para procesar
if st.button("🚀 Cargar y Procesar", type="primary", use_container_width=True):
    # Verificar que haya archivos O ajustes manuales O facturas importadas
    if not archivos and not st.session_state.ajustes_manuales and not facturas_importadas:
        st.error("Por favor sube al menos un archivo de Balance, agrega ajustes manuales o importa facturas")
        st.stop()
    
    todos_los_datos = []
    
    # Procesar archivos si existen
    if archivos:
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
            if not st.session_state.ajustes_manuales:
                st.stop()
            else:
                st.info("📝 Continuando solo con ajustes manuales...")
        
        # Extraer datos de todas las divisiones
        with st.spinner("Leyendo archivos…"):
            for division, archivo in archivos_por_division.items():
                try:
                    config = DIVISIONES_CONFIG.get(division)
                    if not config:
                        st.warning(f"⚠️ No hay configuración para {division}")
                        continue
                    
                    st.info(f"🔍 Procesando {division} desde {archivo.name}...")
                        
                    df = extraer_movimientos(
                        archivo,
                        config,
                        fecha,
                        division
                    )
                    if not df.empty:
                        todos_los_datos.append(df)
                        st.success(f"✅ {division}: {len(df)} registros extraídos")
                    else:
                        st.warning(f"⚠️ {division}: No se encontraron datos (celdas vacías o con valor 0)")
                except Exception as exc:
                    st.error(f"❌ Error en {division} ({archivo.name}): {exc}")
                    import traceback
                    st.code(traceback.format_exc())
    else:
        if st.session_state.ajustes_manuales or facturas_importadas:
            st.info("📝 Procesando solo con ajustes manuales/facturas importadas (sin archivos de Balance)")
    
    # Combinar todos los DataFrames (puede estar vacío si solo hay ajustes)
    if todos_los_datos:
        df_completo = pd.concat(todos_los_datos, ignore_index=True)
    else:
        df_completo = pd.DataFrame()
    
    # Guardar el DataFrame base (sin ajustes ni facturas) en session_state
    st.session_state.df_base = df_completo.copy() if not df_completo.empty else pd.DataFrame()
    
    # Agregar facturas importadas si existen
    if facturas_importadas:
        df_facturas = pd.DataFrame(facturas_importadas)
        if df_completo.empty:
            df_completo = df_facturas.copy()
        else:
            df_completo = pd.concat([df_completo, df_facturas], ignore_index=True)
        st.info(f"📑 Se agregaron {len(facturas_importadas)} factura(s) importada(s)")
    
    # Agregar ajustes manuales si existen
    if st.session_state.ajustes_manuales:
        df_ajustes = pd.DataFrame(st.session_state.ajustes_manuales)
        if df_completo.empty:
            df_completo = df_ajustes.copy()
        else:
            df_completo = pd.concat([df_completo, df_ajustes], ignore_index=True)
        st.info(f"📝 Se agregaron {len(st.session_state.ajustes_manuales)} ajuste(s) manual(es)")
    
    # Guardar df_completo con ajustes en session_state para persistencia
    st.session_state.df_completo = df_completo.copy()
    
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
    from config import RUT_EMPRESAS
    
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
            "Ministro Hales": "98FB98", # Verde pálido
            "Barquito": "ADD8E6",      # Azul claro
        }
        
        # Header de columnas según formato SIREGAD
        columnas = ["dd-mm-aaaa", "Número Factura", "Id. Bodega", "SQC CAS/Nombre Mezcla", 
                   "Concentración (0,00000)", "Ingreso/Egreso", "Tipo de Movimiento", "Cantidad", 
                   "Unidad Medida", "Expediente Comunicación Anticipada", "Rut", "Nombre"]
        
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
            # Escribir valores ANTES de fusionar
            cell_header = ws[f'A{row_actual}']
            cell_header.value = division.upper()
            cell_header.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
            cell_header.font = Font(bold=True, size=12)
            cell_header.alignment = Alignment(horizontal="left", vertical="center")
            ws.merge_cells(f'A{row_actual}:I{row_actual}')
            
            # Agregar INV INICIAL en la misma fila a la derecha
            cell_inv_ini_label = ws[f'J{row_actual}']
            cell_inv_ini_label.value = "INV INICIAL"
            cell_inv_ini_label.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
            cell_inv_ini_label.font = Font(bold=True)
            cell_inv_ini_label.alignment = Alignment(horizontal="right")
            ws.merge_cells(f'J{row_actual}:K{row_actual}')
            
            cell_inv_ini_valor = ws[f'L{row_actual}']
            cell_inv_ini_valor.value = inv_inicial
            cell_inv_ini_valor.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
            cell_inv_ini_valor.font = Font(bold=True)
            cell_inv_ini_valor.alignment = Alignment(horizontal="right")
            cell_inv_ini_valor.number_format = '#,##0.000'
            ws.merge_cells(f'L{row_actual}:M{row_actual}')
            
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
            # Forzar conversión de IncludeBatch a booleano
            df_div["IncludeBatch"] = df_div["IncludeBatch"].astype(bool)
            df_batch = df_div[df_div["IncludeBatch"] == True].copy()
            
            # Agrupar por "Grupo" (suma celdas con mismo grupo), sumando las cantidades
            # Primero asegurar que existan las columnas adicionales
            for col in ["Concentracion", "Expediente", "Rut", "Nombre"]:
                if col not in df_batch.columns:
                    df_batch[col] = ""
            
            df_batch_agrupado = df_batch.groupby("Grupo", as_index=False).agg({
                "Cantidad": "sum",
                "Bodega": "first",
                "Material": "first",
                "Tipo Movimiento": "first",
                "Movimiento": "first",
                "Unidad": "first",
                "Concentracion": "first",
                "Expediente": "first",
                "Rut": "first",
                "Nombre": "first"
            }).copy()
            
            for idx, row in df_batch_agrupado.iterrows():
                # Columna 1: dd-mm-aaaa (Fecha)
                ws.cell(row=row_actual, column=1).value = fecha
                # Columna 2: Número Factura
                ws.cell(row=row_actual, column=2).value = row.get("Grupo", "")
                # Columna 3: Id. Bodega
                ws.cell(row=row_actual, column=3).value = row.get("Bodega", "")
                # Columna 4: SQC CAS/Nombre Mezcla
                ws.cell(row=row_actual, column=4).value = row.get("Material", "")
                # Columna 5: Concentración (0,00000)
                conc = row.get("Concentracion", "")
                ws.cell(row=row_actual, column=5).value = conc if conc else "Ácido Sulfúrico (Conc: 96)"
                # Columna 6: Ingreso/Egreso
                ws.cell(row=row_actual, column=6).value = row.get("Movimiento", "")
                # Columna 7: Tipo de Movimiento
                ws.cell(row=row_actual, column=7).value = row.get("Tipo Movimiento", "")
                # Columna 8: Cantidad
                ws.cell(row=row_actual, column=8).value = row.get("Cantidad", 0)
                # Columna 9: Unidad Medida
                ws.cell(row=row_actual, column=9).value = row.get("Unidad", "TN")
                # Columna 10: Expediente Comunicación Anticipada
                ws.cell(row=row_actual, column=10).value = row.get("Expediente", "")
                # Columna 11: Rut
                rut = row.get("Rut", "")
                ws.cell(row=row_actual, column=11).value = rut if rut else "61.704.000-K"
                # Columna 12: Nombre
                nombre = row.get("Nombre", "")
                ws.cell(row=row_actual, column=12).value = nombre if nombre else "Corporación Nacional del Cobre de Chile (Codelco)"
                
                # Aplicar color a todas las columnas
                for col in range(1, 13):
                    cell = ws.cell(row=row_actual, column=col)
                    cell.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
                    if col == 8:  # Cantidad
                        cell.number_format = '#,##0.000'
                    if col == 1:  # Fecha
                        cell.number_format = 'DD-MM-YYYY'
                
                row_actual += 1
            
            # ===== FOOTER INV FINAL (en una nueva fila) =====
            # Primero escribir valores, luego fusionar
            
            # INV FINAL CALCULADO - Label
            cell_inv_calc_label = ws[f'A{row_actual}']
            cell_inv_calc_label.value = "INV FINAL (CALCULADO)"
            cell_inv_calc_label.fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            cell_inv_calc_label.font = Font(bold=True)
            cell_inv_calc_label.alignment = Alignment(horizontal="right")
            ws.merge_cells(f'A{row_actual}:B{row_actual}')
            
            # INV FINAL CALCULADO - Valor
            cell_inv_calc_valor = ws[f'C{row_actual}']
            cell_inv_calc_valor.value = inv_final_calculado
            cell_inv_calc_valor.fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            cell_inv_calc_valor.font = Font(bold=True)
            cell_inv_calc_valor.alignment = Alignment(horizontal="right")
            cell_inv_calc_valor.number_format = '#,##0.000'
            ws.merge_cells(f'C{row_actual}:D{row_actual}')
            
            # INV FINAL EXTRAIDO - Label
            cell_inv_ext_label = ws[f'E{row_actual}']
            cell_inv_ext_label.value = "INV FINAL (EXTRAÍDO)"
            cell_inv_ext_label.fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            cell_inv_ext_label.font = Font(bold=True)
            cell_inv_ext_label.alignment = Alignment(horizontal="right")
            ws.merge_cells(f'E{row_actual}:F{row_actual}')
            
            # INV FINAL EXTRAIDO - Valor
            cell_inv_ext_valor = ws[f'G{row_actual}']
            cell_inv_ext_valor.value = inv_final_extraido
            cell_inv_ext_valor.fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            cell_inv_ext_valor.font = Font(bold=True)
            cell_inv_ext_valor.alignment = Alignment(horizontal="right")
            cell_inv_ext_valor.number_format = '#,##0.000'
            ws.merge_cells(f'G{row_actual}:H{row_actual}')
            
            # DIFERENCIA - Label
            cell_dif_label = ws[f'I{row_actual}']
            cell_dif_label.value = "DIFERENCIA"
            cell_dif_label.fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            cell_dif_label.font = Font(bold=True)
            cell_dif_label.alignment = Alignment(horizontal="right")
            
            # DIFERENCIA - Valor
            cell_dif_valor = ws[f'J{row_actual}']
            cell_dif_valor.value = diferencia
            # Color rojo si hay diferencia, verde si cuadra
            color_dif = "FF0000" if abs(diferencia) > 0.001 else "00B050"
            cell_dif_valor.fill = PatternFill(start_color=color_dif, end_color=color_dif, fill_type="solid")
            cell_dif_valor.font = Font(bold=True, color="FFFFFF")
            cell_dif_valor.alignment = Alignment(horizontal="right")
            cell_dif_valor.number_format = '#,##0.000'
            ws.merge_cells(f'J{row_actual}:L{row_actual}')
            
            row_actual += 3  # Espacio entre divisiones
        
        # Ajustar anchos de columna
        ws = writer.sheets['Datos']
        # Anchos: Fecha, Nº Factura, Bodega, CAS, Concentración, I/E, Tipo Mov, Cantidad, Unidad, Expediente, Rut, Nombre
        anchos = [12, 18, 12, 15, 25, 12, 18, 12, 12, 30, 15, 50]
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

# =================== SECCIÓN DE VISUALIZACIÓN PERSISTENTE ===================
# Esta sección muestra los datos procesados incluso después de agregar ajustes manuales
# (cuando el botón "Cargar y Procesar" no fue presionado pero ya hay datos en session_state)

elif "df_completo" in st.session_state and st.session_state.df_completo is not None and not st.session_state.df_completo.empty:
    df_completo = st.session_state.df_completo
    
    st.subheader("📊 Datos extraídos (guardados)")
    
    if st.session_state.ajustes_manuales:
        st.info(f"📝 Incluye {len(st.session_state.ajustes_manuales)} ajuste(s) manual(es)")
    
    st.dataframe(df_completo, use_container_width=True)
    
    # Generar Excel intermedio con los datos actualizados
    from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
    from config import RUT_EMPRESAS
    
    buffer_intermedio = io.BytesIO()
    
    with pd.ExcelWriter(buffer_intermedio, engine='openpyxl') as writer:
        df_dummy = pd.DataFrame()
        df_dummy.to_excel(writer, sheet_name='Datos', index=False)
        ws = writer.sheets['Datos']
        
        row_actual = 1
        
        colores_division = {
            "Salvador": "FFFF99", "Caletones": "FFA500", "Potrerillos": "90EE90",
            "TBA": "87CEEB", "San Antonio": "F0E68C", "Chuquicamata": "DDA0DD",
            "Radomiro Tomic": "FFB6C1", "Gabriela Mistral": "D8BFD8",
            "Ministro Hales": "98FB98", "Barquito": "ADD8E6",
        }
        
        columnas = ["dd-mm-aaaa", "Número Factura", "Id. Bodega", "SQC CAS/Nombre Mezcla", 
                   "Concentración (0,00000)", "Ingreso/Egreso", "Tipo de Movimiento", "Cantidad", 
                   "Unidad Medida", "Expediente Comunicación Anticipada", "Rut", "Nombre"]
        
        for division in df_completo["Division"].unique():
            df_div = df_completo[df_completo["Division"] == division].copy()
            
            inv_inicial = df_div[df_div["Concepto"].str.contains("inventario_inicial", na=False)]["Cantidad"].sum()
            ingresos_total = df_div[df_div["Movimiento"] == "I"]["Cantidad"].sum()
            egresos_total = df_div[df_div["Movimiento"] == "E"]["Cantidad"].sum()
            inv_final_calculado = inv_inicial + ingresos_total - egresos_total
            inv_final_extraido = df_div[df_div["Concepto"].str.contains("inventario_final", na=False)]["Cantidad"].sum()
            
            color = colores_division.get(division, "FFFFFF")
            
            # Header de división
            ws[f'A{row_actual}'] = f"DIVISIÓN: {division.upper()}"
            ws.merge_cells(f'A{row_actual}:L{row_actual}')
            cell = ws[f'A{row_actual}']
            cell.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
            cell.font = Font(bold=True, size=14)
            cell.alignment = Alignment(horizontal="center")
            row_actual += 1
            
            # INV INICIAL
            ws[f'A{row_actual}'] = "INV INICIAL"
            ws[f'A{row_actual}'].fill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
            ws[f'A{row_actual}'].font = Font(bold=True)
            ws.merge_cells(f'A{row_actual}:B{row_actual}')
            ws[f'C{row_actual}'] = inv_inicial
            ws[f'C{row_actual}'].fill = PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid")
            ws[f'C{row_actual}'].font = Font(bold=True)
            ws[f'C{row_actual}'].number_format = '#,##0.000'
            ws.merge_cells(f'C{row_actual}:D{row_actual}')
            row_actual += 1
            
            # Encabezados de columna
            for col_idx, col_name in enumerate(columnas, 1):
                cell = ws.cell(row=row_actual, column=col_idx)
                cell.value = col_name
                cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
                cell.font = Font(bold=True, color="FFFFFF")
                cell.alignment = Alignment(horizontal="center", wrap_text=True)
            row_actual += 1
            
            # Datos de movimientos - forzar conversión de IncludeBatch a booleano
            df_div["IncludeBatch"] = df_div["IncludeBatch"].astype(bool)
            df_batch = df_div[df_div["IncludeBatch"] == True].copy()
            
            for col in ["Concentracion", "Expediente", "Rut", "Nombre"]:
                if col not in df_batch.columns:
                    df_batch[col] = ""
            
            if not df_batch.empty:
                df_batch_agrupado = df_batch.groupby("Grupo", as_index=False).agg({
                    "Cantidad": "sum", "Bodega": "first", "Material": "first",
                    "Tipo Movimiento": "first", "Movimiento": "first", "Unidad": "first",
                    "Concentracion": "first", "Expediente": "first", "Rut": "first", "Nombre": "first"
                }).copy()
                
                for idx, row in df_batch_agrupado.iterrows():
                    ws.cell(row=row_actual, column=1).value = fecha
                    ws.cell(row=row_actual, column=2).value = row.get("Grupo", "")
                    ws.cell(row=row_actual, column=3).value = row.get("Bodega", "")
                    ws.cell(row=row_actual, column=4).value = row.get("Material", "")
                    conc = row.get("Concentracion", "")
                    ws.cell(row=row_actual, column=5).value = conc if conc else "Ácido Sulfúrico (Conc: 96)"
                    ws.cell(row=row_actual, column=6).value = row.get("Movimiento", "")
                    ws.cell(row=row_actual, column=7).value = row.get("Tipo Movimiento", "")
                    ws.cell(row=row_actual, column=8).value = row.get("Cantidad", 0)
                    ws.cell(row=row_actual, column=9).value = row.get("Unidad", "TN")
                    ws.cell(row=row_actual, column=10).value = row.get("Expediente", "")
                    rut = row.get("Rut", "")
                    ws.cell(row=row_actual, column=11).value = rut if rut else "61.704.000-K"
                    nombre = row.get("Nombre", "")
                    ws.cell(row=row_actual, column=12).value = nombre if nombre else "Corporación Nacional del Cobre de Chile (Codelco)"
                    
                    for col in range(1, 13):
                        cell = ws.cell(row=row_actual, column=col)
                        cell.fill = PatternFill(start_color=color, end_color=color, fill_type="solid")
                        if col == 8:
                            cell.number_format = '#,##0.000'
                        if col == 1:
                            cell.number_format = 'DD-MM-YYYY'
                    row_actual += 1
            
            # Footer con inventarios finales
            ws[f'A{row_actual}'] = "INV FINAL (CALCULADO)"
            ws[f'A{row_actual}'].fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            ws[f'A{row_actual}'].font = Font(bold=True)
            ws.merge_cells(f'A{row_actual}:B{row_actual}')
            ws[f'C{row_actual}'] = inv_final_calculado
            ws[f'C{row_actual}'].fill = PatternFill(start_color="FF69B4", end_color="FF69B4", fill_type="solid")
            ws[f'C{row_actual}'].number_format = '#,##0.000'
            ws.merge_cells(f'C{row_actual}:D{row_actual}')
            
            ws[f'E{row_actual}'] = "INV FINAL (EXTRAÍDO)"
            ws[f'E{row_actual}'].fill = PatternFill(start_color="9370DB", end_color="9370DB", fill_type="solid")
            ws[f'E{row_actual}'].font = Font(bold=True)
            ws.merge_cells(f'E{row_actual}:F{row_actual}')
            ws[f'G{row_actual}'] = inv_final_extraido
            ws[f'G{row_actual}'].fill = PatternFill(start_color="9370DB", end_color="9370DB", fill_type="solid")
            ws[f'G{row_actual}'].number_format = '#,##0.000'
            ws.merge_cells(f'G{row_actual}:H{row_actual}')
            row_actual += 2
        
        # Ajustar ancho de columnas
        for col_idx in range(1, 13):
            ws.column_dimensions[get_column_letter(col_idx)].width = 15
    
    buffer_intermedio.seek(0)
    
    st.download_button(
        "📥 Descargar Excel Intermedio (Actualizado)",
        buffer_intermedio,
        file_name=f"Intermedio_SIREGAD_{fecha}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        key="download_intermedio_persistente"
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
        st.warning("⚠️ Hay divisiones con inventario negativo. Revisa los datos.")
    
    # Botón para generar Batch
    if st.button("🚀 Generar Batch SIREGAD", key="btn_batch_persistente"):
        df_batch = df_completo[df_completo["IncludeBatch"] == True].copy()
        
        if df_batch.empty:
            st.warning("No hay registros para incluir en el batch.")
        else:
            buffer = io.BytesIO()
            try:
                escribir_batch(
                    df_batch,
                    "templates/PlantillaCargaInventarioBatch_CODELCO.xlsx",
                    buffer,
                )
                st.download_button(
                    "📥 Descargar Batch SIREGAD",
                    buffer,
                    file_name=f"Batch_SIREGAD_{fecha}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    key="download_batch_persistente"
                )
            except FileNotFoundError:
                st.error("No se encontró la plantilla en templates/PlantillaCargaInventarioBatch_CODELCO.xlsx")
            except Exception as exc:
                st.error(f"No se pudo generar el batch: {exc}")
