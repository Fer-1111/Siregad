# config.py

# Diccionario de RUT y nombres de empresas para movimientos con factura
RUT_EMPRESAS = {
    "61.704.000-K": "Corporación Nacional del Cobre de Chile (Codelco)",
    "93.458.000-1": "CELULOSA ARAUCO Y CONSTITUCION",
    "96.595.400-7": "MINERA VALLE CENTRAL S.A.",
    "78.572.860-2": "QUIMICA DEL SUR Y CIA. LTDA.",
    "76.257.082-3": "Quimicos FAS Spa",
    "78.887.880-K": "ECOKORP LTDA.",
    "76.107.905-0": "MOLYMETNOS S.A.",
    "96.959.620-2": "REDOXI WATER S. A.",
    "79.559.670-4": "PROQUIEL QUIMICOS LIMITADA",
    "87.001.500-3": "QUIMETAL INDUSTRIAL S.A.",
    "78.200.830-7": "Minera Cemin Pullalli SPA",
    "77.737.403-6": "Compañía Minera Tres Valles SpA",
    "77.020.457-7": "Mantoverde S.A.",
    "61.703.000-4": "EMPRESA NACIONAL DE MINERIA",
    "77.867.520-K": "COMERCIAL TRANS SUD LIMITADA",
    "96.701.340-4": "SOC. CONTRACTUAL MINERA EL ABRA",
    "76.255.054-7": "PLANTA RECUPERADORA DE METALES SpA.",
    "77.844.523-9": "AMEROPA MARKETING CHILE SPA",
    "76.079.669-7": "Minera Antucoya",
    "78.378.860-8": "INTERACID TRADING (CHILE) S.A.",
    "76.148.338-2": "Sociedad de Procesamiento de Molibdeno Ltda.",
    "76.821.240-6": "GLENCORE CHILE SPA",
    "ZU5K202": "HEXAGON",
    "77.382.103-8": "HEXAGON CHILE SPA",
}

# Diccionario completo de clientes con RUT (para futuro uso)
RUT_CLIENTES = {
    # Clientes nacionales
    "78.378.860-8": "INTERACID TRADING (CHILE) S.A.",
    "77.382.103-8": "HEXAGON CHILE SPA",
    "76.148.338-2": "Sociedad de Procesamiento de Molibdeno Ltda.",
    "77.020.457-7": "Mantoverde S.A.",
    "77.867.520-K": "COMERCIAL TRANS SUD LIMITADA",
    "96.701.340-4": "SOC. CONTRACTUAL MINERA EL ABRA",
    "77.894.990-3": "ORAFTI CHILE S.A.",
    "76.255.054-7": "PLANTA RECUPERADORA DE METALES SpA.",
    "76.257.082-3": "Quimicos FAS Spa",
    "78.887.880-K": "ECOKORP LTDA.",
    "87.550.600-5": "VINICAS S.A.",
    "79.559.670-4": "PROQUIEL QUIMICOS LIMITADA",
    "93.628.000-5": "MOLIBDENOS Y METALES S.A.",
    "96.510.970-6": "MADERAS ARAUCO S.A.",
    "96.595.400-7": "MINERA VALLE CENTRAL S.A.",
    "78.572.860-2": "QUIMICA DEL SUR Y CIA. LTDA.",
    "99.531.960-8": "SCM MINERA LUMINA COPPER CHILE",
    "93.458.000-1": "CELULOSA ARAUCO Y CONSTITUCION",
    "96.532.330-9": "CMPC PULP SpA",
    "96.731.890-6": "Cartulinas CMPC Spa.",
    "76.051.610-4": "SOCIEDAD CONTRACTUAL MINERA FRANKE",
    "96.790.240-3": "MINERA PELAMBRES",
    "61.703.000-4": "EMPRESA NACIONAL DE MINERIA",
    "76.066.160-0": "Sociedad Comercial y Minera",
    "77.950.280-5": "BHP BILLITON CHILE INVERSIONES LTDA",
    "76.858.530-K": "NORACID S.A.",
    "76.821.240-6": "GLENCORE CHILE SPA",
    "96.959.620-2": "REDOXI WATER S. A.",
    "76.455.066-8": "SA SERVICES CHILE SPA",
    "76.107.905-0": "MOLYMETNOS S.A.",
    "78.200.830-7": "Minera Cemin Pullalli SPA",
    "88.325.800-2": "Complejo Metalúrgico Altonorte S.A.",
    "77.762.940-9": "Anglo American Sur S. A.",
    "77.539.056-5": "COMERCIALIZADORA TRICON DRY CHEMICA",
    "76.079.669-7": "MINERA ANTUCOYA",
    "87.001.500-3": "QUIMETAL INDUSTRIAL S.A.",
    "77.844.523-9": "AMEROPA MARKETING CHILE SPA",
    "77.737.403-6": "Compañía Minera Tres Valles SpA",
    "61.704.000-K": "Corporación Nacional del Cobre de Chile (Codelco)",
    # Clientes internacionales (con código ZU)
    "BO1K302": "Sociedad Industrial Tierra S.A.",
    "ZU3K207": "SAS",
    "ZU5K202": "Hexagon",
    "ZU2K211": "TRAMMO",
    "ZU3K214": "AMEROPA",
    "ZU5K204": "TRICON",
    "ZU3K212": "GLENCORE INTERNATIONAL",
    "ZU5K205": "PAN PACIFIC COPPER CO.LTD",
    "ZU5K401": "GLENCORE INTERNATIONAL AG",
}

