# config_programacion.py
# Configuración para extraer datos del Excel PROGRAMACIÓN AS 2025

"""
MAPEO DE CORRESPONDENCIAS:
==========================
PROGRAMACIÓN AS 2025          →    DIVISIONES (Balances)
───────────────────────────────────────────────────────────
SALV / Sal                    →    Potrerillos, Barquito (Salvador)
TTE / Tnte                    →    Caletones, TBA (Los Lirios), San Antonio (Teniente)
DMH / M.Hales                 →    Ministro Hales
Chuqui                        →    Chuquicamata, RT, GM
VENT / Ventana                →    Ventana
MEJICL / Mej ICL              →    Mejillones Interacid
MEJ / Meji                    →    Mejillones TPM  
TERMEJ / Terquim Mej          →    Terquim Mejillones
ALTNORTE                      →    (Solo compra)
MOLYBFILIAL                   →    (Solo compra)
Comp                          →    Compras generales
Canjes                        →    Control de canjes
"""

# ============================================================================
# COLUMNAS POR MES
# ============================================================================
COLUMNA_MES_STANDARD = {
    # Esquema B=ENE hasta M=DIC (hojas Cuadrar, VENT)
    "enero": 2, "febrero": 3, "marzo": 4, "abril": 5, "mayo": 6, "junio": 7,
    "julio": 8, "agosto": 9, "septiembre": 10, "octubre": 11, "noviembre": 12, "diciembre": 13,
}

COLUMNA_MES_C_START = {
    # Esquema C=ENE hasta N=DIC (hojas DMH, Chuqui, MEJICL, MEJ)
    "enero": 3, "febrero": 4, "marzo": 5, "abril": 6, "mayo": 7, "junio": 8,
    "julio": 9, "agosto": 10, "septiembre": 11, "octubre": 12, "noviembre": 13, "diciembre": 14,
}

COLUMNA_MES_D_START = {
    # Esquema D=ENE hasta O=DIC, P=TOTAL (hojas SALV, TTE, TERMEJ)
    "enero": 4, "febrero": 5, "marzo": 6, "abril": 7, "mayo": 8, "junio": 9,
    "julio": 10, "agosto": 11, "septiembre": 12, "octubre": 13, "noviembre": 14, "diciembre": 15,
    "total": 16,
}

MES_ALIAS = {
    "ene": "enero", "jan": "enero", "feb": "febrero", "mar": "marzo",
    "abr": "abril", "apr": "abril", "may": "mayo", "jun": "junio",
    "jul": "julio", "ago": "agosto", "aug": "agosto", "sep": "septiembre",
    "sept": "septiembre", "oct": "octubre", "nov": "noviembre",
    "dic": "diciembre", "dec": "diciembre",
}

COLUMNA_MES = COLUMNA_MES_STANDARD

# ============================================================================
# HOJA "Cuadrar" - Vista general consolidada
# ============================================================================
CONFIG_CUADRAR = {
    "sheet": "Cuadrar",
    "columnas": COLUMNA_MES_STANDARD,
    "secciones": {
        "Chuqui_Produccion": {"produccion": 2, "consumos_ajustes": 3},
        "Chuqui_Consumos": {"hidronorte_rt": 5, "hidrosur": 6, "acl": 7},
        "Salvador": {
            "produccion": 17, "consumos_internos": 18, "consumo_lixiviacion": 19,
            "consumo_refineria": 20, "otros": 21, "diferencia_produccion": 22,
        },
        "Ventanas": {
            "produccion": 25, "consumo_total": 26, "consumo_refineria": 27,
            "consumo_andina": 28, "consumo_plantas": 29, "excedentes": 30,
        },
        "Teniente_Caletones": {
            "saldo_inicial": 35, "produccion_96": 36, "subtotal": 37,
            "consumo_interno": 38, "entregas_desde_caletones": 39,
            "despachos_los_lirios": 40, "despachos_terquim": 41,
            "subtotal_egresos": 42, "ajuste_inventario": 43, "total": 44,
        },
        "Los_Lirios": {
            "saldo_inicial": 47, "recepcion": 48, "subtotal": 49,
            "entregas_desde_los_lirios": 50, "despachos_terquim": 51,
            "subtotal_egresos": 52, "ajuste_inventario": 53, "total": 54,
        },
        "Terquim_San_Antonio": {
            "saldo_inicial": 57, "recepcion_los_lirios": 58, "recepcion_caletones": 59,
            "subtotal": 60, "despachos": 61, "subtotal_egresos": 62,
            "ajuste_inventario": 63, "total": 64,
        },
    }
}

