class Elemento:
    __datos=""
    __prioridad=0
    def __init__(self, datos, prioridad):
        self.__datos=datos
        self.__prioridad=prioridad
    def getdato(self):
        return self.__datos
    def getprioridad(self):
        return self.__prioridad
    def __lt__(self, otro):
        if type(otro)==Elemento:
            return otro.getprioridad()>self.getprioridad()
        else:
            raise TypeError('Ambos deben ser de la clase Elemento')
    def __str__(self):
        return self.__datos+" "+str(self.__prioridad)
    
class MonticuloBinario:
    __lista=[]
    def __init__(self):
        self.__lista=[]
        self.__lista.append(None)
    def insertar(self, elemento):
        self.__lista.append(elemento)
        i=len(self.__lista)-1
        k=i//2
        while k>0 and self.__lista[i]<self.__lista[k]:
            aux=self.__lista[k]
            self.__lista[k]=self.__lista[i]
            self.__lista[i]=aux
            i=k
            k=k//2
    def eliminar_minimo(self):
        i=1
        k=i*2
        eliminado=self.__lista[i]
        while k<len(self.__lista):
            if k+1<len(self.__lista):
                if self.__lista[k]<self.__lista[k+1]:
                    self.__lista[i]=self.__lista[k]
                    i=k
                else:
                    self.__lista[i]=self.__lista[k+1]
                    i=k+1
            else:
                self.__lista[i]=self.__lista[k]
                i=k
            k=k*2
        self.__lista.pop(i)
        for i in range(len(self.__lista)-1,1, -1):
            if self.__lista[i]<self.__lista[i//2]:
                aux=self.__lista[i//2]
                self.__lista[i//2]=self.__lista[i]
                self.__lista[i]=aux
        return eliminado
    def mostrar(self):
        cadena=''
        for i in range(1, len(self.__lista)):
            cadena+=str(self.__lista[i])+' -> '
        print (cadena)

if __name__=='__main__':
    opcion=int(input('1-Insertar\n2-Suprimir\n0-Salir\n'))
    monticulo=MonticuloBinario()
    while opcion:
        if opcion==1:
            monticulo.insertar(Elemento(input('Ingrese datos: '), int(input("Ingrese prioridad (entero): "))))
        elif opcion==2:
            print (monticulo.eliminar_minimo())
        monticulo.mostrar()
        print('-----------------')
        opcion=int(input('1-Insertar\n2-Suprimir\n0-Salir'))



