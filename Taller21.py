# Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la 
# nota del alumno. Definir los métodos para inicializar sus atributos, 
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante():
    def __init__(self, nombre, nota):

        self._nombre= nombre
        self._nota=nota


    def imprimir(self):
        print("Su nombre es: {} \n y su nota es :{}".format(self._nombre,self._nota))

    #Para llamarlos con get
    @property
    def nombre(self):
        return self._nombre
    @property
    def nota(self):
        return self._nota
    def calculoresultado(self):
        if self._nota >=10:
            print("Aprobo la nota")
        else:
            print("No aprobo la nota")


Alumno1= Estudiante("Maria",10)

print("El nombre del Alumno Es {} el cual saco una nota de {}".format(Alumno1.nombre,Alumno1.nota))
Alumno1.calculoresultado()
Alumno1.imprimir()

Alumno2= Estudiante("Juan", 4)
Alumno2.imprimir()
Alumno2.calculoresultado()

