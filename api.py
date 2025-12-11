from negocio import obtener_users_api, obtener_posts_api, crear_user_api, modificar_user_api, eliminar_user_api


def menu():
	url_users = 'https://jsonplaceholder.typicode.com/users'
	url_posts = 'https://jsonplaceholder.typicode.com/posts'

	while True:
		print('\n--- Menú ---')
		print('1) Obtener users (API)')
		print('2) Obtener posts (API)')
		print('3) Crear user (API)')
		print('4) Modificar user (API)')
		print('5) Eliminar user (API)')
		print('0) Salir')
		opcion = input('Elige una opción: ').strip()

		if opcion == '1':
			obtener_users_api(url_users)
		elif opcion == '2':
			obtener_posts_api(url_posts)
		elif opcion == '3':
			crear_user_api(url_users)
		elif opcion == '4':
			id_editar = input('Introduce el id del user a modificar (ej: 1): ').strip()
			if id_editar:
				modificar_user_api(f"{url_users}/{id_editar}")
		elif opcion == '5':
			id_eliminar = input('Introduce el id del user a eliminar (ej: 1): ').strip()
			if id_eliminar:
				eliminar_user_api(f"{url_users}/{id_eliminar}")
		elif opcion == '0':
			print('Saliendo.')
			break
		else:
			print('Opción no válida. Intenta de nuevo.')


if __name__ == '__main__':
	menu()