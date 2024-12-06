import customtkinter as ctk
from PIL import Image  # Para trabajar con imágenes
import tkinter as tk
import csv  # Para crear el archivo que guardará los datos

# Crear la ventana principal
ventana = ctk.CTk()
ventana.title("MECA GUYS")
ventana.geometry("1500x800")  # Ancho x Alto

# Cargar imagen de fondo
imagen_inicio = ctk.CTkImage(Image.open('INTERFAZ_INICIO_SESION.png'), size=(1300, 800))
label_fondo = ctk.CTkLabel(ventana, text='', image=imagen_inicio)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Crear un marco más alto para los elementos de inicio de sesión
frame_inicio = ctk.CTkFrame(ventana, corner_radius=11, width=400, height=700, fg_color="#32ADE6", bg_color="#32ADE6")
frame_inicio.place(relx=0.5, rely=0.75, anchor='center')

# Etiqueta y entrada para usuario
entry_usuario = ctk.CTkEntry(frame_inicio, placeholder_text="Ingresa Su Usuario", width=300)
entry_usuario.place(relx=0.5, rely=0.15, anchor='center')  

# Etiqueta y entrada para contraseña
entry_contraseña = ctk.CTkEntry(frame_inicio, placeholder_text="Ingrese Su Contraseña", show="*", width=300)
entry_contraseña.place(relx=0.5, rely=0.36, anchor='center')  

# Botón de iniciar sesión
boton_iniciar = ctk.CTkButton(frame_inicio, text="Iniciar Sesión", width=300)
boton_iniciar.place(relx=0.5, rely=0.5, anchor='center')  

# Botón de registro
boton_registrar = ctk.CTkButton(frame_inicio, text="Registrar", width=300)
boton_registrar.place(relx=0.5, rely=0.58, anchor='center')


# Iniciar la aplicación
ventana.mainloop()

