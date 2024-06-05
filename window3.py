import tkinter as tk
from tkinter import ttk, messagebox
import csv
from utils.checks import check_digit_product


def create_products_window(master):
    products_window = tk.Toplevel(master)
    products_window.title("Productos")
    products_window.iconbitmap("./scr/icono_venta.ico")
    products_window.configure(bg="white")
    return products_window


def create_widgets_products(window3, master):

    frame1 = tk.Frame(window3, bg="#D4D4D4")
    frame2 = tk.Frame(window3, bg="#D4D4D4", width=900, height=700)
    frame1.grid(row=0, column=0, sticky="nsew")
    frame2.grid(row=0, column=1, sticky="nsew")

    texto_principal = tk.Label(
        frame1,
        text="GESTION DE PRODUCTOS",
        bg="#D4D4D4",
        font=("Arial", 20, "bold"),
    )

    texto_principal.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    texto_id_producto = tk.Label(
        frame1, text="ID Producto", bg="#D4D4D4", font=("Arial", 12), justify="left"
    )
    texto_id_producto.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    entry_id_producto = tk.Entry(frame1, font=("Arial", 12), width=20, justify="center")

    entry_id_producto.grid(row=1, column=1, padx=10, pady=10)

    texto_nombre_producto = tk.Label(
        frame1, text="Nombre Producto", bg="#D4D4D4", font=("Arial", 12), justify="left"
    )

    texto_nombre_producto.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    entry_nombre_producto = tk.Entry(
        frame1, font=("Arial", 12), width=20, justify="center"
    )

    entry_nombre_producto.grid(row=2, column=1, padx=10, pady=10)

    texto_cantidad_producto = tk.Label(
        frame1, text="Cantidad", bg="#D4D4D4", font=("Arial", 12), justify="left"
    )

    texto_cantidad_producto.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    entry_cantidad_producto = tk.Entry(
        frame1, font=("Arial", 12), width=20, justify="center"
    )

    entry_cantidad_producto.grid(row=3, column=1, padx=10, pady=10)

    texto_costo_compra = tk.Label(
        frame1, text="Costo de compra", bg="#D4D4D4", font=("Arial", 12), justify="left"
    )

    texto_costo_compra.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    entry_costo_compra = tk.Entry(
        frame1, font=("Arial", 12), width=20, justify="center"
    )

    entry_costo_compra.grid(row=4, column=1, padx=10, pady=10)

    texto_precio_venta = tk.Label(
        frame1, text="Precio de venta", bg="#D4D4D4", font=("Arial", 12), justify="left"
    )

    texto_precio_venta.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    entry_precio_venta = tk.Entry(
        frame1, font=("Arial", 12), width=20, justify="center"
    )

    entry_precio_venta.grid(row=5, column=1, padx=10, pady=10)

    text_fecha_vencimiento = tk.Label(
        frame1,
        text="Fecha de vencimiento",
        bg="#D4D4D4",
        font=("Arial", 12),
        justify="left",
    )

    text_fecha_vencimiento.grid(row=6, column=0, padx=10, pady=10, sticky="w")

    entry_fecha_vencimiento = tk.Entry(
        frame1, font=("Arial", 12), width=20, justify="center"
    )

    entry_fecha_vencimiento.grid(row=6, column=1, padx=10, pady=10)

    # Boton guardar
    boton_guardar = tk.Button(
        frame1,
        text="Guardar producto",
        bg="blue",
        fg="white",
        font=("Arial", 14),
        width=15,
        height=1,
        command=lambda: save_product(
            entry_id_producto.get(),
            entry_nombre_producto.get(),
            entry_cantidad_producto.get(),
            entry_costo_compra.get(),
            entry_precio_venta.get(),
            entry_fecha_vencimiento.get(),
        ),
    )

    boton_guardar.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Boton actualizar
    boton_actualizar = tk.Button(
        frame1,
        text="Actualizar",
        bg="blue",
        fg="white",
        font=("Arial", 14),
        width=15,
        height=1,
        command=lambda: update_product(
            entry_id_producto.get(),
            entry_nombre_producto.get(),
            entry_cantidad_producto.get(),
            entry_costo_compra.get(),
            entry_precio_venta.get(),
            entry_fecha_vencimiento.get(),
        ),
    )

    boton_actualizar.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
    # Boton eliminar
    boton_eliminar = tk.Button(
        frame1,
        text="Eliminar",
        bg="blue",
        fg="white",
        font=("Arial", 14),
        width=15,
        height=1,
        command=lambda: delete_product(entry_id_producto.get()),
    )

    boton_eliminar.grid(row=9, column=0, columnspan=2, padx=10, pady=10)
    # Boton volver
    boton_volver = tk.Button(
        frame1,
        text="Volver",
        bg="red",
        fg="white",
        font=("Arial", 14),
        width=15,
        height=1,
        command=lambda: back_to_main_window(window3, master),
    )

    boton_volver.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

    # Configuracion de la tabla

    tabla = tk.Label(
        frame2,
        text="Tabla de productos",
        bg="#D4D4D4",
        font=("Arial", 20),
        width=50,
        height=2,
        justify="center",
    )

    tabla.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    estilo_tabla = ttk.Style()
    estilo_tabla.configure("Treeview", rowheight=30)
    tabla_productos = ttk.Treeview(
        frame2,
        columns=("ID", "Nombre", "Cantidad", "Costo", "Precio", "Vencimiento"),
        show="headings",
        height=13,
    )

    tabla_productos.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Configuracion de las columnas
    tabla_productos.heading("ID", text="ID")
    tabla_productos.heading("Nombre", text="Nombre")
    tabla_productos.heading("Cantidad", text="Cantidad")
    tabla_productos.heading("Costo", text="Costo")
    tabla_productos.heading("Precio", text="Precio")
    tabla_productos.heading("Vencimiento", text="Vencimiento")
    # Configuracion de los anchos de las columnas
    tabla_productos.column("ID", width=50, anchor="center")
    tabla_productos.column("Nombre", width=150, anchor="center")
    tabla_productos.column("Cantidad", width=100, anchor="center")
    tabla_productos.column("Costo", width=100, anchor="center")
    tabla_productos.column("Precio", width=100, anchor="center")
    tabla_productos.column("Vencimiento", width=100, anchor="center")

    tabla_productos.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    scrollbar = tk.Scrollbar(frame2, orient="vertical", command=tabla_productos.yview)
    scrollbar.grid(row=1, column=1, sticky="nse")

    tabla_productos.config(yscrollcommand=scrollbar.set)

    boton_refrescar = tk.Button(
        frame2,
        text="Refrescar",
        bg="blue",
        fg="white",
        font=("Arial", 14),
        width=15,
        height=1,
        command=lambda: refresh_table(tabla_productos),
    )

    boton_refrescar.grid(row=2, column=0, padx=10, pady=10)
    # Cargar datos de productos

    try:
        with open("./tablas/productos.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(
                file,
                fieldnames=(
                    "id_producto",
                    "nombre_producto",
                    "cantidad",
                    "costo",
                    "precio",
                    "f_vencimiento",
                ),
            )
            next(reader)
            for row in reader:
                tabla_productos.insert(
                    "",
                    "end",
                    values=(
                        row["id_producto"],
                        row["nombre_producto"],
                        row["cantidad"],
                        row["costo"],
                        row["precio"],
                        row["f_vencimiento"],
                    ),
                )

    except Exception as e:
        print(e)


