import tkinter as tk
from tkinter import ttk, messagebox
import csv


def create_clients_window(master):
    """
    Crear la ventana de clientes

    Args:
        master (tk.Tk): Ventana principal de la aplicación

    Returns:
        tk.Toplevel: Ventana de clientes
    """
    clients_window = tk.Toplevel(master)
    clients_window.title("Clientes")
    clients_window.iconbitmap("./scr/icono_venta.ico")
    clients_window.configure(bg="white")
    return clients_window


def create_widgets_clients(window2, master):
    """
    Crear los widgets de la ventana clientes

    Args:
        window2 (tk.Toplevel): Ventana de clientes
        master (tk.Tk): Ventana principal de la aplicación
    """
    # Crear dos frames en la ventana clientes
    frame1 = tk.Frame(window2, bg="#D4D4D4")
    frame2 = tk.Frame(window2, bg="#D4D4D4", width=900, height=700)
    frame1.grid(row=0, column=0, sticky="nsew")
    frame2.grid(row=0, column=1, sticky="nsew")
    # frame2.columnconfigure(0, weight=1)

    # Crear los widgets de la ventana clientes
    texto_clientes = tk.Label(
        frame1, text="GESTION DE CLIENTES", bg="#D4D4D4", font=("Arial", 20, "bold")
    )
    texto_clientes.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    texto_nombre_cliente = tk.Label(
        frame1, text="NOMBRE", bg="#D4D4D4", font=("Arial", 14)
    )
    texto_nombre_cliente.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
    entry_nombre_cliente = tk.Entry(frame1, font=("Arial", 14), justify="center")
    entry_nombre_cliente.grid(row=2, column=0, padx=10, pady=10, columnspan=3)
    texto_apellido_cliente = tk.Label(
        frame1, text="APELLIDO", bg="#D4D4D4", font=("Arial", 14)
    )
    texto_apellido_cliente.grid(row=3, column=0, padx=10, pady=10, columnspan=3)
    entry_apellido_cliente = tk.Entry(frame1, font=("Arial", 14), justify="center")
    entry_apellido_cliente.grid(row=4, column=0, padx=10, pady=10, columnspan=3)
    texto_fecha_nacimiento = tk.Label(
        frame1, text="FECHA DE NACIMIENTO", bg="#D4D4D4", font=("Arial", 14)
    )
    texto_fecha_nacimiento.grid(row=5, column=0, padx=10, pady=10, columnspan=3)
    entry_fecha_nacimiento = tk.Entry(frame1, font=("Arial", 14), justify="center")
    entry_fecha_nacimiento.grid(row=6, column=0, padx=10, pady=10, columnspan=3)
    texto_documento = tk.Label(
        frame1, text="DOCUMENTO", bg="#D4D4D4", font=("Arial", 14)
    )
    texto_documento.grid(row=7, column=0, padx=10, pady=10, columnspan=3)
    entry_documento = tk.Entry(frame1, font=("Arial", 14), justify="center")
    entry_documento.grid(row=8, column=0, padx=10, pady=10, columnspan=3)
    boton_guardar_cliente = tk.Button(
        frame1,
        text="Guardar Cliente",
        bg="blue",
        fg="white",
        font=("Arial", 14),
        width=15,
        height=1,
        command=lambda: save_client(
            entry_nombre_cliente.get(),
            entry_apellido_cliente.get(),
            entry_fecha_nacimiento.get(),
            entry_documento.get(),
        ),
    )
    boton_guardar_cliente.grid(row=9, column=0, padx=10, pady=10, columnspan=3)
    boton_volver = tk.Button(
        frame1,
        text="Volver",
        bg="red",
        fg="white",
        font=("Arial", 14),
        width=15,
        height=1,
        command=lambda: back_to_main(window2),
    )
    boton_volver.grid(row=10, column=0, padx=10, pady=10, columnspan=3)

    # Crear los widgets de la lista de clientes
    texto_lista_clientes = tk.Label(
        frame2,
        text="LISTA DE CLIENTES",
        bg="#D4D4D4",
        font=("Arial", 20, "bold"),
        width=50,
        height=2,
        justify="center",
    )
    texto_lista_clientes.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    estilo_tabla = ttk.Style()
    estilo_tabla.configure("Treeview", rowheight=30)
    tabla_clientes = ttk.Treeview(
        frame2,
        columns=("ID", "Nombre", "Apellido", "Fecha de Nacimiento", "Documento"),
        height=20,
        show="headings",
    )
    tabla_clientes.column("ID", width=150, anchor="center")
    tabla_clientes.column("Nombre", width=150, anchor="center")
    tabla_clientes.column("Apellido", width=150, anchor="center")
    tabla_clientes.column("Fecha de Nacimiento", width=150, anchor="center")
    tabla_clientes.column("Documento", width=150, anchor="center")
    tabla_clientes.heading("ID", text="ID", anchor="center")
    tabla_clientes.heading("Nombre", text="Nombre", anchor="center")
    tabla_clientes.heading("Apellido", text="Apellido", anchor="center")
    tabla_clientes.heading(
        "Fecha de Nacimiento", text="Fecha de Nacimiento", anchor="center"
    )
    tabla_clientes.heading("Documento", text="Documento", anchor="center")
    tabla_clientes.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)
    scrollbar = ttk.Scrollbar(frame2, orient="vertical", command=tabla_clientes.yview)
    scrollbar.grid(row=1, column=2, sticky="nse")
    tabla_clientes.configure(yscrollcommand=scrollbar.set)

    # Mostrar los clientes en la tabla
    try:
        with open("./tablas/clientes.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(
                file,
                fieldnames=(
                    "id_cliente",
                    "nombre",
                    "apellido",
                    "fecha_nacimiento",
                    "documento",
                ),
            )
            next(reader)
            for row in reader:
                tabla_clientes.insert(
                    "",
                    "end",
                    values=(
                        row["id_cliente"],
                        row["nombre"],
                        row["apellido"],
                        row["fecha_nacimiento"],
                        row["documento"],
                    ),
                )
    except Exception as e:
        print("Error al abrir el archivo", e)
    boton_refrescar = tk.Button(
        frame2,
        text="Refrescar",
        bg="blue",
        fg="white",
        font=("Arial", 14),
        width=15,
        height=1,
        command=lambda: show_clients(tabla_clientes),
    )
    boton_refrescar.grid(row=0, column=1, padx=10, pady=10)


