import customtkinter as ctk
from PIL import Image, ImageTk
import pandas as pd
import os
import serial
import threading
import json
import time
import sys

ser = None
lectura_hilo = None

def inicializar_puerto_serial():
    global ser
    try:
        ser = serial.Serial('COM3', 9600, timeout=2)  # Cambia 'COM6' al puerto serial que estás utilizando
    except serial.SerialException as e:
        print("Error al abrir el puerto serial:", e)

def leer_datos_serial():
    global ser
    while True:
        if ser and ser.is_open:
            try:
                data = ser.readline().decode().strip()  
                if data:
                    try:
                        json_data = json.loads(data)  
                        actualizar_entradas(json_data)  
                    except json.JSONDecodeError:
                        print("Error al decodificar JSON:", data)
            except serial.SerialException as e:
                print("Error en la lectura del puerto serial:", e)
        else:
            time.sleep(2)  

def actualizar_entradas(data):
    """Actualiza las entradas de la interfaz con los datos recibidos del Arduino."""
    if 'datos1' in data:
        datos1.delete(0, ctk.END)
        datos1.insert(0, str(data['datos1']))
    if 'datos2' in data:
        datos2.delete(0, ctk.END)
        datos2.insert(0, str(data['datos2']))
    if 'datos3' in data:
        datos3.delete(0, ctk.END)
        datos3.insert(0, str(data['datos3']))
    if 'datos4' in data:
        datos4.delete(0, ctk.END)
        datos4.insert(0, str(data['datos4']))        

def procesar_registro():
    usuario = registro_usuario.get()
    contraseña = registro_password.get()
    RegistrarDatos(usuario, contraseña)
    pantalla_login()

def VerificarExistencia():
    return os.path.isfile('usuarios.json')

def RegistrarDatos(usuario, contraseña):
    if VerificarExistencia():
        datos = pd.read_json('usuarios.json')
    else:
        datos = pd.DataFrame(columns=['Usuario', 'Contraseña'])
    nuevosDatos = pd.DataFrame({'Usuario': [usuario], 'Contraseña': [contraseña]})
    datos = pd.concat([datos, nuevosDatos], ignore_index=True)
    datos.to_json('usuarios.json', orient='records', indent=4)

def IniciarSesion(usuario, contraseña):
    if VerificarExistencia():
        datos = pd.read_json("usuarios.json")
        datos['Contraseña'] = datos['Contraseña'].astype(str)
        if usuario in datos['Usuario'].values:
            usuarioIndice = datos.index[datos['Usuario'] == usuario][0]
            if datos.at[usuarioIndice, 'Contraseña'] == contraseña:
                return True
            else:
                return 0
        else:
            return 0
    else:
        return 0

def ocultar():
    paginas = [pagina_inicio, pagina_registro, pagina_login, pagina_datos]
    for pagina in paginas:
        pagina.pack_forget()

def mostrar(pagina):
    ocultar()
    pagina.pack(fill='both', expand=True)

def pantalla_inicio():
    mostrar(pagina_inicio)

def pantalla_registro():
    mostrar(pagina_registro)

def pantalla_login():
    mostrar(pagina_login)
def pantalla_datos():
    mostrar(pagina_datos)

# Procesar el inicio de sesión
def procesar_inicio_sesion():
    usuario = entrada_usuario.get() 
    contraseña = entrada_password.get()
    if not usuario or not contraseña:
        mensaje_error.set("Usuario o contraseña no proporcionados")
    else:
        if IniciarSesion(usuario, contraseña):
            pantalla_datos()
        else:
            mensaje_error.set("Usuario o contraseña incorrectos")

ventana = ctk.CTk()
ventana.geometry("1100x600")
ctk.set_appearance_mode("dark")
ventana.title("Mecaguys")

# Cargar las imágenes de fondo 
fondo1 = Image.open("INTERFAZ_BIENVENIDA.png").resize((1900, 1000), Image.LANCZOS)
fondo1_tk = ImageTk.PhotoImage(fondo1)

fondo2 = Image.open("INTERFAZ_INICIO_SESION.png").resize((1900, 1000), Image.LANCZOS)
fondo2_tk = ImageTk.PhotoImage(fondo2)

