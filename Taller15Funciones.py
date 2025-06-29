'''
Ejercicio 1

Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista.
Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nuevas

'''
numeros=[]
cantidad= int (input("Cuantos numeros va a ingresar:"))

def ingresar():
    for i in range(cantidad):
        dato= int (input("Digite numero:"))
        numeros.append(dato)

def separar():
    par=[]
    impar=[]
    for i in numeros:
        if i%2==0:
            par.append(i)
        else:
            impar.append(i)
    par.sort()
    impar.sort()
    print(par)
    print(impar)
ingresar()
separar()

