#Escribir una funcion que reciba una muestra de numeros en una tupla
#y devuelva su medida

def medida(*tupla):

    print(len(tupla))

    for i in tupla:
        print(i)

medida(3,23,4,53,3)
