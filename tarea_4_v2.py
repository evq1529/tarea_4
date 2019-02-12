import math
import random

# Super clase
class Carro():
    numero_ciclos = 1

    def __init__(self):
        self.fuerza_motor = random.uniform(0, 9)

    def rendimiento(self):
        return self.fuerza_motor

# Subclases camion, tractor, sedan y bus
class camion(Carro):
    def __init__(self):
        super().__init__()
        Carro.numero_ciclos += 1

    def rendimiento(self):
        self.fuerza_motor = super().rendimiento()
        return 2*self.fuerza_motor + 1

class tractor(Carro):
    def __init__(self):
        super().__init__()

    def rendimiento(self):
        self.fuerza_motor = super().rendimiento()
        y = math.log(self.fuerza_motor, 2)

        # Por si el resultado del logaritmo da negativo
        while(y<0):
            self.fuerza_motor = random.uniform(0, 9)
            y = math.log(self.fuerza_motor, 2)

        return y

class sedan(Carro):
    def __init__(self):
        super().__init__()

    def rendimiento(self):
        self.fuerza_motor = super().rendimiento()
        return 3*(self.fuerza_motor**2)

class bus(Carro):
    def __init__(self):
        super().__init__()

    def rendimiento(self):
        self.fuerza_motor = super().rendimiento()
        return 5*self.fuerza_motor

def carrera():
    avance = lambda x, y: x + math.floor(y)

    def complemento(lista1, lista2):
        a = set(lista1)
        b = set(lista2)
        return list(a - b)

    def Movimiento(lista):
        p1 = lista.index(min(lista))
        p4 = lista.index(max(lista))
        lista_complementaria = complemento([0, 1, 2, 3], [p1, p4])

        if lista[lista_complementaria[0]] < lista[lista_complementaria[1]]:
            p2 = lista_complementaria[0]
            p3 = lista_complementaria[1]
        else:
            p2 = lista_complementaria[1]
            p3 = lista_complementaria[0]

        p1 += 1
        p2 += 1
        p3 += 1
        p4 += 1

        print(f"Posiciones: {p1}->{p2}->{p3}->{p4}".format(p1, p2, p3, p4))

    print("Ciclo: {}".format(Carro.numero_ciclos))

    carro1 = camion()
    print("Fuerza del motor del camión: {}".format(carro1.fuerza_motor))
    FM1 = carro1.rendimiento()
    Avance1 = math.floor(FM1)

    carro2 = tractor()
    print("Fuerza del motor del tractor: {}".format(carro2.fuerza_motor))
    FM2 = carro2.rendimiento()
    Avance2 = math.floor(FM2)

    carro3 = sedan()
    print("Fuerza del motor del sedan: {}".format(carro3.fuerza_motor))
    FM3 = carro3.rendimiento()
    Avance3 = math.floor(FM3)

    carro4 = bus()
    print("Fuerza del motor del bus: {}".format(carro4.fuerza_motor))
    FM4 = carro4.rendimiento()
    Avance4 = math.floor(FM4)

    lista_avance = [Avance1, Avance2, Avance3, Avance4]
    distancia = max(lista_avance)
    print("Avance: {}".format(lista_avance))
    Movimiento(lista_avance)

    while(distancia <= 1000):
        print("Ciclo: {}".format(Carro.numero_ciclos))

        carro1 = camion()
        print("Fuerza del motor del camión: {}".format(carro1.fuerza_motor))
        FM1 = carro1.rendimiento()
        Avance1 = avance(Avance1, FM1)

        carro2 = tractor()
        print("Fuerza del motor del tractor: {}".format(carro2.fuerza_motor))
        FM2 = carro2.rendimiento()
        Avance2 = avance(Avance2, FM2)

        carro3 = sedan()
        print("Fuerza del motor del sedan: {}".format(carro3.fuerza_motor))
        FM3 = carro3.rendimiento()
        Avance3 = avance(Avance3, FM3)

        carro4 = bus()
        print("Fuerza del motor del bus: {}".format(carro4.fuerza_motor))
        FM4 = carro4.rendimiento()
        Avance4 = avance(Avance4, FM4)

        lista_avance = [Avance1, Avance2, Avance3, Avance4]
        distancia = max(lista_avance)
        print("Avance: {}".format(lista_avance))
        Movimiento(lista_avance)

    if lista_avance.index(max(lista_avance)) == 0:
        print("Ganó el camión")
    if lista_avance.index(max(lista_avance)) == 1:
        print("Ganó el tractor")
    if lista_avance.index(max(lista_avance)) == 2:
        print("Ganó el sedán")
    if lista_avance.index(max(lista_avance)) == 3:
        print("Ganó el bus")

carrera()