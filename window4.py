import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date, datetime
import csv
from datetime import date
from invoice_pdf import ApiConnector
import json


def create_sales_window(master):
    sales_window = tk.Toplevel(master)
    sales_window.title("Ventas")
    sales_window.iconbitmap("./scr/icono_venta.ico")
    sales_window.configure(bg="white")
    return sales_window


def create_widgets_sales(window4, master):

    frame1 = tk.Frame(window4, bg="#D4D4D4")
    frame2 = tk.Frame(window4, bg="#D4D4D4", width=900, height=700)
    frame2.columnconfigure([0, 1, 2, 3], weight=1)
    # frame2.rowconfigure([0, 1, 2, 3, 4], weight=1)
    frame1.grid(row=0, column=0, sticky="nsew")
    frame2.grid(row=0, column=1, sticky="nsew")

    # Crear los widgets de la columna 1
    texto_principal = tk.Label(
        frame1,
        text="GESTION DE VENTAS",
        bg="#D4D4D4",
        font=("Arial", 20, "bold"),
    )
    texto_principal.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    label_id_producto = tk.Label(
        frame1, text="ID PRODUCTO", bg="#D4D4D4", font=("Arial", 12)
    )
    label_id_producto.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
    entry_id_producto = tk.Entry(frame1, font=("Arial", 14))
    entry_id_producto.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

    label_documento_cliente = tk.Label(
        frame1, text="DOCUMENTO CLIENTE", bg="#D4D4D4", font=("Arial", 12)
    )
    label_documento_cliente.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
    entry_documento_cliente = tk.Entry(frame1, font=("Arial", 14))
    entry_documento_cliente.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")

    boton_volver = tk.Button(
        frame1,
        text="Volver",
        bg="red",
        fg="white",
        font=("Arial", 15),
        width=10,
        height=1,
        command=lambda: back_to_main_window(window4, master),
    )
    boton_volver.grid(row=6, column=1, padx=10, pady=10, sticky="nsew")

    # Crear los widgets de la columna 2

    label_nombre_cliente = tk.Label(
        frame2, text="NOMBRE CLIENTE", bg="#D4D4D4", font=("Arial", 12)
    )
    label_nombre_cliente.grid(row=0, column=0, padx=10, pady=10)
    entry_nombre_cliente = tk.Entry(
        frame2, font=("Arial", 14), state="readonly", justify="center"
    )
    entry_nombre_cliente.grid(row=1, column=0, padx=10, pady=10)

    label_apellido_cliente = tk.Label(
        frame2, text="APELLIDO CLIENTE", bg="#D4D4D4", font=("Arial", 12)
    )
    label_apellido_cliente.grid(row=0, column=1, padx=10, pady=10)
    entry_apellido_cliente = tk.Entry(
        frame2, font=("Arial", 14), state="readonly", justify="center"
    )
    entry_apellido_cliente.grid(row=1, column=1, padx=10, pady=10)

    label_documento_cliente = tk.Label(
        frame2, text="DOCUMENTO CLIENTE", bg="#D4D4D4", font=("Arial", 12)
    )
    label_documento_cliente.grid(row=0, column=2, padx=10, pady=10)
    entry_documento_cliente_frame2 = tk.Entry(
        frame2, font=("Arial", 14), state="readonly", justify="center"
    )
    entry_documento_cliente_frame2.grid(row=1, column=2, padx=10, pady=10)

    label_fecha_venta = tk.Label(
        frame2, text="FECHA VENTA", bg="#D4D4D4", font=("Arial", 12)
    )
    label_fecha_venta.grid(row=0, column=3, padx=10, pady=10)

    entry_fecha_venta = tk.Entry(frame2, font=("Arial", 14), justify="center")
    entry_fecha_venta.grid(row=1, column=3, padx=10, pady=10)
    entry_fecha_venta.insert(0, date.today().strftime("%d/%m/%Y"))
    entry_fecha_venta.config(state="readonly")

    label_id_producto = tk.Label(
        frame2, text="ID PRODUCTO", bg="#D4D4D4", font=("Arial", 12)
    )
    label_id_producto.grid(row=2, column=0, padx=10, pady=10)
    entry_id_producto_frame2 = tk.Entry(
        frame2, font=("Arial", 14), state="readonly", justify="center"
    )
    entry_id_producto_frame2.grid(row=3, column=0, padx=10, pady=10)

    label_nombre_producto = tk.Label(
        frame2, text="NOMBRE PRODUCTO", bg="#D4D4D4", font=("Arial", 12)
    )
    label_nombre_producto.grid(row=2, column=1, padx=10, pady=10)

    entry_nombre_producto = tk.Entry(
        frame2, font=("Arial", 14), state="readonly", justify="center"
    )
    entry_nombre_producto.grid(row=3, column=1, padx=10, pady=10)

    label_cantidad = tk.Label(frame2, text="CANTIDAD", bg="#D4D4D4", font=("Arial", 12))
    label_cantidad.grid(row=2, column=2, padx=10, pady=10)
    entry_cantidad = tk.Entry(
        frame2, font=("Arial", 14), justify="center", state="readonly"
    )
    entry_cantidad.grid(row=3, column=2, padx=10, pady=10)

    label_precio = tk.Label(frame2, text="PRECIO", bg="#D4D4D4", font=("Arial", 12))
    label_precio.grid(row=2, column=3, padx=10, pady=10)
    entry_precio = tk.Entry(
        frame2, font=("Arial", 14), justify="center", state="readonly"
    )
    entry_precio.grid(row=3, column=3, padx=10, pady=10)

    # Crear la tabla

    estilo_tabla = ttk.Style()
    estilo_tabla.configure("Treeview", rowheight=30)

    tabla = ttk.Treeview(
        frame2,
        columns=("#1", "#2", "#3", "#4"),
        show="headings",
        height=10,
    )

    tabla.heading("#1", text="ID PRODUCTO")
    tabla.heading("#2", text="NOMBRE PRODUCTO")
    tabla.heading("#3", text="CANTIDAD")
    tabla.heading("#4", text="PRECIO")

    tabla.column("#1", width=200, anchor="center")
    tabla.column("#2", width=200, anchor="center")
    tabla.column("#3", width=200, anchor="center")
    tabla.column("#4", width=200, anchor="center")

    tabla.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

    scrollbar = ttk.Scrollbar(frame2, orient="vertical", command=tabla.yview)
    scrollbar.grid(row=5, column=4, sticky="ns")

    tabla.configure(yscrollcommand=scrollbar.set)

    # Crear los botones de la parte superior
    boton_agregar = tk.Button(
        frame2,
        text="AGREGAR",
        bg="blue",
        fg="white",
        font=("Arial", 15),
        width=10,
        height=1,
        command=lambda: add_product_to_table(
            entry_id_producto_frame2,
            entry_nombre_producto,
            entry_cantidad,
            entry_precio,
            tabla,
        ),
    )
    boton_agregar.grid(row=4, column=1, padx=10, pady=10)

    boton_eliminar = tk.Button(
        frame2,
        text="ELIMINAR",
        bg="red",
        fg="white",
        font=("Arial", 15),
        width=10,
        height=1,
        command=lambda: delete_product_from_table(tabla),
    )

    boton_eliminar.grid(row=4, column=2, padx=10, pady=10)
    # Crear los botones de la parte inferior

    label_pago_cliente = tk.Label(
        frame2, text="PAGO CLIENTE", bg="#D4D4D4", font=("Arial", 12)
    )
    label_pago_cliente.grid(row=6, column=0, padx=10, pady=10)
    entry_pago_cliente = tk.Entry(frame2, font=("Arial", 14))
    entry_pago_cliente.grid(row=6, column=1, padx=10, pady=10)
    boton_guardar = tk.Button(
        frame2,
        text="GUARDAR",
        bg="green",
        fg="white",
        font=("Arial", 15),
        width=10,
        height=1,
        command=lambda: save_sale(
            entry_documento_cliente.get(),
            entry_nombre_cliente.get(),
            entry_apellido_cliente.get(),
            entry_fecha_venta.get(),
            entry_pago_cliente.get(),
            tabla,
        ),
    )
    boton_guardar.grid(row=7, column=1, padx=10, pady=10)

    boton_cancelar = tk.Button(
        frame2,
        text="CANCELAR",
        bg="red",
        fg="white",
        font=("Arial", 15),
        width=10,
        height=1,
        command=lambda: cancel_sale(tabla),
    )

    boton_cancelar.grid(row=7, column=2, padx=10, pady=10)

    boton_buscar_cliente = tk.Button(
        frame1,
        text="Buscar",
        bg="blue",
        fg="white",
        font=("Arial", 12),
        width=10,
        height=1,
        command=lambda: client_search(
            entry_documento_cliente.get(),
            entry_nombre_cliente,
            entry_apellido_cliente,
            entry_documento_cliente_frame2,
        ),
    )
    boton_buscar_cliente.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")

    boton_buscar_producto = tk.Button(
        frame1,
        text="Buscar",
        bg="blue",
        fg="white",
        font=("Arial", 12),
        width=10,
        height=1,
        command=lambda: product_search(
            entry_id_producto.get(),
            entry_nombre_producto,
            entry_cantidad,
            entry_precio,
            entry_id_producto_frame2,
        ),
    )
    boton_buscar_producto.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")


