from datos import insertar_objeto, obtener_company_name
from modelos import Company


def buscar_compania_db_nombre(nombre):
    if nombre != '':
        compania = obtener_company_name(nombre)
        if compania != None:
            return compania


def crear_compania_db(nombre, slogan, negocio):
    compania = Company(
        name=nombre,
        catchPhrase=slogan,
        bs=negocio
    )
    cia = buscar_compania_db_nombre(nombre)
    if not cia:
        try:
            id_compania = insertar_objeto(compania)
            return id_compania
        except Exception as error:
            print(f'Error al guardar la geolocalización: {error}')
    else:
        # Si la compañía ya existe, devolver su id para usarlo en la creación de usuario
        try:
            # `cia` puede ser un objeto Company
            return cia.id if hasattr(cia, 'id') else None
        except Exception:
            return None
