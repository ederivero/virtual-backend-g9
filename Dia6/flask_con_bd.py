from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'empresa'
app.config['MYSQL_PORT'] = 3306

print(app.config)
mysql = MySQL(app)


@app.route('/departamentos', methods=['GET', 'POST'])
def inicio():
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM DEPARTAMENTOS")
        resultado = cur.fetchall()
        print(resultado)
        departamentos = []
        for departamento in resultado:
            print(departamento)
            departamentos.append({
                "id": departamento[0],
                "nombre": departamento[1]
            })
        return {
            "message": None,
            "content": departamentos
        }
    elif request.method == 'POST':
        # CAPTURAR EL BODY
        data = request.get_json()
        print(data)
        cur = mysql.connection.cursor()
        # %s => convierte el valor actual a string
        cur.execute("INSERT INTO DEPARTAMENTOS (NOMBRE) VALUES ('%s')" %
                    data['nombre'])
        mysql.connection.commit()

        return {
            "message": "Departamento creado exitosamente"
        }, 201


if __name__ == '__main__':
    app.run(debug=True)
