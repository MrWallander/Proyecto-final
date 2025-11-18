import tkinter as tk
from tkinter import messagebox

def calcular_promedios():
    for i in range(len(filas)):
        try:
            cal1 = float(filas[i][1].get())
            cal2 = float(filas[i][2].get())
            cal3 = float(filas[i][3].get())
            promedio = (cal1 + cal2 + cal3) / 3
            filas[i][4].config(text=f"{promedio:.2f}")
        except ValueError:
            messagebox.showerror("error",f"Calificaciones invalidas")

ventana = tk.Tk()
ventana.title("Boleta de calificaciones")
ventana.geometry("600x400")

tk.Label(ventana, text="Nombre del Alumno").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.grid(row=0, column=1, columnspan=4,sticky="we")

# Encabezados de la tabla
encabezados = ["Materia","Uidad1","Unidad2","Unidad3","Promedio"]
for col, encabezado in enumerate(encabezados):
    tk.label(ventana, text=encabezado,
             font=('Arial',10,'bold')).grind(row=1,column=col,padx=5,pady=5)
filas = []



ventana.mainloop()                                 
