# Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado
#y la Otra area de un circulo

def areacuadrado(base, altura):
   area= base*altura
   return area

    
print(areacuadrado(10,10))

def areacirculo(radio):
   area=(radio**2)*3.14
   print(area)

areacirculo(10)
   
def areacirculo(radio):
   return pow(radio,2)*3.14

print(areacirculo(10))
