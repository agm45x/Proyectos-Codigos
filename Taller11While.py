'''
Ejercicio 1

Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
'''
numero= int (input("Digite Numero que quisiera ver la tabla de multiplicar:"))

controlador=1

while controlador < 11:

    print(numero,"x", controlador, ":", numero*controlador)

    controlador +=1

print("Esta es toda la tabla de multiplicar")