from typing import TypeVar, List, Set, Dict, Optional

V = TypeVar('V')  # Tipo de los vértices
E = TypeVar('E')  # Tipo de las aristas

from Practica_3.grafo import Grafo

def bfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    visitados: Set[V] = set()
    cola: List[V] = []
    predecesores: Dict[V, Optional[V]] = {}

    cola.append(inicio)
    predecesores[inicio] = None

    while cola:
        vertice = cola.pop(0)

        if vertice == destino:
            break

        if vertice not in visitados:
            visitados.add(vertice)

            for vecino in grafo.successors(vertice):
                if vecino not in visitados and vecino not in cola:
                    cola.append(vecino)
                    predecesores[vecino] = vertice

    return reconstruir_camino(predecesores, destino)

def dfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    visitados: Set[V] = set()
    pila: List[V] = []
    predecesores: Dict[V, Optional[V]] = {}

    pila.append(inicio)
    predecesores[inicio] = None

    while pila:
        vertice = pila.pop()

        if vertice == destino:
            break

        if vertice not in visitados:
            visitados.add(vertice)

            for vecino in reversed(list(grafo.successors(vertice))):
                if vecino not in visitados and vecino not in pila:
                    pila.append(vecino)
                    predecesores[vecino] = vertice

    return reconstruir_camino(predecesores, destino)

def reconstruir_camino(predecesores: Dict[V, Optional[V]], destino: V) -> List[V]:
    camino: List[V] = []
    vertice_actual: Optional[V] = destino

    while vertice_actual is not None:
        camino.insert(0, vertice_actual)
        vertice_actual = predecesores.get(vertice_actual)

    if not camino or camino[0] not in predecesores:
        return []

    return camino


