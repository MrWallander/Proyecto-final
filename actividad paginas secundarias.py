import tkinter as tk
from tkinter import Toplevel

#Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana principal")
ventana_principal.geometry("300x200")

#Función para abrir una ventana secundaria
def abrir_ventana_secundaria():
    ventana_secundaria = Toplevel(ventana_principal)
    ventana_secundaria.title("Ventana secundaria")
    ventana_secundaria.geometry("200x150")

    #La etiqueta en la ventana secundaria
    etiqueta_secundaria = tk.Label(ventana_secundaria, text="esta es la ventana secundaria", font=("comic sans", 12))
    etiqueta_secundaria.pack(pady=20)
    boton_cerrar_secundaria = tk.Button(ventana_secundaria, text="Cerrar", command=ventana_secundaria.destroy)

#boton de la ventana principal
boton_abrir = tk.Button(ventana_principal, text="Abrir ventana secundaria", command=abrir_ventana_secundaria)
boton_abrir.pack(pady=20)

#Iniciar el bucle principal de la interfaz
ventana_principal.mainloop()

