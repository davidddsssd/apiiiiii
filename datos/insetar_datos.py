from .conexion import Session


def insertar_objeto(objeto):
    # Usar una sesión local por operación para evitar estados pendientes globales
    sesion_local = Session()
    try:
        sesion_local.add(objeto)
        sesion_local.flush()
        sesion_local.refresh(objeto)
        id_objeto = objeto.id
        sesion_local.commit()
        print("El objeto se ha guardado correctamente.")
        return id_objeto
    except Exception as error:
        sesion_local.rollback()
        print(f"Error al guardar el objeto: {error}")
        raise
    finally:
        sesion_local.close()