fondo3 = Image.open("INTERFAZ_REGISTRO_USUARIO.png").resize((1900, 1000), Image.LANCZOS)
fondo3_tk = ImageTk.PhotoImage(fondo3)

#Hacer transparentes los frames
pagina_inicio = ctk.CTkFrame(ventana, width=1500, height=800, fg_color="transparent")
pagina_inicio = ctk.CTkFrame(ventana, width=1500, height=800, fg_color="transparent")
pagina_registro = ctk.CTkFrame(ventana, width=1500, height=800, fg_color="transparent")
pagina_login = ctk.CTkFrame(ventana, width=1500, height=800, fg_color="transparent")

pagina_datos = ctk.CTkFrame(ventana, width=1500, height=800, fg_color="transparent")

# Agregar la imagen de fondo 
etiqueta_fondo_inicio = ctk.CTkLabel(pagina_inicio, image=fondo1_tk, text="")
etiqueta_fondo_inicio.place(relwidth=1, relheight=1)

etiqueta_fondo_login = ctk.CTkLabel(pagina_login, image=fondo2_tk, text="")
etiqueta_fondo_login.place(relwidth=1, relheight=1)

etiqueta_fondo_registro = ctk.CTkLabel(pagina_registro, image=fondo3_tk, text="")
etiqueta_fondo_registro.place(relwidth=1, relheight=1)

etiqueta_fondo_datos = ctk.CTkLabel(pagina_datos, image=fondo3_tk, text="")
etiqueta_fondo_datos.place(relwidth=1, relheight=1)

# inicio
boton_bienvenida = ctk.CTkButton(pagina_inicio, text="BIENVENIDOS", font=('Yeah Papa', 30), width=100,corner_radius=11, command=pantalla_login, fg_color="#31A1C9", bg_color="#31A1C9",text_color="black")
boton_bienvenida.place(relx=0.5, rely=0.9, anchor='center') 

#login
mensaje_error = ctk.StringVar()
titulo_login = ctk.CTkLabel(pagina_login, text="Inicio de sesión", font=('Yeah Papa', 55), fg_color="#32ade6", text_color="black")
titulo_login.place(relx=0.5, rely=0.35, anchor='center')
mensaje = ctk.CTkLabel(pagina_login, textvariable=mensaje_error, font=('Zen Dots', 14), text_color="white", fg_color="#32ADE6", bg_color="#32ADE6")
mensaje.place(relx=0.5, rely=0.4, anchor='center')
entrada_usuario = ctk.CTkEntry(pagina_login, placeholder_text="Ingrese datos de Usuario", width=300, corner_radius=10, font=('Squada One', 20), fg_color="white", bg_color="#32ADE6", text_color="black", justify="center"
                               , border_width=3)
entrada_usuario.place(relx=0.5, rely=0.5, anchor='center')
entrada_password = ctk.CTkEntry(pagina_login, placeholder_text="Ingrese datos de su Password", width=300, corner_radius=10, font=('Squada One', 20), fg_color="white", bg_color="#32ADE6", text_color="black", justify="center"
                                , border_width=3)
entrada_password.place(relx=0.5, rely=0.6, anchor='center')
boton_iniciar_sesion = ctk.CTkButton(pagina_login, text="Iniciar Sesión", width=250, height=50, corner_radius=10,  command=procesar_inicio_sesion, font=('Squada One', 22), bg_color="#32ADE6", fg_color="#32ADE6")
boton_iniciar_sesion.place(relx=0.5, rely=0.735, anchor='center') 
boton_registrarse = ctk.CTkButton(pagina_login, text="Registrarse", width=250, height=50, corner_radius=10, command=pantalla_registro, font=('Squada One', 22), bg_color="#32ADE6", fg_color="#32ADE6")
boton_registrarse.place(relx=0.5, rely=0.8, anchor='center')

#registro
titulo_registro = ctk.CTkLabel(pagina_registro, text="Craación de cuenta", font=('Yeah Papa', 55, 'bold'), fg_color="#32ade6", text_color="black")
titulo_registro.place(relx=0.21, rely=0.3)
registro_usuario = ctk.CTkEntry(pagina_registro, placeholder_text="Registre datos de Usuario", width=300, corner_radius=10, font=('Squada One', 20), fg_color="white", bg_color="#32ADE6", text_color="black", justify="center"
                                , border_width=3)
