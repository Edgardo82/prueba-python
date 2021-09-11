class ClaseEjemplo:
    varia = 1
    def __init__(self, val):
        self.__prueba = 1
        ClaseEjemplo.varia = val

#print(ClaseEjemplo.__dict__)
objetoEjemplo = ClaseEjemplo(2)

print(ClaseEjemplo.__dict__)
print(objetoEjemplo.__dict__)

class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia
    def __str__(self):
        return self.nombre + ' en la ' + self.galaxia

sol = Estrella("Sol", "Vía Láctea")
print(sol)