def back_to_main_window(window4, master):
    window4.withdraw()
    master.deiconify()


def client_search(documento, entry_nombre, entry_apellido, entry_documento):
    if documento == "":
        messagebox.showerror("Error", "Ingrese un documento")
        return
    elif not documento.isdigit():
        messagebox.showerror("Error", "El documento debe ser un número")
        return
    else:
        # Buscar el cliente en la base de datos
        try:
            with open(
                "./tablas/clientes.csv", "r", newline="", encoding="utf-8"
            ) as file:
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
                rows = list(reader)
                for row in rows:
                    if row["documento"] == documento:
                        nombre = row["nombre"]
                        apellido = row["apellido"]
                        documento = row["documento"]
                        break
                else:
                    messagebox.showerror("Error", "Cliente no encontrado")
                    return
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró la base de datos de clientes")
            return

        entry_nombre.config(state="normal")
        entry_apellido.config(state="normal")
        entry_documento.config(state="normal")

        entry_nombre.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_documento.delete(0, tk.END)

        entry_nombre.insert(0, nombre)
        entry_apellido.insert(0, apellido)
        entry_documento.insert(0, documento)

        entry_nombre.config(state="readonly")
        entry_apellido.config(state="readonly")
        entry_documento.config(state="readonly")


def product_search(
    id_producto, entry_nombre, entry_cantidad, entry_precio, entry_id_producto
):

    if id_producto == "":
        messagebox.showerror("Error", "Ingrese un ID")
        return
    elif not id_producto.isdigit():
        messagebox.showerror("Error", "El ID debe ser un número")
        return
    else:
        # Buscar el producto en la base de datos
        try:
            with open(
                "./tablas/productos.csv", "r", newline="", encoding="utf-8"
            ) as file:
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
                rows = list(reader)
                for row in rows:

                    if row["id_producto"] == id_producto:
                        id = row["id_producto"]
                        nombre = row["nombre"]
                        cantidad = row["cantidad"]
                        precio = row["precio"]
                        if (
                            datetime.strptime(row["f_vencimiento"], "%d/%m/%Y").date()
                            < datetime.now().date()
                        ):
                            messagebox.showerror("Error", f"Producto {nombre} vencido")
                            return

                        break
                else:
                    messagebox.showerror("Error", "Producto no encontrado")
                    return
        except FileNotFoundError:
            messagebox.showerror(
                "Error", "No se encontró la base de datos de productos"
            )
            return

        entry_nombre.config(state="normal")
        entry_cantidad.config(state="normal")
        entry_precio.config(state="normal")
        entry_id_producto.config(state="normal")

        entry_nombre.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        entry_id_producto.delete(0, tk.END)

        entry_nombre.insert(0, nombre)
        entry_cantidad.insert(0, cantidad)
        entry_precio.insert(0, precio)
        entry_id_producto.insert(0, id)

        entry_nombre.config(state="readonly")
        entry_cantidad.config(state="normal")
        entry_precio.config(state="readonly")
        entry_id_producto.config(state="readonly")


