class Pila:
    def __init__(self, max):
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

if __name__=="__main__":
    num=int(input("Ingrese un numero a calcularle el factorial:\n"))
    pila=Pila(num)
    for i in range(num):
        pila.insertar(i+1)
    print ("Pila cargada")
    factorial=1
    while not pila.vacia():
        factorial*=pila.eliminar()
    print("El factorial del numero es: ", factorial)
    