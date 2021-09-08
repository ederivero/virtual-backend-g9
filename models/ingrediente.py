from conexion_bd import base_de_datos
from sqlalchemy import Column, types, orm


class IngredienteModel(base_de_datos.Model):
    __tablename__ = 'ingredientes'

    # id int primary key not null unique auto_increment,
    ingredienteId = Column(name='id', type_=types.Integer, primary_key=True,
                           unique=True, autoincrement=True, nullable=False)

    ingredienteNombre = Column(name='nombre', type_=types.String(
        length=45), nullable=False, unique=True)

    recetas_ingredientes = orm.relationship(
        'RecetaIngredienteModel', backref='recetaIngredienteIngredientes')

    def __str__(self):
        print(self.ingredienteId)
        # return 'El ingrediente es: %s' % self.ingredienteNombre
        return 'El ingrediente es: {}'.format(self.ingredienteNombre)