# ============================================================================
# HOJA "SALV" - Salvador (Potrerillos + Barquito)
# ============================================================================
CONFIG_SALV = {
    "sheet": "SALV",
    "columnas": COLUMNA_MES_D_START,  # D=ENE hasta O=DIC, P=TOTAL
    "secciones": {
        "Potrerillos": {
            "inventario_inicial": 6,
            "produccion": 8,
            "consumo_interno": 9,
            "otros": 10,
            "excedente": 11,
            "despacho_barquito": 12,
            # Traspasos (fila 17 es título)
            "traspasos_interacid": 18,
            "traspasos_puerto_mejillones": 19,
            "traspasos_desde_barquito": 20,
            # Canjes
            "de_canjes": 22,
            "total_compromisos": 26,
            "ventas": 28,
            # Canjes-Devoluciones (fila 36 es título)
            "canjes_devoluciones": 36,
            "canjes_mantoverde_ZO5J402": 37,
            # Traspasos a (fila 43 es título)
            "traspaso_a_dgm": 44,
            "traspaso_a_drt": 45,
        },
        "Barquito": {
            "inventario_inicial": 59,
            "traspaso_desde_potrerillos": 61,
            "traspaso_desde_t_mejillones": 62,
            "traspaso_desde_teniente": 63,
            "compras": 65,
            # Canjes Recepción (fila 68 es título)
            "canjes_recepcion": 68,
            "canjes_mantoverde_ZR5K402": 69,
            "canjes_transsud_ZR4K311": 70,
            "canjes_transsud_ZR5K404": 71,
            "total_compromisos": 73,
            # Ventas desde Barquitos (fila 75 es título)
            "ventas": 75,
            "ventas_enami_CL5K419": 76,
            "ventas_transsud": 80,
            # A Canjes-Devoluciones (fila 83 es título)
            "a_canjes_devoluciones": 83,
            "a_canjes_mantoverde_ZO5K402": 84,
            "a_canjes_transsud_ZO5K404": 85,
            # Traspasos desde Barquitos (fila 91 es título)
            "traspasos_desde": 91,
            "traspaso_consumo_interno_potrerillos": 92,
            "traspaso_tte": 93,
            "traspaso_drt": 94,
            "traspaso_dgm": 95,
            # Embarques desde Barquitos (fila 98 es título)
            "embarques": 98,
            "embarque_mejillones_puerto": 99,
            "embarque_mejillones_icl": 100,
            "embarque_mejillones_terquim": 101,
        },
    }
}