def refresh_table(tabla_productos):
    """
    Funcion para refrescar la tabla de productos

    Args:
        tabla_productos (tk.ttk.Treeview): Tabla de productos
    """

    tabla_productos.delete(*tabla_productos.get_children())
    try:
        with open("./tablas/productos.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(
                file,
                fieldnames=(
                    "id_producto",
                    "nombre_producto",
                    "cantidad",
                    "costo",
                    "precio",
                    "f_vencimiento",
                ),
            )
            next(reader)
            for row in reader:
                tabla_productos.insert(
                    "",
                    "end",
                    values=(
                        row["id_producto"],
                        row["nombre_producto"],
                        row["cantidad"],
                        row["costo"],
                        row["precio"],
                        row["f_vencimiento"],
                    ),
                )

    except Exception as e:
        print(e)


def back_to_main_window(window3, master):
    """
    Funcion para volver a la ventana principal

    Args:
        window3 (tk.Toplevel): Ventana de productos
        master (tk.Tk): Ventana principal
    """
    window3.withdraw()
    master.deiconify()


def save_product(id_producto, nombre_producto, cantidad, costo, precio, f_vencimiento):
    """
    Funcion para guardar un producto

    Args:
        id_producto (str): ID del producto
        nombre_producto (str): Nombre del producto
        cantidad (str): Cantidad del producto
        costo (str): Costo del producto
        precio (str): Precio del producto
        f_vencimiento (str): Fecha de vencimiento del producto
    """
    try:
        with open("./tablas/productos.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(
                file,
                fieldnames=(
                    "id_producto",
                    "nombre_producto",
                    "cantidad",
                    "costo",
                    "precio",
                    "f_vencimiento",
                ),
            )
            next(reader)
            for row in reader:
                if row["id_producto"] == id_producto:
                    messagebox.showerror("Error", "El producto ya existe")
                    return
    except Exception as e:
        print(e)

    try:

        if not check_digit_product(
            id_producto, nombre_producto, cantidad, costo, precio, f_vencimiento
        ):
            return

        with open("./tablas/productos.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=(
                    "id_producto",
                    "nombre_producto",
                    "cantidad",
                    "costo",
                    "precio",
                    "f_vencimiento",
                ),
            )
            writer.writerow(
                {
                    "id_producto": id_producto,
                    "nombre_producto": nombre_producto,
                    "cantidad": cantidad,
                    "costo": costo,
                    "precio": precio,
                    "f_vencimiento": f_vencimiento,
                }
            )
            messagebox.showinfo("Guardado", "Producto guardado con exito")
    except Exception as e:
        print(e)


