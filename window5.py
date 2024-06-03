import tkinter as tk


def create_reports_window(master):
    reports_window = tk.Toplevel(master)
    reports_window.title("Reportes")
    reports_window.iconbitmap("./scr/icono_venta.ico")
    reports_window.configure(bg="white")
    return reports_window
