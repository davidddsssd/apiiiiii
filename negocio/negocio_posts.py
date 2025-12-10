import requests
from prettytable import PrettyTable
from modelos import Post
from datos import insertar_objeto


def obtener_posts_api(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        listado_posts = respuesta.json()
        for post in listado_posts:
            crear_post_db(
                post['title'],
                post['body'],
                post['userId'])


def crear_post_db(titulo, contenido, id_usuario):
    publicacion = Post(
        title=titulo,
        body=contenido,
        userId=id_usuario
    )
    try:
        id_publicacion = insertar_objeto(publicacion)
        return id_publicacion
    except Exception as error:
        print(f'Error al guardar la publicación: {error}')
