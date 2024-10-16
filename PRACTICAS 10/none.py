class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, nodo1, nodo2):
        if nodo1 in self.grafo and nodo2 in self.grafo:
            self.grafo[nodo1].append(nodo2)
            self.grafo[nodo2].append(nodo1)

    def mostrar_grafo(self):
        for nodo, adyacentes in self.grafo.items():
            print(f"{nodo}: {adyacentes}")

# Esempio di utilizzo
mi_grafo = Grafo()
mi_grafo.agregar_nodo('A')
mi_grafo.agregar_nodo('B')
mi_grafo.agregar_nodo('C')
mi_grafo.agregar_arista('A', 'B')
mi_grafo.agregar_arista('B', 'C')
mi_grafo.mostrar_grafo()

# Stampare il dizionario del grafo (non ordinato)
print(mi_grafo.grafo)