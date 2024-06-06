import csv
from datetime import date, datetime


columns = [
    "id_producto",
    "nombre_producto",
    "cantidad",
    "costo",
    "precio",
    "f_vencimiento",
]
try:
    with open("./tablas/productos.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=columns)
        for row in reader:
            print(row["f_vencimiento"])
except:
    print("Error al abrir el archivo")