registro_usuario.place(relx=0.3, rely=0.5, anchor='center')
registro_password = ctk.CTkEntry(pagina_registro, placeholder_text="Registre datos de su Password", width=300, corner_radius=10, show="*", font=('Squada One', 20), fg_color="white", bg_color="#32ADE6", text_color="black", justify="center"
                                 , border_width=3)
registro_password.place(relx=0.3, rely=0.6, anchor='center')
iniciar_sesion = ctk.CTkButton(pagina_registro, text="Guardar", width=250, height=50, corner_radius=10, command=procesar_registro, font=('Squada One', 22), bg_color="#32ADE6", fg_color="#32ADE6")
iniciar_sesion.place(relx=0.3, rely=0.75, anchor='center')


#pantalla de datos
datos1 = ctk.CTkEntry(pagina_datos, placeholder_text="Presencia A", width=250, height=50, corner_radius=15, font=('Squada One', 20), fg_color="white", bg_color="#32ade6", text_color="black", justify='center')
datos1.place(relx=0.2, rely=0.4, anchor='center')

datos2 = ctk.CTkEntry(pagina_datos, placeholder_text="Presencia B", width=250, height=50, corner_radius=15, font=('Squada One', 20), fg_color="white", bg_color="#32ade6", text_color="black", justify='center')
datos2.place(relx=0.4, rely=0.4, anchor='center')

datos3 = ctk.CTkEntry(pagina_datos, placeholder_text="Luminosidad 1", width=250, height=50, corner_radius=15, font=('Squada One', 20), fg_color="white", bg_color="#32ade6", text_color="black", justify='center')
datos3.place(relx=0.2, rely=0.6, anchor='center')

datos4 = ctk.CTkEntry(pagina_datos, placeholder_text="Luminosidad 2", width=250, height=50, corner_radius=15, font=('Squada One', 20), fg_color="white", bg_color="#32ade6", text_color="black", justify='center')
datos4.place(relx=0.4, rely=0.6, anchor='center')

boton_guardar = ctk.CTkButton(pagina_datos, text="GUARDAR", width=200, height=40, corner_radius=10, font=('Squada One', 30), command=lambda: [guardar_datos_csv()], fg_color="#32ADE6", bg_color="#32ade6")
boton_guardar.place(relx=0.9, rely=0.9, anchor='center')

boton_menu = ctk.CTkButton(pagina_datos, text="Volver al Inicio", width=200, height=40, corner_radius=10, font=('Squada One', 30), command=pantalla_inicio, fg_color="#32ADE6", bg_color="#32ade6")
boton_menu.place(relx=0.1, rely=0.9, anchor='center')
pantalla_inicio()

# Ejecuta la función para leer datos serial en un hilo aparte después de cargar la interfaz
def iniciar_lectura_serial():
    global lectura_hilo
    inicializar_puerto_serial()
    lectura_hilo = threading.Thread(target=leer_datos_serial, daemon=True)
    lectura_hilo.start()

ventana.after(1000, iniciar_lectura_serial)
def guardar_datos_csv():
    """Recoge los datos de los campos y guarda en un archivo CSV."""
    data = {
        "Presencia A": datos1.get(),
        "Presencia B": datos2.get(),
        "Luminosidad 1": datos3.get(),
        "Luminosidad 2": datos4.get(),
    }
    df = pd.DataFrame([data])
    file_path = ctk.filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*")],
        title="Guardar datos como"
    )
    if file_path:
        df.to_csv(file_path, index=False)
        print(f"Datos guardados en {file_path}")
def resource_path(relative_path):
    
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
path_bienvenida = resource_path("INTERFAZ_BIENVENIDA.png")
image_bienvenida = Image.open(path_bienvenida)

path_inicio_sesion = resource_path("INTERFAZ_INICIO_SESION.png")
image_inicio_sesion = Image.open(path_inicio_sesion)

path_registro_usuario = resource_path("INTERFAZ_REGISTRO_USUARIO.png")
image_registro_usuario = Image.open(path_registro_usuario)


ventana.mainloop()

