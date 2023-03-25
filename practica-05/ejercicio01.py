"""Base de Datos - Creación de Clase en ORM"""

# pip install sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Socio(Base):
    """Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
        - id_socio: entero (clave primaria, auto-incremental, unico)
        - dni: entero (unico)
        - nombre: string (longitud 250)
        - apellido: string (longitud 250)
    """
    __tablename__ = 'socios'

    id_socio = Column(Integer, primary_key=True, unique=True)
    dni = Column(Integer, unique=True)
    nombre = Column(String(250))
    apellido = Column(String(250))

    def __repr__(self):
        return f'Socio(id_socio={self.id_socio}, dni={self.dni}, nombre={self.nombre}, apellido={self.apellido})'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
