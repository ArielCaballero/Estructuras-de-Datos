class ListaSecuencialPosicion:
    def __init__(self,n):
        self.__Lista=[]
        self.__cantidad=0
        self.__max=n
    def insertar(self, elemento, posicion):
        if 0<posicion and self.__cantidad>=posicion-1 and not self.llena():
            if not self.vacia():
                i=self.__cantidad-1
                self.__Lista.append(self.__Lista[i])
                while i>posicion-1:
                    self.__Lista[i]=self.__Lista[i-1]
                    i-=1
                self.__Lista[posicion-1]=elemento
            else:
                self.__Lista.append(elemento)
            self.__cantidad+=1
        else:
            print("Indice invalido")
    def suprimir(self, posicion):
        variable=None
        if 0<posicion and not self.vacia() and self.__cantidad>=posicion:
            i=posicion-1
            variable=self.__Lista[i]
            while i<self.__cantidad-2:
                self.__Lista[i]=self.__Lista[i+1]
                i+=1
            self.__cantidad-=1
            self.__Lista.pop(i)
        else:
            print("Indice invalido")
        return variable
    def Recuperar(self, posicion):
        if 0<posicion and not self.vacia() and self.__cantidad>posicion-1:
            return self.__Lista[posicion-1]
        else:
            print("Indice invalido")
    def Buscar(self, elemento):
        i=0
        bandera=True
        while i<self.__cantidad and bandera:
            if self.__Lista[i]==elemento:
                bandera=not bandera
            i+=1
        if not bandera:
            return i
        else:
            print("No se encontro el elemento")
    def Primer_Elemento(self):
        return self.__Lista[0]
    def Ultimo_Elemento(self):
        return self.__Lista[self.__cantidad-1]
    def Siguiente(self, posicion):
        if 0<posicion and not self.vacia() and self.__cantidad>posicion:
            return self.__Lista[posicion]
        else:
            print("Indice invalido")
    def Anterior(self, posicion):
        if 1<posicion and not self.vacia() and self.__cantidad>posicion-1:
            return self.__Lista[posicion-2]
        else:
            print("Indice invalido")
    def vacia(self):
        return self.__cantidad==0
    def llena(self):
        return self.__max==self.__cantidad
    def recorrer(self):
        cadena=""
        for i in range(self.__cantidad):
            cadena=cadena +" "+self.__Lista[i]
        print(cadena)
    def mostrar(self):
        print(self.__Lista)

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
    def insertar(self, elemento, posicion):
        if type(elemento)!=Nodo:
            elemento=Nodo(elemento)
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
        valor=None
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
            else:
                print("No se encontro el elemento")
        else:
            print("La lista esta vacia")
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

class ListaSecuencialContenido:
    def __init__(self,n):
        self.__Lista=[]
        self.__cantidad=0
        self.__max=n
    def insertar(self, elemento):
        if not self.llena():
            if self.vacia():
                self.__Lista.append(elemento)
            else:
                i=0
                while i<self.__cantidad and elemento<self.__Lista[i]:
                    i+=1
                self.__Lista.append(self.__Lista[self.__cantidad-1])
                j=self.__cantidad-1
                while j>i:
                    self.__Lista[j]=self.__Lista[j-1]
                    j-=1
                self.__Lista[i]=elemento
            self.__cantidad+=1
        else:
            print("La lista está llena")
    def suprimir(self, elemento):
        variable=None
        if not self.vacia():
            i=0
            while i<self.__cantidad and self.__Lista[i]!=elemento:
                i+=1
            if i<self.__cantidad:
                variable=self.__Lista[i]
                while i<self.__cantidad-2:
                    self.__Lista[i]=self.__Lista[i+1]
                    i+=1
                self.__cantidad-=1
                self.__Lista.pop(i)
        else:
            print("No se encontro el elemento")
        return variable
    def Recuperar(self, posicion):
        if 0<posicion and not self.vacia() and self.__cantidad>posicion-1:
            return self.__Lista[posicion-1]
        else:
            print("No se encontro el elemento")
    def Buscar(self, elemento):
        i=0
        bandera=True
        while i<self.__cantidad and bandera:
            if self.__Lista[i]==elemento:
                bandera=not bandera
            i+=1
        if not bandera:
            return i
        else:
            print("No se encontro el elemento")
    def Primer_Elemento(self):
        return self.__Lista[0]
    def Ultimo_Elemento(self):
        return self.__Lista[self.__cantidad-1]
    def Siguiente(self, elemento):
        if not self.vacia():
            i=0
            while i<self.__cantidad and self.__Lista[i]!=elemento:
                i+=1
            if i==self.__cantidad-1:
                print("Este elemento no tiene siguiente")
            else:
                return self.__Lista[i+1]
        else:
            print("No se encontro el elemento")
    def Anterior(self, elemento):
        if not self.vacia():
            i=0
            while i<self.__cantidad and self.__Lista[i]!=elemento:
                i+=1
            if i==0:
                print("Este elemento no tiene anterior")
            else:
                return self.__Lista[i-1]
        else:
            print("No se encontro el elemento")
    def vacia(self):
        return self.__cantidad==0
    def llena(self):
        return self.__max==self.__cantidad
    def recorrer(self):
        cadena=""
        for i in range(self.__cantidad):
            cadena=cadena +" "+self.__Lista[i]
        print(cadena)
    def mostrar(self):
        print(self.__Lista)