# ============================================================================
# HOJA "TTE" - Teniente (Caletones + Los Lirios + San Antonio)
# ============================================================================
CONFIG_TTE = {
    "sheet": "TTE",
    "columnas": COLUMNA_MES_D_START,  # D=ENE hasta O=DIC, P=TOTAL
    "secciones": {
        "Caletones": {
            "inventario_inicial": 6,
            "produccion": 8,
            "consumo": 9,
            "excedentes": 10,
            "ajuste_disponibilidad": 12,
            "traspaso_a_los_lirios": 14,
            "traspaso_desde_los_lirios": 15,
            "saldo_mes": 17,
            "saldo_acumulado": 19,
        },
        "Los_Lirios": {
            "inventario_inicial": 23,
            "recepcion_desde_caletones": 25,
            "entregas_hacia_caletones": 26,
            "canjes_recepcion": 30,
            # Ventas desde Los Lirios
            "ventas": 34,
            "ventas_orafti_CL4K301": 36,
            "ventas_arauco_CL5K402": 37,
            "ventas_maderas_arauco_CL5K403": 38,
            "ventas_valle_central_CL5K404": 39,
            "ventas_quimica_del_sur_CL5K405": 40,
            "ventas_quimicos_fas_CL5K407": 41,
            "ventas_ecokorp_CL5K408": 42,
            "ventas_molymetnos_CL5K409": 43,
            "ventas_vinicas_CL4K310": 44,
            "ventas_redoxi_CL5K411": 45,
            "ventas_proquiel_CL5K412": 46,
            "ventas_pelambres_CL4K313": 47,
            "ventas_cemin_CL5K421": 48,
            "ventas_quimetal_CL5K420": 49,
            "ventas_cmpc_CL4K314": 50,
            "ventas_minera_tres_valles_CL5K425": 51,
            "ventas_valle_central_CL4K320": 52,
            "ventas_minera_tres_valles_CL5K431": 53,
            # Canjes-Devoluciones
            "canjes_devoluciones": 61,
            # Traspasos
            "traspaso_a_san_antonio": 66,
            "traspaso_a_ventanas": 67,
            "traspaso_andina": 68,
            # Saldos
            "saldo_mes": 70,
            "ajustes_disponibilidades": 72,
            "saldo_mes_ajustado": 74,
            "saldo_por_asignar": 76,
            "saldo_acumulado": 78,
        },
        "San_Antonio": {
            "inventario_inicial": 81,
            "recepcion_desde_los_lirios": 83,
            "total_compromisos": 85,
            # Ventas desde San Antonio
            "ventas": 87,
            "ventas_amsa_CL5K423": 88,
            "ventas_glencore_ZU5K401": 89,
            # Exportación
            "exportacion": 92,
            # Embarques desde San Antonio
            "embarques": 96,
            "embarque_barquito": 97,
            "embarque_mejillones_icl": 98,
            "embarque_mejillones_puerto": 99,
            "embarque_terquim_mejillones": 100,
            # Canjes-Devoluciones
            "canjes_devoluciones": 102,
            # Saldos
            "saldo_mes": 106,
            "ajustes_disponibilidades": 108,
            "saldo_mes_ajustado": 111,
            "saldo_acumulado": 115,
        },
    }
}

# ============================================================================
# HOJA "DMH" - Ministro Hales
# ============================================================================
CONFIG_DMH_PROGRA = {
    "sheet": "DMH",
    "columnas": COLUMNA_MES_D_START,  # D=ENE hasta O=DIC, P=TOTAL
    "secciones": {
        "DMH": {
            "inventario_inicial": 7,
            "produccion": 9,
            "consumo": 10,
            "excedentes": 11,
            # Traspasos (fila 13 es título)
            "traspasos": 13,
            "traspaso_desde_puerto_mejillones": 14,
            "traspaso_desde_interacid_mejillones": 15,
            "traspaso_desde_chuquicamata": 16,
            "compras": 18,
            "retornos_canjes": 21,
            "total_compromisos": 24,
            "ventas": 26,
            "canjes_devoluciones": 32,
            # Traspasos a (fila 35 es título)
            "traspasos_a": 35,
            "traspaso_a_rt": 36,
            "traspaso_a_dch": 37,
            "traspaso_a_dgm": 38,
            # Saldos
            "saldo_mes": 40,
            "ajustes_disponibilidades": 42,
            "saldo_mes_ajustado": 44,
            "saldo_por_asignar": 46,
            "saldo_acumulado": 48,
        },
    }
}

