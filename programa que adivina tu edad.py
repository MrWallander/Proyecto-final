import tkinter as tk
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Widgets en Tkinter")
ventana.geometry("300x200")

# Etiqueta de texto
etiqueta = tk.Label(ventana, text="Escribe tu edad y adivinaré tu edad", font=("Arial", 12))
etiqueta.pack(pady=10)

# Cuadro de texto
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

# Botón que responde a un evento
def mostrar_texto():
    texto = entrada.get()
    etiqueta_resultado.config(text=f"tu edad es: {texto}")

boton = tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=5)

# Iniciar el loop principal
ventana.mainloop()