def show_clients(tabla_clientes):
    """
    Mostrar los clientes en la tabla

    Args:
        tabla_clientes (ttk.Treeview): Tabla de clientes
    """
    for i in tabla_clientes.get_children():
        tabla_clientes.delete(i)
    try:
        with open("./tablas/clientes.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(
                file,
                fieldnames=(
                    "id_cliente",
                    "nombre",
                    "apellido",
                    "fecha_nacimiento",
                    "documento",
                ),
            )
            next(reader)
            for row in reader:
                tabla_clientes.insert(
                    "",
                    "end",
                    values=(
                        row["id_cliente"],
                        row["nombre"],
                        row["apellido"],
                        row["fecha_nacimiento"],
                        row["documento"],
                    ),
                )
    except Exception as e:
        print("Error al abrir el archivo", e)


def save_client(nombre, apellido, fecha_nacimiento, documento):
    """
    Guardar un cliente en el archivo clientes.csv

    Args:
        nombre (str): Nombre del cliente
        apellido (str): Apellido del cliente
        fecha_nacimiento (str): Fecha de nacimiento del cliente
        documento (str): Documento del cliente
    """
    try:
        with open("./tablas/clientes.csv", "r", newline="", encoding="utf-8") as file:

            reader = csv.DictReader(
                file,
                fieldnames=(
                    "id_cliente",
                    "nombre",
                    "apellido",
                    "fecha_nacimiento",
                    "documento",
                ),
            )
            next(reader)
            for row in reader:
                if row["documento"] == documento:
                    messagebox.showerror(
                        "Error", "El documento ya se encuentra registrado"
                    )
                    return
                id_cliente = int(row["id_cliente"])
    except Exception as e:
        print("Error al abrir el archivo", e)
    try:

        if nombre == "" or apellido == "" or fecha_nacimiento == "" or documento == "":
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        else:
            with open(
                "./tablas/clientes.csv", "a", encoding="utf-8", newline=""
            ) as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=(
                        "id_cliente",
                        "nombre",
                        "apellido",
                        "fecha_nacimiento",
                        "documento",
                    ),
                )
                if id_cliente == 0:
                    writer.writeheader()
                writer.writerow(
                    {
                        "id_cliente": id_cliente + 1,
                        "nombre": nombre,
                        "apellido": apellido,
                        "fecha_nacimiento": fecha_nacimiento,
                        "documento": documento,
                    }
                )
                messagebox.showinfo("Exito", "Cliente guardado correctamente")
    except Exception as e:
        print("Error al abrir el archivo", e)


def back_to_main(window2):
    """
    Volver a la ventana principal

    Args:
        master (tk.Tk): Ventana principal de la aplicación
        window2 (tk.Toplevel): Ventana de clientes
    """
    window2.withdraw()
