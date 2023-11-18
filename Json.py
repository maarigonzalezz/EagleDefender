import json

def registrar_usuario(entry_usuario, entry_correo, entry_contrasena):
    # Obtener los valores de los campos
    nombre_usuario = entry_usuario.get()
    correo = entry_correo.get()
    contrasena = entry_contrasena.get()

    # Crear un diccionario con los datos del nuevo usuario
    nuevo_usuario = {
        "nombre_usuario": nombre_usuario,
        "correo": correo,
        "contrasena": contrasena,
        # Agrega más campos según sea necesario
    }

    # Leer usuarios existentes (si hay alguno)
    try:
        with open("usuarios.json", "r") as archivo_json:
            usuarios = json.load(archivo_json)
    except FileNotFoundError:
        usuarios = []

    # Agregar el nuevo usuario a la lista de usuarios
    usuarios.append(nuevo_usuario)

    # Escribir de nuevo al archivo JSON
    with open("usuarios.json", "w") as archivo_json:
        json.dump(usuarios, archivo_json, indent=2)