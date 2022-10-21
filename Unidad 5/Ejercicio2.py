from random import randint
import numpy
import sympy

class TablaHash:
    __M=None
    __tabla=None
    def __init__(self, N):
        #self.__M=int(N/0.7)
        self.__M=sympy.nextprime(N/0.7)
        self.__random=randint(0, 1000)
        self.__tabla=numpy.zeros(self.__M)
    def insertar(self, elemento):
        i=self.h(elemento)
        if self.__tabla[i]==0:
            self.__tabla[i]=elemento
        else:
            index=i
            i=self.h(i+self.__random)
            while self.__tabla[i]!=elemento and self.__tabla[i]!=0 and i!=index:
                i=self.h(i+self.__random)
            if self.__tabla[i]==0:
                self.__tabla[i]=elemento
            elif i==index:
                print("La tabla esta llena")
            elif self.__tabla[i]==elemento:
                print("El elemento ya esta almacenado en la tabla.")
            else:
                raise ValueError('Error')
    def buscar(self, elemento):
        i=self.h(elemento)
        if self.__tabla[i]==elemento:
            return 1
        else:
            index=i
            i=self.h(i+self.__random)
            while self.__tabla[i]!=elemento and self.__tabla[i]!=0 and i!=index:
                i=self.h(i+self.__random)
            if self.__tabla[i]==0:
                return 0
            elif i==index:
                return 0
            elif self.__tabla[i]==elemento:
                return 1
            else:
                raise ValueError('Error')
    def h(self, n):
        return n%self.__M
    def rand(self):
        return self.__random

if __name__=='__main__':
    n=1000
    tabla=TablaHash(n)
    print (tabla.rand())
    for i in range(n):
        a=randint(0, n*n)
        tabla.insertar(a)
    print(a)
    print(tabla.h(a))
    print(tabla.buscar(a))
    
