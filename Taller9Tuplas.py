'''
Ejercicio 1

Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla
'''
meses=('Enero','Febrero','marzo',
       'abril','mayo','junio','julio',
       'agosto','septiembre', 'octubre',
       'noviembre','diciembre'
       
       )
numero= int (input("Digite un numero del 1 al 12:"))
print("Usted digito el mes: " ,meses[numero-1])