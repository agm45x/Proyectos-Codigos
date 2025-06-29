class Animales():
    def __init__(self,nombre):
        self.nombre=nombre

class Perro(Animales):
    def __init__(self, nombre,sonido):
        #Herredar el metodo init
        super().__init__(nombre)
        self.sonido=sonido

perro= Perro("Firulais", "Guaooo!")
print(perro.nombre)
print(perro.sonido)