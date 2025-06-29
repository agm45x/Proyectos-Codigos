'''
Ejercicio 1

Crear un programa que pida al usuario una letra, y si es vocal, muestre el mensaje "Es vocal". Sino, decirle al usuario que no es vocal



Ejercicio 2

Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

'''
print("\t Menu")
print("\n 1.Ejercicio")
print("\n 2.Ejercicio")
print("\n 3.Ejercicio")
menu=int(input("Digite una Opcion: "))
if menu==1:
    letra=input("Digite una letra:")
    if letra.lower()=='a':
        print("Es una Vocal")
    elif letra.lower()=='e':
        print("Es una vocal")
    elif letra.lower()=='i':
        print("Es una vocal")
    elif letra.lower()=='o':
        print("Es una vocal")
    elif letra.lower()=='u':
        print("Es una vocal")
    else:
        print("No es una vocal")
elif menu==2:
    num=int(input("Digite un numero"))
    if num>=0:
        print("El valor absoluto es: ", num)
    else:
        num=num*-1
        print("El valor absoluto es: ", num)
elif menu==3:
    letra=input("Digite una letra:")
    letra=letra.lower()
    if letra in 'aeiou':
        print("Es una vocal")



