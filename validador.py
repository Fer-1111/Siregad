# validator.py
#agregar formula

def validar_inventario(df):
    inv_inicial = df[df["Concepto"] == "inventario_inicial"]["Cantidad"].sum()
    ingresos = df[df["Tipo Movimiento"] == "MPRO"]["Cantidad"].sum()
    egresos = df[df["Tipo Movimiento"].isin(["VENT", "ECIP"])]["Cantidad"].sum()

    inv_final = inv_inicial + ingresos - egresos

    return {
        "inventario_inicial": inv_inicial,
        "inventario_final_calculado": inv_final,
        "cuadra": inv_final >= 0
    }
