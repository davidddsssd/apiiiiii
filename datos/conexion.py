from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from auxiliares import usuario_db, servidor_db, puerto_db, nombre_db

url_db = f"mysql+mysqlconnector://{usuario_db}@{servidor_db}:{puerto_db}/{nombre_db}"
# pool_pre_ping ayuda a reconectar si hay conexiones muertas
motor_db = create_engine(url_db, pool_pre_ping=True)
Session = sessionmaker(bind=motor_db)
sesion = Session()