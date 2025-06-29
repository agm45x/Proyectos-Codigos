'''
Ejercicio 1

En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, 
debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:
[20, 50, "Curso", 'Python', 3.14]

Ejercicio 2

Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están 
en las posiciones 4, 7 y 9 sean multiplicados por 2; por último, 
mostrar la lista nueva con los nuevos datos



'''
print("\v Menu \n")
print("1. Opcion")
print("2. Opcion")
menu=int(input(("Digite una Opcion:")))
if menu==1:
    lista=[20, 50, "Curso", 'Python', 3.14]
    print(lista)
    dato1=input("Digita un dato 1:")
    dato2=input("Digite un dato 2:")
    lista[0]=dato1
    lista[1]=dato2
    print(lista)
elif menu==2:
    numero=[1,2,3,4,5,6,7,8,9,10]
    numero[4]*=2
    numero[7]=numero[6]*2
    numero[9]=numero[8]*2
    print(numero)