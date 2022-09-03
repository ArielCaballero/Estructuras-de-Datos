import numpy

class Nodo:
    __dato=None
    __siguiente=None
    def __init__(self, dato=0,siguiente=-1):
        self.__dato=dato
        self.__siguiente=siguiente
    def getdato(self):
        return self.__dato
    def setdato(self, dato):
        self.__dato=dato
    def getsiguiente(self):
        return self.__siguiente
    def setsiguiente(self, siguiente):
        self.__siguiente=siguiente

class ListaEnlazadaCursores:
    def __init__(self, n):
        self.__cantidad=n
        Lista=[]
        for i in range(n+2):
            Lista.append(Nodo(siguiente=i+1))
        self.__Lista=numpy.array(Lista, dtype=Nodo)
        self.__Lista[0]=Nodo(self.__cantidad)
        self.__Lista[0].setsiguiente(2)
        self.__Lista[1]=Nodo(0)
        self.__Lista[1].setsiguiente(-1)
        self.__Lista[self.__cantidad+1].setsiguiente(-1)
    def insertar(self, elemento, posicion):
        if type(elemento)!=Nodo:
            elemento=Nodo(elemento)
        if posicion>0 and posicion-1<=self.__Lista[1].getdato():
            if not self.llena():
                auxiliar=1
                i=0
                while i<posicion:
                    anterior=auxiliar
                    auxiliar=self.__Lista[auxiliar].getsiguiente()
                    i+=1
                pos=self.__Lista[0].getsiguiente()
                self.__Lista[0].setsiguiente(self.__Lista[pos].getsiguiente())
                self.__Lista[anterior].setsiguiente(pos)
                self.__Lista[pos]=elemento
                if auxiliar!=-1:
                    self.__Lista[pos].setsiguiente(auxiliar)
                else:
                    self.__Lista[pos].setsiguiente(-1)
                self.__Lista[0].setdato(self.__Lista[0].getdato()-1)
                self.__Lista[1].setdato(self.__Lista[1].getdato()+1)
            else:
                print("Lista Llena")
        else:
            print("Indice invalido")
    def suprimir(self, posicion):
        valorretorno=None
        if posicion>=1 and posicion-1<=self.__Lista[1].getdato():
            if self.vacia():
                print("La lista ya esta vacia")
            else:
                auxiliar=1
                i=0
                while i<posicion:
                    anterior=auxiliar
                    auxiliar=self.__Lista[auxiliar].getsiguiente()
                    i+=1
                self.__Lista[auxiliar].setdato(0)
                self.__Lista[anterior].setsiguiente(self.__Lista[auxiliar].getsiguiente())
                self.__Lista[0].setdato(self.__Lista[0].getdato()+1)
                self.__Lista[1].setdato(self.__Lista[1].getdato()-1)
                self.__Lista[auxiliar].setsiguiente(self.__Lista[0].getsiguiente())
                self.__Lista[0].setsiguiente(auxiliar)
                valorretorno=self.__Lista[auxiliar].getdato()
        else:
            print("Posicion no valida")
        return valorretorno
    def Recuperar(self, posicion):
        if posicion>=1 and posicion-1<=self.__Lista[1].getdato():
            if self.vacia():
                print("La lista ya esta vacia")
            else:
                auxiliar=self.__Lista[1].getsiguiente()
                i=1
                while i<posicion:
                    auxiliar=self.__Lista[auxiliar].getsiguiente()
                    i+=1
                valorretorno=self.__Lista[auxiliar].getdato()
        else:
            print("Posicion no valida")
        return valorretorno
    def Buscar(self, elemento):
        valorretorno=None
        if not self.vacia():
                auxiliar=self.__Lista[1].getsiguiente()
                i=1
                while auxiliar!=-1 and elemento!=self.__Lista[auxiliar].getdato():
                    auxiliar=self.__Lista[auxiliar].getsiguiente()
                    i+=1
                if auxiliar!=-1:
                    valorretorno=i
                else:
                    print("No se encontro el elemento")
        else:
            print("La lista esta vacia")
        return valorretorno
    def Primer_Elemento(self):
        return self.__Lista[self.__Lista[1].getsiguiente()].getdato()
    def Ultimo_Elemento(self):
        auxiliar=1
        i=1
        while self.__Lista[auxiliar].getsiguiente()!=-1:
            auxiliar=self.__Lista[auxiliar].getsiguiente()
        return self.__Lista[auxiliar].getdato()
    def Siguiente(self, posicion):
        valorretorno=-1
        if posicion>=1 and posicion<self.__Lista[1].getdato():
            if self.vacia():
                print("La lista esta vacia")
            else:
                auxiliar=self.__Lista[1].getsiguiente()
                i=1
                while i<=posicion:
                    auxiliar=self.__Lista[auxiliar].getsiguiente()
                    i+=1
                valorretorno=self.__Lista[auxiliar].getdato()
        else:
            print("Posicion no valida")
        return valorretorno
    def Anterior(self, posicion):
        valorretorno=-1
        if posicion>1 and posicion<=self.__Lista[1].getdato():
            if self.vacia():
                print("La lista esta vacia")
            else:
                auxiliar=self.__Lista[1].getsiguiente()
                i=1
                while i<posicion-1:
                    auxiliar=self.__Lista[auxiliar].getsiguiente()
                    i+=1
                valorretorno=self.__Lista[auxiliar].getdato()
        else:
            print("Posicion no valida")
        return valorretorno
    def vacia(self):
        return self.__Lista[1].getsiguiente()==-1
    def llena(self):
        return self.__Lista[0].getsiguiente()==-1
    def recorrer(self):
        cadena=""
        for i in range(len(self.__Lista)):
            cadena=cadena+"  {:2}".format(i)
        cadena=cadena+"\n"
        for elemento in self.__Lista:
            cadena=cadena+"  {:2}".format(elemento.getdato())
        cadena=cadena+"\n"
        for elemento in self.__Lista:
            cadena=cadena+"  {:2}".format(elemento.getsiguiente())
        print(cadena)

a=ListaEnlazadaCursores(5)
a.recorrer()
b=int(input("1-Insertar\n2-Suprimir\n3-Recuperar\n4-Buscar\n5-Primero\n6-Ultimo\n7-Siguiente\n8-Anterior\n0-Salir\n"))
while b!=0:
    if b==1:
        a.insertar(input("Ingrese un elemento a la lista\n"),int(input("Ingrese una posicion\n")))
    elif b==2:
        a.suprimir(int(input("Ingrese una posicion\n")))
    elif b==3:
        print(a.Recuperar(int(input("Ingrese una posicion\n"))))
    elif b==4:
        print(a.Buscar(input("Ingrese un elemento de la lista\n")))
    elif b==5:
        print(a.Primer_Elemento())
    elif b==6:
        print(a.Ultimo_Elemento())
    elif b==7:
        print(a.Siguiente(int(input("Ingrese una posicion\n"))))
    elif b==8:
        print(a.Anterior(int(input("Ingrese una posicion\n"))))
    a.recorrer()
    b=int(input("1-Insertar\n2-Suprimir\n3-Recuperar\n4-Buscar\n5-Primero\n6-Ultimo\n7-Siguiente\n8-Anterior\n0-Salir\n"))
