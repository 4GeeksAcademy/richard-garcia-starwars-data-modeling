import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planetas(Base) :
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(100), nullable=True)
    terrain = Column(String(50), nullable=True)
    favoritos = relationship("favoritos")

class Personajes(Base) :
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    eye_color = Column(String(10), nullable=True)
    hair_color = Column(String(10), nullable=True)
    favoritos = relationship("favoritos")

class Usuarios(Base) :
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    mail = Column(String(20), nullable=True)
    password = Column(String(200), nullable=True)
    favoritos = relationship("favoritos")

class Favoritos(Base) :
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    personajes_id = Column(Integer, ForeignKey('personajes.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
