import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk

#Ejercicio 3 ,Creado por Raziel perez wallander
# --- Función para animar la imagen ---
def animate_image(label, image, start_y, end_y, step=5, delay=10):
    """
    Mueve la imagen en el Label desde start_y hasta end_y
    """
    def move(y):
        label.place(x=(ventana.winfo_width() - image.width()) // 2, y=y)
        if y > end_y:
            ventana.after(delay, lambda: move(y - step))
    move(start_y)

#la siguiente linea obtiene la ruta del directorio actual del script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
figure= {
    "cuadrado":os.path.join(BASE_DIR,"cuadro.png"),
    "rectangulo":os.path.join(BASE_DIR,"rectangulo.png"),
    "circulo":os.path.join(BASE_DIR,"circulo.png"),
    "triangulo":os.path.join(BASE_DIR,"triangulo.png")
}

def show_image(event):
    selected = list_figures.get(list_figures.curselection())
    route = figure.get(selected)
    image = Image.open(route)
    image = image.resize((200, 200))
    image_tk = ImageTk.PhotoImage(image)
    image_label.config(image=image_tk)
    image_label.image.image=image_tk
   # Posicionar la imagen fuera del marco inferior
    ventana.update()
    start_y = ventana.winfo_height()
    end_y = (ventana.winfo_height() - 150) // 2

    # Iniciar animación
    animate_image(image_label, image, start_y, end_y)


ventana = tk.Tk()
ventana.title("Visualizador de Figuras")
ventana.geometry("400x400")

titulo = tk.Label(ventana,text="selecciona una figura geometrica", font=("Arial", 14))
titulo.pack(pady=10)

list_figures = tk.Listbox(ventana, font=("Arial", 12), height=4)
for figura in figure.keys():
    list_figures.insert(tk.END, figura)
    list_figures.pack()

image_label = tk.Label(ventana)
image_label.pack(pady=20)
list_figures.bind("<<ListboxSelect>>", show_image)
ventana.mainloop()



    