# Diccionario inverso: nombre -> RUT
NOMBRE_A_RUT = {v: k for k, v in RUT_CLIENTES.items()}

CONFIG_POTRERILLOS = {
    "inventario_inicial": {
        "sheet": "Dic 2025",
        "cell": "E11",
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "SALPO",
        "material": "7664-93-9"
    },
    "ajuste_tas": {
        "sheet": "Dic 2025",
        "cell": "E25",
        "tipo_mov": "(preguntar)",
        "movimiento": "I",
        "bodega": "SALPO",
        "material": "7664-93-9"
    },
    "ventas": {
        "sheet": "Dic 2025",
        "cell": "E37",
        "tipo_mov": "VENT",
        "movimiento": "E",
        "bodega": "SALPO",
        "material": "7664-93-9"
    },

    # Nuevos movimientos solicitados desde Potrerillos
    "ingreso_neto_almacenes": {
        "sheet": "Dic 2025",
        "cell": "D1",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "include_if_zero": True
    },
    "ingreso_neto_detalle_d14_d17": {
        "sheet": "Dic 2025",
        "cell": "D14:D17",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "include_if_zero": True,
        "grupo": "ingresos_neto"
    },
    "ajuste_tas": {
        "sheet": "Dic 2025",
        "cell": "D25",
        "tipo_mov": "EDEV",
        "movimiento": "E",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "include_if_zero": True
    },
    "consumo_refineria": {
        "sheet": "Noviembre 2025",
        "cell": "D30",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "include_if_zero": True
    },
    "salidas_por_ventas_picking_facturas": {
        "sheet": "Dic 2025",
        "cell": "D28",
        "tipo_mov": "VENT",
        "movimiento": "E",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "include_if_zero": True,
    },
    "salidas_por_ventas_picking_facturas": {
        "sheet": "Dic 2025",
        "cell": "D29",
        "tipo_mov": "VENT",
        "movimiento": "E",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "include_if_zero": True,
    },
    "salidas_por_ventas_picking_facturas": {
        "sheet": "Dic 2025",
        "cell": "D30",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "include_if_zero": True,
    },
    "salidas_por_ventas_picking_facturas": {
        "sheet": "Dic 2025",
        "cell": "D31",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "include_if_zero": False,
    },
    "salidas_por_ventas_picking_facturas": {
        "sheet": "Dic 2025",
        "cell": "D32",
        "tipo_mov": "",
        "movimiento": "E",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "include_if_zero": True,
    },
    "salidas_por_ventas_picking_facturas": {
        "sheet": "Dic 2025",
        "cell": "D33",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "include_if_zero": True,
    },
    "rebaja_por_ventas_consumos": {
        "sheet": "Dic 2025",
        "cell": "D34",
        "tipo_mov": "",
        "movimiento": "E",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "include_if_zero": False
    },
    "consumo_desde_proceso_plantas_gases": {
        "sheet": "Dic 2025",
        "cell": "D36",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "include_if_zero": False
    },
    "inventario_final": {
        "sheet": "Dic 2025",
        "cell": "D37",
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": False,
    },
    "total_libre_disposicion_almacenes_mat_114": {
        "sheet": "Dic 2025",
        "cell": "E52",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "SALPO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "include_if_zero": True,
        "grupo": "total_libre_disposicion"
    }
}

