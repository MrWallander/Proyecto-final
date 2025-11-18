import tkinter as tk
from tkinter import messagebox



def calcular_ventas():
    for i in range(len(filas)):
        try:
            costo = float(filas[i][1].get())
            precio = float(filas[i][2].get())
            venta = float(filas[i][3].get())
            venta_final = (costo + precio + venta) / 3
            filas[i][4].config(text=f"{calcular_ventas:.2f}")
        except ValueError:
            messagebox.showerror("error",f"informacion invalida")

ventana = tk.Tk()
ventana.title("venta de productos")
ventana.geometry("600x400")
# Nombre del alumno
tk.Label(ventana, text="Nombre del cliente:").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(ventana, width=40)
entry_nombre.grid(row=0, column=1, columnspan=4, sticky="we")

# Encabezados de tabla
encabezados = ["producto", "costo", "precio", "cantidad", "total"]
for col, encabezado in enumerate(encabezados):
   tk.Label(ventana, text=encabezado, font=('Arial', 10, 'bold')).grid(row=1, column=col, padx=5, pady=5)
filas = []
for i in range(3):
    fila=[]
    #aqui va la materia
    entry_materia = tk.Entry(ventana)
    entry_materia.grid(row=i+2, column=0, padx=5, pady=5)
    fila.append(entry_materia)
    
    #Calificaciones
    for j in range(1,4):
        entry_cal=tk.Entry(ventana, width=10)
        entry_cal.grid(row=i+2, column=j, padx=5, pady=5)
        fila.append(entry_cal)
        label_promedio = tk.Label(ventana, text="uwu")

#promedios
btn_promedio = tk.Button(ventana, text="calcular", command=calcular_ventas)
btn_promedio.grid(row=7, column=0, columnspan=5, pady=10)




ventana.mainloop()
