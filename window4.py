import tkinter as tk
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
