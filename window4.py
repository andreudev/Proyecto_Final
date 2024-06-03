import tkinter as tk


def create_sales_window(master):
    sales_window = tk.Toplevel(master)
    sales_window.title('Ventas')
    sales_window.iconbitmap('./scr/icono_venta.ico')
    sales_window.configure(bg='white')
    return sales_window