class ListaEnlazadaContenido:
    def __init__(self):
        self.__cantidad=0
        self.__primero=None
        self.__ultimo=None
    def insertar(self, elemento):
        if type(elemento)!=Nodo:
            elemento=Nodo(elemento)
        if self.vacia():
            self.__primero=elemento
            self.__ultimo=elemento
        else:
            if self.__primero.getdato()<elemento.getdato():
                elemento.setsiguiente(self.__primero)
                self.__primero=elemento
            else:
                aux=self.__primero.getsiguiente()
                anterior=self.__primero
                while aux!=None and aux.getdato()>elemento.getdato():
                    anterior=aux
                    aux=aux.getsiguiente()
                if aux==None:
                    self.__ultimo.setsiguiente(elemento)
                    self.__ultimo=elemento
                else:
                    anterior.setsiguiente(elemento)
                    elemento.setsiguiente(aux)
        self.__cantidad+=1
    def suprimir(self, elemento):
        valorretorno=None
        if self.vacia():
            print("La lista ya esta vacia")
        else:
            i=0
            aux=self.__primero
            anterior=aux
            while aux!=None and aux.getdato()!=elemento:
                anterior=aux
                aux=aux.getsiguiente()
                i+=1
            if aux!=None:
                if aux==self.__ultimo:
                    self.__ultimo=anterior
                    anterior.setsiguiente(aux.getsiguiente())
                elif aux==self.__primero:
                    self.__primero=aux.getsiguiente()
                else:
                    anterior.setsiguiente(aux.getsiguiente())
                self.__cantidad-=1
                valorretorno=aux.getdato()
            else:
                print("No se encontro el elemento a suprimir")
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
            print("No se encontro el elemento")
    def Buscar(self, elemento):
        valor=None
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
            else:
                print("No se encontro el elemento")
        else:
            print("La lista esta vacia")
        return valor
    def Primer_Elemento(self):
        return self.__primero.getdato()
    def Ultimo_Elemento(self):
        return self.__ultimo.getdato()
    def Siguiente(self, elemento):
        if not self.vacia():
            aux=self.__primero
            i=0
            while aux.getsiguiente()!=None and aux.getdato()!=elemento:
                aux=aux.getsiguiente()
                i+=1
            if aux.getsiguiente()!=None:
                return aux.getsiguiente().getdato()
            else:
                if i==self.__cantidad-1:
                    print("El elemento no tiene siguiente")
                else:
                    print("No se encontro el elemento")
        else:
            print("Lista vacia")
    def Anterior(self, elemento):
        if not self.vacia():
            aux=self.__primero.getsiguiente()
            anterior=self.__primero
            i=1
            if self.__primero.getdato()==elemento:
                print("Este elemento no tiene anterior")
                return None
            while aux!=None and aux.getdato()!=elemento:
                anterior=aux
                aux=aux.getsiguiente()
                i+=1
            if aux!=None:
                return anterior.getdato()
            else:
                print("No se encontro el elemento")
        else:
            print("Lista vacia")
    def vacia(self):
        return self.__cantidad==0
    def recorrer(self):
        cadena=""
        aux=self.__primero
        while aux!=None:
            cadena=cadena+str(aux.getdato())+"->"
            aux=aux.getsiguiente()
        print(cadena+str(aux))

  
a=ListaSecuencialPosicion(5)
b=int(input("1-Insertar\n2-Suprimir\n3-Recuperar\n4-Buscar\n5-Primero\n6-Ultimo\n7-Siguiente\n8-Anterior\n0-Salir\n"))
while b!=0:
    if b==1:
        a.insertar(input("Ingrese un elemento a la lista\n"), int(input("Ingrese una posicion\n")))
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

a=ListaEnlazadaContenido()
b=int(input("1-Insertar\n2-Suprimir\n3-Recuperar\n4-Buscar\n5-Primero\n6-Ultimo\n7-Siguiente\n8-Anterior\n0-Salir\n"))
while b!=0:
    if b==1:
        a.insertar(int(input("Ingrese un elemento a la lista\n")))
    elif b==2:
        a.suprimir(int(input("Ingrese un elemento\n")))
    elif b==3:
        print(a.Recuperar(int(input("Ingrese una posicion\n"))))
    elif b==4:
        print(a.Buscar(int(input("Ingrese un elemento de la lista\n"))))
    elif b==5:
        print(a.Primer_Elemento())
    elif b==6:
        print(a.Ultimo_Elemento())
    elif b==7:
        print(a.Siguiente((int(input("Ingrese un elemento\n")))))
    elif b==8:
        print(a.Anterior(int(input("Ingrese un elemento\n"))))
    a.recorrer()
    b=int(input("1-Insertar\n2-Suprimir\n3-Recuperar\n4-Buscar\n5-Primero\n6-Ultimo\n7-Siguiente\n8-Anterior\n0-Salir\n"))