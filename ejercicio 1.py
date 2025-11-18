#ejercicio 1
#Creado por: Raziel perez wallander
import tkinter as TK

ventana=TK.Tk()
ventana.title("ejercicio 1: sumar")
ventana.geometry("400x200")

entrada1=TK.Entry(ventana)
entrada2=TK.Entry(ventana)
entrada1.pack(pady=5)
entrada2.pack(pady=5)
def sumar():
    try:
        num1 =int(entrada1.get())
        num2 =int(entrada2.get())
        suma = num1 + num2
        resultado.config(text=f"Resultado: {suma}")
    except ValueError:
        resultado.config(text="Escribe solo numeros")

boton_resta = TK.Button(ventana, text="Restar", command=lambda: restar())
boton_resta.pack(pady=5)
def restar():
    try:
        num1 =int(entrada1.get())
        num2 =int(entrada2.get())
        resta = num1 - num2
        resultado.config(text=f"Resultado: {resta}")
    except ValueError:
        resultado.config(text="Escribe solo numeros")

boton_multiplicar = TK.Button(ventana, text="Multiplicar", command=lambda: multiplicar())
boton_multiplicar.pack(pady=5)

def multiplicar():
    try:
        num1 =int(entrada1.get())
        num2 =int(entrada2.get())
        multiplicacion = num1 * num2
        resultado.config(text=f"Resultado: {multiplicacion}")
    except ValueError:
        resultado.config(text="Escribe solo numeros")

boton_multiplicar = TK.Button(ventana, text="Multiplicar", command=lambda: multiplicar())
boton_multiplicar.pack(pady=5)

boton_dividir = TK.Button(ventana, text="Dividir", command=lambda: dividir())
boton_dividir.pack(pady=5)
def dividir():
    try:
        num1 =int(entrada1.get())
        num2 =int(entrada2.get())
        if num2 == 0:
            resultado.config(text="Error: Division por cero")
        else:
            division = num1 / num2
            resultado.config(text=f"Resultado: {division}")
    except ValueError:
        resultado.config(text="Escribe solo numeros")
        




resultado=TK.Label(ventana, text="Resultado: ")
resultado.pack(pady=5)


ventana.mainloop()