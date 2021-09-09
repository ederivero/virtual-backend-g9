from flask import Flask
from config.conexion_bd import base_de_datos
from dotenv import load_dotenv
from os import environ

load_dotenv()

app = Flask(__name__)
# config => las variables de configuracion de mi proyecto de flask DEBUG=TRUE, PORT= 5000, ENVIRONMENT=DEVELOPMENT
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

base_de_datos.init_app(app)
base_de_datos.create_all(app=app)

if __name__ == '__main__':
    app.run(debug=True)
