from sqlalchemy.sql.sqltypes import Integer
from conexion_bd import base_de_datos
from sqlalchemy import Column, types


class IngredientesModel(base_de_datos.Model):
    __tablename__ = 'ingredientes'

    ingredienteId = Column(name='id', type_=types.Integer)
