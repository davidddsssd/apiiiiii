import requests
from prettytable import PrettyTable

from modelos import User
from datos import insertar_objeto, obtener_user_name, obtener_listado_objetos, obtener_user_por_id, actualizar_user, eliminar_user
from .negocio_geos import crear_geolocalizacion_db
from .negocio_addresses import crear_direccion_db
from .negocio_companies import crear_compania_db


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
        # Mostrar los usuarios guardados
        listar_users_db()

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
    
    # Guardar también en la BD local (sin dirección ni compañía, solo datos básicos)
    if respuesta.status_code == 201:
        # Crear usuario sin dirección ni compañía por defecto
        usuario = User(
            name=nombre,
            username=nomre_usuario,
            email=correo,
            phone=telefono,
            website=web,
            addressId=1,  # ID por defecto
            companyId=1   # ID por defecto
        )
        try:
            id_usuario = insertar_objeto(usuario)
            print(f'Usuario guardado en BD local con ID: {id_usuario}')
        except Exception as error:
            print(f'Error al guardar el usuario en BD: {error}')



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
    
    # Actualizar también en la BD local
    # Extraer el ID del usuario desde la URL (ej: /users/5)
    try:
        user_id = int(url.split('/')[-1])
        if actualizar_user(user_id, name=nombre, username=nomre_usuario, email=correo, phone=telefono, website=web):
            print(f'Usuario {user_id} actualizado en BD local')
        else:
            print(f'No se encontró el usuario {user_id} en BD local')
    except Exception as error:
        print(f'Error al actualizar en BD: {error}')


def eliminar_user_api(url):
    respuesta = requests.delete(url)
    print(respuesta.text)
    
    # Eliminar también de la BD local
    # Extraer el ID del usuario desde la URL (ej: /users/5)
    try:
        user_id = int(url.split('/')[-1])
        if eliminar_user(user_id):
            print(f'Usuario {user_id} eliminado de BD local')
        else:
            print(f'No se encontró el usuario {user_id} en BD local')
    except Exception as error:
        print(f'Error al eliminar de BD: {error}')


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


def listar_users_db():
    tabla_users = PrettyTable()
    tabla_users.field_names = ['ID', 'Nombre', 'Usuario', 'Email', 'Telefono', 'Sitio Web']
    listado_users = obtener_listado_objetos(User)
    
    if listado_users:
        for user in listado_users:
            tabla_users.add_row([user.id, user.name, user.username, user.email, user.phone, user.website])
        print('\n--- Usuarios en la Base de Datos ---')
        print(tabla_users)
    else:
        print('No hay usuarios guardados.')


def modificar_user_db():
    pass


def eliminar_user_db(arg):
    pass
