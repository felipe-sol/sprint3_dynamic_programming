import heapq

def dijkstra(grafo, inicio):
    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0

    fila = [(0, inicio)]
    caminhos = {}

    while fila:
        dist_atual, no_atual = heapq.heappop(fila)

        for vizinho, peso in grafo.get(no_atual, []):
            nova_dist = dist_atual + peso

            if nova_dist < distancias.get(vizinho, float('inf')):
                distancias[vizinho] = nova_dist
                caminhos[vizinho] = no_atual
                heapq.heappush(fila, (nova_dist, vizinho))

    return distancias, caminhos


def reconstruir_caminho(caminhos, inicio, fim):
    caminho = []
    atual = fim

    while atual != inicio:
        caminho.append(atual)
        atual = caminhos.get(atual)

        if atual is None:
            return []

    caminho.append(inicio)
    return caminho[::-1]