class Electrodomestico:
    def __init__(self):
        self.__nombre = ''
        self.__color = ''
        self.__precio = 0.0

    def __setNombre(self, nombre):
        """El setter sirve para definir el contenido del atributo de una manera mas formal"""
        self.__nombre = nombre

    def __getNombre(self):
        """El getter sirve para devolver el valor del atributo privado"""
        return self.__nombre

    def __deleteNombre(self):
        """El deleter sirve para eliminar el contenido del atributo privado"""
        del self.__nombre

    # property => sirve para definir el comportamiento que tendra un atributo de la clase
    nombre = property(__getNombre, __setNombre, __deleteNombre)


objElectrodomestico = Electrodomestico()
objElectrodomestico.nombre = "Lavadora"  # setter
print(objElectrodomestico.nombre)  # getter
# del objElectrodomestico.nombre  # deletter
# print(objElectrodomestico.nombre)