# ============================================================================
# HOJA "CHU" - Chuquicamata
# ============================================================================
CONFIG_CHUQUI = {
    "sheet": "CHU",
    "columnas": COLUMNA_MES_D_START,  # D=ENE hasta O=DIC, P=TOTAL
    "secciones": {
        "Chuquicamata": {
            "inventario_inicial": 7,
            "produccion": 9,
            "consumo_interno": 10,
            "ajuste_consumos_produccion": 12,
            "excedentes": 13,
            # Traspasos desde Mejillones (fila 15 es título)
            "traspasos_desde_mejillones": 15,
            "traspaso_desde_puerto_mejillones": 16,
            "traspaso_desde_terquim_mejillones": 17,
            "traspaso_desde_interacid_mejillones": 19,
            # Traspasos divisionales (fila 21 es título)
            "traspasos_divisionales": 21,
            "traspaso_desde_dmh": 22,
            "traspaso_desde_drt": 23,
            # Traspasos a (fila 25 es título)
            "traspasos_a": 25,
            "traspaso_a_drt": 26,
            "traspaso_a_dgm": 27,
            "traspaso_a_dmh": 28,
            # Compras (fila 30 es título)
            "compras": 30,
            "compras_altonorte": 31,
            "compras_molyb": 32,
            "retornos_canjes": 34,
            "total_compromisos": 37,
            "ventas": 39,
            "canjes_devoluciones": 44,
            # Traspasos a Tocopilla
            "traspasos_a_tocopilla": 47,
            "traspaso_tocopilla": 48,
            # Saldos
            "saldo_mes": 50,
            "ajustes_disponibilidades": 52,
            "saldo_mes_ajustado": 54,
            "saldo_por_asignar": 56,
            "saldo_acumulado": 58,
        },
    }
}

# ============================================================================
# HOJA "VENT" - Ventanas
# ============================================================================
CONFIG_VENT = {
    "sheet": "VENT",
    "columnas": COLUMNA_MES_D_START,  # D=ENE hasta O=DIC, P=TOTAL
    "secciones": {
        "Ventanas": {
            "inventario_inicial": 7,
            "produccion": 9,
            "consumo_interno": 10,
            "excedentes": 11,
            # De Traspasos (fila 13 es título)
            "de_traspasos": 13,
            "traspaso_desde_teniente": 14,
            "traspaso_desde_salvador": 15,
            "compras": 17,
            "de_canjes": 20,
            "total_compromisos": 24,
            "ventas": 26,
            "ventas_cif": 47,
            # Embarques desde las Ventanas (fila 52 es título)
            "embarques": 52,
            "embarque_barquito": 53,
            "embarque_mejillones_puerto": 54,
            "embarque_mejillones_icl": 55,
            # A Canjes
            "a_canjes": 58,
            # A Traspasos (fila 63 es título)
            "a_traspasos": 63,
            "traspaso_a_teniente": 64,
            # Saldos
            "saldo_mensual": 68,
            "diferencia_recepcion_camiones_tte": 70,
            "diferencia_inventario_fisico": 71,
            "ajustes_disponibilidades": 72,
            "saldo_mensual_ajustado": 74,
            "saldo_por_asignar": 76,
            "saldo_acumulado": 78,
        },
    }
}

