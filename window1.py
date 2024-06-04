import tkinter as tk
from window2 import create_clients_window, create_widgets_clients
from window3 import create_products_window, create_widgets_products
from window4 import create_sales_window
from window5 import create_reports_window


def create_main_window():
    """
    Crear la ventana principal de la aplicación

    Returns:
        tk.Tk: Ventana principal de la aplicación
    """
    # Crear la ventana principal
    main_window = tk.Tk()
    main_window.title("GESTION DE NEGOCIO")
    main_window.iconbitmap("./scr/icono_venta.ico")
    main_window.configure(bg="white")
    main_window.resizable(0, 0)

    # Crear las ventanas secundarias
    window2 = create_clients_window(main_window)
    window3 = create_products_window(main_window)
    window4 = create_sales_window(main_window)
    window5 = create_reports_window(main_window)

    # Crear la ventana de clientes
    # window_show_clients = show_clients()

    # Ocultar las ventanas secundarias
    window2.withdraw()
    window3.withdraw()
    window4.withdraw()
    window5.withdraw()

    # Crear los widgets de la ventana principal
    create_widgets(main_window, window2, window3, window4, window5)

    return main_window


def create_widgets_main_window(main_window, window2, window3, window4, window5):
    """
    Crear los widgets de la ventana principal

    Args:
        main_window (tk.Tk): Ventana principal de la aplicación
        window2 (tk.Toplevel): Ventana de clientes
        window3 (tk.Toplevel): Ventana de productos
        window4 (tk.Toplevel): Ventana de ventas
        window5 (tk.Toplevel): Ventana de reportes
    """
    # Crear los widgets de ventana principal
    texto_principal = tk.Label(
        main_window,
        text="BIENVENIDO A GESTION DE NEGOCIO",
        bg="white",
        font=("Arial", 20, "bold"),
    )
    texto_principal.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    boton_clientes = tk.Button(
        main_window,
        text="Clientes",
        bg="blue",
        fg="white",
        font=("Arial", 18),
        width=10,
        height=2,
        command=lambda: show_clients_window(window2, master=main_window),
    )
    boton_clientes.grid(row=1, column=1, padx=10, pady=10)

    boton_productos = tk.Button(
        main_window,
        text="Productos",
        bg="blue",
        fg="white",
        font=("Arial", 18),
        width=10,
        height=2,
        command=window3.deiconify,
    )
    boton_productos.grid(row=2, column=1, padx=10, pady=10)

    boton_ventas = tk.Button(
        main_window,
        text="Ventas",
        bg="blue",
        fg="white",
        font=("Arial", 18),
        width=10,
        height=2,
        command=window4.deiconify,
    )
    boton_ventas.grid(row=3, column=1, padx=10, pady=10)

    boton_reportes = tk.Button(
        main_window,
        text="Reportes",
        bg="blue",
        fg="white",
        font=("Arial", 18),
        width=10,
        height=2,
        command=window5.deiconify,
    )
    boton_reportes.grid(row=4, column=1, padx=10, pady=10)

    boton_salir = tk.Button(
        main_window,
        text="Salir",
        bg="red",
        fg="white",
        font=("Arial", 18),
        width=10,
        height=2,
        command=main_window.destroy,
    )
    boton_salir.grid(row=5, column=1, padx=10, pady=10)


def create_widgets(main_window, window2, window3, window4, window5):
    """
    Crear los widgets de la ventana principal
    Args:
        main_window (tk.Tk): Ventana principal de la aplicación
        window2 (tk.Toplevel): Ventana de clientes
        window3 (tk.Toplevel): Ventana de productos
        window4 (tk.Toplevel): Ventana de ventas
        window5 (tk.Toplevel): Ventana de reportes
    """

    # Llamar a la función que crea los widgets de la ventana principal
    create_widgets_main_window(main_window, window2, window3, window4, window5)
    # Llamar a la función que crea los widgets de la ventana clientes
    create_widgets_clients(window2, main_window)
    # Llamar a la función que crea los widgets de la ventana productos
    create_widgets_products(window3, main_window)


def show_clients_window(window2, master):
    """
    Mostrar la ventana de clientes y ocultar la ventana principal

    Args:
        window2 (tk.Toplevel): Ventana de clientes
        master (tk.Tk): Ventana principal de la aplicación
    """
    window2.deiconify()
    master.withdraw()
