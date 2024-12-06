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


