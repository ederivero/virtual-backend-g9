from flask_jwt import JWTError


def manejo_error_JWT(error: JWTError):
    print(error.status_code)
    print(error.description)
    print(error.headers)
    print(error.error)
    message = ""
    if error.error == 'Invalid token':
        message = "Token invalida"
    elif error.error == 'Authorization Required':
        message = "Necesitas una token para esta peticion"
    elif error.error == 'Invalid JWT header':
        message = "Token sin el prefijo correcto"
    else:
        message = "Error desconocido"

    return {
        "message": message,
        "content": None
    }, error.status_code
