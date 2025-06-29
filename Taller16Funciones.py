'''
Escribir una función que reciba un número entero positivo y 
devuelva su factorial.


'''
num= int (input("Digite un numero entero positivo: "))
multiplicacion=1
def factorial():
    multiplicacion=1
    for i in range(1,num+1):
       multiplicacion=multiplicacion*i
    print("El factorial es {} ".format(multiplicacion))

factorial()  