def add_product_to_table(
    entry_id_producto_frame2, entry_nombre_producto, entry_cantidad, entry_precio, tabla
):
    id_producto = entry_id_producto_frame2.get()
    nombre_producto = entry_nombre_producto.get()
    cantidad = entry_cantidad.get()
    precio = entry_precio.get()

    try:
        with open("./tablas/productos.csv", "r", newline="", encoding="utf-8") as file:
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
            rows = list(reader)
            for row in rows:
                if row["id_producto"] == id_producto:
                    if int(row["cantidad"]) < int(cantidad):
                        messagebox.showerror(
                            "Error", "No hay suficiente cantidad de productos"
                        )
                        return
                    else:
                        row["cantidad"] = str(int(row["cantidad"]) - int(cantidad))
                    break
            else:
                messagebox.showerror("Error", "Producto no encontrado")
                return

        with open("./tablas/productos.csv", "w", newline="", encoding="utf-8") as file:
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
            writer.writerows(rows)

        for child in tabla.get_children():
            if tabla.item(child)["values"][0] == int(id_producto):
                messagebox.showerror("Error", "Producto ya agregado")
                return
        tabla.insert(
            "", tk.END, values=(id_producto, nombre_producto, cantidad, precio)
        )
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró la base de datos de productos")
        return


