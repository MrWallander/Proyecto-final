#ejercicio 2 inicio de sesion
import tkinter as tk
from tkinter import messagebox
from tkinter import font
#funcion para verificar la contraseña

#crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de Sesion")
ventana.geometry("500x250")
ventana.configure(bg="#A3AFF0") # color de fondo claro
#fuente personalizada
fuente_titulo = font.Font(family="comic sans ms", size=14, 
                          weight="bold")
fuente_normal = font.Font(family="helvetica", size=12)
# Marco centrado
marco = tk.Frame(ventana, bg="#ffffff", bd=2, relief="groove")
marco.place(relx=0.5, rely=0.5, anchor="center")


etiqueta = tk.Label(marco, text="Ingrese su contraseña:", bg="#ffffff", font=fuente_normal)

etiqueta.pack(padx=20, pady=(15,5))

entrada_password = tk.Entry(marco, show="*", font=fuente_normal, width=25, bd=2, relief="solid")
entrada_password.pack(padx=20, pady=10)
#funcion para verificar la contraseña
#nueva ventana y verificacion 
def verificar_password():

    password = entrada_password.get()
    if password == "JOJO":
        # Cierra la ventana de login
        ventana.destroy()

        # Crea la nueva ventana de bienvenida
        ventana_bienvenida = tk.Tk()
        ventana_bienvenida.title("Sistema")
        ventana_bienvenida.geometry("400x200")
        ventana_bienvenida.configure(bg="#50348a")

        # Mensaje de bienvenida
        etiqueta_bienvenida = tk.Label(
            ventana_bienvenida,
            text="¡Bienvenido al sistema wallander!",
            font=fuente_titulo,
            bg="#f3f3f3",
            pady=20
        )
        etiqueta_bienvenida.pack(expand=True)

        # Inicia el bucle para la nueva ventana
        ventana_bienvenida.mainloop()

    else:
        messagebox.showerror("Acceso", "Acceso denegado")

boton_verificar = tk.Button(marco, text="verificar", command=verificar_password,bg="#9B83D2", fg="white", font=fuente_normal, bd=0, relief="raised", padx=10, pady=5)
boton_verificar.pack(pady=10)



ventana.mainloop()

