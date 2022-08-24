class ColaSecuencial:
    __Lista=[]
    __max=0
    __pr=None
    __ul=None
    __cant=None
    def __init__(self, max=0):
        self.__Lista=[]
        self.__max=max
        self.__pr=0
        self.__ul=0
        self.__cant=0
    def vacia(self):
        return self.__cant==0
    def insertar(self, elemento):
        valor=None
        if self.__cant<self.__max:
            self.__ul==(self.__ul+1)%self.__max
            self.__Lista[self.__ul]=elemento
            self.__cant+=1
            valor=elemento
        else:
            print("La pila esta llena\n")
        return valor
    def suprimir(self):
        valor=None
        if not self.vacia():
            valor=self.__Lista[self.__pr]
            self.__pr==(self.__pr+1)%self.__max
            self.__cant-=1
        else:
            print("La pila esta vacia\n")
        return valor
    def recorrer(self):
        if not self.vacia():
            j=self.__pr
            for i in range(self.__cant):
                print(self.__Lista[j])
                j+=(j+1)%self.__max

class Nodo:
    __dato=None
    __siguiente=None
    def __init__(self, elemento):
        self.__dato=elemento
        self.__siguiente=None
    def getdato(self):
        return self.__dato
    def getsiguiente(self):
        return self.__siguiente
    def setdato(self, elemento):
        self.__dato=elemento
    def setsiguiente(self, siguiente):
        self.__siguiente=siguiente


class ColaEnlazada:
    __cant=0
    __pr=None
    __ul=None
    def __init__(self, cant=0, pr=None, ul=None):
        self.__cant=cant
        self.__pr=pr
        self.__ul=ul
    def vacia(self):
        return self.__cant==0
    def insertar(self, elemento):
        if type(elemento!=Nodo):
            elemento=Nodo(elemento)
        if not self.vacia():
            self.__ul.setsiguiente(elemento)
            self.__ul=elemento
        else:
            self.__pr=elemento
            self.__ul=elemento
        self.__cant+=1
        return elemento
    def suprimir(self):
        if not self.vacia():
            aux=self.__pr
            dato=self.__pr.getdato()
            self.__pr=self.__pr.getsiguiente()
            self.__cant-=1
            valor=dato
            del aux
            if self.__pr==None:
                self.__ul=None
        else:
            print("La cola ya esta vacia")
            valor=None
        return valor
    def recorrer(self):
        aux=self.__pr
        while aux!=None:
            print(aux)
            aux=aux.getsiguiente()