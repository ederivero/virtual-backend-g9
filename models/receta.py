from conexion_bd import base_de_datos
from sqlalchemy import Column, types, orm
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

    # el relationship sirve para indicar los "hijos" que puede tener ese modelo con algunas relaciones previamente declaradas
    # backref => crea un atributo virtual en el otro modelo y sirve para que se pueda acceder a todo el objeto inverso
    # lazy => define como SQLAlchemy va a cargar la informacion adyacente de la base de datos
    # True / 'select' (default)=> carga toda la informacion siempre
    # False / 'joined' => solamente cargara cuando sea necesario (cuando se vaya a usar los atributos auxiliares)
    # 'subquery' => trabajara con todos los datos PEEERO en forma de una sub consulta
    # 'dynamic' => se puede agregar filtro adicionales. SQLAlchemy devolvera otro objeto dentro de la clase
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#one-to-many-relationships
    preparaciones = orm.relationship(
        'PreparacionModel', backref='preparacionRecetas', lazy=True)

    recetas_ingredientes = orm.relationship(
        'RecetaIngredienteModel', backref='recetaIngredienteRecetas')
