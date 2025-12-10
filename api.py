from negocio import obtener_users_api,obtener_posts_api,crear_user_api,modificar_user_api,eliminar_user_api

# obtener_users_api('https://jsonplaceholder.typicode.com/users')
# obtener_posts_api('https://jsonplaceholder.typicode.com/posts')

url = 'https://jsonplaceholder.typicode.com/users'
url2 = 'https://jsonplaceholder.typicode.com/users/1'
eliminar_user_api(url2)