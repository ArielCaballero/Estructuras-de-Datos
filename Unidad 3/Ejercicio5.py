class Nodo:
    __dato=None
    __siguiente=None
    def __init__(self, dato):
        if type(dato)==int:
            self.__dato=dato
            self.__siguiente=None
        else:
            print("Error al crear Nodo")
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
                if posicion==1:
                    eliminado=self.__primero
                    self.__primero=eliminado.getsiguiente()
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
        if type(elemento)==int:
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

                '''else:
                    print("No se encontro el elemento")
            else:
                print("La lista esta vacia")
        else:
            print("Error en el tipo de dato")'''
        return valor
    def Primer_Elemento(self):
        return self.__primero.getdato()
    def Ultimo_Elemento(self):
        return self.__ultimo.getdato()
    def Siguiente(self, posicion):
        valor=None
        if 0<posicion and not self.vacia() and self.__cantidad>posicion:
            aux=self.__primero
            i=0
            while i<posicion:
                aux=aux.getsiguiente()
                i+=1
            valor= aux.getdato()
        return valor
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
            cadena+=str(aux.getdato())+"->"
            aux=aux.getsiguiente()
        print(cadena)

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
            """
            else:
                if i==self.__cantidad-1:
                    print("El elemento no tiene siguiente")
                else:
                    print("No se encontro el elemento")
            """
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

def entradaspos(lista):
    lista.insertar(10, 1)
    lista.insertar(5, 2)
    lista.insertar(7, 3)
    lista.insertar(5, 4)
    lista.insertar(2, 5)
    lista.insertar(10, 6)

def entradascon(lista):
    lista.insertar(10)
    lista.insertar(5)
    lista.insertar(7)
    lista.insertar(5)
    lista.insertar(2)
    lista.insertar(10)

if __name__=="__main__":
    #Lista Enlazada por Posicion
    listapos=ListaEnlazadaPosicion()
    entradaspos(listapos)
    if not listapos.vacia():
        print("Lista antes")
        listapos.recorrer()
        aux=listapos.Primer_Elemento()
        i=1
        while aux!=None:
            otroaux=listapos.suprimir(i)
            repetido=listapos.Buscar(otroaux)
            while repetido!=None:
                listapos.suprimir(repetido)
                repetido=listapos.Buscar(otroaux)
            listapos.insertar(otroaux, i)
            aux=listapos.Siguiente(i)
            i+=1
        print("Lista Despues")
        listapos.recorrer()
    else:
        print("Lista vacia")
    #Lista Enlazada por Contenido
    listacon=ListaEnlazadaContenido()
    entradascon(listacon)
    if not listacon.vacia():
        print("Lista antes")
        listacon.recorrer()
        aux=listacon.Primer_Elemento()
        while aux!=None:
            otroaux=listacon.Siguiente(aux)
            while aux==otroaux:
                listacon.suprimir(otroaux)
                otroaux=listacon.Siguiente(aux)
            aux=otroaux
        print("Lista Despues")
        listacon.recorrer()