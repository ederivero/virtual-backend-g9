from flask import Flask, request

app = Flask(__name__)

productos = []


@app.route("/")
def inicio():
    # siempre que vamos a responser al client tiene que ser por el return
    return {
        "message": "Bienvenido a mi API",
        "content": ""
    }


@app.route("/productos", methods=['POST'])
def gestion_productos():
    # el get_json() sirve para visualizar toda la informacion que el usuario me esta enviando por el body
    # body es el cuerpo de la peticion (donde el front adjunta la informacion que quiere enviar)
    # body se envia en formato JSON | multipart | TEXT | XML
    print(request.get_json())
    return {
        "message": "Producto Creado exitosamente",
        "content": ""
    }


if __name__ == "__main__":
    app.run(debug=True, port=8000)
