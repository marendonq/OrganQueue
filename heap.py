from utils import binary_insert

class MinHeap:
    def __init__(self):
        self.heap = []
        self.heapOrdenado = []
        self.posiciones = {}

    def tamanio(self):
        return len(self.heap)

    def _subir(self, i):
        while i > 0 and self.heap[i].getLifeExpectation() < self.heap[(i - 1) // 2].getLifeExpectation():
            self._intercambiar(i, (i - 1) // 2)
            i = (i - 1) // 2

    def _intercambiar(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.posiciones[self.heap[i].getId()] = i
        self.posiciones[self.heap[j].getId()] = j

    def insertar(self, patient):
        self.heap.append(patient)
        binary_insert(self.heapOrdenado, patient)
        self.posiciones[patient.getId()] = self.tamanio() - 1
        self._subir(self.posiciones[patient.getId()])

    def hijoMenor(self, i):
        hijoIzq = 2 * i + 1
        hijoDer = 2 * i + 2
        if hijoDer < self.tamanio() and self.heap[hijoDer].getLifeExpectation() < self.heap[hijoIzq].getLifeExpectation():
            return hijoDer
        return hijoIzq

    def _bajar(self, i):
        while 2 * i + 1 < self.tamanio():
            iMenor = self.hijoMenor(i)
            if self.heap[i].getLifeExpectation() <= self.heap[iMenor].getLifeExpectation():
                break
            self._intercambiar(i, iMenor)
            i = iMenor

    def extraer_minimo(self):
        if self.tamanio() == 0:
            return None
        min_patient = self.heap[0]
        self.posiciones.pop(min_patient.getId())
        if self.tamanio() > 1:
            self.heap[0] = self.heap.pop()
            self._bajar(0)
        else:
            self.heap.pop()
        self.heapOrdenado.pop(0)
        return min_patient

    def vacio(self):
        return self.tamanio() == 0
