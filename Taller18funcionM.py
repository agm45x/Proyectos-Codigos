'''
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, 
y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
deberá aplicar un 21%.
'''
def calculoiva():
    monto= int (input("Digite el monto de la factura:"))
    iva= (int (input("Digite porcentaje IVA: ")))/100
    if iva != 0:
        valorfactura=monto*(1+iva)
    else:
        valorfactura= monto*1.21
    return valorfactura


print(calculoiva())
