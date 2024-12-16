from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, TypeVar, Set, Optional, Tuple, Generic
from datetime import date, datetime
from Practica_3.grafo import Grafo as BaseGrafo


# Tipos genéricos para vértices y aristas
V = TypeVar('V')
E = TypeVar('E')

# -------------------------
# Clase Usuario
# -------------------------
@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date

    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> Usuario:
        if len(dni) != 9 or not dni[:-1].isdigit() or not dni[-1].isalpha():
            raise ValueError("El DNI debe tener 8 dígitos y una letra al final.")
        if fecha_nacimiento > date.today():
            raise ValueError("La fecha de nacimiento no puede estar en el futuro.")
        return Usuario(dni, nombre, apellidos, fecha_nacimiento)

    def __str__(self) -> str:
        return f"{self.dni}: {self.nombre} {self.apellidos} ({self.fecha_nacimiento})"

# -------------------------
# Clase Relacion
# -------------------------
@dataclass(frozen=True)
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    __n: int = 0  # Contador de relaciones para IDs únicos

    @staticmethod
    def of(interacciones: int, dias_activa: int) -> Relacion:
        Relacion.__n += 1
        return Relacion(Relacion.__n, interacciones, dias_activa)

    def __str__(self) -> str:
        return f"Relacion {self.id}: {self.interacciones} interacciones, {self.dias_activa} días activa"

# -------------------------
# Clase Grafo (Base)
# -------------------------
class Grafo(Generic[V, E]):
    def __init__(self, es_dirigido: bool = False):
        self.es_dirigido = es_dirigido
        self.adj: Dict[V, List[Tuple[V, E]]] = {}

    def add_vertex(self, vertice: V):
        if vertice not in self.adj:
            self.adj[vertice] = []

    def add_edge(self, origen: V, destino: V, arista: E):
        self.add_vertex(origen)
        self.add_vertex(destino)
        self.adj[origen].append((destino, arista))
        if not self.es_dirigido:
            self.adj[destino].append((origen, arista))

    def vertices(self) -> Set[V]:
        return set(self.adj.keys())

    def successors(self, vertice: V) -> List[V]:
        return [destino for destino, _ in self.adj.get(vertice, [])]

    def subgraph(self, vertices: Set[V]) -> Grafo[V, E]:
        sub: Grafo[V, E] = Grafo(self.es_dirigido)
        for vertice in vertices:
            if vertice in self.adj:
                for destino, arista in self.adj[vertice]:
                    if destino in vertices:
                        sub.add_edge(vertice, destino, arista)
        return sub

# -------------------------
# Clase Red_social
# -------------------------
class Red_social(BaseGrafo[Usuario, Relacion]):
    def __init__(self, es_dirigido: bool = False):
        super().__init__(es_dirigido)
        self.usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> Red_social:
        return Red_social(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> Red_social:
        red = Red_social(es_dirigido)

        # Leer usuarios
        with open(f1, 'r') as archivo_usuarios:
            for linea in archivo_usuarios:
                dni, nombre, apellidos, fecha = linea.strip().split(',')
                usuario = Usuario.of(dni, nombre, apellidos, datetime.strptime(fecha, "%Y-%m-%d").date())
                red.add_vertex(usuario)
                red.usuarios_dni[dni] = usuario

        # Leer relaciones
        with open(f2, 'r') as archivo_relaciones:
            for linea in archivo_relaciones:
                dni1, dni2, interacciones, dias_activa = linea.strip().split(',')
                if dni1 in red.usuarios_dni and dni2 in red.usuarios_dni:
                    usuario1 = red.usuarios_dni[dni1]
                    usuario2 = red.usuarios_dni[dni2]
                    relacion = Relacion.of(int(interacciones), int(dias_activa))
                    red.add_edge(usuario1, usuario2, relacion)

        return red

# -------------------------
# Funciones BFS, DFS y reconstruir_camino
# -------------------------
def bfs(grafo: Grafo[V, E], inicio: V, destino: V) -> List[V]:
    visitados: Set[V] = set()
    cola: List[V] = [inicio]
    predecesores: Dict[V, Optional[V]] = {inicio: None}

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
    pila: List[V] = [inicio]
    predecesores: Dict[V, Optional[V]] = {inicio: None}

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

    return camino

# -------------------------
# Ejecución Principal
# -------------------------

if __name__ == '__main__':
    raiz = '../../'  # Cambia esta variable si ejecutas este script desde otro directorio
    rrss = Red_social.parse(r"C:\Users\mario\git\PruebaFP\src\Practica_3\ficheros_practica3\usuarios.txt",
                            r"C:\Users\mario\git\PruebaFP\src\Practica_3\ficheros_practica3\relaciones.txt",
                            es_dirigido=False)

    print("El camino más corto desde 25143909I hasta 87345530M es:")
    camino = bfs(rrss, rrss.usuarios_dni['25143909I'], rrss.usuarios_dni['87345530M'])
    print(" -> ".join(str(usuario) for usuario in camino))

    g_camino = rrss.subgraph(set(camino))
    g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.dni}", lambda_arista=lambda e: str(e.id))
    
    
    
    
    
    
    
    