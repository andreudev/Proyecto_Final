import csv
from datetime import date, datetime


documento = 111111

columns = [
    "id_producto",
    "nombre_producto",
    "cantidad",
    "costo",
    "precio",
    "f_vencimiento",
]
try:
    with open(
        f"./facturas/factura{documento}_{date.today().strftime('%d-%m-%Y')}.txt",
        "w",
        encoding="utf-8",
    ) as file:
        file.write("id_producto,nombre_producto,cantidad,costo,precio,f_vencimiento\n")

except:
    print("Error al abrir el archivo")
