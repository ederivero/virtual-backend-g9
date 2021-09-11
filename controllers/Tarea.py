from config.conexion_bd import base_de_datos
from models.Tarea import TareaModel
from flask_restful import Resource, reqparse
from flask_jwt import current_identity, jwt_required


class TareasController(Resource):
    serializador = reqparse.RequestParser(bundle_errors=True)
    serializador.add_argument(
        'titulo',
        location='json',
        required=True,
        help='Falta el titulo',
        type=str
    )
    serializador.add_argument(
        'descripcion',
        location='json',
        required=True,
        help='Falta la descripcion',
        type=str
    )
    serializador.add_argument(
        'tags',
        type=list,
        required=True,
        help='Falta los tags',
        location='json'
    )
    serializador.add_argument(
        'estado',
        choices=['por_hacer', 'haciendo', 'finalizado'],
        type=str,
        help='Falta el estado',
        required=True,
        location='json'
    )

    @jwt_required()
    def post(self):
        data = self.serializador.parse_args()
        nuevaTarea = TareaModel()
        nuevaTarea.tareaDescripcion = data.get('descripcion')
        nuevaTarea.tareaEstado = data.get('estado')
        nuevaTarea.tareaTags = data.get('tags')
        nuevaTarea.tareaTitulo = data.get('titulo')
        print(current_identity)
        return {
            "message": "Tarea creada exitosamente",
            "content": None
        }, 201

    @jwt_required()
    def get(self):
        pass
