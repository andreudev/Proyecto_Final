import tkinter as tk


def create_products_window(master):
    products_window = tk.Toplevel(master)
    products_window.title("Productos")
    products_window.iconbitmap("./scr/icono_venta.ico")
    products_window.configure(bg="white")
    return products_window
