'''
Ejercicio 1
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los 
resultados obtenidos. Llamar a la clase Calculadora.'''

class Calculadora():

    def __init__(self, num1, num2):
        self._num1= num1
        self._num2=num2
    
    def suma(self):
        print("La suma de los numeros {} + {} es igual a {}".format(self._num1,self._num2,self._num1+self._num2))
    
    def resta(self):
        print("La resta de los numeros {} - {} es: {}".format(self._num1,self._num2,self._num1-self._num2))

    def multiplicacion(self):
        print("La multiplicacion de los numero {} * {} es: {}".format(self._num1,self._num2,self._num1*self._num2))


print("Buen Dia")
Operaciones= Calculadora(int (input("Digite el primer numero")), int (input("Digite el segundo dato")))

Operaciones.suma()
Operaciones.resta()
Operaciones.multiplicacion()

