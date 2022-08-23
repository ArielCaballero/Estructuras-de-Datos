class Nodo:
    __siguiente=None
    __Dato=None
    def __init__(self, dato):
        self.__Dato=dato
        self.__siguiente=None
    def getDato(self):
        return self.__Dato
    def setDato(self, dato):
        self.__Dato=dato
    def getsiguiente(self):
        return self.__siguiente
    def setsiguiente(self, siguiente):
        self.__siguiente=siguiente

class PilaSecuencial:
    __lista=[]
    __tope=-1
    __max=0
    def __init__(self, max=0):
        self.__lista=[]
        self.__tope=-1
        self.__max=max
    def insertar(self, elemento):
        if self.__tope==self.__max-1:
            self.__max+=5
        self.__lista.append(elemento)
        self.__tope+=1
    def suprimir(self):
        if not self.vacia():
            valor=self.__lista.pop(self.__tope)
            self.__tope-=1
        else:
            print("La lista ya esta vacia")
            valor=-1
        return valor
    def vacia(self):
        return(self.__tope==-1)
    def mostrar(self):
        print (self.__lista)
    
class PilaEnlazada:
    __cabeza=None
    __tope=-1
    def __init__(self):
        self.__cabeza=None
        self.__tope=-1
    def insertar(self, elemento):
        if type(elemento)==Nodo:
            elemento.setsiguiente(self.__cabeza)
            self.__cabeza=elemento
            self.__tope+=1
        else:
            print("El dato a insertar no del tipo nodo")
    def suprimir(self):
        if self.__cabeza!=None:
            aux=self.__cabeza
            self.__cabeza=self.__cabeza.getsiguiente()
            self.__tope-=1
            return aux.getdato()
        else:
            print("La pila ya esta vacía")
            return None
    def vacia(self):
        return (self.__tope==-1)
    def mostrar(self):
        auxiliar=self.__cabeza
        while auxiliar!=None:
            print(auxiliar.getdato())
            auxiliar=auxiliar.getsiguiente()