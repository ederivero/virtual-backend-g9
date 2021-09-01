from sqlalchemy.sql.sqltypes import Integer
from conexion_bd import base_de_datos
from sqlalchemy import Column, types


class IngredienteModel(base_de_datos.Model):
    __tablename__ = 'ingredientes'

    # id int primary key not null unique auto_increment,
    ingredienteId = Column(name='id', type_=types.Integer, primary_key=True,
                           unique=True, autoincrement=True, nullable=False)

    ingredienteNombre = Column(name='nombre', type_=types.String(length=45))
