import customtkinter as ctk
from PIL import Image, ImageTk
import pandas as pd
import os
import serial
import threading
import json
import time
import sys

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
