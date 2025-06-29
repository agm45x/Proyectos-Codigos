while True:
    try:
        num1= int (input("Digite un Numero: "))
        resultado=100/num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("Nose puede dividir entre cero")


while True:
    try:
        edad= int (input("Digite tu edad: "))
        
        print("Tu edad es: ", edad)
        break
    except ValueError:
        print("Dato no valido")

while True:
    try:
        edad= int (input("Digite tu edad: "))
        print("Tu edad es: ", edad)
        break
    except KeyboardInterrupt:
        print("Has Cancelado la ejecucion")
        break