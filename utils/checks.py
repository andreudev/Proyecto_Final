from tkinter import messagebox


def check_digit(id_producto, nombre_producto, cantidad, costo, precio, f_vencimiento):
    if (
        not id_producto
        or not nombre_producto
        or not cantidad
        or not costo
        or not precio
        or not f_vencimiento
    ):
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return False
    elif not id_producto.isdigit():
        messagebox.showerror("Error", "El ID debe ser un número")
        return False
    elif not cantidad.isdigit():
        messagebox.showerror("Error", "La cantidad debe ser un número")
        return False
    elif not costo.isdigit():
        messagebox.showerror("Error", "El costo debe ser un número")
        return False
    elif not precio.isdigit():
        messagebox.showerror("Error", "El precio debe ser un número")
        return False
    return True
