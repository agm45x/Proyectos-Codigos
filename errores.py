
while True:
    try:
        edad = int(input("Digite su edad: "))
        print("Tu edad es: ", edad)
        break
        
    except: 
        print("Ingresastes un valor erroneo")
    finally:
        print("La ejecucion a terminado")