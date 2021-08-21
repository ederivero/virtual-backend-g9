class Vehiculo:
    def __init__(self, largo, ancho, cilindrada, enMarcha=False):
        self.largo = largo
        self.ancho = ancho
        self.cilindrada = cilindrada
        self.enMarcha = enMarcha

        # cuando queremos indicar que un atributo va a ser privado (no puede ser accedido desde fuera de la clase) se le pone antes del nombre __
        self.__alarma = True

    # crear un metodo para que la alarma se active/desactive toggle_alarma
    def toggle_alarma(self):
        # self.__alarma = True if self.__alarma == False else False
        if self.__alarma == True:
            self.__alarma = False
        else:
            self.__alarma = True
        print(self.__alarma)

    def encender(self, estado=True):
        resultado = self.__verificar_alarma()
        if resultado:
            self.enMarcha = estado
            print("El vehiculo puede andar correctamente 🚗🚗")
        else:
            print("El vehiculo intenta ser robado 🚨🚨🚨")

    def __verificar_alarma(self):
        if self.__alarma == True:
            return False
        else:
            return True


objVehiculo = Vehiculo(2.20, 1.65, 1500)
objVehiculo.toggle_alarma()

print(objVehiculo.encender())
# print(objVehiculo.alarma)


class Persona:
    def __init__(self, nombre, apellido, correo, password):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = self.__encriptar_password(password)

    def __encriptar_password(self, password):
        return "asdfasdfasdfasdf"+password+"asdasdadadada"


objPersona = Persona(nombre="Raul", apellido="Perez",
                     correo="rperez@empresa.com", password="123456")


print(objPersona.password)
