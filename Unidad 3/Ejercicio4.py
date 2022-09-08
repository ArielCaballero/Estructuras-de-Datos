import csv


class Designacion:
    __anio=""
    __justicia=""
    __cargo=""
    __instancia=""
    __materia=""
    __varones=""
    __mujeres=""
    def __init__(self, anio, justicia, cargo, instancia, materia, varones, mujeres):
        self.__anio=anio
        self.__justicia=justicia
        self.__cargo=cargo
        self.__instancia=instancia
        self.__materia=materia
        self.__varones=varones
        self.__mujeres=mujeres
    def getanio(self):
        return self.__anio
    def getmujeres(self):
        return self.__mujeres
    def getvarones(self):
        return self.__varones
    def getcargo(self):
        return self.__cargo
    def getmateria(self):
        return self.__materia
    def getjusticia(self):
        return self.__justicia
    def getinstancia(self):
        return self.__instancia
    def __lt__(self, otro):
        if type(otro)==type(self):
            return self.getanio()<otro.getanio()
        else:
            print ("Los dos datos deben ser designaciones")
            return None
    def __str__(self):
        #return ("{}".format(self.getanio()))
        return ("Año: {}    Justicia: {}    Cargo: {}    Instancia: {}    Materia: {}    Varones: {}    Mujeres: {}".format(self.getanio(),self.getjusticia(),self.getcargo(), self.getinstancia(), self.getmateria(),self.getvarones(), self.getmujeres()))

class Nodo:
    __designacion=""
    __siguiente=""
    def __init__(self,  designacion, siguiente=None):
        if type(designacion)==Designacion:
            self.__designacion=designacion
            self.__siguiente=siguiente
        else:
            print("Error de tipo al crear nodo.")
    def getsiguiente(self):
        return self.__siguiente
    def getdato(self):
        return self.__designacion
    def setsiguiente(self, siguiente):
        self.__siguiente=siguiente
    def setdato(self, designacion):
        if type(designacion)==Designacion:
            self.__designacion=designacion
    
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
    def mujeres(self, cargo):
        aux=self.__primero
        contador=0
        control=aux.getdato().getanio()
        print("la cantidad de mujeres por en el cargo {}".format(cargo))
        while aux!=None:
            if(aux.getdato().getanio()!=control):
                print("{}: {}".format(control, contador))
                contador=0
                control=aux.getdato().getanio()
            if aux.getdato().getcargo().lower()==cargo.lower():
                contador+=int(aux.getdato().getmujeres())
            aux=aux.getsiguiente()
        print("{}: {}".format(control, contador))
    def agentes(self, materia, cargo, anio):
        aux=self.__primero
        contador=0
        while aux!=None and aux.getdato().getanio()>=anio:
            if(aux.getdato().getanio()==anio and aux.getdato().getmateria().lower()==materia.lower() and aux.getdato().getcargo().lower()==cargo.lower()):
                contador+=int(aux.getdato().getmujeres())
                contador+=int(aux.getdato().getvarones())
            aux=aux.getsiguiente()
        print("la cantidad de agentes desginados para el cargo {} en  la materia, {} y en el año {} es de: {}".format(cargo, materia, anio, contador))
    def mostrar(self):
        cadena=""
        aux=self.__primero
        while aux!=None:
            cadena=cadena+str(aux.getdato())+"->"
            aux=aux.getsiguiente()
        print(cadena+str(aux))

if __name__=="__main__":
    archivo=open("estadistica-designacion-magistrados-federal-nacional-por-genero-20220323.csv", encoding="UTF-8")
    reader=csv.reader(archivo, delimiter=",")
    lista=ListaEnlazadaContenido()
    reader.__next__()
    for fila in reader:
        lista.insertar(Nodo(Designacion(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6])))
    #lista.mujeres(cargo=input("Ingrese un cargo: "))
    lista.agentes(cargo=input("Ingrese un cargo: "), materia=input("Ingrese una materia: "), anio=input("Ingrese un año: "))