# ============================================================================
# HOJA "MEJICL" - Mejillones Interacid
# ============================================================================
CONFIG_MEJICL = {
    "sheet": "MEJICL",
    "columnas": COLUMNA_MES_D_START,  # D=ENE hasta O=DIC, P=TOTAL
    "secciones": {
        "Mejillones_Interacid": {
            "inventario_inicial": 7,
            # Traspasos Codelco (fila 9 es título)
            "traspasos_codelco": 9,
            "traspaso_desde_chuquicamata": 10,
            "traspaso_desde_salvador": 11,
            "traspaso_desde_ventanas": 12,
            "traspaso_desde_teniente": 13,
            # Compras (fila 15 es título)
            "compras": 15,
            "compras_hexagon_ZU5K202_CL5K206": 16,
            "compras_transsud_CL4K211": 17,
            "compras_tricon_ZU5K204_CL5K205": 18,
            "compras_sas_ZU5K203_CL5K201": 19,
            # De Canjes Recepción (fila 40 es título)
            "de_canjes_recepcion": 40,
            "canjes_mantoverde_ZR5K402": 41,
            "canjes_transsud_ZR4K311": 42,
            "canjes_interacid_ZR5K416": 43,
            "canjes_bhp_ZR5K415": 44,
            "canjes_interacid_ZR5K417": 45,
            "canjes_sas_ZR5K418": 46,
            "canjes_mantoverde_ZR4K302": 47,
            "canjes_bhp_ZR5K419": 48,
            "canjes_interacid_ZR5K421": 49,
            "canjes_interacid_ZR5K422": 50,
            "canjes_hexagon_ZR5K425": 51,
            "canjes_interacid_ZR5K427": 52,
            "total_compromisos": 62,
            # Ventas (fila 64 es título)
            "ventas": 64,
            "ventas_proquiel_CL5K412": 65,
            "ventas_ameropa_CL5K424": 66,
            "ventas_prm_CL5K406": 68,
            # Traspasos (fila 87 es título)
            "traspasos": 87,
            "traspaso_a_terquim": 88,
            "traspaso_a_rt": 89,
            "traspaso_a_dgm": 90,
            "traspaso_a_dch": 91,
            "traspaso_a_dsal": 92,
            "traspaso_a_dmh": 93,
            # A Canjes-Devoluciones (fila 95 es título)
            "a_canjes_devoluciones": 95,
            "canje_dev_sas_ZO5K409": 96,
            "canje_dev_mantoverde": 97,
            "canje_dev_interacid_ZO5K416": 98,
            "canje_dev_bhp_ZO5K415": 99,
            "canje_dev_interacid_ZO5K417": 100,
            "canje_dev_sas_ZO5K418": 101,
            "canje_dev_bhp_ZO5K419": 102,
            "canje_dev_interacid_ZO5K421": 103,
            "canje_dev_interacid_ZO5K422": 104,
            "canje_dev_hexagon_ZO5K425": 105,
            "canje_dev_interacid_ZO5K427": 106,
            # Saldos
            "saldo_mes": 118,
            "diferencia_medicion_naves": 120,
            "diferencia_inventario_fisico": 121,
            "ajustes_disponibilidades": 122,
            "saldo_mes_ajustado": 124,
            "saldo_por_asignar": 126,
            "saldo_acumulado": 128,
        },
    }
}

# ============================================================================
# HOJA "MEJ" - Mejillones (Puerto/TPM)
# ============================================================================
CONFIG_MEJ = {
    "sheet": "MEJ",
    "columnas": COLUMNA_MES_D_START,  # D=ENE hasta O=DIC, P=TOTAL
    "secciones": {
        "Mejillones": {
            "inventario_inicial": 7,
            # Traspasos Codelco (fila 9 es título)
            "traspasos_codelco": 9,
            "traspaso_desde_chuquicamata": 10,
            "traspaso_desde_salvador": 11,
            "traspaso_desde_ventanas": 12,
            "traspaso_desde_teniente": 13,
            # Compras (fila 15 es título)
            "compras": 15,
            "compras_sas": 16,
            "compras_transsud_CL5K208": 17,
            "compras_tricon_CL4K210": 18,
            "compras_transsud_CL4K209": 19,
            "compras_transsud_CL4K211": 20,
            "compras_hexagon_CL5K206": 21,
            "compras_tricon_ZU5K204": 22,
            "compras_jxnmn_ZU5K205": 23,
            "compras_transsud_CL5K204": 24,
            # De Canjes Recepción (fila 36 es título)
            "de_canjes_recepcion": 36,
            "canjes_mantoverde_ZR5K402": 37,
            "canjes_transsud_ZR4K311": 38,
            "canjes_transsud_ZR5K404": 39,
            "canjes_transsud_ZR5K407": 40,
            "canjes_transsud_ZR5K408": 41,
            "canjes_noracid_ZR5K403": 42,
            "canjes_mantucoya_ZR5K406": 43,
            "canjes_altonorte_ZR5K411": 44,
            "canjes_transsud_ZR5K410": 45,
            "canjes_transsud_ZR5K414": 46,
            "canjes_noracid_ZR5K413": 47,
            "canjes_elabra_ZR5K420": 48,
            "canjes_elabra_ZR5K423": 49,
            "canjes_transsud_ZR5K424": 50,
            "canjes_elabra_ZR5K426": 51,
            "total_compromisos": 56,
            # Ventas (fila 58 es título)
            "ventas": 58,
            "ventas_elabra_CL5K400": 59,
            "ventas_transsud_CL5K422": 60,
            "ventas_elabra_CL5K426": 61,
            "ventas_transsud_CL5K427": 62,
            "ventas_transsud_CL5K428": 63,
            # Traspasos (fila 79 es título)
            "traspasos": 79,
            "traspaso_a_dgm": 80,
            "traspaso_a_rt": 81,
            "traspaso_a_dch": 82,
            "traspaso_a_dsal": 83,
            "traspaso_a_dmh": 84,
            # Canjes-Devoluciones (fila 86 es título)
            "canjes_devoluciones": 86,
            "canje_dev_transsud_ZO5K407": 87,
            "canje_dev_transsud_ZO5K408": 88,
            "canje_dev_mantucoya_ZO5K406": 89,
            "canje_dev_noracid_ZO5K403": 90,
            "canje_dev_altonorte_ZO5K411": 91,
            "canje_dev_transsud_ZO5K410": 92,
            "canje_dev_transsud_ZO5K414": 93,
            "canje_dev_noracid_ZO5K413": 94,
            "canje_dev_elabra_ZO5K420": 95,
            "canje_dev_elabra_ZO5K423": 96,
            "canje_dev_transsud_ZO5K424": 97,
            "canje_dev_elabra_ZO5K426": 98,
            # Saldos
            "saldo_mes": 109,
            "diferencia_medicion_naves": 111,
            "diferencia_inventario_fisico": 112,
            "ajustes_disponibilidades": 113,
            "saldo_mes_ajustado": 115,
            "saldo_por_asignar": 117,
            "saldo_acumulado": 119,
            # Ofertas y saldos finales
            "ofertas": 123,
            "saldo_mes_mejillones": 127,
            "saldo_acumulado_mejillones": 129,
        },
    }
}

