class Animales():
    def __init__(self, mensaje):
        self.mensaje=mensaje

    def hablar(self):
        print(self.mensaje)


class Perro(Animales):
    def hablar(self):
        print("Yo hago Guau!")


class Pez(Animales):
    def hablar(self):
        print("Yo hago Glu!")


perro= Perro("Guaaaoo")
perro.hablar()
animal= Animales("miauu")
animal.hablar()