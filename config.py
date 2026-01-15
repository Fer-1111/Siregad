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
    # 🔹 Inventario inicial X5 (NO se carga al batch)
    "inventario_inicial": {
        "sheet": "NOV 25",
        "cell": "X5",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    
    # 🔹 Datos independientes C6 a C36 → I CL (guardar como datos separados, no sumados)
    "dato_c6": {
        "sheet": "NOV 25",
        "cell": "C6",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c7": {
        "sheet": "NOV 25",
        "cell": "C7",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c8": {
        "sheet": "NOV 25",
        "cell": "C8",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c9": {
        "sheet": "NOV 25",
        "cell": "C9",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c10": {
        "sheet": "NOV 25",
        "cell": "C10",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c11": {
        "sheet": "NOV 25",
        "cell": "C11",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c12": {
        "sheet": "NOV 25",
        "cell": "C12",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c13": {
        "sheet": "NOV 25",
        "cell": "C13",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c14": {
        "sheet": "NOV 25",
        "cell": "C14",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c15": {
        "sheet": "NOV 25",
        "cell": "C15",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c16": {
        "sheet": "NOV 25",
        "cell": "C16",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c17": {
        "sheet": "NOV 25",
        "cell": "C17",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c18": {
        "sheet": "NOV 25",
        "cell": "C18",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c19": {
        "sheet": "NOV 25",
        "cell": "C19",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c20": {
        "sheet": "NOV 25",
        "cell": "C20",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c21": {
        "sheet": "NOV 25",
        "cell": "C21",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c22": {
        "sheet": "NOV 25",
        "cell": "C22",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c23": {
        "sheet": "NOV 25",
        "cell": "C23",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c24": {
        "sheet": "NOV 25",
        "cell": "C24",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c25": {
        "sheet": "NOV 25",
        "cell": "C25",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c26": {
        "sheet": "NOV 25",
        "cell": "C26",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c27": {
        "sheet": "NOV 25",
        "cell": "C27",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c28": {
        "sheet": "NOV 25",
        "cell": "C28",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c29": {
        "sheet": "NOV 25",
        "cell": "C29",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c30": {
        "sheet": "NOV 25",
        "cell": "C30",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c31": {
        "sheet": "NOV 25",
        "cell": "C31",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c32": {
        "sheet": "NOV 25",
        "cell": "C32",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c33": {
        "sheet": "NOV 25",
        "cell": "C33",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c34": {
        "sheet": "NOV 25",
        "cell": "C34",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c35": {
        "sheet": "NOV 25",
        "cell": "C35",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    "dato_c36": {
        "sheet": "NOV 25",
        "cell": "C36",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "datos_c"
    },
    
    # 🔹 Datos independientes E6 a E36 → I CL (guardar con contenido, no sumados)
    "dato_e6": {
        "sheet": "NOV 25",
        "cell": "E6",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e7": {
        "sheet": "NOV 25",
        "cell": "E7",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e8": {
        "sheet": "NOV 25",
        "cell": "E8",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e9": {
        "sheet": "NOV 25",
        "cell": "E9",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e10": {
        "sheet": "NOV 25",
        "cell": "E10",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e11": {
        "sheet": "NOV 25",
        "cell": "E11",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e12": {
        "sheet": "NOV 25",
        "cell": "E12",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e13": {
        "sheet": "NOV 25",
        "cell": "E13",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e14": {
        "sheet": "NOV 25",
        "cell": "E14",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e15": {
        "sheet": "NOV 25",
        "cell": "E15",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e16": {
        "sheet": "NOV 25",
        "cell": "E16",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e17": {
        "sheet": "NOV 25",
        "cell": "E17",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e18": {
        "sheet": "NOV 25",
        "cell": "E18",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e19": {
        "sheet": "NOV 25",
        "cell": "E19",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e20": {
        "sheet": "NOV 25",
        "cell": "E20",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e21": {
        "sheet": "NOV 25",
        "cell": "E21",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e22": {
        "sheet": "NOV 25",
        "cell": "E22",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e23": {
        "sheet": "NOV 25",
        "cell": "E23",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e24": {
        "sheet": "NOV 25",
        "cell": "E24",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e25": {
        "sheet": "NOV 25",
        "cell": "E25",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e26": {
        "sheet": "NOV 25",
        "cell": "E26",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e27": {
        "sheet": "NOV 25",
        "cell": "E27",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e28": {
        "sheet": "NOV 25",
        "cell": "E28",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e29": {
        "sheet": "NOV 25",
        "cell": "E29",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e30": {
        "sheet": "NOV 25",
        "cell": "E30",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e31": {
        "sheet": "NOV 25",
        "cell": "E31",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e32": {
        "sheet": "NOV 25",
        "cell": "E32",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e33": {
        "sheet": "NOV 25",
        "cell": "E33",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e34": {
        "sheet": "NOV 25",
        "cell": "E34",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e35": {
        "sheet": "NOV 25",
        "cell": "E35",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    "dato_e36": {
        "sheet": "NOV 25",
        "cell": "E36",
        "tipo_mov": "CL",
        "movimiento": "I",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True,
        
    },
    
    # 🔹 P41 → E VENT
    "vent_p41": {
        "sheet": "NOV 25",
        "cell": "P41",
        "tipo_mov": "VENT",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    
    # 🔹 P42 → E VENT
    "vent_p42": {
        "sheet": "NOV 25",
        "cell": "P42",
        "tipo_mov": "VENT",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    
    # 🔹 P43 → E TIEB
    "tieb_p43": {
        "sheet": "NOV 25",
        "cell": "P43",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "BARQUITO",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    
    # 🔹 Z41 → I TIPB (si no hay valor, guardar 0,000)
    "recepcion_z41": {
        "sheet": "NOV 25",
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
        "sheet": "NOV 25",
        "cell": "AN14",
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
        "sheet": "Balance",
        "cell": "A1",  # Placeholder - se actualizará cuando se proporcione el Excel
        "tipo_mov": "MPRO",
        "movimiento": "I",
        "bodega": "DGM",
        "material": "7664-93-9",
        "include_in_batch": False
    },
    
    # 🔹 E41 → I TIPB (Recepción)
    "recepcion_e41": {
        "sheet": "Balance",
        "cell": "E41",
        "tipo_mov": "TIPB",
        "movimiento": "I",
        "bodega": "DGM",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    
    # 🔹 J41 → E ECIP (Consumo interno)
    "consumo_j41": {
        "sheet": "Balance",
        "cell": "J41",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "DGM",
        "material": "7664-93-9",
        "include_in_batch": True
    }
}
