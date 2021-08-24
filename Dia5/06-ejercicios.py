# ejemplo
# Para evitar que en cada impresion se ejecute una nueva linea, se puede agregar el parametro end y este indicara como queremos que actue al finalizar la linea
# for numero in range(5):
#     print(numero, end="")

# Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y
# que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****
# dibujar_rectangulo()

def dibujar_rectangulo():
    alto = int(input('Ingresa la altura: '))
    ancho = int(input('Ingresa el ancho: '))
    for numero in range(alto):
        print("*"*ancho)
    # for numero in range(alto):
    #     for numero2 in range(ancho):
    #         print("*", end="")
    #     print("")


# dibujar_rectangulo()

# Escribir una funcion que nosotros le ingresemos el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****
# dibujar_octagono()


def dibujar_octagono():
    grosor = int(input("Ingrese el grosor del octagono: "))
    if grosor == 1:
        return print("*")
    # es el grosor maximo que va a tener mi octagono
    tope = (2*(grosor-1)) + grosor
    espacio = grosor
    for numero in range(grosor, tope+1, 2):
        espacio -= 1
        espacios = " "*espacio
        simbolo = "*"*numero
        if(numero == tope):
            limite = 0
            while (limite < grosor):
                print(simbolo)
                limite += 1
            break
        print(espacios + simbolo)
    espacio += 1
    for numero in range(tope - 2, grosor - 1, -2):
        espacios = " "*espacio
        espacio += 1
        simbolo = "*"*numero
        print(espacios+simbolo)


# dibujar_octagono()

# De acuerdo a la altura que nosotros ingresemos, nos tiene que dibujar el triangulo
# invertido
# Ejemplo
# Altura: 4
# ****
# ***
# **
# *
# triangulo_invertido()

def triangulo_invertido():
    altura = int(input("Ingrese la altura: "))
    for fila in range(altura, 0, -1):
        print("*"*fila)


# triangulo_invertido()
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 12
# serie_collatz()


def serie_collatz():
    numero = int(input("Ingrese el numero inicial: "))
    while (numero != 1):
        if numero % 2 == 0:
            numero /= 2
        else:
            numero = (numero * 3) + 1
        print(numero)


serie_collatz()
