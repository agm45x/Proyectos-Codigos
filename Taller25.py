# Ejercicio 1

# Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad).
# Otra llamada Carerra, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). 
# Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. 
# El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona.

class Universidad():
    def __init__(self,nombre):
        self._Nombre=nombre
    
class Carerra():
    def carrera(self,especialidad):
        self._especilidad=especialidad
        

class Estudiante(Universidad, Carerra):
    def datos(self, nombre, edad):
        self._nombre=nombre
        self._edad=edad
        print("Mi nombre es {}, tengo {} años. mi especilidad es {} y estudio en la universidad {}".format(self._nombre,self._edad, self._especilidad, self._Nombre))


persona= Estudiante("UTB")
persona.carrera("Sistemas")
persona.datos("Juan Martin", 20)