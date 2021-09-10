from flask_restful import Resource, reqparse
from re import search
PATRON_CORREO = r'\w+[@]\w+[.]\w{2,3}'
PATRON_PASSWORD = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#&?])[A-Za-z\d@$!%*#&?]{6,}'


class RegistroController(Resource):
    serializador = reqparse.RequestParser(bundle_errors=True)
    serializador.add_argument(
        'nombre',
        type=str,
        location='json',
        required=True,
        help='Falta el nombre'
    )

    serializador.add_argument(
        'apellido',
        type=str,
        location='json',
        required=True,
        help='Falta el apellido'
    )

    serializador.add_argument(
        'correo',
        type=str,
        location='json',
        required=True,
        help='Falta el correo'
    )

    serializador.add_argument(
        'password',
        type=str,
        location='json',
        required=True,
        help='Falta el password'
    )

    serializador.add_argument(
        'telefono',
        type=str,
        location='json',
        required=True,
        help='Falta el telefono'
    )

    def post(self):
        data = self.serializador.parse_args()
        print(data)
        correo = data['correo']
        password = data['password']
        if search(PATRON_CORREO, correo) is None:
            return {
                "message": "Correo incorrecto"
            }, 400

        if search(PATRON_PASSWORD, password) is None:
            return {
                "message": "Password incorrecto, minimo 6 caracteres una mayuscula, una minuscula y un simbolo especial"
            }, 400

        return {
            "message": "Usuario creado exitosamente"
        }, 201
