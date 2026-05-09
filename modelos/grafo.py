class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_aresta(self, origem, destino, peso):
        if origem not in self.grafo:
            self.grafo[origem] = []

        self.grafo[origem].append((destino, peso))