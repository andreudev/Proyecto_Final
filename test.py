import csv
from datetime import date, datetime
import json

try:
    with open("./tablas/facturas.csv", "r") as file:
        reader = csv.DictReader(
            file,
            fieldnames=(
                "id_venta",
                "nombre_cliente",
                "documento_cliente",
                "fecha_venta",
                "items",
            ),
        )
        next(reader)
        for row in reader:
            try:
                items = json.loads(row["items"].replace("'", '"'))
                print(items)
            except json.decoder.JSONDecodeError:
                print("Error al decodificar el JSON")

except FileNotFoundError:
    print("No se ha encontrado el archivo de facturas")


# items = "[{'name': 'Papa', 'quantity': 1, 'unit_cost': 10}, {'name': 'Papa', 'quantity': 1, 'unit_cost': 10}, {'name': 'Papa', 'quantity': 1, 'unit_cost': 10}]"

# items = json.loads(items.replace("'", '"'))
# print(items[0])
# print(items[1])
# print(type(items))
