from .conexion import sesion
from sqlalchemy import func
from modelos import Company, User


def obtener_listado_objetos(objeto):
    listado_objetos = sesion.query(objeto).all()
    if len(listado_objetos) > 0:
        return listado_objetos


def obtener_user_por_id(user_id):
    user = sesion.query(User).filter(User.id == user_id).first()
    return user


def actualizar_user(user_id, **kwargs):
    try:
        user = sesion.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            sesion.commit()
            return True
        return False
    except Exception as error:
        sesion.rollback()
        print(f'Error al actualizar usuario: {error}')
        return False


def eliminar_user(user_id):
    try:
        user = sesion.query(User).filter(User.id == user_id).first()
        if user:
            sesion.delete(user)
            sesion.commit()
            return True
        return False
    except Exception as error:
        sesion.rollback()
        print(f'Error al eliminar usuario: {error}')
        return False



def obtener_user_name(valor):
    user_identificado = sesion.query(User).filter(
        User.name.like(f'%{valor}%')).first()
    if user_identificado != None and isinstance(user_identificado, User):
        return user_identificado


def obtener_company_name(valor):
    company_identificada = sesion.query(Company).filter(
        Company.name.like(f'%{valor}%')).first()
    if company_identificada != None and isinstance(company_identificada, Company):
        return company_identificada
