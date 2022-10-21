from random import randint
import numpy
import sympy

class Nodo:
    __dato=None
    __siguiente=None
    def __init__(self, dato):
        self.__dato=dato
        self.__siguiente=None
    def getdato(self):
        return self.__dato
    def setdato(self, dato):
        self.__dato=dato
    def getsiguiente(self):
        return self.__siguiente
    def setsiguiente(self, siguiente):
        self.__siguiente=siguiente

class ListaEnlazadaPosicion:
    def __init__(self):
        self.__cantidad=0
        self.__primero=None
        self.__ultimo=None
    def insertar(self, elemento, posicion=-1):
        if type(elemento)!=Nodo:
            elemento=Nodo(elemento)
        if posicion==-1:
            posicion=self.__cantidad+1
        if posicion>=1 and posicion-1<=self.__cantidad:
            if self.vacia():
                self.__primero=elemento
                self.__ultimo=elemento
            else:
                if posicion==1:
                    aux=self.__primero
                    self.__primero=elemento
                    self.__primero.setsiguiente(aux)
                else:
                    i=0
                    aux=self.__primero
                    while i<posicion-2:
                        aux=aux.getsiguiente()
                        i+=1
                    auxiliar=aux.getsiguiente()
                    aux.setsiguiente(elemento)
                    elemento.setsiguiente(auxiliar)
                    if auxiliar==None:
                        self.__ultimo=elemento
            self.__cantidad+=1
        else:
            print("Posicion no valida")
    def suprimir(self, posicion):
        valorretorno=None
        if posicion>=1 and posicion-1<=self.__cantidad:
            if self.vacia():
                print("La lista ya esta vacia")
            else:
                i=0
                aux=self.__primero
                while i<posicion-2:
                    aux=aux.getsiguiente()
                    i+=1
                eliminado=aux.getsiguiente()
                aux.setsiguiente(eliminado.getsiguiente())
                self.__cantidad-=1
                valorretorno=eliminado.getdato()
        else:
            print("Posicion no valida")
        return valorretorno
    def Recuperar(self, posicion):
        if 0<posicion and not self.vacia() and self.__cantidad>posicion-1:
            aux=self.__primero
            i=0
            while i<posicion-1:
                aux=aux.getsiguiente()
                i+=1
            return aux.getdato()
        else:
            print("Indice invalido")
    def Buscar(self, elemento):
        valor=-1
        if not self.vacia():
            bandera=True
            aux=self.__primero
            i=0
            while aux!=None and bandera:
                if aux.getdato()==elemento:
                    bandera=not bandera
                aux=aux.getsiguiente()
                i+=1
            if not bandera:
                valor=i
        return valor
    def Primer_Elemento(self):
        return self.__primero.getdato()
    def Ultimo_Elemento(self):
        return self.__ultimo.getdato()
    def Siguiente(self, posicion):
        if 0<posicion and not self.vacia() and self.__cantidad>posicion:
            aux=self.__primero
            i=0
            while i<posicion:
                aux=aux.getsiguiente()
                i+=1
            return aux.getdato()
        else:
            print("Indice invalido")
    def Anterior(self, posicion):
        if 1<posicion and not self.vacia() and self.__cantidad>posicion-1:
            aux=self.__primero
            i=0
            while i<posicion-2:
                aux=aux.getsiguiente()
                i+=1
            return aux.getdato()
        else:
            print("Indice invalido")
    def vacia(self):
        return self.__cantidad==0
    def recorrer(self):
        cadena=""
        aux=self.__primero
        while aux!=None:
            cadena+=aux.getdato()+"->"
            aux=aux.getsiguiente()
        print(cadena)
    def getcantidad(self):
        return self.__cantidad



class TablaHash:
    __M=None
    __tabla=None
    def __init__(self, N):
        self.__M=sympy.nextprime(54)
        self.__tabla=[]
        for i in range(self.__M):
            self.__tabla.append(ListaEnlazadaPosicion())
        self.__tabla=numpy.array(self.__tabla)
    def insertar(self, elemento):
        self.__tabla[self.h(elemento)].insertar(elemento)
    def buscar(self, elemento):
        if self.__tabla[self.h(elemento)].Buscar(elemento):
            return 1
        else:
            return 0
    def longitud(self):
        for i in range(len(self.__tabla)):
            print(i,": ", self.__tabla[i].getcantidad())
    def promedio(self):
        prom=0
        for i in self.__tabla:
            prom+=i.getcantidad()
        return prom/self.__M
    
    def cantidad(self):
        prom=self.promedio()
        cant=0
        for i in self.__tabla:
            if abs(prom-i.getcantidad())>3:
                cant+=1
        return cant
    def h(self, numero):
        cadena=str(numero)
        suma=0
        for c in cadena:
            suma+=int(c)
        return suma
    def numero(self, numero):
        return self.__tabla[self.h(numero)].Recuperar(1)

if __name__=='__main__':
    n=1000
    tabla=TablaHash(n)
    for i in range(n):
        a=randint(0, n*n)
        tabla.insertar(a)
    tabla.longitud()
    print("Promedio: ", tabla.promedio(), "   Cantidad: ", tabla.cantidad())