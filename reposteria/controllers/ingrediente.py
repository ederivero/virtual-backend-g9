from flask_restful import Resource, request, reqparse
import sqlalchemy
from models.ingrediente import IngredienteModel
from models.log import LogModel
from conexion_bd import base_de_datos

# serializador => elemento que convierte los parametros que me envia el front para tener un uso correcto en el backend
serializador = reqparse.RequestParser()
serializador.add_argument(
    'nombre',  # nombre del argumento que esperara ser recibido
    required=True,  # indica si el argumento es requerido o no lo es
    location='json',  # indica la ubicacion por donde se debera proveer el argumento
    help='Falta el nombre',  # mensaje si es que es requerido y no es proveido
    type=str,  # tipo de dato que me tiene que enviar el front
)


class IngredientesController(Resource):
    def get(self):
        print("Ingreso al get")
        return {
            "message": "Bievenido al get"
        }

    def post(self):
        # validar en base a los argumentos indicados si esta cumpliendo o no el front con pasar dicha informacion
        data = serializador.parse_args()
        try:
            nuevoIngrediente = IngredienteModel(
                ingredienteNombre=data['nombre'])
            # inicializando una transaccion
            base_de_datos.session.add(nuevoIngrediente)
            base_de_datos.session.commit()
            # print(nuevoIngrediente.__dict__)
            json = {
                "id": nuevoIngrediente.ingredienteId,
                "nombre": nuevoIngrediente.ingredienteNombre
            }
            error = None
            return {
                "message": "Ingrediente creado exitosamente",
                "content": json
            }, 201
        except sqlalchemy.exc.DataError as err:
            error = err
            return {
                "message": "Error al ingresar el ingrediente"
            }, 500

        except sqlalchemy.exc.IntegrityError as err:
            error = err
            return {
                "message": "Ese ingrediente ya existe"
            }, 500

        except Exception as err:
            error = err
            print(err)
            return {
                "message": "Error Desconocido"
            }, 500

        finally:
            # se va a ejecutar si ingreso o no ingreso a algun except
            print('ingreso al finally')
            if error is not None:
                base_de_datos.session.rollback()
                nuevoLog = LogModel()
                nuevoLog.logRazon = str(error)
                base_de_datos.session.add(nuevoLog)
                base_de_datos.session.commit()
