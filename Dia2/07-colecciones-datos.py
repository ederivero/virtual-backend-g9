# list => listas
# ordernadas, y modificables


colores = ['morado', 'azul', 'rosado', 'amarillo']
mezclada = ['otoño', 14, False, 15.2, [1, 2, 3]]

# imprimir la primera posicion
# en Python si la posicion no existe, lanzara un error, a diferencia de JS, que indicara undefined (no definido)
print(colores[0])
# al usar valores negativos en las posiciones de la lista, se 'invertira' y podremos recorrer dicha lista
print(colores[-1])
# las posiciones que sean desde la 1 hasta <3
print(colores[1:3])
# toda la lista hasta la posicion <2
print(colores[:2])
# sirve para copiar EL CONTENIDO de la lista mas no su ubicacion de memoria
colores_2 = colores[:]
print(id(colores_2))
print(id(colores))

print(colores[1:-1])

# metodo para agregar un elemento a una lista
colores.append('naranja')
print(colores)

# metodo para eliminar un valor
# 1. solamente si existe lo eliminara, sino lanzara un error
colores.remove('azul')
print(colores)
# colores.remove('azul')
# print(colores)

# 2. si queremos eliminarlo y ADEMAS guardar el valor eliminado en una variable
color_eliminado = colores.pop(0)
print(colores)
print(color_eliminado)

# 3. el metodo para eliminar el valor
# este metodo tambien sirve para eliminar variables
# nombre = "eduardo"
# del nombre
# print(nombre)

del colores[0]
print(colores)

# sacar la longitud de la lista
print(len(colores))

# TUPLAS
# la tupla a diferencia de la lista es una coleccion de datos ordenada PERO que una vez creada no se puede editar

notas = (10, 15, 20, 9, 17, 10, 10, 10, 10)
print(notas[0])
print(len(notas))

print(notas.count(10))

# DICCIONARIOS
# coleccion de datos ordenada PERO no por indices ya que se maneja un ordenamiento segun su clave-valor, se puede modificar
persona = {
    'nombre': 'Eduardo',
    'nombre': 'Ramiro',
    'apellido': 'de Rivero',
    'correo': 'correo@correo.com',
    'edad': 28,
    'donacion_organos': True,
    'hobbies': [
        {
            'nombre': 'Volar drones',
            'conocimiento': 'avanzado',
        },
        {
            'nombre': 'Montar bici',
            'conocimiento': 'Intermedio'
        }
    ]
}

persona['edad'] = 35
persona['nacionalidad'] = 'peruano'
print(persona["edad"])
print(persona['nombre'])
print(persona)

# imprimir el primer hobby de la persona
# Volar drones
print(persona['hobbies'][0])
