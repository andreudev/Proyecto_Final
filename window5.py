import tkinter as tk
import csv
from datetime import date, datetime
from tkinter import ttk
import json


def create_reports_window(master):
    reports_window = tk.Toplevel(master)
    reports_window.title("Reportes")
    reports_window.iconbitmap("./scr/icono_venta.ico")
    reports_window.configure(bg="white")
    return reports_window


def create_widgets_reports(window5, master):

    frame1 = tk.Frame(window5, bg="#D4D4D4")
    frame1.grid(row=0, column=0, sticky="nsew")
    frame2 = tk.Frame(window5, bg="#D4D4D4", width=700, height=500)
    frame2.grid(row=0, column=1, sticky="nsew")

    label_reportes = tk.Label(
        frame1, text="Reportes", bg="#D4D4D4", font=("Arial", 14, "bold")
    )
    label_reportes.grid(row=0, column=0, padx=10, pady=10)
    label_generar_reporte_vencidos = tk.Label(
        frame1,
        text="Generar reporte de productos vencidos",
        bg="#D4D4D4",
        font=("Arial", 12),
    )
    label_generar_reporte_vencidos.grid(row=1, column=0, padx=10, pady=10)
    button_generar_reporte_vencidos = tk.Button(
        frame1,
        text="Generar",
        bg="#FF7E29",
        font=("Arial", 12),
        command=generar_reporte,
    )
    button_generar_reporte_vencidos.grid(row=1, column=1, padx=10, pady=10)

    label_generar_reporte_ventas = tk.Label(
        frame1, text="Generar reporte de ventas", bg="#D4D4D4", font=("Arial", 12)
    )
    label_generar_reporte_ventas.grid(row=2, column=0, padx=10, pady=10)

    label_fecha_inicio = tk.Label(
        frame1, text="Fecha inicio", bg="#D4D4D4", font=("Arial", 12)
    )
    label_fecha_inicio.grid(row=3, column=0, padx=10, pady=10)

    entry_fecha_inicio = tk.Entry(frame1, font=("Arial", 12))
    entry_fecha_inicio.grid(row=3, column=1, padx=10, pady=10)

    label_fecha_fin = tk.Label(
        frame1, text="Fecha fin", bg="#D4D4D4", font=("Arial", 12)
    )
    label_fecha_fin.grid(row=4, column=0, padx=10, pady=10)

    entry_fecha_fin = tk.Entry(frame1, font=("Arial", 12))
    entry_fecha_fin.grid(row=4, column=1, padx=10, pady=10)

    button_salir = tk.Button(
        frame1,
        text="Salir",
        bg="#FF7E29",
        font=("Arial", 12),
        command=lambda: cerrar_ventana(window5, master),
    )
    button_salir.grid(row=6, column=1, padx=10, pady=10)

    estilo_tabla = ttk.Style()
    estilo_tabla.configure("mystyle.Treeview", rowheight=30)

    tabla = ttk.Treeview(
        frame2,
        columns=("Nombre", "Cantidad", "Costo", "Precio"),
        show="headings",
        style="mystyle.Treeview",
    )

    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Cantidad", text="Cantidad")
    tabla.heading("Costo", text="Costo")
    tabla.heading("Precio", text="Precio")

    tabla.column("Nombre", width=200)
    tabla.column("Cantidad", width=100)
    tabla.column("Costo", width=100)
    tabla.column("Precio", width=100)

    tabla.grid(row=0, column=0, padx=10, pady=10)

    button_generar_reporte_ventas = tk.Button(
        frame1,
        text="Generar",
        bg="#FF7E29",
        font=("Arial", 12),
        command=lambda: generar_reporte_ventas(
            entry_fecha_inicio.get(), entry_fecha_fin.get(), tabla
        ),
    )
    button_generar_reporte_ventas.grid(row=5, column=1, padx=10, pady=10)


def generar_reporte():
    try:
        with open("./tablas/productos.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(
                file,
                fieldnames=(
                    "id_producto",
                    "nombre",
                    "cantidad",
                    "costo",
                    "precio",
                    "f_vencimiento",
                ),
            )
            next(reader)
            productos_vencidos = []
            for row in reader:

                if (
                    datetime.strptime(
                        row["f_vencimiento"].replace("/", "-"), "%d-%m-%Y"
                    ).date()
                    < date.today()
                ):
                    productos_vencidos.append(row)
            with open(
                "./reportes/productos_vencidos.csv", "w", newline="", encoding="utf-8"
            ) as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=(
                        "id_producto",
                        "nombre",
                        "cantidad",
                        "costo",
                        "precio",
                        "f_vencimiento",
                    ),
                )
                writer.writeheader()
                for producto in productos_vencidos:
                    writer.writerow(producto)
    except FileNotFoundError:
        print("No se ha encontrado el archivo de productos")


def generar_reporte_ventas(fecha_inicio, fecha_fin, tabla):
    try:
        with open("./tablas/facturas.csv", "r", encoding="utf-8") as file:
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
            ventas = []

            for row in reader:
                fecha_venta = datetime.strptime(
                    row["fecha_venta"].replace("/", "-"), "%d-%m-%Y"
                ).date()
                if (
                    datetime.strptime(fecha_inicio, "%d/%m/%Y").date()
                    <= fecha_venta
                    <= datetime.strptime(fecha_fin, "%d/%m/%Y").date()
                ):
                    ventas.append(row)

            tabla.delete(*tabla.get_children())
            for venta in ventas:
                items = json.loads(venta["items"].replace("'", '"'))
                for item in items:
                    tabla.insert(
                        "",
                        tk.END,
                        values=(
                            item["name"],
                            item["quantity"],
                            item["unit_cost"],
                            item["unit_cost"] * item["quantity"],
                        ),
                    )
        with open(
            f"./reportes/ventas_{fecha_inicio.replace('/', '-')}_"
            f"{fecha_fin.replace('/', '-')}.csv",
            "w",
            newline="",
            encoding="utf-8",
        ) as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Cantidad", "Costo", "Precio"])
            suma = 0
            for venta in ventas:
                items = json.loads(venta["items"].replace("'", '"'))

                for item in items:
                    writer.writerow(
                        [
                            item["name"],
                            item["quantity"],
                            item["unit_cost"],
                            item["unit_cost"] * item["quantity"],
                        ]
                    )
                    suma += int(item["unit_cost"]) * int(item["quantity"])
            writer.writerow(["Total", "", "", suma])

    except FileNotFoundError:
        print("No se ha encontrado el archivo de facturas")


def cerrar_ventana(window, master):
    window.withdraw()
    master.deiconify()


if __name__ == "__main__":

    def cerrar_ventana(window, master):
        window.destroy()
        master.destroy()

    master = tk.Tk()
    master.title("GESTION DE NEGOCIO")
    master.withdraw()
    window5 = create_reports_window(master)
    window5.protocol("WM_DELETE_WINDOW", lambda: cerrar_ventana(window5, master))
    create_widgets_reports(window5, master)
    window5.mainloop()
