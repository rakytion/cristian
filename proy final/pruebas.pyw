import tkinter as tk
from PIL import Image, ImageTk

def on_button_click():
    print("¡Botón clickeado!")

# Crear una instancia de la ventana
ventana = tk.Tk()

# Cargar la imagen utilizando Pillow (PIL)
ruta_imagen = "proy final\logo.ico"
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((100, 100))  # Cambiar el tamaño de la imagen si es necesario

# Convertir la imagen a un formato compatible con tkinter
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear un botón y agregar la imagen
boton_con_imagen = tk.Button(ventana, image=imagen_tk, command=on_button_click)
boton_con_imagen.pack()

# Iniciar el bucle de eventos
ventana.mainloop()