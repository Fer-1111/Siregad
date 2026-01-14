# config.py

CONFIG_POTRERILLOS = {
    "inventario_inicial": {
        "sheet": "Noviembre 2025",
        "cell": "E11",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "SALPO",
        "material": "7664-93-9"
    },
    "ventas": {
        "sheet": "Noviembre 2025",
        "cell": "E37",
        "tipo_mov": "VENT",
        "movimiento": "E",
        "bodega": "SALPO",
        "material": "7664-93-9"
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
    "consumo_tieb_c28": {
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
        "tipo_mov": "TIEB",
        "movimiento": "I",
        "bodega": "TETBA",
        "material": "7664-93-9",
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
    "ajuste_inventario": {
        "sheet": "Balance",
        "cell": "F10",
        "tipo_mov": "MDEV",
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
    "entregado_f21": {
        "sheet": "Balance",
        "cell": "F21",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "entregado"
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
    }
}

# RT RADOMIRO TOMIC
CONFIG_RT = {
    "inventario_inicial": {
        "sheet": "ÁCIDO (SAP)",
        "cell": "E13",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    "retiro": {
        "sheet": "ÁCIDO (SAP)",
        "cell": "E27",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "recepcion": {
        "sheet": "ÁCIDO (SAP)",
        "cell": "E22",
        "tipo_mov": "TIPB",
        "movimiento": "I",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "inventario_final": {
        "sheet": "ÁCIDO (SAP)",
        "cell": "E31",
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
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    "produccion": {
        "sheet": "Balance Acido",
        "cell": "F18",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "conacsa_linea_rt": {
        "sheet": "Balance Acido",
        "cell": "K15",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "ptmp": {
        "sheet": "Balance Acido",
        "cell": "K17",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "salida_k10": {
        "sheet": "Balance Acido",
        "cell": "K10",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "salida_ecip"
    },
    "salida_k11": {
        "sheet": "Balance Acido",
        "cell": "K11",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "salida_ecip"
    },
    "salida_k12": {
        "sheet": "Balance Acido",
        "cell": "K12",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "salida_ecip"
    },
    "salida_k13": {
        "sheet": "Balance Acido",
        "cell": "K13",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "salida_ecip"
    },
    "inventario_final": {
        "sheet": "Balance Acido",
        "cell": "K27",
        "tipo_mov": "MPRO",
        "movimiento": "F",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": False
    }
}

# DMH - MINISTRO HALES
CONFIG_DMH = {
    "inventario_inicial": {
        "sheet": "REPORTE VCO",
        "cell": "O35",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "DMH",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    "produccion": {
        "sheet": "REPORTE VCO",
        "cell": "D35",
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "DMH",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "despacho_dgm": {
        "sheet": "REPORTE VCO",
        "cell": "F35",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "DMH",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "despacho_dch": {
        "sheet": "REPORTE VCO",
        "cell": "H35",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "DMH",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "despacho_drt": {
        "sheet": "REPORTE VCO",
        "cell": "L35",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "DMH",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "inventario_final": {
        "sheet": "REPORTE VCO",
        "cell": "P35",
        "tipo_mov": "MPRO",
        "movimiento": "F",
        "bodega": "DMH",
        "material": "7664-93-9",
        "include_in_batch": False
    }
}

# BARQUITO
CONFIG_BARQUITO = {
    "nave_trade": {
        "sheet": "NOV 25",
        "cell": "C37",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    
    # 🔹 Ventas P41 (celda combinada PQRS41) → E VENT
    "vent_p41": {
        "sheet": "NOV 25",
        "cell": "P41",
        "tipo_mov": "VENT",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    # 🔹 Ventas P42 (celda combinada PQRS42) → E VENT (NO SE SUMAN)
    "vent_p42": {
        "sheet": "NOV 25",
        "cell": "P42",
        "tipo_mov": "VENT",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False  # NO SE SUMAN
    },
    # 🔹 Transfer interno P43 (celda combinada PQRS43) → E TIEB
    "tieb_p43": {
        "sheet": "NOV 25",
        "cell": "P43",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    
    # 🔹 CANJES - Despacho AA6 hasta AA36 (no se suman) → I CL
    "canjes_despacho_aa6": {
        "sheet": "NOV 25",
        "cell": "AA6",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,  # NO SE SUMAN
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa7": {
        "sheet": "NOV 25",
        "cell": "AA7",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa8": {
        "sheet": "NOV 25",
        "cell": "AA8",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa9": {
        "sheet": "NOV 25",
        "cell": "AA9",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa10": {
        "sheet": "NOV 25",
        "cell": "AA10",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa11": {
        "sheet": "NOV 25",
        "cell": "AA11",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa12": {
        "sheet": "NOV 25",
        "cell": "AA12",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa13": {
        "sheet": "NOV 25",
        "cell": "AA13",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa14": {
        "sheet": "NOV 25",
        "cell": "AA14",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa15": {
        "sheet": "NOV 25",
        "cell": "AA15",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa16": {
        "sheet": "NOV 25",
        "cell": "AA16",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa17": {
        "sheet": "NOV 25",
        "cell": "AA17",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa18": {
        "sheet": "NOV 25",
        "cell": "AA18",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa19": {
        "sheet": "NOV 25",
        "cell": "AA19",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa20": {
        "sheet": "NOV 25",
        "cell": "AA20",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa21": {
        "sheet": "NOV 25",
        "cell": "AA21",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa22": {
        "sheet": "NOV 25",
        "cell": "AA22",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa23": {
        "sheet": "NOV 25",
        "cell": "AA23",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa24": {
        "sheet": "NOV 25",
        "cell": "AA24",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa25": {
        "sheet": "NOV 25",
        "cell": "AA25",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa26": {
        "sheet": "NOV 25",
        "cell": "AA26",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa27": {
        "sheet": "NOV 25",
        "cell": "AA27",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa28": {
        "sheet": "NOV 25",
        "cell": "AA28",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa29": {
        "sheet": "NOV 25",
        "cell": "AA29",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa30": {
        "sheet": "NOV 25",
        "cell": "AA30",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa31": {
        "sheet": "NOV 25",
        "cell": "AA31",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa32": {
        "sheet": "NOV 25",
        "cell": "AA32",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa33": {
        "sheet": "NOV 25",
        "cell": "AA33",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa34": {
        "sheet": "NOV 25",
        "cell": "AA34",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa35": {
        "sheet": "NOV 25",
        "cell": "AA35",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    "canjes_despacho_aa36": {
        "sheet": "NOV 25",
        "cell": "AA36",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False,
        "grupo": "canjes_despacho"
    },
    
    # 🔹 CANJES - Recepción AB6 hasta AB36 (si no hay nada no se agrega) → I CL
    "canjes_recepcion_ab6": {
        "sheet": "NOV 25",
        "cell": "AB6",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab7": {
        "sheet": "NOV 25",
        "cell": "AB7",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab8": {
        "sheet": "NOV 25",
        "cell": "AB8",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab9": {
        "sheet": "NOV 25",
        "cell": "AB9",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab10": {
        "sheet": "NOV 25",
        "cell": "AB10",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab11": {
        "sheet": "NOV 25",
        "cell": "AB11",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab12": {
        "sheet": "NOV 25",
        "cell": "AB12",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab13": {
        "sheet": "NOV 25",
        "cell": "AB13",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab14": {
        "sheet": "NOV 25",
        "cell": "AB14",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab15": {
        "sheet": "NOV 25",
        "cell": "AB15",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab16": {
        "sheet": "NOV 25",
        "cell": "AB16",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab17": {
        "sheet": "NOV 25",
        "cell": "AB17",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab18": {
        "sheet": "NOV 25",
        "cell": "AB18",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab19": {
        "sheet": "NOV 25",
        "cell": "AB19",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab20": {
        "sheet": "NOV 25",
        "cell": "AB20",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab21": {
        "sheet": "NOV 25",
        "cell": "AB21",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab22": {
        "sheet": "NOV 25",
        "cell": "AB22",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab23": {
        "sheet": "NOV 25",
        "cell": "AB23",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab24": {
        "sheet": "NOV 25",
        "cell": "AB24",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab25": {
        "sheet": "NOV 25",
        "cell": "AB25",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab26": {
        "sheet": "NOV 25",
        "cell": "AB26",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab27": {
        "sheet": "NOV 25",
        "cell": "AB27",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab28": {
        "sheet": "NOV 25",
        "cell": "AB28",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab29": {
        "sheet": "NOV 25",
        "cell": "AB29",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab30": {
        "sheet": "NOV 25",
        "cell": "AB30",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab31": {
        "sheet": "NOV 25",
        "cell": "AB31",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab32": {
        "sheet": "NOV 25",
        "cell": "AB32",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab33": {
        "sheet": "NOV 25",
        "cell": "AB33",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab34": {
        "sheet": "NOV 25",
        "cell": "AB34",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab35": {
        "sheet": "NOV 25",
        "cell": "AB35",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    "canjes_recepcion_ab36": {
        "sheet": "NOV 25",
        "cell": "AB36",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "canjes_recepcion"
    },
    
    # 🔹 Recepción Z41 y AA41 → I CL
    "recepcion_z41": {
        "sheet": "NOV 25",
        "cell": "Z41",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "recepcion_aa41": {
        "sheet": "NOV 25",
        "cell": "AA41",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    
    # 🔹 Codelco Z42 y AA42 → I CL (actualmente en 0, pero configurados)
    "codelco_z42": {
        "sheet": "NOV 25",
        "cell": "Z42",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "codelco_aa42": {
        "sheet": "NOV 25",
        "cell": "AA42",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    }
}