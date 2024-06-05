from tkinter import messagebox


def check_digit_product(
    id_producto, nombre_producto, cantidad, costo, precio, f_vencimiento
):
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
    elif not is_float(costo):
        messagebox.showerror("Error", "El costo debe ser un número")
        return False
    elif not precio.isdigit():
        messagebox.showerror("Error", "El precio debe ser un número")
        return False
    return True


def check_digit_client(nombre, apellido, fecha_nacimiento, documento):
    if not nombre or not apellido or not fecha_nacimiento or not documento:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return False
    elif not documento.isdigit():
        messagebox.showerror("Error", "El documento debe ser un número")
        return False
    return True


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
