'''
Ejercicio 1

Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.

'''
#Creacion de la variable
Cadena="Te quiero solo como amigo"
 #Primer punto
print(Cadena[0:2])
 #Segundo punto
print(Cadena[-3:])
 #tercer punto
print(Cadena[::2])
#cuarto punto
print(Cadena[::-1])
#cuarto punto
print(Cadena+Cadena[::-1])