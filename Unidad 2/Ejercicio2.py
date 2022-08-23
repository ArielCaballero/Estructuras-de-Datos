import Ejercicio1 as Pilas

if __name__=="__main__":
    Pila= Pilas.PilaSecuencial()
    numero=int(input("Ingrese un numero entero positivo (ingrese un negativo para terminar)\n"))
    while numero>=0:
        while numero!=0:
            if (numero%2==0):
                Pila.insertar(0)
            else:
                Pila.insertar(1)
            numero=numero//2
        numeroenbinario=""
        while not Pila.vacia():
            numeroenbinario = numeroenbinario+str(Pila.suprimir()) 
        print("El numero en binario es: {}\n".format(numeroenbinario))
        numero=int(input("Ingrese un numero entero positivo (ingrese un negativo para terminar)\n"))
    print("Termino el programa")