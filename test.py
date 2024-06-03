import csv
import csv


columns = ["id_cliente", "nombre", "apellido", "fecha_nacimiento", "documento"]

try:
    with open("clientes.csv", "r") as file:
        reader = csv.DictReader(file, fieldnames=columns)
        for row in reader:
            print(row)
except:
    print("Error al abrir el archivo")
