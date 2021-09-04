from conexion_bd import base_de_datos
from sqlalchemy import Column, types
from enum import Enum


class EnumPorcion(Enum):
    personal = "personal"
    familiar = "familiar"
    mediano = "mediano"


class RecetaModel(base_de_datos.Model):
    __tablename__ = "recetas"

    recetaId = Column(type_=types.Integer, name="id",
                      primary_key=True, autoincrement=True, unique=True)

    recetaNombre = Column(
        name='nombre', type_=types.String(length=255), nullable=False)

    recetaPorcion = Column(name='porcion', type_=types.Enum(EnumPorcion))
