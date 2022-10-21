import numpy
import sympy
import random

class Registro:
    __Bucket=None
    __tam=None
    __contador=None
    def __init__(self, N):
        self.__tam=N
        self.__Bucket=numpy.zeros(self.__tam, dtype=int)
        self.__contador=0
    def getcontador(self):
        return self.__contador
    def setbucket(self, elemento):
        if self.__contador<self.__tam:
            self.__Bucket[self.__contador]=elemento
            self.__contador+=1
            valor=1
        else:
            valor=0
        return valor
    def getbucket(self, elemento):
        i=0
        encontrado=0
        while i<self.__tam and self.__Bucket[i]!=elemento:
            i+=1
        if i<self.__tam:
            encontrado=1
        return encontrado
    def setcontador(self, cont):
        self.__contador=cont
    def desbordado(self):
        return not self.__contador<self.__tam
    def subocupado(self):
        return self.__contador<(self.__tam/3)
    def __str__(self):
        return str(self.__Bucket)


class TablaHash:
    __M=None
    __N=None
    __tabla=None
    def __init__(self, N, K):
        self.__N=N
        self.__M=int(N/0.7)
        self.__M=sympy.nextprime(self.__M)
        self.__tabla=[]
        for i in range(self.__M):
            self.__tabla.append(Registro(K))
        self.__tabla=numpy.array(self.__tabla)
    def insertar(self, elemento):
        if not self.__tabla[self.h(elemento)].setbucket(elemento):
            i=self.__N
            while(i<self.__M and not self.__tabla[i].setbucket(elemento)):
                i+=1
            if not i<self.__M:
                print("Se lleno el area de overflow")
    def buscar(self, elemento):
        valor=0
        if self.__tabla[self.h(elemento)].getbucket(elemento):
            valor=1
        else:
            i=self.__N
            while(i<self.__M and self.__tabla[i].setbucket(elemento)):
                i+=1
            if i<self.__M:
                valor=1
        return valor
    def cantidaddesbordes(self):
        contador=0
        for elemento in self.__tabla:
            if elemento.desbordado():
                contador+=1
        return contador
    def cantidadsubocupados(self):
        contador=0
        for elemento in self.__tabla:
            if elemento.subocupado():
                contador+=1
        return contador
    def h(self, numero):
        return ((numero%self.__N)%self.__N)
    def __str__(self):
        return ("Tamaño: {}  Claves: {}".format(self.__M, self.__N))
    def ultimo(self):
        for i in self.__tabla:
            print (i)

if __name__=='__main__':
    n=10
    k=2
    tabla=TablaHash(n, k)
    print (tabla)
    for i in range(n):
        a=random.randint(1, n*n)
        tabla.insertar(a)
    print("Subocupados: ", tabla.cantidadsubocupados(), "   Desbordados: ", tabla.cantidaddesbordes())
    tabla.ultimo()