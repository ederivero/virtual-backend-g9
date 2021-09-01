from flask_restful import Resource, request, reqparse
from models.ingrediente import IngredienteModel

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
    # def get(self):
    #     print("Ingreso al get")
    #     return {
    #         "message": "Bievenido al get"
    #     }

    def post(self):
        # validar en base a los argumentos indicados si esta cumpliendo o no el front con pasar dicha informacion
        data = serializador.parse_args()
        nuevoIngrediente = IngredienteModel(ingredienteNombre=data['nombre'])
        print(nuevoIngrediente)
        return {
            "message": "Bienvenido al post"
        }
