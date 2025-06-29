'''
Crear una funcion que pida dos numeros. 
Si el primero es mayor al segundo, el programa debe retornar el valor 1; 
si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0
'''
def mayor():
    n1= int (input("Digite primer numero: "))
    n2= int (input("Digite segundo numero:"))

    if n1> n2:
        return 1
    elif n2> n1:
        return -1
    else:
        return 0
    
print(mayor())
