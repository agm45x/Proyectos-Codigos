class A():

    def __init__(self):
        self._cuenta=0
        self._contador=0

    #Significa que puede ser llamado como un atributo
    @property
    def cuenta(self):
        return self._cuenta
    
    @property
    def contador(self):
        return self._contador

    #Metodos Set, modificar un atributo
    @cuenta.setter
    def cuenta(self,cuenta):
        self._cuenta=cuenta
    
    @contador.setter
    def contador(self, contador):
        self._contador=contador



a= A()
print(a.cuenta)
a.cuenta=20
a.contador=10
print(a.cuenta)
print(a.contador)
