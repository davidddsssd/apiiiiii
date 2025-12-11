import requests
from prettytable import PrettyTable
from modelos import Post
from datos import insertar_objeto, obtener_listado_objetos


def obtener_posts_api(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        listado_posts = respuesta.json()
        for post in listado_posts:
            crear_post_db(
                post['title'],
                post['body'],
                post['userId'])
        # Mostrar los posts guardados
        listar_posts_db()


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


def listar_posts_db():
    tabla_posts = PrettyTable()
    tabla_posts.field_names = ['ID', 'Titulo', 'Contenido', 'ID Usuario']
    listado_posts = obtener_listado_objetos(Post)
    
    if listado_posts:
        for post in listado_posts:
            tabla_posts.add_row([post.id, post.title, post.body, post.userId])
        print('\n--- Posts en la Base de Datos ---')
        print(tabla_posts)
    else:
        print('No hay posts guardados.')
