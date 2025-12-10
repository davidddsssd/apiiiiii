from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Geo(Base):
    __tablename__ = 'geos'
    id = Column(Integer, primary_key=True)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street = Column(String(30), nullable=False)
    suite = Column(String(15), nullable=False)
    city = Column(String(20), nullable=False)
    zipcode = Column(String(15), nullable=False)
    geoId = Column(Integer, ForeignKey('geos.id'), nullable=False)


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    catchPhrase = Column(String(255), nullable=False)
    bs = Column(String(100), nullable=False)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    username = Column(String(15), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(25), nullable=False)
    website = Column(String(255), nullable=False)
    addressId = Column(Integer, ForeignKey('addresses.id'), nullable=False)
    companyId = Column(Integer, ForeignKey('companies.id'), nullable=False)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    body = Column(String(255), nullable=False)
    userId = Column(Integer, ForeignKey('users.id'), nullable=False)


class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    username = Column(String(15), nullable=False)
    email = Column(String(255), nullable=False)
    contrasena = Column(String(255), nullable=False)
    sal = Column(String(255), nullable=False)
