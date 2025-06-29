'''
Ejercicio 1

Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas

Ejercicio 2

Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>
'''
print('\n Menu')
print("1. Ejercicio 1")
print('\n2. Ejercicio 2')
menu=int(input(("Digite una opcion 1 o 2: ")))

if(menu==1):
    vocal=input("Digite una vocal en minuscula:")
    letra=input("Digite una letra en Mayuscula")
    print(vocal.upper() + letra.lower())

elif(menu==2):

    nombre=input("Digite su nombre:")
    edad=int(input("Digite su edad:"))
    sexo=input("Digite su sexo:")
    print("Te llamas: {} \n Tu edad: {} \n Tu sexo: {}".format(nombre, edad, sexo))

