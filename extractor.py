# extractor.py

from openpyxl import load_workbook
import pandas as pd


def extraer_movimientos(path_excel, config, fecha, division):
    registros = []

    if hasattr(path_excel, "seek"):
        path_excel.seek(0)

    wb = load_workbook(path_excel, data_only=True)
    
    # Debug: mostrar hojas disponibles
    hojas_disponibles = wb.sheetnames
    print(f"[DEBUG] División: {division}")
    print(f"[DEBUG] Hojas disponibles: {hojas_disponibles}")

    for concepto, cfg in config.items():
        try:
            hoja_requerida = cfg["sheet"]
            
            # Verificar si la hoja existe
            if hoja_requerida not in hojas_disponibles:
                print(f"[DEBUG] ERROR: La hoja '{hoja_requerida}' NO existe!")
                raise Exception(f"La hoja '{hoja_requerida}' no existe. Hojas disponibles: {hojas_disponibles}")
            
            ws = wb[hoja_requerida]
            
            # Detectar si es un rango (ej: K10:K13) o una celda simple
            celda = cfg["cell"]
            if ":" in celda:
                # Es un rango, sumar todas las celdas
                valores = []
                for row in ws[celda]:
                    for cell in row:
                        if cell.value is not None:
                            valores.append(float(cell.value))
                valor = sum(valores) if valores else None
            else:
                # Es una celda simple
                valor = ws[celda].value
            
            print(f"[DEBUG] {concepto}: celda {celda} = {valor}")

            # Saltar si el valor es None o 0 (pero NO para inventarios)
            if valor is None or valor == 0:
                # Siempre incluir inventario_inicial e inventario_final aunque sea 0
                if "inventario" not in concepto:
                    continue
                else:
                    valor = 0  # Forzar 0 para inventarios

            # Guardar todo en registro intermedio
            registro = {
                "Division": division,
                "Concepto": concepto,
                "Grupo": cfg.get("grupo", concepto),  # Usar grupo si existe, sino usar concepto
                "Fecha": fecha,
                "Cantidad": abs(float(valor)),  # Valor absoluto
                "Unidad": "TN",
                "IncludeBatch": cfg.get("include_in_batch", True)
            }

            # Solo agregar campos de batch si va incluido
            if cfg.get("include_in_batch", True):
                registro.update({
                    "Bodega": cfg.get("bodega", ""),
                    "Material": cfg.get("material", ""),
                    "Tipo Movimiento": cfg.get("tipo_mov", ""),
                    "Movimiento": cfg.get("movimiento", ""),
                })
            else:
                # Para registros que no van al batch, poner valores vacíos
                registro.update({
                    "Bodega": "",
                    "Material": "",
                    "Tipo Movimiento": "",
                    "Movimiento": "",
                })

            registros.append(registro)
        except Exception as e:
            raise Exception(f"Error en concepto '{concepto}' (hoja: {cfg.get('sheet')}, celda: {cfg.get('cell')}): {str(e)}")

    return pd.DataFrame(registros)

    return pd.DataFrame(registros)


def extraer_siregad(path_excel):
    """
    Extrae datos de la hoja 'Batch completo' del archivo SIREGAD
    """
    if hasattr(path_excel, "seek"):
        path_excel.seek(0)
    
    try:
        # Leer la hoja "Batch completo"
        df = pd.read_excel(path_excel, sheet_name="Batch completo")
        
        # Columnas relevantes (ajustar según estructura real)
        columnas_relevantes = [
            "Número Factura", "Id. Bodega", "SQC CAS/Nombre Mezcla", 
            "Concentración (0,00000)", "Ingreso/Egreso", "Tipo de Movimiento",
            "Cantidad", "Unidad Medida", "Expediente Comunicación Anticipada",
            "Rut", "Nombre"
        ]
        
        # Filtrar solo las columnas que existen
        columnas_disponibles = [col for col in columnas_relevantes if col in df.columns]
        
        if columnas_disponibles:
            df_filtrado = df[columnas_disponibles].copy()
        else:
            df_filtrado = df.copy()
        
        # Eliminar filas completamente vacías
        df_filtrado = df_filtrado.dropna(how='all')
        
        return df_filtrado
    
    except Exception as e:
        raise Exception(f"Error al extraer SIREGAD: {str(e)}")
