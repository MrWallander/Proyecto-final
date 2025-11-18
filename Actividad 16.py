import tkinter as TK
ventana_principal = TK.Tk()
ventana_principal.title("Actividad 16")
ventana_principal.geometry("500x500")

def abrir_ventana_uno():
 ventana_uno=TK.Toplevel(ventana_principal)
 ventana_uno.title("Ventana Uno")
 ventana_uno.geometry("200x150")
 #Etiquetas
 etiqueta=TK.Label(ventana_uno, text="Raziel perez Wallander", font=("Arial", 12), fg="black")
 etiqueta.pack()
 boton_cerrar_secundaria = TK.Button(ventana_uno, text="Cerrar", command=ventana_uno.destroy)
 boton_cerrar_secundaria.pack()

def abrir_ventana_dos():
    ventana_dos=TK.Toplevel(ventana_principal)
    ventana_dos.title("Ventana Dos")
    ventana_dos.geometry("200x150")
    #Etiquetas
    etiqueta=TK.Label(ventana_dos, text="Programado con Python", font=("Arial", 12), fg="black")
    etiqueta.pack()
    boton_cerrar_secundaria = TK.Button(ventana_dos, text="Cerrar", command=ventana_dos.destroy)
    boton_cerrar_secundaria.pack()

boton_abrir=TK.Button(ventana_principal, text="Abrir Ventana Uno", command=abrir_ventana_uno)
boton_abrir.pack(pady=20)
boton_abrir_dos=TK.Button(ventana_principal, text="Abrir Ventana Dos", command=abrir_ventana_dos)
boton_abrir_dos.pack(pady=20)
ventana_principal.mainloop()