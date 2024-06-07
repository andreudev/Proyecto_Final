import tkinter as tk
import csv
from datetime import date, datetime


def create_reports_window(master):
    reports_window = tk.Toplevel(master)
    reports_window.title("Reportes")
    reports_window.iconbitmap("./scr/icono_venta.ico")
    reports_window.configure(bg="white")
    return reports_window


def create_widgets_reports(window5, master):

    frame1 = tk.Frame(window5, bg="#D4D4D4")
    frame1.grid(row=0, column=0, sticky="nsew")

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