# CALETONES
CONFIG_CALETONES = {

    # 🔹 Inventario inicial (solo referencia, NO se carga al batch)
    "inventario_inicial": {
        "sheet": "Balance",
        "cell": "C6",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": False
    },

    # 🔹 Producción total → I MPRO
    "produccion_total": {
        "sheet": "Balance",
        "cell": "C8",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True
    },

    # 🔹 Ajuste inventario → E EDEV
    "ajuste_inventario": {
        "sheet": "Balance",
        "cell": "C9",
        "tipo_mov": "EDEV",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
     ##ajuste
    "ajuste_prod": {
        "sheet": "Balance",
        "cell": "C11",
        "tipo_mov": "(preguntar)",
        "movimiento": "I",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    # 🔹 Consumo interno (ECIP) - celdas individuales
    "consumo_ecip_c18": {
        "sheet": "Balance",
        "cell": "C18",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "consumo_ecip"
    },
    "consumo_ecip_c19": {
        "sheet": "Balance",
        "cell": "C19",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "consumo_ecip"
    },
    "consumo_ecip_c20": {
        "sheet": "Balance",
        "cell": "C20",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "consumo_ecip"
    },
    "consumo_ecip_c21": {
        "sheet": "Balance",
        "cell": "C21",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "consumo_ecip"
    },
    "consumo_ecip_c22": {
        "sheet": "Balance",
        "cell": "C22",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "consumo_ecip"
    },
    "consumo_ecip_c23": {
        "sheet": "Balance",
        "cell": "C23",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "consumo_ecip"
    },

    # 🔹 Consumo interno a TBA (TIEB) - celdas individuales
    "consumo_tieb_c26": {
        "sheet": "Balance",
        "cell": "C26",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "consumo_tieb"
    },
    "consumo_tieb_c27": {
        "sheet": "Balance",
        "cell": "C27",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "consumo_tieb"
    },
    "consumo_tieb_c28": { ##revisar
        "sheet": "Balance",
        "cell": "C28",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "consumo_tieb"
    },

    "inventario_final": {
        "sheet": "Balance",
        "cell": "C31",
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "",
        "material": "",
        "include_in_batch": False
    }
}

# TBA - Usa columna F en hoja "Balance" del Excel de Caletones
CONFIG_TBA = {
    "inventario_inicial": {
        "sheet": "Balance",
        "cell": "F6",
        "tipo_mov": "", ##TIPB
        "movimiento": "",
        "bodega": "",
        "material": "",
        "include_in_batch": False
    },
    "recibido_tba": {
        "sheet": "Balance",
        "cell": "F8",
        "tipo_mov": "TIPB",
        "movimiento": "I",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "reingreso_tansap": {
        "sheet": "Balance",
        "cell": "F9",
        "tipo_mov": "TIPB (revisar)",
        "movimiento": "I",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "ajuste_inventario": {
        "sheet": "Balance",
        "cell": "F10",
        "tipo_mov": "MDEV(revisar)",
        "movimiento": "I",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    # Entregado F17 a F22 - ETIEB
    "entregado_f17": {
        "sheet": "Balance",
        "cell": "F17",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado"
    },
    "entregado_f18": {
        "sheet": "Balance",
        "cell": "F18",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado"
    },
    "entregado_f19": {
        "sheet": "Balance",
        "cell": "F19",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado"
    },
    "entregado_f20": {
        "sheet": "Balance",
        "cell": "F20",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado"
    },
    "consumo_interno_en_planta": {
        "sheet": "Balance",
        "cell": "F21",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado" ##revisar
    },
    "entregado_f22": {
        "sheet": "Balance",
        "cell": "F22",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado"
    },
    "venta_local": {
        "sheet": "Balance",
        "cell": "F24",
        "tipo_mov": "VENT",
        "movimiento": "E",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "inventario_final": {
        "sheet": "Balance",
        "cell": "F29",
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "",
        "material": "",
        "include_in_batch": False
    }
}

# SAN ANTONIO (Casa Matriz) - Usa columna I en hoja "Balance" del Excel de Caletones
CONFIG_SAN_ANTONIO = {
    "inventario_inicial": {
        "sheet": "Balance",
        "cell": "I6",
        "tipo_mov": "TIEB",
        "movimiento": "I",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    "recibido": {
        "sheet": "Balance",
        "cell": "I8",
        "tipo_mov": "TIPB",
        "movimiento": "I",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "entregado_i17": {
        "sheet": "Balance",
        "cell": "I17",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado"
    },
    "entregado_i18": {
        "sheet": "Balance",
        "cell": "I18",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado"
    },
    "entregado_i19": {
        "sheet": "Balance",
        "cell": "I19",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado"
    },
    "entregado_i20": {
        "sheet": "Balance",
        "cell": "I20",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado"
    },
    "entregado_i21": {
        "sheet": "Balance",
        "cell": "I21",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado"
    },
    "entregado_i22": {
        "sheet": "Balance",
        "cell": "I22",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado"
    },
    "ajuste_inv": {
        "sheet": "Balance",
        "cell": "I27",
        "tipo_mov": "(preguntar)",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "inventario_final": {
        "sheet": "Balance",
        "cell": "I31",
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "",
        "material": "",
        "include_in_batch": False
    }
}

# RT RADOMIRO TOMIC
CONFIG_RT = {
    "inventario_inicial": {
        "sheet": "ÁCIDO (SAP)",
        "cell": "E13",
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    "retiro": {
        "sheet": "ÁCIDO (SAP)",
        "cell": "E29",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "recepcion": {
        "sheet": "ÁCIDO (SAP)",
        "cell": "E24",
        "tipo_mov": "TIPB",
        "movimiento": "I",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "inventario_final": {
        "sheet": "ÁCIDO (SAP)",
        "cell": "E29",
        "tipo_mov": "MPRO",
        "movimiento": "F",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": False
    }
}

# CHUQUICAMATA
CONFIG_CHUQUICAMATA = {
    "inventario_inicial": {
        "sheet": "Balance Acido",
        "cell": "F27",
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "CH",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    "produccion": {
        "sheet": "Balance Acido",
        "cell": "F18",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "CH",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "conacsa_linea_rt": {
        "sheet": "Balance Acido",
        "cell": "K15",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "CH",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "terminal_as": {
        "sheet": "Balance Acido",
        "cell": "K16",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "CH",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "ptmp": {
        "sheet": "Balance Acido",
        "cell": "K17",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "CH",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "salida_k10": {
        "sheet": "Balance Acido",
        "cell": "K10",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "CH",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "salida_ecip"
    },
    "salida_k11": {
        "sheet": "Balance Acido",
        "cell": "K11",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "CH",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "salida_ecip"
    },
    "salida_k12": {
        "sheet": "Balance Acido",
        "cell": "K12",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "CH",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "salida_ecip"
    },
    "salida_k13": {
        "sheet": "Balance Acido",
        "cell": "K13",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "CH",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "salida_ecip"
    },
    "inventario_final": {
        "sheet": "Balance Acido",
        "cell": "K27",
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "CH",
        "material": "7664-93-9",
        "include_in_batch": False
    }
}

# DMH - MINISTRO HALES
CONFIG_DMH = {
    "inventario_inicial": {
        "sheet": "REPORTE VCO",
        "cell": "O36",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    "produccion": {
        "sheet": "REPORTE VCO",
        "cell": "D36",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "despacho_dgm": {
        "sheet": "REPORTE VCO",
        "cell": "F36",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "despacho_dch": {
        "sheet": "REPORTE VCO",
        "cell": "H36",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "despacho_drt": {
        "sheet": "REPORTE VCO",
        "cell": "L36",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "inventario_final": {
        "sheet": "REPORTE VCO",
        "cell": "P36",
        "tipo_mov": "MPRO",
        "movimiento": "F",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": False
    }
}

# BARQUITO O TAS
CONFIG_BARQUITO = {
    # 🔹 Inventario inicial X5 (NO se carga al batch)
    "inventario_inicial": {
        "sheet": "DIC 25",
        "cell": "X5",
        "tipo_mov": "",
        "movimiento": "",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    
    # 🔹 Datos independientes C6 a C36 → I CL (guardar como datos separados, no sumados)
    "dato_c6": {
        "sheet": "DIC 25",
        "cell": "C6",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c7": {
        "sheet": "DIC 25",
        "cell": "C7",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c8": {
        "sheet": "DIC 25",
        "cell": "C8",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c9": {
        "sheet": "DIC 25",
        "cell": "C9",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c10": {
        "sheet": "DIC 25",
        "cell": "C10",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c11": {
        "sheet": "DIC 25",
        "cell": "C11",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c12": {
        "sheet": "DIC 25",
        "cell": "C12",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c13": {
        "sheet": "DIC 25",
        "cell": "C13",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c14": {
        "sheet": "DIC 25",
        "cell": "C14",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c15": {
        "sheet": "DIC 25",
        "cell": "C15",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c16": {
        "sheet": "DIC 25",
        "cell": "C16",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c17": {
        "sheet": "DIC 25",
        "cell": "C17",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c18": {
        "sheet": "DIC 25",
        "cell": "C18",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c19": {
        "sheet": "DIC 25",
        "cell": "C19",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c20": {
        "sheet": "DIC 25",
        "cell": "C20",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c21": {
        "sheet": "DIC 25",
        "cell": "C21",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c22": {
        "sheet": "DIC 25",
        "cell": "C22",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c23": {
        "sheet": "DIC 25",
        "cell": "C23",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c24": {
        "sheet": "DIC 25",
        "cell": "C24",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c25": {
        "sheet": "DIC 25",
        "cell": "C25",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c26": {
        "sheet": "DIC 25",
        "cell": "C26",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c27": {
        "sheet": "DIC 25",
        "cell": "C27",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c28": {
        "sheet": "DIC 25",
        "cell": "C28",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c29": {
        "sheet": "DIC 25",
        "cell": "C29",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c30": {
        "sheet": "DIC 25",
        "cell": "C30",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c31": {
        "sheet": "DIC 25",
        "cell": "C31",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c32": {
        "sheet": "DIC 25",
        "cell": "C32",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c33": {
        "sheet": "DIC 25",
        "cell": "C33",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c34": {
        "sheet": "DIC 25",
        "cell": "C34",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c35": {
        "sheet": "DIC 25",
        "cell": "C35",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c36": {
        "sheet": "DIC 25",
        "cell": "C36",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    # 🔹 Datos independientes D8 a D38 → E CL (guardar con contenido, no sumados)
    "dato_d8_dic25": {
        "sheet": "DIC 25",
        "cell": "D8",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d9_dic25": {
        "sheet": "DIC 25",
        "cell": "D9",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d10_dic25": {
        "sheet": "DIC 25",
        "cell": "D10",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d11_dic25": {
        "sheet": "DIC 25",
        "cell": "D11",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d12_dic25": {
        "sheet": "DIC 25",
        "cell": "D12",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d13_dic25": {
        "sheet": "DIC 25",
        "cell": "D13",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d14_dic25": {
        "sheet": "DIC 25",
        "cell": "D14",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d15_dic25": {
        "sheet": "DIC 25",
        "cell": "D15",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d16_dic25": {
        "sheet": "DIC 25",
        "cell": "D16",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d17_dic25": {
        "sheet": "DIC 25",
        "cell": "D17",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d18_dic25": {
        "sheet": "DIC 25",
        "cell": "D18",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d19_dic25": {
        "sheet": "DIC 25",
        "cell": "D19",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d20_dic25": {
        "sheet": "DIC 25",
        "cell": "D20",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d21_dic25": {
        "sheet": "DIC 25",
        "cell": "D21",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d22_dic25": {
        "sheet": "DIC 25",
        "cell": "D22",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d23_dic25": {
        "sheet": "DIC 25",
        "cell": "D23",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d24_dic25": {
        "sheet": "DIC 25",
        "cell": "D24",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d25_dic25": {
        "sheet": "DIC 25",
        "cell": "D25",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d26_dic25": {
        "sheet": "DIC 25",
        "cell": "D26",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d27_dic25": {
        "sheet": "DIC 25",
        "cell": "D27",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d28_dic25": {
        "sheet": "DIC 25",
        "cell": "D28",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d29_dic25": {
        "sheet": "DIC 25",
        "cell": "D29",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d30_dic25": {
        "sheet": "DIC 25",
        "cell": "D30",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d31_dic25": {
        "sheet": "DIC 25",
        "cell": "D31",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d32_dic25": {
        "sheet": "DIC 25",
        "cell": "D32",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d33_dic25": {
        "sheet": "DIC 25",
        "cell": "D33",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d34_dic25": {
        "sheet": "DIC 25",
        "cell": "D34",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d35_dic25": {
        "sheet": "DIC 25",
        "cell": "D35",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d36_dic25": {
        "sheet": "DIC 25",
        "cell": "D36",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d37_dic25": {
        "sheet": "DIC 25",
        "cell": "D37",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_d38_dic25": {
        "sheet": "DIC 25",
        "cell": "D38",
        "tipo_mov": "CL",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },

    # 🔹 Datos independientes E8 a E38 → I CL (guardar con contenido, no sumados)
    "dato_e8_dic25": {
        "sheet": "DIC 25",
        "cell": "E8",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e9_dic25": {
        "sheet": "DIC 25",
        "cell": "E9",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e10_dic25": {
        "sheet": "DIC 25",
        "cell": "E10",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e11_dic25": {
        "sheet": "DIC 25",
        "cell": "E11",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e12_dic25": {
        "sheet": "DIC 25",
        "cell": "E12",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e13_dic25": {
        "sheet": "DIC 25",
        "cell": "E13",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e14_dic25": {
        "sheet": "DIC 25",
        "cell": "E14",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e15_dic25": {
        "sheet": "DIC 25",
        "cell": "E15",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e16_dic25": {
        "sheet": "DIC 25",
        "cell": "E16",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e17_dic25": {
        "sheet": "DIC 25",
        "cell": "E17",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e18_dic25": {
        "sheet": "DIC 25",
        "cell": "E18",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e19_dic25": {
        "sheet": "DIC 25",
        "cell": "E19",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e20_dic25": {
        "sheet": "DIC 25",
        "cell": "E20",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e21_dic25": {
        "sheet": "DIC 25",
        "cell": "E21",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e22_dic25": {
        "sheet": "DIC 25",
        "cell": "E22",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e23_dic25": {
        "sheet": "DIC 25",
        "cell": "E23",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e24_dic25": {
        "sheet": "DIC 25",
        "cell": "E24",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e25_dic25": {
        "sheet": "DIC 25",
        "cell": "E25",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e26_dic25": {
        "sheet": "DIC 25",
        "cell": "E26",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e27_dic25": {
        "sheet": "DIC 25",
        "cell": "E27",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e28_dic25": {
        "sheet": "DIC 25",
        "cell": "E28",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e29_dic25": {
        "sheet": "DIC 25",
        "cell": "E29",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e30_dic25": {
        "sheet": "DIC 25",
        "cell": "E30",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e31_dic25": {
        "sheet": "DIC 25",
        "cell": "E31",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e32_dic25": {
        "sheet": "DIC 25",
        "cell": "E32",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e33_dic25": {
        "sheet": "DIC 25",
        "cell": "E33",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e34_dic25": {
        "sheet": "DIC 25",
        "cell": "E34",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e35_dic25": {
        "sheet": "DIC 25",
        "cell": "E35",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e36_dic25": {
        "sheet": "DIC 25",
        "cell": "E36",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e37_dic25": {
        "sheet": "DIC 25",
        "cell": "E37",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e38_dic25": {
        "sheet": "DIC 25",
        "cell": "E38",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    
    # 🔹 P41 → E VENT#n42
    "vent_p41": {
        "sheet": "DIC 25",
        "cell": "N42",
        "tipo_mov": "VENT",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    
    # 🔹 P42 → E VENT
    "vent_p42": {
        "sheet": "DIC 25",
        "cell": "N43",
        "tipo_mov": "VENT",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    
    # 🔹 P43 → E TIEB
    "tieb_p43": {
        "sheet": "DIC 25",
        "cell": "N44",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    
    # 🔹 Z41 → I TIPB (si no hay valor, guardar 0,000)
    "recepcion_z41": {
        "sheet": "DIC 25",
        "cell": "Z41",
        "tipo_mov": "TIPB",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "default_value": "0,000"
    },
    
    # 🔹 Inventario final AN 14 (NO se carga al batch)
    "inventario_final": {
        "sheet": "DIC 25",
        "cell": "AP16",
        "tipo_mov": "CL",
        "movimiento": "",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False
    }
}

# DGM - GABRIELA MISTRAL
CONFIG_DGM = {
    # 🔹 Inventario inicial (se obtendrá de otro Excel, por ahora placeholder)
    "inventario_inicial": {
        "sheet": "Acido ",
        "cell": "A1",  # Placeholder - se actualizará cuando se proporcione el Excel
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "DGM",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    
    # 🔹 E41 → I TIPB (Recepción)
    "recepcion_e41": {
        "sheet": "Acido ",
        "cell": "E42",
        "tipo_mov": "TIPB",
        "movimiento": "I",
        "bodega": "DGM",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    
    # 🔹 J41 → E ECIP (Consumo interno)
    "consumo_j41": {
        "sheet": "Acido ",
        "cell": "J42",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "DGM",
        "material": "7664-93-9",
        "include_in_batch": True
    }
}
