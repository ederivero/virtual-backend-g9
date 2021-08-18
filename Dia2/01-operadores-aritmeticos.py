numero1 = 10
numero2 = 80

persona1 = "Eduardo"
persona2 = "Ricardo"

# SUMA
# Nota: si las dos o mas variables son numericas entonces se realizara la suma, si por el contrario las variables son string (caracteres) se CONCATENARAN (se juntaran)
# en el caso de JS si se puede sumar diferentes tipos de variables, en el caso de Python eso no esta permitido
print(numero1 + numero2)
print(persona1 + persona2)
numero1_string = str(numero1)
print(numero1_string + persona1)
# RESTA

print(numero1 - numero2)
# No se puede usar la resta en variables que no sean numericas
# print(persona1 - persona2)

# MULTIPLICACION
print(numero1 * numero2)
print(persona1 * 2)
# La multiplicacion de 10 y 80 es: 800

print("La multiplicacion de {0} y {1} es: {2}".format(
    numero1, numero2, numero1 * numero2))

print(f"La multiplicacion de {numero1} y {numero2} es: {numero1 * numero2}")

# DIVISION
# Toda division aun asi sea entera siempre sera flotante (tiene una parte entera y una parte decimal)
print(numero2 / numero1)
print(numero1 / numero2)


# MODULO
# el modulo es el resultado de la division
print(numero2 % numero1)
print(numero1 % numero2)

# COCIENTE
print(numero2 // numero1)
print(numero1 // numero2)
