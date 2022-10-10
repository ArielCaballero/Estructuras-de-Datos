class Nodo:
    def __init__(self,elemento):
        self.__elemento=elemento
        self.__izq=None
        self.__der=None
    def getdato(self):
        return self.__elemento
    def setdato(self, dato):
        self.__elemento=dato
    def getizq(self):
        return self.__izq
    def getder(self):
        return self.__der
    def setizq(self, izq):
        self.__izq=izq
    def setder (self, der):
        self.__der=der

class Arbol:
    __cabeza=None
    def __init__(self):
        self.__cabeza=None
    def insertar(self, elemento, nodo=-1):
        if nodo==-1:
            nodo=self.__cabeza
            elemento=Nodo(elemento)
        if nodo!=None:
            if elemento.getdato()<nodo.getdato():
                if nodo.getizq()==None:
                    nodo.setizq(elemento)
                else:
                    self.insertar(elemento, nodo.getizq())
            elif elemento.getdato()>nodo.getdato():
                if nodo.getder()==None:
                    nodo.setder(elemento)
                else:self.insertar(elemento, nodo.getder())
            else:
                raise ValueError('Elemento ya existente en el arbol')
        else:
            self.__cabeza=elemento
    def suprimir(self, elemento):
        nodo=self.__cabeza
        anterior=nodo
        while(nodo!=None and nodo.getdato()!=elemento):
            anterior=nodo
            if nodo.getdato()>elemento:
                nodo=nodo.getizq()
            else:
                nodo=nodo.getder()
        if nodo !=None:
            if nodo.getizq()!=None:
                mayor=nodo.getizq()
                if mayor.getder()!=None:
                    anterior=nodo
                    while mayor.getder()!=None:
                        anterior=mayor
                        mayor=mayor.getder()
                    nodo.setdato(mayor.getdato())
                    anterior.setder(None)
                    nodo=mayor
                else:
                    anterior=nodo
                    while not self.hoja(mayor):
                        anterior.setdato(mayor.getdato())
                        anterior=mayor
                        if mayor.getizq()!=None:
                            mayor=mayor.getizq()
                        else:
                            mayor=mayor.getder()
                    anterior.setdato(mayor.getdato())         
                    nodo=mayor    
            elif nodo.getder()!=None:
                menor=nodo.getder()
                if menor.getizq()!=None:
                    anterior=nodo
                    while menor.getizq()!=None:
                        anterior=menor
                        menor=menor.getizq()
                    nodo.setdato(menor.getdato())
                    anterior.setizq(None)
                    nodo=menor
                else:
                    anterior=nodo
                    while not self.hoja(menor):
                        anterior.setdato(menor.getdato())
                        anterior=menor
                        if menor.getizq()!=None:
                            menor=menor.getizq()
                        else:
                            menor=menor.getder()
                    anterior.setdato(menor.getdato())
                    nodo=menor
            if anterior.getizq()==nodo:
                anterior.setizq(None)
            elif anterior.getder()==nodo:
                anterior.setder(None)
        else:
            raise ValueError('Elemento inexistente')

    def nivel(self, elemento, nodo=-1):
        if nodo==-1:
            nodo=self.__cabeza
        if nodo!=None:
            if nodo.getdato()>elemento:
                return self.nivel(elemento, nodo.getizq())+1
            elif nodo.getdato()<elemento:
                return self.nivel(elemento, nodo.getder())+1
            else:
                return 1
        else:
            raise ValueError('Elemento no encontrado')
    def buscar(self, elemento, nodo=-1):
        if nodo==-1:
            nodo=self.__cabeza
        if nodo!=None:
            if nodo.getdato()>elemento:
                return self.buscar(elemento, nodo.getizq())
            elif nodo.getdato()<elemento:
                return self.buscar(elemento, nodo.getder())
            else:
                return nodo
        else:
            raise ValueError('Elemento no encontrado')

    def camino(self, origen, destino):
        if type(origen)!=Nodo:
            origen=self.buscar(origen)
        if type(destino)!=Nodo:
            destino=self.buscar(destino)
        cadena=''
        while origen!=None and origen!=destino:
            cadena=cadena+str(origen.getdato())+'->'
            if origen.getdato()>destino.getdato():
                origen=origen.getizq()
            elif origen.getdato()<destino.getdato():
                origen=origen.getder()
        if origen!=None:
            cadena+=str(origen.getdato())
            return(cadena)
        else:
            return("No existe camino")

    def hoja(self, hoja):
        if type(hoja)!=Nodo:
            hoja=self.buscar(hoja)
        return hoja.getizq()==None and hoja.getder()==None

    def hijo(self, hijo, padre):
        if type(padre)!=Nodo:
            padre=self.buscar(padre)
        if type(hijo)==Nodo:
            return padre.getizq()==hijo or padre.getder()==hijo
        else:
            if padre.getizq()!=None and padre.getizq().getdato()==hijo:
                bandera=True
            elif padre.getder()!=None and padre.getder().getdato()==hijo:
                bandera=True
            else:
                bandera=False
            return bandera

    def padre(self, padre, hijo):
        return self.hijo(hijo, padre)

    def altura(self, nodo=-1, contador=0, lista=None):
        if nodo==-1:
            nodo=self.__cabeza
            lista=[]
        if nodo!=None:
            contador+=1
            lista.append(contador)
            self.altura(nodo.getizq(), contador, lista)
            self.altura(nodo.getder(), contador, lista)
        if nodo==self.__cabeza:
            lista.sort(reverse=True)
            print (lista[0])
        

    def Preorden(self, nodo=1):
        if nodo==1:
            nodo=self.__cabeza
        if nodo!=None:
            print(nodo.getdato())
            self.Preorden(nodo.getizq())
            self.Preorden(nodo.getder())
    def Inorden(self, nodo=1):
        if nodo==1:
            nodo=self.__cabeza
        if nodo!=None:
            self.Inorden(nodo.getizq())
            print(nodo.getdato())
            self.Inorden(nodo.getder())
    def Postorden(self, nodo=1):
        if nodo==1:
            nodo=self.__cabeza
        if nodo!=None:
            self.Postorden(nodo.getizq())
            self.Postorden(nodo.getder())
            print(nodo.getdato()) 

class registro:
    def __init__(self, c):
        self.__caracter=c
        self.__contador=0
    def inc(self):
        self.__contador+=1
    def getcontador(self):
        return self.__contador
    def getcaracter(self):
        return self.__caracter
    def __lt__(self, otro):
        return self.getcontador()<otro.getcontador()
    def __eq__(self, otro):
        return self.getcaracter()==otro.getcaracter()
    def __str__(self):
        return ('{}: {}'.format(self.__caracter, self.__contador))

if __name__=='__main__':
    archivo=open('texto.txt', encoding='UTF-8')
    cadena=archivo.read().replace(' ','').lower()
    lista=[]
    for c in cadena:
        i=0
        while(i<len(lista) and c!=lista[i].getcaracter()):
            i+=1
        if i<len(lista):
            lista[i].inc()
        else:
            c=registro(c)
            c.inc()
            lista.append(c)
    lista.sort()
    for i in lista:
        print(i)

            
