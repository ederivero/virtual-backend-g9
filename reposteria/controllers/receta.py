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
