import tkinter as tk
import os
from tkinter import ttk
from PIL import Image, ImageTk

# Ejercicio 3, Creado por Raziel Perez Wallander

# --- Función para animar la imagen ---
def animate_image(label, image_tk, start_y, end_y, step=5, delay=10):
    """
    Mueve la imagen en el Label desde start_y hasta end_y
    """
    def move(y):
        # Centra horizontalmente la imagen
        label.place(x=(ventana.winfo_width() - image_tk.width()) // 2, y=y)
        if y > end_y:
            ventana.after(delay, lambda: move(y - step))
    move(start_y)


# --- Diccionario de figuras ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
figure = {
    "cuadrado": os.path.join(BASE_DIR, "cuadro.png"),
    "rectangulo": os.path.join(BASE_DIR, "rectangulo.png"),
    "circulo": os.path.join(BASE_DIR, "circulo.png"),
    "triangulo": os.path.join(BASE_DIR, "triangulo.png"),
    "THEWORLD": os.path.join(BASE_DIR, "THEWORLD.png"),
    
}


# --- Función para mostrar la imagen seleccionada ---
def show_image(event):
    try:
        selected = list_figures.get(list_figures.curselection())
    except tk.TclError:
        return  # evita error si no hay selección

    route = figure.get(selected)
    image = Image.open(route)
    image = image.resize((200, 200))
    image_tk = ImageTk.PhotoImage(image)

    # Mostrar imagen en el label (corrección: se guarda referencia)
    image_label.config(image=image_tk)
    image_label.image = image_tk

    # Posicionar la imagen fuera del marco inferior
    ventana.update()
    start_y = ventana.winfo_height()
    end_y = (ventana.winfo_height() - 200) // 2  # posición final centrada

    # Iniciar animación
    animate_image(image_label, image_tk, start_y, end_y)


# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Visualizador de Figuras")
ventana.geometry("400x400")

titulo = tk.Label(ventana, text="Selecciona una figura geométrica", font=("Arial", 14))
titulo.pack(pady=10)

# --- Listbox con las figuras ---
list_figures = tk.Listbox(ventana, font=("Arial", 12), height=4)
for figura in figure.keys():
    list_figures.insert(tk.END, figura)
list_figures.pack()

# --- Label para mostrar la imagen ---
image_label = tk.Label(ventana, bg="white")
image_label.place(x=0, y=0)

# --- Evento al seleccionar ---
list_figures.bind("<<ListboxSelect>>", show_image)

ventana.mainloop()