# # Ejercicio 1

# # Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
# # luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. 
# # Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
# # Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

# class Fabrica():

#     def __init__(self, llantas, color, precio):
#         self._llantas= llantas
#         self._color= color
#         self._precio=precio

#     @property
#     def llantas(self):
#         return self._llantas
    
#     @property
#     def color(self):
#         return self._color
#     @property
#     def  precio(self):
#         return self._precio
    

# class Carro(Fabrica):
#     pass

# class Moto(Fabrica):
#     pass


# Transporte1= Fabrica(4,"azul",1000)
# carro1= Carro(4,"rojo",5000)
# moto1=Moto(2,"verde",1000)

# print("El Transporte 1 tiene:{} llantas, es de Color:{}, su precio es:{} ".format(Transporte1.llantas,Transporte1.color,Transporte1.precio))

# print("El Carro tiene:{} llantas, es de Color:{}, su precio es:{} ".format(carro1.llantas,carro1.color,carro1.precio))

# print("La Moto tiene:{} llantas, es de Color:{}, su precio es:{} ".format(moto1.llantas,moto1.color,moto1.precio))


class Fabrica():

    def __init__(self, llantas, color, precio):
        self._llantas= llantas
        self._color= color
        self._precio=precio

    @property
    def llantas(self):
        return self._llantas
    
    @property
    def color(self):
        return self._color
    @property
    def  precio(self):
        return self._precio


class Carro(Fabrica):
    pass
class Moto(Fabrica):
        def datos(self):
            print("Este transporte tiene una cantidad de {} llantas".format(self._llantas))
            print("Este transporte es de color: {}".format(self._color))

 


Transporte1= Fabrica(4,"azul",1000)
carro1= Carro(4,"rojo",5000)
moto1=Moto(2,"verde",1000)

moto1.datos()
