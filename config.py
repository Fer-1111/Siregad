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
        "include_in_batch": True
    },
    "consumo_ecip_c19": {
        "sheet": "Balance",
        "cell": "C19",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "consumo_ecip_c20": {
        "sheet": "Balance",
        "cell": "C20",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "consumo_ecip_c21": {
        "sheet": "Balance",
        "cell": "C21",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "consumo_ecip_c22": {
        "sheet": "Balance",
        "cell": "C22",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "consumo_ecip_c23": {
        "sheet": "Balance",
        "cell": "C23",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True
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
        "grupo": "TIEB"
    },
    "consumo_tieb_c27": {
        "sheet": "Balance",
        "cell": "C27",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "TIEB"
    },
    "consumo_tieb_c28": {
        "sheet": "Balance",
        "cell": "C28",
        "tipo_mov": "TIEB",
        "movimiento": "E",
        "bodega": "TECA",
        "material": "7664-93-9",
        "include_in_batch": True,
        "grupo": "TIEB"
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
        "include_in_batch": True
    },
    "entregado_f18": {
        "sheet": "Balance",
        "cell": "F18",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "entregado_f19": {
        "sheet": "Balance",
        "cell": "F19",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "entregado_f20": {
        "sheet": "Balance",
        "cell": "F20",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "entregado_f21": {
        "sheet": "Balance",
        "cell": "F21",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "TETBA",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "entregado_f22": {
        "sheet": "Balance",
        "cell": "F22",
        "tipo_mov": "ETIEB",
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
        "include_in_batch": True
    },
    "entregado_i18": {
        "sheet": "Balance",
        "cell": "I18",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "entregado_i19": {
        "sheet": "Balance",
        "cell": "I19",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "entregado_i20": {
        "sheet": "Balance",
        "cell": "I20",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "entregado_i21": {
        "sheet": "Balance",
        "cell": "I21",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "entregado_i22": {
        "sheet": "Balance",
        "cell": "I22",
        "tipo_mov": "ETIEB",
        "movimiento": "E",
        "bodega": "CM",
        "material": "7664-93-9",
        "include_in_batch": True
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
        "cell": "E17",
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
        "include_in_batch": True
    },
    "salida_k11": {
        "sheet": "Balance Acido",
        "cell": "K11",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "salida_k12": {
        "sheet": "Balance Acido",
        "cell": "K12",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "salida_k13": {
        "sheet": "Balance Acido",
        "cell": "K13",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True
    },
    "salida_k12": {
        "sheet": "Balance Acido",
        "cell": "K12",
        "tipo_mov": "ECIP",
        "movimiento": "E",
        "bodega": "RT",
        "material": "7664-93-9",
        "include_in_batch": True
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