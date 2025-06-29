'''Ejercicio 2

Escribir un programa que pregunte al usuario su edad
 y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

'''

edad= int (input("Digite la edad que presenta: "))
año_nacimiento= 2025-edad
cont=1
while edad > 0:
    
    print("En el Año {} cumplio {} años".format(año_nacimiento, cont))
    año_nacimiento+=1
    edad-=1
    cont+=1