def update_product(
    id_producto, nombre_producto, cantidad, costo, precio, f_vencimiento
):
    """
    Funcion para actualizar un producto

    Args:
        id_producto (str): ID del producto
        nombre_producto (str): Nombre del producto
        cantidad (str): Cantidad del producto
        costo (str): Costo del producto
        precio (str): Precio del producto
        f_vencimiento (str): Fecha de vencimiento del producto
    """
    try:
        if not check_digit_product(
            id_producto, nombre_producto, cantidad, costo, precio, f_vencimiento
        ):
            return
        else:
            with open(
                "./tablas/productos.csv", "r", newline="", encoding="utf-8"
            ) as file:
                reader = csv.DictReader(
                    file,
                    fieldnames=(
                        "id_producto",
                        "nombre_producto",
                        "cantidad",
                        "costo",
                        "precio",
                        "f_vencimiento",
                    ),
                )
                next(reader)
                rows = list(reader)
                for row in rows:
                    # print(row)
                    if row["id_producto"] == id_producto:
                        break
                else:
                    messagebox.showerror("Error", "El producto no existe")
                    return
            with open(
                "./tablas/productos.csv", "w", newline="", encoding="utf-8"
            ) as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=(
                        "id_producto",
                        "nombre_producto",
                        "cantidad",
                        "costo",
                        "precio",
                        "f_vencimiento",
                    ),
                )
                writer.writeheader()
                for row in rows:
                    # print(row)
                    if row["id_producto"] == id_producto:
                        # print("Actualizando producto", id_producto)
                        writer.writerow(
                            {
                                "id_producto": id_producto,
                                "nombre_producto": nombre_producto,
                                "cantidad": cantidad,
                                "costo": costo,
                                "precio": precio,
                                "f_vencimiento": f_vencimiento,
                            }
                        )
                    else:
                        writer.writerow(
                            {
                                "id_producto": row["id_producto"],
                                "nombre_producto": row["nombre_producto"],
                                "cantidad": row["cantidad"],
                                "costo": row["costo"],
                                "precio": row["precio"],
                                "f_vencimiento": row["f_vencimiento"],
                            }
                        )
                messagebox.showinfo("Actualizado", "Producto actualizado con exito")
    except Exception as e:
        print(e)


def delete_product(id_producto):
    """
    Funcion para eliminar un producto

    Args:
        id_producto (str): ID del producto
    """

    try:
        if not id_producto:
            messagebox.showerror("Error", "El campo ID es obligatorio")
            return
        else:
            with open(
                "./tablas/productos.csv", "r", newline="", encoding="utf-8"
            ) as file:
                reader = csv.DictReader(
                    file,
                    fieldnames=(
                        "id_producto",
                        "nombre_producto",
                        "cantidad",
                        "costo",
                        "precio",
                        "f_vencimiento",
                    ),
                )
                next(reader)
                rows = list(reader)
                for row in rows:
                    if row["id_producto"] == id_producto:
                        break
                else:
                    messagebox.showerror("Error", "El producto no existe")
                    return
    except Exception as e:
        print(e)

    try:
        with open("./tablas/productos.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=(
                    "id_producto",
                    "nombre_producto",
                    "cantidad",
                    "costo",
                    "precio",
                    "f_vencimiento",
                ),
            )
            writer.writeheader()
            for row in rows:
                if row["id_producto"] == id_producto:
                    continue
                writer.writerow(
                    {
                        "id_producto": row["id_producto"],
                        "nombre_producto": row["nombre_producto"],
                        "cantidad": row["cantidad"],
                        "costo": row["costo"],
                        "precio": row["precio"],
                        "f_vencimiento": row["f_vencimiento"],
                    }
                )
            messagebox.showinfo("Eliminado", "Producto eliminado con exito")
    except Exception as e:
        print(e)
