from config.conexion_bd import base_de_datos
from models.Tarea import TareaModel
from flask_restful import Resource, reqparse
from flask_jwt import current_identity, jwt_required
from cloudinary import CloudinaryImage, CloudinaryVideo


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
        choices=['POR_HACER', 'HACIENDO', 'FINALIZADO'],
        type=str,
        help='Falta el estado',
        required=True,
        location='json'
    )
    serializador.add_argument(
        'imagen',
        type=str,
        required=False,
        location='json'
    )

    @jwt_required()
    def post(self):
        data = self.serializador.parse_args()
        try:
            nuevaTarea = TareaModel()
            nuevaTarea.tareaDescripcion = data.get('descripcion')
            nuevaTarea.tareaEstado = data.get('estado')
            nuevaTarea.tareaTags = data.get('tags')
            nuevaTarea.tareaTitulo = data.get('titulo')
            nuevaTarea.tareaImagen = data.get('imagen')
            nuevaTarea.usuario = current_identity.get('usuarioId')

            base_de_datos.session.add(nuevaTarea)
            base_de_datos.session.commit()
            print(current_identity)
            return {
                "message": "Tarea creada exitosamente",
                "content": {
                    "tareaId": nuevaTarea.tareaId,
                    "tareaDescripcion": nuevaTarea.tareaDescripcion,
                    "tareaEstado": nuevaTarea.tareaEstado.value,
                    "tareaTags": nuevaTarea.tareaTags,
                    "tareaTitulo": nuevaTarea.tareaTitulo,
                    "tareaFechaCreacion": str(nuevaTarea.tareaFechaCreacion),
                    "usuario": nuevaTarea.usuario,
                }
            }, 201
        except Exception as e:
            base_de_datos.session.rollback()
            return{
                "message": "Error al crear la tarea",
                "content": e.args
            }, 400

    @jwt_required()
    def get(self):
        tareasEncontradas = base_de_datos.session.query(TareaModel).filter(
            TareaModel.usuario == current_identity.get('usuarioId')).all()
        resultado = []
        for tarea in tareasEncontradas:
            tareaDict = tarea.__dict__.copy()
            del tareaDict['_sa_instance_state']
            tareaDict['tareaFechaCreacion'] = str(
                tareaDict['tareaFechaCreacion'])

            # respuestaCD = CloudinaryImage(tarea.tareaImagen).video(transformation=[
            #     {'background': "#ce6767", 'border': "17px_solid_rgb:000", 'height': 310,
            #         'quality': 46, 'radius': 14, 'width': 634, 'zoom': "1.8", 'crop': "scale"},
            #     {'angle': 185}
            # ])

            respuestaCD = CloudinaryVideo(tarea.tareaImagen).video(controls=True, transformation=[
                {"width": 3.4, "angle": 20}
            ], audio_frequency="96000")
            # cuando en vez de solamente usar la instancia de la clase, llamamos a su metodo image entonces ya no retornara una instancia sino que retornara una etiqueta img con sus propiedad src para que pueda ser renderizada en el frontend, caso contrario si solamente usamos la clase CloudinaryImage esa nos retornara un metodo llamado url que sera la url de la imagen sin modificaciones
            print(respuestaCD)

            tareaDict['tareaEstado'] = tareaDict['tareaEstado'].value
            tareaDict['tareaImagen'] = respuestaCD
            resultado.append(tareaDict)
        # devolver todas las tareas correspondiente al usuario del current_identity
        return{
            "message": None,
            "content": resultado
        }
