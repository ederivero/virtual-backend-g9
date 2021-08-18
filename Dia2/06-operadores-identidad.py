# is => es
# is not => no es
frutas = ['carambola', 'guayaba', 'higo', 'melocoton']
fruta = frutas[0]
fruta = 'platano'
# para poder ver en que posicion de la memoria esta siendo ubicada una variable se usa el metodo id()
print(id(fruta))
print(id(frutas))
# el 'is' e 'is not' se usa mas que todo para validar si las variables a comparar estan apuntando a la misma direccion de memoria o no
# las variables que son colecciones de datos como listas, tuplas y diccionarios son variables mutables
# las otras variables (int, str, float) son variables inmutables
frutas2 = frutas
frutas2.append('fresa')
print(frutas)
print(id(frutas2))
print(id(frutas))
print(frutas2 is frutas)
# las dos variables NO COMPARTEN la misma ubicacion de memoria
print(fruta is frutas)

# variables mutables e inmutables
# para hacer la copia de la lista sin que se ubique en la misma posicion de memoria hacemos uso del metodo copy (propio de las listas)
frutas_variadas = frutas.copy()
print(id(frutas_variadas))
print(id(frutas))
print(frutas_variadas is frutas)
