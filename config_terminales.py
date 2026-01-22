# config_terminales.py
# Configuración de movimientos desde terminales hacia divisiones

# TERMINAL TERQUIM - Movimientos de traspaso a divisiones
CONFIG_TERMINAL_TERQUIM = {
    "inventario_inicial": {
        "sheet": "Traspasos",  # Nombre de la hoja en el Excel
        "cell": "B5",  # Celda con inventario inicial
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "TERQ",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    "recepcion_total": {
        "sheet": "Traspasos",
        "cell": "B8",  # Ácido recibido en terminal
        "tipo_mov": "TIPB",  # Traspaso entre plantas/bodegas
        "movimiento": "I",
        "bodega": "TERQ",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "recepcion_terquim"
    },
    "traspaso_rt": {
        "sheet": "Traspasos",
        "cell": "B10",  # Según tu imagen: 3.128,580
        "tipo_mov": "TIEB",  # Traspaso entre bodegas
        "movimiento": "E",
        "bodega": "TERQ",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "traspaso_rt"
    },
    "traspaso_dgm": {
        "sheet": "Traspasos",
        "cell": "B11",  # Según tu imagen: 60.648,952
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "TERQ",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "traspaso_dgm"
    },
    "traspaso_dch": {
        "sheet": "Traspasos",
        "cell": "B12",  # Según tu imagen: 472,170
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "TERQ",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "traspaso_dch"
    },
    "traspaso_dsal": {
        "sheet": "Traspasos",
        "cell": "B13",  # Según tu imagen: 0,000
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "TERQ",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "traspaso_dsal",
        "include_if_zero": True  # Incluir aunque sea 0
    },
    "traspaso_dmh": {
        "sheet": "Traspasos",
        "cell": "B14",  # Según tu imagen: 0,000
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "TERQ",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "traspaso_dmh",
        "include_if_zero": True
    },
    "inventario_final": {
        "sheet": "Traspasos",
        "cell": "B20",
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "TERQ",
        "material": "7664-93-9",
        "include_in_batch": False
    }
}

# TERMINAL 2 (ejemplo si tienes más terminales)
CONFIG_TERMINAL_2 = {
    "inventario_inicial": {
        "sheet": "Terminal2",
        "cell": "C5",
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "TER2",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    # ... agregar movimientos según necesites
}

# TERMINAL 3 (ejemplo)
CONFIG_TERMINAL_3 = {
    "inventario_inicial": {
        "sheet": "Terminal3",
        "cell": "D5",
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "TER3",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    # ... agregar movimientos según necesites
}
