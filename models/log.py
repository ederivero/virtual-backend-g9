from conexion_bd import base_de_datos
from sqlalchemy import Column, types
from datetime import datetime


class LogModel(base_de_datos.Model):
    __tablename__ = 'logs'

    logId = Column(name='id', type_=types.Integer,
                   autoincrement=True, primary_key=True)

    logFecha = Column(name='fecha', type_=types.DateTime(),
                      default=datetime.utcnow)

    logRazon = Column(name='razon', type_=types.Text)
