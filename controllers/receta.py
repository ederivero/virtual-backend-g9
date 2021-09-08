from flask_restful import Resource, reqparse
from sqlalchemy.sql.expression import true
from models.receta import RecetaModel
from conexion_bd import base_de_datos
from math import ceil
# CREAR RECETA
# DEVOLVER RECETAS PAGINADAS


class RecetasController(Resource):
    serializador = reqparse.RequestParser(bundle_errors=True)

    def post(self):
        self.serializador.add_argument(
            'nombre',
            required=True,
            location='json',
            help='Falta el nombre',
            type=str
        )

        self.serializador.add_argument(
            'porcion',
            required=True,
            choices=['personal', 'familiar', 'mediano'],
            type=str,
            help='Falta la porcion {error_msg}',
            location='json'
        )
        data = self.serializador.parse_args()
        print(data)
        try:
            nuevaReceta = RecetaModel()
            nuevaReceta.recetaNombre = data.get('nombre')
            nuevaReceta.recetaPorcion = data['porcion']
            base_de_datos.session.add(nuevaReceta)
            base_de_datos.session.commit()

            return {
                "message": "Receta agregada exitosamente",
                "content": {
                    "recetaId": nuevaReceta.recetaId,
                    "recetaNombre": nuevaReceta.recetaNombre,
                    "recetaPorcion": nuevaReceta.recetaPorcion.value
                }

            }, 201
        except:
            return {
                "message": "Hubo un error al guardar la receta, intentelo nuevamente"
            }, 500

    def get(self):

        self.serializador.add_argument(
            'page',
            location='args',
            type=int,
            required=True,
            help='Falta el page'
        )
        self.serializador.add_argument(
            'perPage',
            location='args',
            type=int,
            required=True,
            help='Falta el page'
        )

        data = self.serializador.parse_args()

        # ------------ HELPER DE PAGINACION (AYUDANTE)
        perPage = data['perPage']
        page = data['page']
        limit = perPage
        offset = (page - 1) * limit
        # ------------ FIN DEL HELPER

        # CREAMOS LOS DATOS DE LA PAGINACION
        # SELECT count(*) FROM recetas;
        total = base_de_datos.session.query(RecetaModel).count()
        print(total)
        itemsPorPagina = perPage if total >= perPage else None
        totalPaginas = ceil(total / itemsPorPagina)
        if page > 1:
            paginaPrevia = page - 1 if page <= totalPaginas else None
        else:
            paginaPrevia = None
        if totalPaginas > 1:
            paginaSiguiente = page + 1 if page < totalPaginas else None
        else:
            paginaSiguiente = None
        # FIN DE CREACION

        recetas = base_de_datos.session.query(
            RecetaModel).limit(limit).offset(offset).all()
        resultado = []
        for receta in recetas:
            recetaDict = receta.__dict__
            del recetaDict['_sa_instance_state']
            recetaDict['recetaPorcion'] = recetaDict['recetaPorcion'].value
            resultado.append(recetaDict)
        print(data)
        return {
            "content": resultado,
            "pagination": {
                "total": total,
                "perPages": itemsPorPagina,
                "paginaPrevia": paginaPrevia,
                "paginaSiguiente": paginaSiguiente,
                "totalPaginas": totalPaginas
            }
        }


class RecetaController(Resource):

    def get(self, id):
        receta = base_de_datos.session.query(RecetaModel).filter(
            RecetaModel.recetaId == id).first()

        if receta is None:
            return {
                "message": "Receta no existe",
                "content": None
            }, 404

        diccionario_receta = receta.__dict__.copy()
        del diccionario_receta['_sa_instance_state']
        diccionario_receta['recetaPorcion'] = receta.recetaPorcion.value

        # print(receta.recetas_ingredientes[0].recetaIngredienteIngredientes)

        diccionario_receta['preparaciones'] = []

        for preparacion in receta.preparaciones:
            diccionario_preparacion = preparacion.__dict__.copy()
            del diccionario_preparacion['_sa_instance_state']
            diccionario_receta['preparaciones'].append(diccionario_preparacion)
            # print(preparacion.__dict__)

        diccionario_receta['ingredientes'] = []

        for receta_ingrediente in receta.recetas_ingredientes:
            diccionario_receta_ingrediente = receta_ingrediente.__dict__.copy()
            del diccionario_receta_ingrediente['_sa_instance_state']

            diccionario_receta_ingrediente['ingrediente'] = receta_ingrediente.recetaIngredienteIngredientes.__dict__.copy(
            )

            del diccionario_receta_ingrediente['ingrediente']['_sa_instance_state']
            # print(receta_ingrediente.recetaIngredienteIngredientes)
            print(diccionario_receta_ingrediente)

            diccionario_receta['ingredientes'].append(
                diccionario_receta_ingrediente)

        return {
            "message": None,
            "content": diccionario_receta
        }
