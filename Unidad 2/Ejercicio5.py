class Pila:
    def __init__(self, max=0):
        self.__Lista=[]
        self.__max=max
        self.__cant=0
    def insertar(self, elemento):
        if self.__max==self.__cant:
            self.__max+=5
        self.__Lista.append(elemento)
        self.__cant+=1
    def eliminar(self):
        self.__cant-=1
        return self.__Lista.pop()
    def vacia(self):
        return len(self.__Lista)==0
    def llena(self):
        return self.__cant==self.__max
    def mostrar(self):
        print (self.__Lista)
    
                

    def verultimo(self):
        return self.__Lista[self.__cant-1]

def moverdisco(torreorigen, torredestino):
    if not torreorigen.vacia():
        discoorigen=torreorigen.eliminar()
        if not torredestino.vacia():
            discodestino=torredestino.eliminar()
            if discoorigen<discodestino:
                torredestino.insertar(discodestino)
                torredestino.insertar(discoorigen)
            else:
                torreorigen.insertar(discoorigen)
                torredestino.insertar(discodestino)
                print("Jugada no valida\n")
        else:
            torredestino.insertar(discoorigen)
    else:
        print("Jugada no valida\n")

def seguirjugando(torre1, torre2, torre3):
    return torre3.llena() and torre2.vacia() and torre1.vacia()

def mostrartorre(torre, n):
        discos=[]
        while not torre.vacia():
            discos.append(torre.eliminar())
        dibujofinal=""
        discos.reverse()
        for i in range(n):
            dibujo="|"
            k=0
            if len(discos)>i:
                for j in range(discos[i]):
                    dibujo="_"+dibujo+"_"
                    k+=1
            while k<n:
                dibujo=" "+dibujo+" "
                k+=1
            dibujofinal="\n"+dibujo+dibujofinal
        print(dibujofinal)
        discos.reverse()
        for m in range(len(discos)):
            torre.insertar(discos[len(discos)-1-m])
        print("\n")

if __name__=="__main__":
    n=int(input("Ingrese el numero de discos con los que se jugara\n"))
    Torres=[]
    torre1=Pila(n)
    torre2=Pila(n)
    torre3=Pila(n)
    Torres.append(torre1)
    Torres.append(torre2)
    Torres.append(torre3)
    for i in range(n):
        torre1.insertar(n-i)
    for torre in Torres:
            print ("\nTorre "+str(Torres.index(torre)+1))
            mostrartorre(torre, n)
    contador=0
    while not seguirjugando(torre1, torre2, torre3):
        origen=int(input("Ingrese la torre de la que desea extraer un disco (1, 2 o 3): "))
        destino=int(input("Ingrese la torre en la que desea colocar el disco (1, 2 o 3): "))
        if origen>=1 and origen<=3 and destino>=1 and destino<=3:
            moverdisco(Torres[origen-1], Torres[destino-1])
        for torre in Torres:
            print ("\nTorre "+str(Torres.index(torre)+1))
            mostrartorre(torre, n)
        contador+=1
    print("\n --------------------------------\n")
    print("Se finalizo el juego en {} jugadas".format(contador))
    print("Numero minimo de jugadas: ", (2**n)-1)
    