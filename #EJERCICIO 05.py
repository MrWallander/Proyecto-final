#EJERCICIO 05
import tkinter as tk
from tkinter import Toplevel
from tkinter import messagebox

ventana_principal= tk.Tk()
ventana_principal.title("ventana rancia")
ventana_principal.geometry("600x600")
etiqueta_1= tk.Label(text="seleccione una opcion")
etiqueta_1.pack(padx=20)
def abrir_ventana_autor():
    ventana_autor = Toplevel(ventana_principal)
    ventana_autor.title("Autor")
    ventana_autor.geometry("200x150")

    #La etiqueta en la ventana secundaria
    etiqueta_secundaria = tk.Label(ventana_autor, text="Autor: Raziel Wallander", font=("comic sans", 12))
    etiqueta_secundaria.pack(pady=20)
    boton_cerrar = tk.Button(ventana_autor, text="Cerrar", command=ventana_autor.destroy)
    boton_cerrar.pack(pady=20)






boton_abrir = tk.Button(ventana_principal, text="Abrir ventana secundaria", command=abrir_ventana_autor)
boton_abrir.pack(pady=20)





ventana_principal.mainloop()
