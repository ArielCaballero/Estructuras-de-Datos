import numpy

class casilla:
    def __init__(self):
        self.__numero=0
        self.__direccion=""
    def getnumero(self):
        return self.__numero
    def getdireccion(self):
        return self.__direccion
    def setnumero(self, numero):
        self.__numero=numero
    def setdireccion(self, direccion):
        self.__direccion=direccion
    def __str__(self):
        return str(self.__numero)+'-'+str(self.__direccion)

def mostrar(tabla, n, m):
    for i in range(n):
        cadena=""
        for j in range(m):
            cadena=cadena +str(tabla[i, j])+ "  "
        print(cadena+'\n')

def SCMC(cadena1, cadena2):
    cadena1=cadena1.lower()
    cadena2=cadena2.lower()
    n=len(cadena1)+1
    m=len(cadena2)+1
    tabla=[]
    for i in range(n):
        lista=[]
        for j in range(m):
            lista.append(casilla())
        tabla.append(lista)
    tabla=numpy.array(tabla)
    for i in range(1,n):
        for j in range(1,m):
            if cadena1[i-1]==cadena2[j-1]:
                tabla[i,j].setnumero(tabla[i-1,j-1].getnumero()+1)
                tabla[i,j].setdireccion('D')
            else:
                if tabla[i-1,j].getnumero()>=tabla[i,j-1].getnumero():
                    tabla[i,j].setnumero(tabla[i-1, j].getnumero())
                    tabla[i,j].setdireccion("S")
                else:
                    tabla[i,j].setnumero(tabla[i, j-1].getnumero())
                    tabla[i,j].setdireccion("I")
        mostrar(tabla, n, m)
        print("-----------------------------")
    i=n-1
    j=m-1
    subsec=""
    while i>0 and j>0:
        if tabla[i, j].getdireccion()=='D':
            subsec=cadena1[i-1]+subsec
            i-=1
            j-=1
        elif tabla[i, j].getdireccion()=='S':
            i-=1
        elif tabla[i, j].getdireccion()=='I':
            j-=1
    return subsec

if __name__=='__main__':
    c1="abd"
    c2="abbadb"
    Subsecuencia=SCMC(c1, c2)
    print ("Subsecuencia: ",Subsecuencia)