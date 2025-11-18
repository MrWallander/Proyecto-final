#REPASO DE LA ACT 15
import tkinter as tk

# Para crear la ventana principal
ventana = tk.Tk()
ventana.title("Repaso Act 15")
ventana.geometry("400x300")

#Agregar un label
label = tk.Label(ventana, text="Escribe tu edad y adivinare tu edad")
label.pack()

#Agregar un entry
Edad = tk.Entry(ventana)
Edad.pack()
#posicionar el entry
Edad.pack()
def adivinar_edad():
    textto = Edad.get()
    label.config(text=f"Tu edad es {textto} años")
#Boton
boton = tk.Button(ventana, text="Adivinar edad", command=adivinar_edad)
boton.pack()

ventana.mainloop()


