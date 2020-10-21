from Particula import Particula

class Organizador:
    def __init__(self):
        self.org = []

    def agregar_inicio(self,part):
        self.org.insert(0,part)

    def agregar_final(self,part):
        self.org.append(part)

    def mostrar(self):
        for i in self.org:
            print(i)

particula_1 = Particula(7,5,4,1)
particula_2 = Particula(100,200,200,1)
particula_3 = Particula(500,500,200,200)
organizador_1 = Organizador()
organizador_1.agregar_inicio(particula_1)
organizador_1.agregar_final(particula_2)
organizador_1.agregar_final(particula_3)
organizador_1.mostrar()
