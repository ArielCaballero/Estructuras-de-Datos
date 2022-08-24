from random import random


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
    __frecuencia=None
    __tiempoatencion=None
    def __init__(self, frecuencia, tiempoatencion, cant=0, pr=None, ul=None):
        self.__cant=cant
        self.__pr=pr
        self.__ul=ul
        self.__frecuencia=frecuencia
        self.__tiempoatencion=tiempoatencion
    def getfrecuencia(self):
        return self.__frecuencia
    def gettiempo(self):
        return self.__tiempoatencion
    def vacia(self):
        return self.__cant==0
    def insertar(self, elemento=0):
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
    def mostrar(self):
        aux=self.__pr
        cola=""
        while aux!=None:
            cola=cola+ str(aux.getdato()) + "->"
            aux=aux.getsiguiente()
        print(cola)
    def actualizar(self):
        aux=self.__pr
        while aux!=None:
            aux.setdato(aux.getdato()+1)
            aux=aux.getsiguiente()

if __name__=="__main__":
    Colaespera=ColaEnlazada(2, 5)
    tiempototal=int(input("Ingrese la cantidad de minutos a analizar en la simulación: "))
    cajero=0
    Tiempomaxespera=0
    Clientesatendidos=0
    for contador in range(tiempototal):
        llegadacliente=random()
        if llegadacliente<(1/Colaespera.getfrecuencia()):
            Colaespera.insertar()
        if cajero==0:
            if (not Colaespera.vacia()):
                esperacliente=Colaespera.suprimir()
                if Tiempomaxespera<esperacliente:
                    Tiempomaxespera=esperacliente
                Clientesatendidos+=1
                cajero=Colaespera.gettiempo()
        else:
            cajero-=1
        Colaespera.actualizar()
        Colaespera.mostrar()
    print("Tiempo maximo de espera de un cliente en la Cola: ", Tiempomaxespera, " minutos")

        