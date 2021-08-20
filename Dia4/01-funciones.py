# una funcion es un bloque de codigo que se va a ejecutar cuantas veces sea llamada la funcion

def saludar():
    print("Hola buenas tardes")


# saludar()


# funciones con parametros
# los parametros que usan las funciones o las variables creadas dentro de las mismas solamente podran ser accedidas dentro de ellas
def saludarPersona(nombre):
    edad = 40
    print(f"Hola {nombre} como te va")


# saludarPersona("Eduardo")


def sin_nombre():
    """Funcion que no hace nada y solamente es de muestra"""
    print("Yo soy una funcion sin nombre")


# sin_nombre()


# las funciones pueden recibir parametros y estos pueden ser opcionales
def registro(nombre, correo=None):
    print("Registro exitoso")


# registro("Eduardo")
# registro("Eduardo", "ederiveroman@gmail.com")


# Crear una funcion llamada identificacion en la cual se reciba el nombre, apellido y la nacionalidad del cliente, si en el caso no se pasa la nacionalidad entonces sera Peruano, imprimir el resultado en forma de un diccionario
def identificacion(nombre, apellido, nacionalidad="Peruano"):
    resultado = {
        "nombre": nombre,
        "apellido": apellido,
        "nacionalidad": nacionalidad
    }
    print(resultado)


# identificacion("eduardo", "de rivero", "uruguayo")


# todos los parametros que tengan un valor predeterminado SIEMPRE van al final
def sumatoria(num1, num2=10, num3=15):
    print(num1+num2+num3)


# sumatoria(10)


# el parametro que tiene el simbolo * es un parametro especial de python que sirve para almacenar n valores
# todos los valores que pasemos a ese parametro se almacenaran en una tupla en el mismo orden con el cual hemos pasado los parametros
def alumnos(*args):
    print(args)


# alumnos(
#     "Eduardo",
#     "Siannet",
#     "Pablo",
#     "Fernando",
#     "Rick",
#     "Jhonathan")


def tareas(nombre, apellido, *args):
    print("ok")


# tareas("Eduardo", "martinez", "1", "2", 3)


# en la funcion alumnos_notas se recibira una cantidad N de alumnos en la cual se debe indicar cuantos aprobaron y cuantos desaprobaron siendo la nota minima 11
def alumnos_notas(*args):
    # todo: implementar logica
    aprobados = 0
    desaprobados = 0
    for alumno in args:
        if alumno['promedio'] > 10:
            aprobados += 1
        else:
            desaprobados += 1
    print(
        f"Hay {aprobados} alumnos aprobados y {desaprobados} alumnos desaprobados")


alumnos_notas(
    {"nombre": "Raul", "promedio": 17},
    {"nombre": "Roxana", "promedio": 20},
    {"nombre": "Alfonso", "promedio": 10},
    {"nombre": "Pedro", "promedio": 8},
    {"nombre": "Katherine", "promedio": 16}
)


# keyword arguments => es muy similar a los *args solo con la diferencia que los kwargs usan el nombre del parametro (nombre="Eduardo"), el resultado se guardara en forma de un diccionario
def indeterminada(**kwargs):
    print(kwargs)


indeterminada(nombre="eduardo", apellido="de rivero", nacionalidad="Peruano")
indeterminada(edad=50, estatura=2.10)


def variada(*args, **kwargs):
    print(args)
    print(kwargs)


variada(10, "Eduardo", {"est_civil": "Viudo"},
        mascota="Firulais", raza="Bulldog")


def sumatoria(num1, num2):
    return num1+num2
    print("otra cosa")


rpta = sumatoria(10, 5)
