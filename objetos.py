class Vehiculo():
    def __init__(self, color,ruedas):
        self.color = color
        self.ruedas=ruedas
    def __str__(self):
        return "color {}, {} ruedas".format(self.color,self.ruedas)

class Carro(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindraje):
        super().__init__( color, ruedas)
        self.velocidad=velocidad
        self.cilindraje=cilindraje
    def __str__(self):
        return super().__str__() +" ,velocidad {} kmts/hs, cilindraje {} cc".format(self.velocidad,self.cilindraje)

class Camioneta(Carro):
    def __init__ (self,color,ruedas,velocidad,cilindraje,carga):
        super().__init__(color,ruedas,velocidad,cilindraje)
        self.carga=carga
    def __str__(self):
        return super().__str__()+", {}kg de carga".format(self.carga)

    
toyota = Carro("azul", 4, 220, 8)
print(toyota) 
Hilux = Camioneta("blanca", 4, 200, 16, 2000)
print(Hilux)


## variables de instacia
class ClaseEjemplo:
    def __init__(self, val = 1):
        self.primera = val

    def setSegunda(self, val):
        self.segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.tercera = 5


print(objetoEjemplo1.__dict__)
print(objetoEjemplo2.__dict__)
print(objetoEjemplo3.__dict__)