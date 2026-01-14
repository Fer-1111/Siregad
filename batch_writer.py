# batch_writer.py

from openpyxl import load_workbook


def escribir_batch(df, plantilla_path, output):
    wb = load_workbook(plantilla_path)
    ws = wb["Datos"]

    for _, row in df.iterrows():
        ws.append([
            row["Fecha"],
            row["Bodega"],
            row["Material"],
            row["Tipo Movimiento"],
            row["Cantidad"],
            row["Unidad"],
        ])

    wb.save(output)

    if hasattr(output, "seek"):
        output.seek(0)
