import requests
from prettytable import PrettyTable

from modelos import User
from datos import insertar_objeto, obtener_user_name
from negocio import crear_geolocalizacion_db,crear_direccion_db,crear_compania_db


def obtener_users_api(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        print("Solicitud correcta, procesando data Users...")
        usuarios = respuesta.json()
        for user in usuarios:
            id_geo = crear_geolocalizacion_db(
                user['address']['geo']['lat'],
                user['address']['geo']['lng']
            )

            id_direccion = crear_direccion_db(
                user['address']['street'],
                user['address']['suite'],
                user['address']['city'],
                user['address']['zipcode'],
                id_geo
            )

            id_compania = crear_compania_db(
                user['company']['name'],
                user['company']['catchPhrase'],
                user['company']['bs']
            )

            crear_user_db(
                user['name'],
                user['username'],
                user['email'],
                user['phone'],
                user['website'],
                id_direccion,
                id_compania
            )

    elif respuesta.status_code == 204:
        print("Consulta ejecutada correctamente, pero NO se han encontrado datos.")
    else:
        print(
            f"La solicitud falló con el siguiente código de error: {respuesta.status_code}")



def crear_user_api(url):
    nombre = input('Nombre: ')
    nomre_usuario = input('Usuario: ')
    correo = input('Correo: ')
    telefono = input('Celular: ')
    web = input('Web: ')

    user = {
        "name": nombre,
        "username": nomre_usuario,
        "email": correo,
        "phone": telefono,
        "website": web
    }

    respuesta = requests.post(url, data=user)
    print(f'{respuesta.text} {respuesta.status_code}')


def modificar_user_api(url):
    nombre = input('Nombre: ')
    nomre_usuario = input('Usuario: ')
    correo = input('Correo: ')
    telefono = input('Celular: ')
    web = input('Web: ')

    user = {
        "name": nombre,
        "username": nomre_usuario,
        "email": correo,
        "phone": telefono,
        "website": web
    }

    respuesta = requests.put(url, data=user)
    print(respuesta.text)


def eliminar_user_api(url):
    respuesta = requests.delete(url)
    print(respuesta.text)


def buscar_user_db_name(nombre):
    if nombre != '':
        user = obtener_user_name(nombre)
        if user != None:
            return user


def crear_user_db(nombre, nombre_usuario, correo, telefono, sitio_web, id_direccion, id_compania):
    user = buscar_user_db_name(nombre)
    if not user:
        usuario = User(
            name=nombre,
            username=nombre_usuario,
            email=correo,
            phone=telefono,
            website=sitio_web,
            addressId=id_direccion,
            companyId=id_compania
        )
        try:
            id_usuario = insertar_objeto(usuario)
            return id_usuario
        except Exception as error:
            print(f'Error al guardar al usuario: {error}')
    else:
        print('Usuario ya existe, no será agregado.')


def modificar_user_db():
    pass


def eliminar_user_db(arg):
    pass
