import customtkinter as ctk
from PIL import Image, ImageTk
import pandas as pd


ventana = ctk.CTk()
ventana.geometry("1366x768")
ctk.set_appearance_mode("dark")
ventana.title("Pantallas")

fondo_registro = Image.open("INTERFAZ_REGISTRO_USUARIO.png").resize((1500, 800), Image.LANCZOS)
fondo1_tk = ImageTk.PhotoImage(fondo_registro)
pagina_registro = ctk.CTkFrame(ventana, width=1366, height=768, fg_color="transparent")

etiqueta_fondo_registro = ctk.CTkLabel(pagina_registro, image=fondo1_tk, text="")
etiqueta_fondo_registro.place(relwidth=1, relheight=1)
titulo_registro = ctk.CTkLabel(pagina_registro, text="BIENVENIDO", font=('Zen Dots', 30, 'bold'), fg_color="#32ade6", text_color="black")
titulo_registro.place(relx=0.20, rely=0.3)
registro_usuario = ctk.CTkEntry(pagina_registro, placeholder_text="Registre datos de Usuario", width=300, corner_radius=10, font=('Squada One', 16), fg_color="white", bg_color="#32ADE6", text_color="black", justify="center")
registro_usuario.place(relx=0.3, rely=0.5, anchor='center')
registro_password = ctk.CTkEntry(pagina_registro, placeholder_text="Registre datos de su Password", width=300, corner_radius=10, show="*", font=('Squada One', 16), fg_color="white", bg_color="#32ADE6", text_color="black", justify="center")
registro_password.place(relx=0.3, rely=0.6, anchor='center')
guardar = ctk.CTkButton(pagina_registro, text="Guardar", width=100, height=50, corner_radius=10, command=None, font=('Squada One', 20), bg_color="#32ADE6", fg_color="#32ADE6")
guardar.place(relx=0.3, rely=0.75, anchor='center')
pagina_registro.pack(fill="both", expand=True)
ventana.mainloop()
