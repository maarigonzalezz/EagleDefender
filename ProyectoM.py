import json
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import shutil
import os
import pygame, sys
from pygame.locals import *
import math
from PIL import Image, ImageTk

# VENTANA PRINCIPAL
ventanaP = tk.Tk()
ventanaP.title("Eagle Defender")
ventanaP.geometry("987x629")
ventanaP.resizable(False, False)


def abrir_ventana_registro():
    # VENTANA DE REGISTRO
    ventanaP.withdraw()
    ventana_registro = tk.Toplevel(ventanaP)
    ventana_registro.title("Registro")
    ventana_registro.geometry("400x400")

    canvas_registro = tk.Canvas(ventana_registro, width=400, height=650, bg="black")
    canvas_registro.pack()

    # Campos para ingresar información
    tk.Label(canvas_registro, text="Nombre de Usuario:").place(x=50, y=50)
    entry_usuario = tk.Entry(canvas_registro)
    entry_usuario.place(x=200, y=50)

    tk.Label(canvas_registro, text="Correo:").place(x=50, y=100)
    entry_correo = tk.Entry(canvas_registro)
    entry_correo.place(x=200, y=100)

    tk.Label(canvas_registro, text="Contraseña (máx. 10 caracteres):").place(x=50, y=150)
    entry_contrasena = tk.Entry(canvas_registro, show="*")
    entry_contrasena.place(x=200, y=150)

    def registrar_usuario():
        # Obtener los valores de los campos
        nombre_usuario = entry_usuario.get()
        correo = entry_correo.get()
        contrasena = entry_contrasena.get()

        # Verificar que no haya dos usuarios con el mismo nombre
        if nombre_usuario in usuarios_registrados:
            messagebox.showerror("Registro", "Usuario ya existente. Por favor elija otro.")

        # Verificar que no haya campos en blanco
        elif not nombre_usuario or not correo or not contrasena:
            messagebox.showerror("Registro", "Por favor rellene todos los espacios")

        elif len(contrasena) >= 8:
            messagebox.showerror("Registro", "La contraseña no puede ser mayor de 8 caracteres")

        #Guardar datos
        else:
            nuevo_usuario = {
                "nombre_usuario": nombre_usuario,
                "correo": correo,
                "contrasena": contrasena,
                # Agrega más campos según sea necesario
            }

            # Guardar el nuevo usuario en el archivo JSON
            with open("usuarios.json", "a") as file:
                json.dump(nuevo_usuario, file)
                file.write("\n")  # Agregar salto de línea para separar usuarios


    def cargar_imagen():
        # Abrir un cuadro de diálogo para seleccionar la imagen
        ruta_imagen = filedialog.askopenfilename(title="Seleccionar imagen")
        # Podrías almacenar la ruta en la base de datos o hacer algo con la imagen aquí


    tk.Button(canvas_registro, text="Cargar Imagen", command=cargar_imagen).place(x=50, y=200)
    tk.Button(canvas_registro, text="Guardar", command=registrar_usuario).place(x=200, y=200)



usuarios_registrados = []  # Puedes cargar los usuarios existentes al inicio

btn_registrar = tk.Button(ventanaP, text="Registrar", command=abrir_ventana_registro).place(relx=0.452, rely=0.7)
#botones de la ventana principal
btn_iniciar_sesion = tk.Button(ventanaP, text="Iniciar Sesión").place(relx=0.445, rely=0.65)
btnjugar = tk.Button(ventanaP, text="JUGAR", width=10, height=2).place(relx=0.44, rely=0.9)
btnmp = tk.Button(ventanaP, text="MEJORES PUNTUACIONES", width=20, height=2).place(relx=0.403, rely=0.78)
btninfo = tk.Button(ventanaP, text="ACERCA DE", width=12, height=2).place(relx=0.83, rely=0.05)
fuera = tk.Button(ventanaP, text="CERRAR", width=12, height=2, command=lambda: [ventanaP.destroy()]).place(relx=0.057, rely=0.05)
ventanaP.mainloop()