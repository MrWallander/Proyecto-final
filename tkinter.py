import tkinter as tk
ventana = tk.Tk()
#configurar la ventana
ventana.title("ejemplo de widget")
ventana.geometry("300x200")

#etiqueta texto
etiqueta = tk.Label(ventana, text="Escribe:", font=("Arial", 12)),
etiqueta.pack(pady=10)

#campo de texto
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=10)


#iniciar la ventana
ventana.mainloop()


