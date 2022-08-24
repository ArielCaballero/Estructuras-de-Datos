from random import random

class paciente:
    def __init__(self, nombre, apellido, especialidad):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__especialidad=especialidad
        self.__tiempo=0
    def getnombre(self):
        return self.__nombre
    def getapellido(self):
        return self.__apellido
    def getespecialidad(self):
        return self.__especialidad
    def gettiempo(self):
        return self.__tiempo
    def settiempo(self, tiempo):
        self.__tiempo=tiempo
    def actualizar(self):
        self.__tiempo+=1
    


class Nodo:
    __dato=None
    __siguiente=None
    def __init__(self, elemento):
        self.__dato=elemento
        self.__siguiente=None
    def getdato(self):
        return self.__dato
    def getsiguiente(self):
        return self.__siguiente
    def setdato(self, elemento):
        self.__dato=elemento
    def setsiguiente(self, siguiente):
        self.__siguiente=siguiente


class ColaEnlazada:
    __cant=0
    __contador=0
    __pr=None
    __ul=None
    __frecuencia=None
    __tiempoatencion=None
    def __init__(self, frecuencia, tiempoatencion, max, especialidad="", cant=0, pr=None, ul=None):
        self.__especialidad=especialidad
        self.__cant=cant
        self.__pr=pr
        self.__ul=ul
        self.__frecuencia=frecuencia
        self.__tiempoatencion=tiempoatencion
        self.__contador=0
        self.__pacientesatendidos=0
        self.__tiempototal=0
        self.__max=max
    def getespecialidad(self):
        return self.__especialidad
    def getpacientesatendidos(self):
        return self.__pacientesatendidos
    def actualizarpacientes(self):
        self.__pacientesatendidos+=1
    def gettiempototal(self):
        return self.__tiempototal
    def actualizartiempototal(self, tiempo):
        self.__tiempototal+=tiempo
    def getcontador(self):
        return self.__contador
    def setcontador(self, valor):
        self.__contador=valor
    def getfrecuencia(self):
        return self.__frecuencia
    def gettiempo(self):
        return self.__tiempoatencion
    def vacia(self):
        return self.__cant==0
    def getcant(self):
        return self.__cant
    def insertar(self, elemento=0):
        if type(elemento!=Nodo):
            elemento=Nodo(elemento)
        if not self.vacia():
            if self.__cant<self.__max:
                self.__ul.setsiguiente(elemento)
                self.__ul=elemento
        else:
            self.__pr=elemento
            self.__ul=elemento
        self.__cant+=1
        return elemento
    def suprimir(self):
        if not self.vacia():
            aux=self.__pr
            dato=self.__pr.getdato()
            self.__pr=self.__pr.getsiguiente()
            self.__cant-=1
            valor=dato
            del aux
            if self.__pr==None:
                self.__ul=None
        else:
            print("La cola ya esta vacia")
            valor=None
        return valor
    def mostrar(self):
        aux=self.__pr
        cola="F"
        while aux!=None:
            cola= str(aux.getdato().gettiempo()) + "->"+ cola
            aux=aux.getsiguiente()
        print(cola)
    def actualizar(self):
        aux=self.__pr
        while aux!=None:
            aux.getdato().actualizar()
            aux=aux.getsiguiente()

if __name__=="__main__":
    Colaturnos=ColaEnlazada(1, 2, 100)
    colasespecialidades=[]
    colasespecialidades.append(ColaEnlazada(-1, 20, 10, "Ginecologia"))
    colasespecialidades.append(ColaEnlazada(-1, 20, 10,"Clinica Medica"))
    colasespecialidades.append(ColaEnlazada(-1, 20, 10,"Oftalmologia"))
    colasespecialidades.append(ColaEnlazada(-1, 20, 10,"Pediatria"))
    tiempototal=240
    for contador in range(tiempototal):
        llegadapaciente=random()
        if llegadapaciente<1/Colaturnos.getfrecuencia():
            numero=random()
            nombre="Nombre"+str(contador+1)
            apellido="Apellido"+str(contador+1)
            if numero<0.25:
                especialidad="Ginecologia"
            elif numero<0.5:
                especialidad="Clinica Medica"
            elif numero<0.75:
                especialidad="Oftalmologia"
            elif numero<1:
                especialidad="Pediatria" 
            persona=paciente(nombre, apellido, especialidad)
            Colaturnos.insertar(persona)
        if Colaturnos.getcontador()==0 and contador<60:
            if (not Colaturnos.vacia()):
                pacientees=Colaturnos.suprimir()
                Colaturnos.actualizarpacientes()
                Colaturnos.actualizartiempototal(pacientees.gettiempo())
                pacientees.settiempo(0)
                for cola in colasespecialidades:
                    if pacientees.getespecialidad()==cola.getespecialidad():
                        cola.insertar(pacientees)
                Colaturnos.setcontador(Colaturnos.gettiempo())
        else:
            Colaturnos.setcontador(Colaturnos.getcontador()-1)
        for cola in colasespecialidades:
            if cola.getcontador()==0:
                if not cola.vacia():
                    pacienteatendido=cola.suprimir()
                    cola.actualizarpacientes()
                    cola.actualizartiempototal(pacienteatendido.gettiempo())
                    cola.setcontador(cola.gettiempo())
            else:
                cola.setcontador(cola.getcontador()-1)
        for cola in colasespecialidades:
            cola.actualizar()
        Colaturnos.actualizar()
    Tiempomedioturnos=Colaturnos.gettiempototal()/Colaturnos.getpacientesatendidos()
    pacientessinturno=Colaturnos.getcant()
    print("Tiempo medio de espera de un cliente en la Cola de Turnos: ", Tiempomedioturnos, " minutos")
    print("Pacientes que se quedaron sin turnos: ", pacientessinturno)
    for cola in colasespecialidades:
        Tiempomedio=cola.gettiempototal()/cola.getpacientesatendidos()
        print("Tiempo medio de espera de un cliente en la Cola de {}: {:.2f} minutos".format(cola.getespecialidad(), Tiempomedio))

        