# ============================================================================
# HOJA "TERMEJ" - Terquim Mejillones
# ============================================================================
CONFIG_TERMEJ = {
    "sheet": "TERMEJ",
    "columnas": COLUMNA_MES_D_START,  # D=ENE hasta O=DIC, P=TOTAL
    "secciones": {
        "Terquim_Mejillones": {
            "inventario_inicial": 7,
            # Traspasos Codelco (fila 9 es título)
            "traspasos_codelco": 9,
            "traspaso_desde_chuquicamata": 10,
            "traspaso_desde_salvador": 11,
            "traspaso_desde_ventanas": 12,
            "traspaso_desde_itc": 13,
            "traspaso_desde_tpm": 14,
            "traspaso_desde_teniente": 15,
            # Compras (fila 17 es título)
            "compras": 17,
            "compras_transsud": 18,
            "compras_jxnmn_ZU5K205": 19,
            "compras_ameropa_ZU5K201": 20,
            "compras_transsud_CL4K211": 21,
            "compras_hexagon_ZU5K202_CL5K206": 22,
            "compras_tricon_CL4K210": 23,
            "compras_sas_ZU5K203_CL5K201": 24,
            # De Canjes Recepción (fila 36 es título)
            "de_canjes_recepcion": 36,
            "canjes_sas_ZR5K409": 37,
            "canjes_mantucoya_ZR5K406": 38,
            "canjes_mantoverde_ZR5K402": 39,
            "canjes_sas_ZR5K412": 40,
            "canjes_sas_ZR5K418": 41,
            "total_compromisos": 54,
            # Ventas (fila 56 es título)
            "ventas": 56,
            "ventas_ameropa_CL5K424": 57,
            "ventas_proquiel_CL5K412": 58,
            "ventas_ameropa_CL5K430": 59,
            # Traspasos (fila 72 es título)
            "traspasos": 72,
            "traspaso_a_rt": 73,
            "traspaso_a_dgm": 74,
            "traspaso_a_dch": 75,
            "traspaso_a_dsal": 76,
            "traspaso_a_dmh": 77,
            # Canjes-Devoluciones (fila 79 es título)
            "canjes_devoluciones": 79,
            "canje_dev_mantucoya_ZO5K406": 80,
            "canje_dev_sas_ZO5K409": 81,
            "canje_dev_sas_ZO5K412": 82,
            "canje_dev_sas_ZO5K418": 83,
            "canje_dev_mantoverde": 84,
            # Saldos
            "saldo_mes": 102,
            "diferencia_medicion_naves": 104,
            "diferencia_inventario_fisico": 105,
            "ajustes_disponibilidades": 106,
            "saldo_mes_ajustado": 108,
            "saldo_por_asignar": 110,
            "saldo_acumulado": 112,
        },
    }
}

