import csv

class Nodo:
    __siguiente=None
    def __init__(self, hectareas, nombre,siguiente=None):
        self.__hectareas=hectareas
        self.__nombre=nombre
        self.__siguiente=siguiente
    def getnombre(self):
        return self.__nombre
    def gethectareas(self):
        return self.__hectareas
    def sethectareas(self, dato):
        self.__hectareas=dato
    def getsiguiente(self):
        return self.__siguiente
    def setsiguiente(self, siguiente):
        self.__siguiente=siguiente

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
            self.__cantidad+=1
        else:
            if self.__primero.getnombre()>elemento.getnombre():
                elemento.setsiguiente(self.__primero)
                self.__primero=elemento
                self.__cantidad+=1
            else: 
                aux=self.__primero
                anterior=self.__primero
                while aux!=None and aux.getnombre()<elemento.getnombre():
                    anterior=aux
                    aux=aux.getsiguiente()
                if aux==None:
                    self.__ultimo.setsiguiente(elemento)
                    self.__ultimo=elemento
                    self.__cantidad+=1
                elif aux.getnombre()==elemento.getnombre():
                    acum=aux.gethectareas()+elemento.gethectareas()
                    aux.sethectareas(acum)
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
            while aux!=None and aux.getnombre()!=elemento.getnombre():
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
                valorretorno=aux
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
            return aux
        else:
            print("No se encontro el elemento")
    def Buscar(self, elemento):
        valor=None
        if not self.vacia():
            bandera=True
            aux=self.__primero
            i=0
            while aux!=None and bandera:
                if aux.getnombre()==elemento.getnombre():
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
        return self.__primero
    def Ultimo_Elemento(self):
        return self.__ultimo
    def Siguiente(self, elemento):
        if not self.vacia():
            aux=self.__primero
            i=0
            while aux.getsiguiente()!=None and aux.getnombre()!=elemento.getnombre():
                aux=aux.getsiguiente()
                i+=1
            if aux.getsiguiente()!=None:
                return aux.getsiguiente()
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
            while aux!=None and aux.getnombre()!=elemento.getnombre():
                anterior=aux
                aux=aux.getsiguiente()
                i+=1
            if aux!=None:
                return anterior
            else:
                print("No se encontro el elemento")
        else:
            print("Lista vacia")
    def vacia(self):
        return self.__cantidad==0
    def recorrer(self):
        cadena=""
        Lista=[]
        while not self.vacia():
            aux=self.__primero
            supr=aux
            mayorsup=self.__primero.gethectareas()
            while aux!=None:
                if mayorsup<aux.gethectareas():
                    mayorsup=aux.gethectareas()
                    supr=aux
                aux=aux.getsiguiente()
            cadena=cadena+str(supr.getnombre())+": "+str(supr.gethectareas())+"\n"
            Lista.append(self.suprimir(supr))
        for elemento in Lista:
            self.insertar(elemento)
        print(cadena)


if __name__=="__main__":
    archivo=open('incendio_forestales.csv', encoding="UTF-8")
    reader=csv.reader(archivo, delimiter=';')
    Lista=ListaEnlazadaContenido()
    reader.__next__()
    auxiliar=[]
    for fila in reader:
        if fila[6]=="":
            Lista.insertar(Nodo(0.0,fila[3]))
        else:
            Lista.insertar(Nodo(float(fila[6]),fila[3]))
    Lista.recorrer()