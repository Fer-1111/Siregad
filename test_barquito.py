#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test para verificar CONFIG_BARQUITO"""

from config import CONFIG_BARQUITO

print(f"✅ CONFIG_BARQUITO importado exitosamente")
print(f"📊 Número de conceptos: {len(CONFIG_BARQUITO)}")
print(f"\n🔍 Verificando celdas P41-P43:")

for key in ['vent_p41', 'vent_p42', 'tieb_p43']:
    if key in CONFIG_BARQUITO:
        config = CONFIG_BARQUITO[key]
        print(f"  ✓ {key}: celda={config['cell']}, sheet={config['sheet']}, tipo_mov={config['tipo_mov']}")
    else:
        print(f"  ✗ {key}: NO ENCONTRADO")

print(f"\n🔍 Verificando canjes despacho (AA6-AA36):")
despacho_keys = [k for k in CONFIG_BARQUITO.keys() if 'canjes_despacho' in k]
print(f"  Total: {len(despacho_keys)} celdas")

print(f"\n🔍 Verificando canjes recepción (AB6-AB36):")
recepcion_keys = [k for k in CONFIG_BARQUITO.keys() if 'canjes_recepcion' in k]
print(f"  Total: {len(recepcion_keys)} celdas")

print(f"\n🔍 Verificando recepción Z41, AA41:")
for key in ['recepcion_z41', 'recepcion_aa41']:
    if key in CONFIG_BARQUITO:
        print(f"  ✓ {key}: {CONFIG_BARQUITO[key]['cell']}")
    else:
        print(f"  ✗ {key}: NO ENCONTRADO")

print(f"\n🔍 Verificando codelco Z42, AA42:")
for key in ['codelco_z42', 'codelco_aa42']:
    if key in CONFIG_BARQUITO:
        print(f"  ✓ {key}: {CONFIG_BARQUITO[key]['cell']}")
    else:
        print(f"  ✗ {key}: NO ENCONTRADO")

print("\n✅ Todas las verificaciones completadas")
