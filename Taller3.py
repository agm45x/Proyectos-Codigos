'''
Ejercicio 1

Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula 
general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y 
el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”


Ejercicio 2

Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final

'''

#importar libreria
from math import sqrt
print("\t 1-Primer Ejercicio")
print("\t 2-Segundo Ejercicio")
print("\n")
menu=int(input("Digite la tarea a realiza 1 o 2:"))

if(menu==1):

    a=float(input("Digite el valor de A:"))
    b=float(input("Digite el valor de B:"))
    c=float(input("Digite el valor de C:"))


    if((b**2)-(4*a*c))< 0:

        print("No se puede realizar operacion porque no se puede sacar raiz a un numero negativo")


    else:
        solucion1=((-b) + sqrt((b**2)-(4*a*c)))/(2*a)
        solucion2=((-b) - sqrt((b**2)-(4*a*c)))/(2*a)
        print("La solucion es: ", "X1:",solucion1," \n X2:",solucion2)
elif(menu==2):

    p1=float(input("Digite el valor de Practica1:"))
    p2=float(input("Digite el valor de Practica2:"))
    p3=float(input("Digite el valor de Practica3:"))
    ep=float(input("Digite el valor de Examen Parcial:"))
    ef=float(input("Digite el valor de Examen final:"))

    pp= (p1+p2+p3)/3
    prom=(pp+(2*ep)+ (3*ef))/6

    print("El promedio del estudiante es: " + "\n Promedio practicas: ", pp, "\n Promedio final: ", prom)
    
