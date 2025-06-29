#En el siguiente diccionario se encuentran capitales de los paises en el mundo, debes realizar un programa que pida un pais al usuario, y muestre la capital de ese pais, en dado caso el pais no este en el diccionario, se debe mostrar un mensaje diciendo que ese pais no se encuentra.
# {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

#Creamos el diccionario
diccionario = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela" : "Caracas", "España": "Madrid"}

pais= input("Ingrese un pais para conocer su Capital: ")

'''
#IN para verificar si un elemento esta dentro de otro
letra= pais.capitalize() in diccionario


if letra :
    print(diccionario[pais.capitalize()])

else:
    print("El Pais no se encuentra en el diccionario")
'''
#Otra forma

if pais.capitalize().title() in diccionario:
    print(diccionario[pais.title()])
else:
    print("El pais digitado no se encuentra en la lista")