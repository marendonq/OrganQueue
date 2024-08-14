from datetime import datetime

class Patient:
    def __init__(self, name, id, lifeExpectation):
        self.name = name
        self.id = id
        self.lifeExpectation = lifeExpectation
        self.ingress_time = datetime.now()

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getLifeExpectation(self):
        return self.lifeExpectation

    def getIngressTime(self):
        return self.ingress_time

    def __str__(self):
        return (f'Nombre: {self.getName()}\nIdentificación: {self.getId()}\n'
                f'Expectativa de vida: {self.getLifeExpectation()}\n'
                f'Hora de ingreso: {self.getIngressTime()}')
