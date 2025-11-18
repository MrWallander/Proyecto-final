import tkinter as tk
#Crear la ventana principal
ventana = tk.Tk()
ventana.title("Actividad 15 De Raziel wallander")
ventana.geometry("400x300")
#Agregar una etiqueta
etiqueta = tk.Label(ventana, text="nombre y apellido:")
etiqueta.pack()

#Agregar campos de entrada
nombre = tk.Entry(ventana)
apellido = tk.Entry(ventana)

#Posicionar los campos de entrada
nombre.pack()
apellido.pack()

def mostrar_nombre():
 texto = nombre.get() + " " + apellido.get()
 etiqueta_resultado.config(text=f"{texto}")

etiqueta_resultado = tk.Label(ventana,font=("Arial", 14),fg="black")
etiqueta_resultado.pack(pady=20)

boton = tk.Button(ventana, text="Mostrar Nombre Completo", command=mostrar_nombre)
boton.pack()

ventana.mainloop()

