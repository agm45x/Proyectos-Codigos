'''
Ejercicio 2

Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, 
pero, solo imprimiendo los números que sean impares
'''
num1= int (input("Digite numero 1:"))
num2= int (input ("Digite numero 2:"))
for i in range(num1, num2+1):
    if i%2 != 0:
        print(i)