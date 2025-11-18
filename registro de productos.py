import tkinter as tk
from tkinter import messagebox

def ventana_registro():
    ventana_registro=tk.Toplevel(ventana_principal)
    ventana_registro.title("Ventana de Registro de Productos")
    ventana_registro.geometry("700x600")
    #Etiquetas
    etiqueta=tk.Label(ventana_registro, text="ingrese el producto", font=("Arial", 12), fg="black")
    etiqueta.pack()
    entrada_producto = tk.Entry(ventana_registro, width=50)
    entrada_producto.pack(pady=10)
    etiqueta_precio = tk.Label(ventana_registro, text="ingrese el precio", font=("Arial", 12), fg="black")
    etiqueta_precio.pack()
    entrada_precio = tk.Entry(ventana_registro, width=50)
    entrada_precio.pack(pady=10)
    etiqueta_cantidad = tk.Label(ventana_registro, text="ingrese la cantidad", font=("Arial", 12), fg="black")
    etiqueta_cantidad.pack()
    entrada_cantidad = tk.Entry(ventana_registro, width=50)
    entrada_cantidad.pack(pady=10)
    def show_message():
        producto = entrada_producto.get()
        precio = entrada_precio.get()
        cantidad = entrada_cantidad.get()
        mensaje = f"Producto: {producto}\nPrecio: {precio}\nCantidad: {cantidad}"
        messagebox.showinfo("Producto Registrado", mensaje)
    boton_registrar = tk.Button(ventana_registro, text="Registrar Producto", command=show_message)
    boton_registrar.pack(pady=20)


ventana_principal = tk.Tk()
ventana_principal.title("Registro de productos")
ventana_principal.geometry("400x300")
etiqueta_nombre = tk.Label(ventana_principal, text="presiona el boton para registrar un producto:")
etiqueta_nombre.pack(pady=10)
boton_abrir = tk.Button(ventana_principal, text="Abrir ventana de registro", command=ventana_registro)
boton_abrir.pack(pady=20)


ventana_principal.mainloop()
