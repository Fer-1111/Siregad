# validator.py


def validar_inventario(df):
    # Agrupar por división
    resultados = []
    
    for division in df["Division"].unique():
        df_div = df[df["Division"] == division]
        
        inv_inicial = df_div[df_div["Concepto"].str.contains("inventario_inicial", na=False)]["Cantidad"].sum()
        ingresos = df_div[df_div["Tipo Movimiento"].isin(["MPRO", "TIEB"])]["Cantidad"].sum()
        egresos = df_div[df_div["Tipo Movimiento"].isin(["VENT", "ECIP", "EDEV", "TIEB"])]["Cantidad"].sum()
        
        # Para TIEB: si es I suma, si es E resta
        tieb_ingresos = df_div[(df_div["Tipo Movimiento"] == "TIEB") & (df_div["Movimiento"] == "I")]["Cantidad"].sum()
        tieb_egresos = df_div[(df_div["Tipo Movimiento"] == "TIEB") & (df_div["Movimiento"] == "E")]["Cantidad"].sum()
        
        inv_final = inv_inicial + ingresos - egresos + tieb_ingresos

        resultados.append({
            "division": division,
            "inventario_inicial": inv_inicial,
            "ingresos": ingresos,
            "egresos": egresos,
            "inventario_final_calculado": inv_final,
            "cuadra": inv_final >= 0,
        })
    
    # Validación global
    cuadra_todo = all(r["cuadra"] for r in resultados)
    
    return {
        "por_division": resultados,
        "cuadra": cuadra_todo
    }
