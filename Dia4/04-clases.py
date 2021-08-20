class Mueble:
    precio = 00.00
    color = "Blanco"
    especificaciones = []
    tipo = ""

    def indicar_tipo(self):
        return "El tipo es: {}".format(self.tipo)


mueble1 = Mueble()
mueble1.tipo = "Sofa-cama"
print(mueble1.indicar_tipo())

mueble2 = Mueble()
mueble2.tipo = "Silla"
print(mueble2.indicar_tipo())