def delete_product_from_table(tabla):
    selected = tabla.selection()
    if not selected:
        messagebox.showerror("Error", "Seleccione un producto")
        return

    id_producto = tabla.item(selected)["values"][0]
    cantidad = tabla.item(selected)["values"][2]

    try:
        with open("./tablas/productos.csv", "r", newline="", encoding="utf-8") as file:
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
            rows = list(reader)
            for row in rows:
                if row["id_producto"] == str(id_producto):
                    row["cantidad"] = str(int(row["cantidad"]) + int(cantidad))
                    break
            else:
                messagebox.showerror("Error", "Producto no encontrado")
                return

        with open("./tablas/productos.csv", "w", newline="", encoding="utf-8") as file:
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
            writer.writerows(rows)
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró la base de datos de productos")
        return

    messagebox.showinfo("Info", "Producto eliminado")
    tabla.delete(selected)


def save_sale(documento, nombre, apellido, fecha, pago, tabla):
    if not documento:
        messagebox.showerror("Error", "Ingrese un documento")
        return
    elif not nombre:
        messagebox.showerror("Error", "Ingrese un nombre")
        return
    elif not fecha:
        messagebox.showerror("Error", "Ingrese una fecha")
        return
    elif not tabla.get_children():
        messagebox.showerror("Error", "Agregue productos a la venta")
        return

    items = []
    for child in tabla.get_children():
        items.append(
            {
                "name": tabla.item(child)["values"][1],
                "quantity": tabla.item(child)["values"][2],
                "unit_cost": tabla.item(child)["values"][3],
            }
        )
    total = 0
    for item in items:
        total += int(item["quantity"]) * int(item["unit_cost"])

    if int(pago) < total:
        messagebox.showerror("Error", "El pago no cubre el total de la venta")
        return

    messagebox.showinfo("Pago", f"El cambio es de {int(pago) - total} COP")

    try:
        with open("./tablas/facturas.csv", "r", newline="", encoding="utf-8") as file:
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
            rows = list(reader)
            try:
                last_id = int(rows[-1]["id_venta"])
            except IndexError:
                last_id = 0

    except FileNotFoundError:
        print("No se encontró la base de datos de facturas")

    with open("./tablas/facturas.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=(
                "id_venta",
                "nombre_cliente",
                "documento_cliente",
                "fecha_venta",
                "items",
            ),
        )
        writer.writerow(
            {
                "id_venta": last_id + 1,
                "nombre_cliente": f"{nombre} {apellido}",
                "documento_cliente": documento,
                "fecha_venta": fecha,
                "items": items,
            }
        )

        with open(
            f"./facturas/factura{last_id + 1}_{fecha.replace('/', '-')}.txt",
            "w",
            encoding="utf-8",
        ) as file:
            file.write(
                f"SUPER MUCHACHON S.A.S\n\n"
                f"ID VENTA: {last_id + 1}\n"
                f"NOMBRE CLIENTE: {nombre} {apellido}\n"
                f"DOCUMENTO CLIENTE: {documento}\n"
                f"FECHA VENTA: {fecha}\n"
                f"ITEMS:"
            )
            total = 0
            for item in items:
                file.write(
                    f"\n{item['name']:20} --- CANTIDAD {item['quantity']:5} --- {item['unit_cost']} COP"
                )
                total += int(item["quantity"]) * int(item["unit_cost"])
            file.write(f"\nTOTAL: {total} COP")

    api = ApiConnector()
    api.connect_api_and_save_invoice_pdf(
        "GESTOR DE VENTAS",
        f"{nombre} {apellido} - {documento}",
        last_id + 1,
        fecha.replace("/", "-"),
        items,
    )

    messagebox.showinfo("Info", "Venta guardada")

    for child in tabla.get_children():
        tabla.delete(child)


def cancel_sale(tabla):
    for child in tabla.get_children():
        try:
            with open(
                "./tablas/productos.csv", "r", newline="", encoding="utf-8"
            ) as file:
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
                rows = list(reader)
                for row in rows:
                    if row["id_producto"] == str(tabla.item(child)["values"][0]):
                        row["cantidad"] = str(
                            int(row["cantidad"]) + int(tabla.item(child)["values"][2])
                        )
                        break
                else:
                    messagebox.showerror("Error", "Producto no encontrado")
                    return

            with open(
                "./tablas/productos.csv", "w", newline="", encoding="utf-8"
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
                writer.writerows(rows)
        except FileNotFoundError:
            messagebox.showerror(
                "Error", "No se encontró la base de datos de productos"
            )
            return
        tabla.delete(child)


if __name__ == "__main__":

    def cerrar_ventana(window, master):
        window.destroy()
        master.destroy()

    master = tk.Tk()
    master.withdraw()
    window4 = create_sales_window(master)
    window4.protocol("WM_DELETE_WINDOW", lambda: cerrar_ventana(window4, master))
    create_widgets_sales(window4, master)
    window4.mainloop()
