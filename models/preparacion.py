from conexion_bd import base_de_datos
from sqlalchemy import Column, types
from sqlalchemy.sql.schema import ForeignKey


class PreparacionModel(base_de_datos.Model):
    __tablename__ = "preparaciones"

    preparacionId = Column(type_=types.Integer, name='id',
                           primary_key=True, autoincrement=True, unique=True)

    preparacionOrden = Column(type_=types.Integer, name='orden', default=1)

    preparacionDescripcion = Column(
        type_=types.Text, name='descripcion', nullable=False)

    # Asi se crean las relaciones
    # en el parametro column => el nombre de la tabla y su columna
    # ondelete => indicar que accion debe de tomar el hijo (tabla donde esta ubicada la FK) cuando se elimine el registro de la fk
    # CASCADE => eliminar el registro de recetas y luego todos los registros ligados a esa receta
    # DELETE => se eliminar y dejara a las FK con el mismo valor aunque este ya no exista
    # RESTRINCT => restrige y prohibe la eliminacion de las recetas que tengan preparaciones (primero tendremos que eliinar las preparaciones y luego recien a la receta)
    # None => eliminalo y en las preparaciones setea el valor de la receta a Null
    # https://docs.sqlalchemy.org/en/14/core/constraints.html?highlight=ondelete#sqlalchemy.schema.ForeignKey.params.ondelete
    receta = Column(ForeignKey(column='recetas.id', ondelete='RESTRICT'),
                    name='recetas_id', type_=types.Integer, nullable=False)

    def __str__(self):
        return self.preparacionDescripcion
