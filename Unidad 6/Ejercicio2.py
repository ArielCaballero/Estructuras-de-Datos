import numpy
from Practica1 import ColaSecuencial

class Tabla:
    def __init__(self, n):
        self.__lista=[]
        for v in range(n):
            aux=[]
            aux.append(100000)
            aux.append(False)
            aux.append(None)
            self.__lista.append(aux)
    def conocido(self, i):
        return self.__lista[i][1]
    def setconocido(self, i):
        self.__lista[i][1]=True
    def distancia(self, i):
        return self.__lista[i][0]
    def setdistancia(self, i, distancia):
        self.__lista[i][0]=distancia
    def camino(self, i):
        return self.__lista[i][2]
    def setcamino(self, i, camino):
        self.__lista[i][2]=camino
    def minimo(self):
        j=0
        min=1000000
        for i in range(len(self.__lista)):
            if (not self.__lista[i][1]) and min>self.__lista[i][0]:
                min=self.__lista[i][0]
                j=i
        return j
    def __str__(self):
        return str(self.__lista)

class GrafoSecuencialAdyacencia:
    def __init__(self):
        self.__vertices=[]
        self.__n=0
        self.__relaciones=[]
    def insertarvertices(self, vertices):
        self.__n=len(vertices)
        self.__vertices=vertices
        self.__relaciones=numpy.zeros((self.__n,self.__n), dtype=int)  
    def insertararista(self, origen, destino, peso=1):
        i=self.__vertices.index(origen)
        j=self.__vertices.index(destino)
        self.__relaciones[i][j]=peso
    def adyacentes(self, A):
        i=self.__vertices.index(A)
        for j in range(i, self.__n):
            if self.__relaciones[i*(i+1)//2+j]==1:
                print(self.__relaciones[i*(i+1)//2+j])
    def camino(self, A, B):
        index=self.__vertices.index(A)
        indice=self.__vertices.index(B)
        T=Tabla(self.__n)
        T.setdistancia(index, 0)
        bandera=True
        i=0
        while bandera and i<( self.__n):
            v=T.minimo()
            T.setconocido(v)
            for w in range(self.__n):
                if self.__relaciones[v][w]!=0:
                    if not T.conocido(w):
                        dist=T.distancia(v)+self.__relaciones[v][w]
                        if dist<T.distancia(w):
                            T.setdistancia(w, dist)
                            T.setcamino(w, v)
                            if w==indice:
                                bandera=not bandera
            i+=1
        camino=""
        distancia=T.distancia(indice)
        while(indice!=index):
            camino="->"+str(self.__vertices[indice])+camino
            indice=T.camino(indice)
        camino=str(A)+camino
        print("El camino es:\n",camino,"\nDe distancia: ", distancia)
    def caminominimo(self, A, B):
        index=self.__vertices.index(A)
        T=Tabla(self.__n)
        T.setdistancia(index, 0)
        for i in range(self.__n):
            v=T.minimo()
            T.setconocido(v)
            for w in range(self.__n):
                if self.__relaciones[v][w]!=0:
                    if not T.conocido(w):
                        dist=T.distancia(v)+self.__relaciones[v][w]
                        if dist<T.distancia(w):
                            T.setdistancia(w, dist)
                            T.setcamino(w, v)
        indice=self.__vertices.index(B)
        camino=""
        distancia=T.distancia(indice)
        while(indice!=index):
            camino="->"+str(self.__vertices[indice])+camino
            indice=T.camino(indice)
        camino=str(A)+camino
        print("El camino minimo es:\n",camino,"\nDe distancia: ", distancia)
    def __str__(self):
        cadena=""
        for i in range(self.__n):
            cadena=cadena+"\n"+str(self.__vertices[i])+" "
            cadena=cadena + str(self.__relaciones[i]) +" "
        cadena2="  "
        for i in self.__vertices:
            cadena2=cadena2+" "+str(i)
        return cadena2+cadena
    def REA(self, origen):
        arreglo=numpy.full((self.__n), 1000000, int)
        origen=self.__vertices.index(origen)
        arreglo[origen]=0
        cola=ColaSecuencial(self.__n)
        cola.insertar(origen)
        while not cola.vacia():
            v=cola.suprimir()
            for i in range(self.__n):
                if self.__relaciones[v][i]!=0:
                    if arreglo[i]==1000000:
                        arreglo[i]=arreglo[v]+1
                        cola.insertar(i)
        print("Orden de acceso REA")
        for j in range(self.__n):
            print(self.__vertices[j], " -> ", arreglo[j])
    def REP_Visita(self, tiempo, arreglo, s):
        tiempo+=1
        arreglo[s]=tiempo
        for i in range(self.__n):
            if self.__relaciones[s][i]!=0:
                if arreglo[i]==0:
                    self.REP_Visita(tiempo, arreglo, i)
    def REP(self):
        arreglo=numpy.full((self.__n), 0, int)
        tiempo=0
        for s in range(self.__n):
            if arreglo[s]==0:
              self.REP_Visita(tiempo, arreglo, s)
        for i in range(self.__n):
            print(self.__vertices[i]," - ",arreglo[i])
    def Aciclico_Visita(self, bandera, tiempo, arreglo, s):
        tiempo+=1
        arreglo[s]=tiempo
        for i in range(self.__n):
            if self.__relaciones[s][i]!=0:
                if arreglo[i]==0:
                    bandera=self.Aciclico_Visita(bandera, tiempo, arreglo, i)
                else:
                    if abs(arreglo[i]-arreglo[s])>1:
                        bandera=False
        return bandera
    def Aciclico(self):
        arreglo=numpy.full((self.__n), 0, int)
        tiempo=0
        bandera=True
        for s in range(self.__n):
            if arreglo[s]==0:
               bandera=self.Aciclico_Visita(bandera, tiempo, arreglo, s)
        return bandera
    def conexo(self):
        arreglo=numpy.full((self.__n), 1000000, int)
        origen=0
        arreglo[origen]=0
        cola=ColaSecuencial(self.__n)
        cola.insertar(origen)
        while not cola.vacia():
            v=cola.suprimir()
            for i in range(self.__n):
                if self.__relaciones[v][i]!=0:
                    if arreglo[i]==1000000:
                        arreglo[i]=arreglo[v]+1
                        cola.insertar(i)
        bandera=True
        i=0
        while i<len(arreglo) and bandera:
            if arreglo[i]==1000000:
                bandera=not bandera
            i+=1
        return bandera
    def Arbol_Recubrimiento(self):
        index=0
        T=Tabla(self.__n)
        T.setdistancia(index, 0)
        for i in range(self.__n):
            v=T.minimo()
            T.setconocido(v)
            for w in range(self.__n):
                if self.__relaciones[v][w]!=0:
                    if not T.conocido(w):
                        if self.__relaciones[v][w]<T.distancia(w):
                            T.setdistancia(w, self.__relaciones[v][w])
                            T.setcamino(w, v)
        print("Arbol de Recubrimiento")
        lista=[]
        for i in range (self.__n):
            if T.conocido(i):
                lista.append(self.__vertices[i])
        nuevo=GrafoSecuencialAdyacencia()
        nuevo.insertarvertices(lista)
        for i in lista:
            j=lista.index(i)
            if T.camino(j)!=None:
                nuevo.insertararista(self.__vertices[T.camino(j)], i, T.distancia(j))
        print(nuevo)
    def sumidero(self, vertice):
        index=self.__vertices.index(vertice)
        bandera=True
        i=0
        while i<self.__n and bandera:
            if self.__relaciones[index][i]!=0:
                bandera=not bandera
            i+=1
        return bandera
    def fuente(self, vertice):
        index=self.__vertices.index(vertice)
        bandera=True
        i=0
        while i<self.__n and bandera:
            if self.__relaciones[i][index]!=0:
                bandera=not bandera
            i+=1
        return bandera

class nodo:
    def __init__(self, vertice):
        self.__ver=vertice
        self.__siguiente=None
    def getvertice(self):
        return self.__ver
    def getsiguiente(self):
        return self.__siguiente
    def setsiguiente(self, siguiente):
        self.__siguiente=siguiente
    def setver(self, ver):
        self.__ver=ver
    def __str__(self):
        return str(self.__ver)

class GrafoEnlazado:
    def __init__(self):
        self.__vertices=[]
        self.__n=0
        self.__relaciones=[]
    def insertarvertices(self, vertices):
        self.__n=len(vertices)
        self.__vertices=vertices
        self.__relaciones=numpy.full((self.__n), None ,dtype=nodo)  
    def insertararista(self, origen, destino):
        i=self.__vertices.index(origen)
        j=self.__vertices.index(destino)
        if self.__relaciones[i]==None:
           self.__relaciones[i]=nodo(destino) 
        else:
            aux=self.__relaciones[i]
            while aux.getsiguiente()!=None:
                aux=aux.getsiguiente()
            aux.setsiguiente(nodo(destino))
    def adyacentes(self, vertice):
        aux=self.__relaciones[self.__vertices.index(vertice)]
        while aux!=None:
            print(aux, " ")
            aux=aux.getsiguiente()
    def __str__(self):
        cadena=""
        for i in range(self.__n):
            cadena=cadena+str(self.__vertices[i])+": "
            aux=self.__relaciones[i]
            while aux!=None:
                cadena=cadena+str(aux)+"<-"
                aux=aux.getsiguiente()
            cadena=cadena+"\n"
        return cadena
    def caminominimo(self, A, B):
        index=self.__vertices.index(A)
        T=Tabla(self.__n)
        T.setdistancia(index, 0)
        for i in range(self.__n):
            v=T.minimo()
            T.setconocido(v)
            aux=self.__relaciones[i]
            while aux!=None:
                w=self.__vertices.index(aux.getvertice())
                if not T.conocido(w):
                    dist=T.distancia(v)+1
                    if dist<T.distancia(w):
                        T.setdistancia(w, dist)
                        T.setcamino(w, v)
                aux=aux.getsiguiente()
        indice=self.__vertices.index(B)
        camino=""
        distancia=T.distancia(indice)
        while(indice!=index):
            camino="->"+str(self.__vertices[indice])+camino
            indice=T.camino(indice)
        camino=str(A)+camino
        print("El camino minimo es:\n",camino,"\nDe distancia: ", distancia)
    
    def camino(self, A, B):
        index=self.__vertices.index(A)
        indice=self.__vertices.index(B)
        T=Tabla(self.__n)
        T.setdistancia(index, 0)
        bandera=True
        i=0
        while i<self.__n and bandera:
            v=T.minimo()
            T.setconocido(v)
            aux=self.__relaciones[i]
            while aux!=None:
                w=self.__vertices.index(aux.getvertice())
                if w==indice:
                    bandera=not bandera
                if not T.conocido(w):
                    dist=T.distancia(v)+1
                    if dist<T.distancia(w):
                        T.setdistancia(w, dist)
                        T.setcamino(w, v)
                aux=aux.getsiguiente()
            i+=1
        camino=""
        distancia=T.distancia(indice)
        while(indice!=index):
            camino="->"+str(self.__vertices[indice])+camino
            indice=T.camino(indice)
        camino=str(A)+camino
        print("El camino es:\n",camino,"\nDe distancia: ", distancia)
    def REA(self, origen):
        arreglo=numpy.full(self.__n, 1000000, int)
        origen=self.__vertices.index(origen)
        arreglo[origen]=0
        cola=ColaSecuencial(self.__n)
        cola.insertar(origen)
        while not cola.vacia():
            v=cola.suprimir()
            aux=self.__relaciones[v]
            while aux!=None:
                i=self.__vertices.index(aux.getvertice())
                if arreglo[i]==1000000:
                    arreglo[i]=arreglo[v]+1
                    cola.insertar(i)
                aux=aux.getsiguiente()
        print("Orden de acceso REA")
        for j in range(len(arreglo)):
            print(self.__vertices[j], " -> ", arreglo[j])
    def REP_Visita(self, tiempo, arreglo, s):
        tiempo+=1
        arreglo[s]=tiempo
        aux=self.__relaciones[s]
        while aux!=None:
            i=self.__vertices.index(aux.getvertice())
            if arreglo[i]==0:
                self.REP_Visita(tiempo, arreglo, i)
            aux=aux.getsiguiente()
    def REP(self):
        arreglo=numpy.full((self.__n), 0, int)
        tiempo=0
        for s in range(self.__n):
            if arreglo[s]==0:
              self.REP_Visita(tiempo, arreglo, s)
        for i in range(self.__n):
            print(self.__vertices[i]," - ",arreglo[i])
    def Aciclico_Visita(self, bandera, tiempo, arreglo, s):
        tiempo+=1
        arreglo[s]=tiempo
        aux=self.__relaciones[s]
        while aux!=None:
            i=self.__vertices.index(aux.getvertice())
            if arreglo[i]==0:
                bandera=self.Aciclico_Visita(bandera, tiempo, arreglo, i)
            else:
                if abs(arreglo[i]-arreglo[s])>1:
                    bandera=False
            aux=aux.getsiguiente()
        return bandera
    def Aciclico(self):
        arreglo=numpy.full((self.__n), 0, int)
        tiempo=0
        bandera=True
        for s in range(self.__n):
            if arreglo[s]==0:
               bandera=self.Aciclico_Visita(bandera, tiempo, arreglo, s)
        return bandera
    def conexo(self):
        arreglo=numpy.full(self.__n, 1000000, int)
        origen=0
        arreglo[origen]=0
        cola=ColaSecuencial(self.__n)
        cola.insertar(origen)
        while not cola.vacia():
            v=cola.suprimir()
            aux=self.__relaciones[v]
            while aux!=None:
                i=self.__vertices.index(aux.getvertice())
                if arreglo[i]==1000000:
                    arreglo[i]=arreglo[v]+1
                    cola.insertar(i)
                aux=aux.getsiguiente()
        bandera=True
        i=0
        while i<len(arreglo) and bandera:
            if arreglo[i]==1000000:
                bandera=not bandera
            i+=1
        return bandera
    def sumidero(self, vertice):
        index=self.__vertices.index(vertice)
        bandera=False
        if self.__relaciones[index]==None:
            bandera=True
        return bandera
    def fuente(self, vertice):
        index=self.__vertices.index(vertice)
        bandera=True
        i=0
        while i<self.__n and bandera:
            aux=self.__relaciones[i]
            while aux!=None:
                if aux.getvertice()==vertice:
                    bandera=False
                aux=aux.getsiguiente()
            i+=1
        return bandera


if __name__=='__main__':
    grafo=GrafoEnlazado()
   
    nodos=[1,2,3,4,5,6]
    grafo.insertarvertices(nodos)
    grafo.insertararista(1,2)
    grafo.insertararista(1,3)
    grafo.insertararista(2,5)
    grafo.insertararista(2,4)
    grafo.insertararista(3,5)
    grafo.insertararista(4,5)
    grafo.insertararista(5,6)
    grafo.insertararista(4,6)
    """
    nodos=[1,2,3]
    grafo.insertarvertices(nodos)
    grafo.insertararista(1,2,2)
    grafo.insertararista(2,3,6)
    grafo.insertararista(3,3,4)
    """
    print(grafo)