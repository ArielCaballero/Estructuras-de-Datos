class Pila:
    def __init__(self, max):
        self.__Lista=[]
        for i in range(max):
            self.__Lista.append(None)
        self.__max1=0
        self.__max2=max-1
        self.__tope1=self.__max1-1
        self.__tope2=self.__max2+1
    def insertaren1(self, elemento):
        if not self.llena():
            self.__tope1+=1
            self.__Lista[self.__tope1]=elemento
        else:
            print("\nLA PILA ESTA LLENA\n")
    def insertaren2(self, elemento):
        if not self.llena():
            self.__tope2-=1
            self.__Lista[self.__tope2]=elemento
        else:
            print("\nLA PILA ESTA LLENA\n")
    def eliminaren1(self):
        if not self.vacialista1():
            valor=self.__Lista[self.__tope1]
            self.__Lista[self.__tope1]=None
            self.__tope1-=1
        else:
            valor=None
            print("\nLA PILA YA ESTA VACIA\n")
        return valor
    def eliminaren2(self):
        if not self.vacialista2():
            valor=self.__Lista[self.__tope2]
            self.__Lista[self.__tope2]=None
            self.__tope2+=1
        else:
            valor=None
            print("\nLA PILA YA ESTA VACIA\n")
        return valor
    def vacialista1(self):
        return self.__tope1+1==self.__max1
    def vacialista2(self):
        return self.__tope2-1==self.__max2
    def llena(self):
        return self.__tope1+1==self.__tope2
    def mostrar(self):
        print(self.__Lista)

if __name__=="__main__":
    opcion=-1
    mipila=Pila(10)
    print("")
    mipila.mostrar()
    print("")
    opcion=int(input("Ingrese opcion\n1-Agregar en Pila 1\n2-Agregar en Pila 2\n3-Remover en Pila 1\n4-Remover en Pila 2\n0-Salir\n"))
    while (opcion!=0):
        if opcion==1:
            mipila.insertaren1(elemento=input("Ingresar elemento: "))
        elif opcion==2:
            mipila.insertaren2(elemento=input("Ingresar elemento: "))
        elif opcion==3:
            mipila.eliminaren1()     
        elif opcion==4:
            mipila.eliminaren2()
        print("")
        mipila.mostrar()
        print("")
        opcion=int(input("Ingrese opcion\n1-Agregar en Pila 1\n2-Agregar en Pila 2\n3-Remover en Pila 1\n4-Remover en Pila 2\n0-Salir\n"))