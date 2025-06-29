# Encapsulamiento es guion bajo __


class A():
    def __init__(self):
        self.contador=0
    
    def incrementar(self):
        self.contador +=1

    def cuenta (self):
        return self.contador

class B():
    def __init__(self):
        self.__contador=0
    
    def incrementar(self):
        self.__contador +=1

    def cuenta (self):
        return self.__contador



a= A()
b=B()
a.incrementar()
print("Objeto 1")
print(a.cuenta())
print(a.contador)
print("Objeto 2")
b.incrementar()
print(b.cuenta())
print(b.__contador)