

class Animales():

    def habla(self):
        print("Yo soy un Animal")

    def descripcion(self):
        print("Yo soy un {}".format(self.animal))
#Añadimos la herencia colocando la clase en los parentises
class Perro(Animales):
    pass

class Abeja(Animales):
    def __init__(self, animal):
        self.animal=animal

animal= Animales()

animal.habla()

perro= Perro()

perro.habla()

abeja= Abeja("Abeja")
abeja.descripcion()