# ============================================================================
# HOJA "Canjes" - Control de Canjes
# ============================================================================
CONFIG_CANJES = {
    "sheet": "Canjes",
    "columnas": {
        "enero": 3, "febrero": 4, "marzo": 5, "abril": 6, "mayo": 7, "junio": 8,
        "julio": 9, "agosto": 10, "septiembre": 11, "octubre": 12, "noviembre": 13, "diciembre": 14,
    },
    "clientes": {
        "Mantoverde": {"prog_mejillones": 4, "retiros": 8, "prog_barquito": 20, "retiros_barquito": 24},
    }
}

# ============================================================================
# HOJA "COMPRAS" - Compras consolidadas
# ============================================================================
CONFIG_COMPRAS = {
    "sheet": "COMPRAS",
    "columnas": COLUMNA_MES_D_START,  # D=ENE hasta O=DIC, P=TOTAL
    "secciones": {
        "Compras": {
            # Compras (fila 7 es título)
            "compras": 7,
            "compras_molyb_CL5K200": 8,
            "compras_altonorte_lt_tpm_CL5K203": 9,
            "compras_altonorte_lt_an_CL5K203": 10,
            "compras_altonorte_2_tpm_CL5K202": 11,
            "compras_altonorte_2_an_CL5K202": 12,
            "compras_sas_ZU5K203_CL5K201": 13,
            "compras_transsud_CL5K204": 14,
            "compras_tricon_ZU5K204_CL5K205": 15,
            "compras_hexagon_ZU5K202_CL5K206": 16,
            "compras_interacid_CL5K209": 17,
            "compras_jxnmn_ZU5K205": 18,
            "compras_ameropa_ZU5K201": 19,
            "compras_transsud_CL5K208": 20,
            "compras_transsud_CL5K207": 21,
            "compras_tricon_CL4K210": 22,
            "compras_transsud_CL4K211": 23,
            "compras_transsud_CL4K209": 24,
            "compras_interacid_fca_CL4K205A": 25,
            "compras_glencore_altonorte_CL4K203A": 26,
            # Ventas (fila 40 es título)
            "ventas": 40,
            "ventas_elabra": 42,
            # Puerto Destino (fila 45 es título)
            "puerto_destino": 45,
            "destino_molyb": 46,
            "destino_mejillones_puerto": 47,
            "destino_mejillones_icl": 48,
            "destino_barquito": 49,
            "destino_altonorte": 50,
            "destino_terquim_mejillones": 51,
            # A Canjes
            "a_canjes": 53,
            # Saldos
            "ajustes_disponibilidades": 59,
            "saldo_mensual_ajustado": 61,
            "saldo_por_asignar": 63,
            "saldo_acumulado": 65,
        },
    }
}

# ============================================================================
# MAPEOS Y TOLERANCIAS
# ============================================================================
DIVISION_A_GRUPO_PROGRA = {
    "Potrerillos": "Salvador", "Barquito": "Salvador",
    "Ministro Hales": "DMH",
    "Caletones": "Teniente", "TBA": "Teniente", "San Antonio": "Teniente",
    "Chuquicamata": "Chuqui", "Radomiro Tomic": "Chuqui", "Gabriela Mistral": "Chuqui",
    "Ventana": "Ventanas",
}

DATOS_CUADRAR = {
    "produccion": "📈 Producción",
    "consumo": "📉 Consumo", 
    "ajuste": "🔧 Ajuste",
    "venta": "💰 Venta",
    "a_canje": "↗️ A Canje",
    "compras": "🛒 Compras",
    "de_canje": "↙️ De Canje",
}

TOLERANCIA_DIFERENCIA = 0.01
TOLERANCIA_WARNING = 10

ESTADO_OK = "✅ Cuadra"
ESTADO_WARN = "⚠️ Dif. pequeña"  
ESTADO_ERROR = "❌ No cuadra"
