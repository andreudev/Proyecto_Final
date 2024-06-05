import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date


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

    boton_buscar_producto = tk.Button(
        frame1,
        text="Buscar",
        bg="blue",
        fg="white",
        font=("Arial", 12),
        width=10,
        height=1,
    )
    boton_buscar_producto.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

    label_documento_cliente = tk.Label(
        frame1, text="DOCUMENTO CLIENTE", bg="#D4D4D4", font=("Arial", 12)
    )
    label_documento_cliente.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
    entry_documento_cliente = tk.Entry(frame1, font=("Arial", 14))
    entry_documento_cliente.grid(row=5, column=1, padx=10, pady=10, sticky="nsew")

    boton_buscar_cliente = tk.Button(
        frame1,
        text="Buscar",
        bg="blue",
        fg="white",
        font=("Arial", 12),
        width=10,
        height=1,
    )
    boton_buscar_cliente.grid(row=5, column=2, padx=10, pady=10, sticky="nsew")

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
    entry_cantidad = tk.Entry(frame2, font=("Arial", 14), justify="center")
    entry_cantidad.grid(row=3, column=2, padx=10, pady=10)

    label_precio = tk.Label(frame2, text="PRECIO", bg="#D4D4D4", font=("Arial", 12))
    label_precio.grid(row=2, column=3, padx=10, pady=10)
    entry_precio = tk.Entry(frame2, font=("Arial", 14), justify="center")
    entry_precio.grid(row=3, column=3, padx=10, pady=10)

    boton_agregar = tk.Button(
        frame2,
        text="AGREGAR",
        bg="blue",
        fg="white",
        font=("Arial", 15),
        width=10,
        height=1,
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
    )

    boton_eliminar.grid(row=4, column=2, padx=10, pady=10)

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

    # Crear los botones de la parte inferior

    boton_guardar = tk.Button(
        frame2,
        text="GUARDAR",
        bg="green",
        fg="white",
        font=("Arial", 15),
        width=10,
        height=1,
    )
    boton_guardar.grid(row=6, column=1, padx=10, pady=10)

    boton_cancelar = tk.Button(
        frame2,
        text="CANCELAR",
        bg="red",
        fg="white",
        font=("Arial", 15),
        width=10,
        height=1,
    )

    boton_cancelar.grid(row=6, column=2, padx=10, pady=10)


def back_to_main_window(window4, master):
    window4.withdraw()
    master.deiconify()


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
