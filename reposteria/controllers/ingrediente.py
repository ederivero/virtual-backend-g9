from flask_restful import Resource, request
from models.ingrediente import IngredienteModel


class IngredientesController(Resource):
    # def get(self):
    #     print("Ingreso al get")
    #     return {
    #         "message": "Bievenido al get"
    #     }

    def post(self):
        print(request.get_json())
        return {
            "message": "Bienvenido al post"
        }
