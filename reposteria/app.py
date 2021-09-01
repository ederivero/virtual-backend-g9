from flask import Flask
from conexion_bd import base_de_datos
from models.ingrediente import IngredientesModel
from models.receta import RecetaModel
from models.preparacion import PreparacionModel
from models.recetas_ingredientes import RecetaIngredienteModel
from os import environ
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
#                                        mysql://username:password@host/db_name
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
# si se establece True SqlAchemy rastreara las modificaciones de los objetos (modelos) y lanzara señales de cambio, su valor predeterminado es None . igual habilita el tracking pero emite una advertencia que en futuras versiones se removera el valor x default None y si o si tendremos que indicar un valor inicial
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicia la conexion con la bd para darle las credenciales definidias en el app.config
base_de_datos.init_app(app)

# creara las tablas aun no mapeadas y si todo esta bien no devolvera nada
base_de_datos.create_all(app=app)


@app.route("/")
def initial_controller():
    return {
        "message": "Bienvenido a mi API de REPOSTERIA 🥧"
    }


if __name__ == '__main__':
    app.run(debug=True)
