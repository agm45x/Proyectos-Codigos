'''
Ejercicio 1

Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.



Ejercicio 2

Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

Pista: Si la letra ingresada por el usuario es en minúscula, el programa debe convertirla en mayúscula

'''
print('\v Menu \n')
print('1. Opcion')
print('2. Opcion')
menu=int(input("Digite una opcion: "))
if menu==1:
    firstword=input("Type the first Word: ")
    secondword=input("Type the second Word: ")

    if len(firstword) < 3 or len(secondword)< 3:
        print("No puede Rimar porque tiene menos de 3 caracteres") 
    else:

        if firstword[-3:] == secondword[-3:]:
            print("las palabras riman")
        elif firstword[-2:] == secondword[-2:]:
            print("Riman un poco")
        else:
            print("No Riman nada")
elif menu==2:
    opcion=input("Ingrese un valor A, B, C: ")    
    if opcion.lower()=='a':
        print("Usted a Votado por partido Rojo")
    elif opcion.lower()=='b':
        print("Usted a Votado por partido Verde")
    elif opcion.lower()=='c':
        print("Usted a Votado por partido Azul")
    else:
        print("Usted se a equivocado de opcion")



