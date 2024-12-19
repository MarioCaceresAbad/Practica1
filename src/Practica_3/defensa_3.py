'''
Created on 19 dic 2024

@author: mario
'''
from dataclasses import dataclass
from typing import List, Dict
from Practica_3.grafo import Grafo

@dataclass(frozen=True)
class Gen:
    nombre: str
    tipo: str
    num_mutaciones: int
    loc_cromosoma: str

    @staticmethod
    def of(nombre: str, tipo: str, num_mutaciones: int, loc_cromosoma: str):
        if num_mutaciones < 0:
            raise ValueError("El número de mutaciones debe ser mayor o igual a cero.")
        return Gen(nombre, tipo, num_mutaciones, loc_cromosoma)

    @staticmethod
    def parse(line: str):
        # Supongamos que el formato de la línea es: nombre,tipo,num_mutaciones,loc_cromosoma
        partes = line.split(",")
        if len(partes) != 4:
            raise ValueError("La línea debe tener exactamente 4 campos separados por comas.")
        nombre, tipo, num_mutaciones_str, loc_cromosoma = partes
        try:
            num_mutaciones = int(num_mutaciones_str)
        except ValueError:
            raise ValueError("El número de mutaciones debe ser un entero válido.")

        return Gen.of(nombre, tipo, num_mutaciones, loc_cromosoma)

# Función para cargar genes desde un fichero
def cargar_genes_desde_fichero(ruta_fichero: str) -> List[Gen]:
    genes = []
    with open(ruta_fichero, 'r') as fichero:
        for linea in fichero:
            linea = linea.strip()  # Elimina espacios y saltos de línea
            if linea:  # Asegúrate de que no esté vacía
                try:
                    gen = Gen.parse(linea)
                    genes.append(gen)
                except ValueError as e:
                    print(f"Error al parsear la línea: {linea}. Detalles: {e}")
    return genes

# Ejf main():
def main():
    ruta_fichero = r"C:\Users\mario\git\PruebaFP\src\Practica_3\ficheros_practica3\genes.txt"
    genes = cargar_genes_desde_fichero(ruta_fichero)
    for gen in genes:
        print(gen)

if __name__ == "__main__":
    main()

print("-----------------------------------------------------")
@dataclass(frozen=True)
class RelacionGenAGen:
    nombre_gen1: str
    nombre_gen2: str
    conexion: float

    @staticmethod
    def of(nombre_gen1: str, nombre_gen2: str, conexion: float):
        if not (-1.0 <= conexion <= 1.0):
            raise ValueError("La conexión debe estar entre -1 y 1, inclusive.")
        return RelacionGenAGen(nombre_gen1, nombre_gen2, conexion)

    @staticmethod
    def parse(line: str):
        # Supongamos que el formato de la línea es: nombre_gen1,nombre_gen2,conexion
        partes = line.split(",")
        if len(partes) != 3:
            raise ValueError("La línea debe tener exactamente 3 campos separados por comas.")
        nombre_gen1, nombre_gen2, conexion_str = partes
        try:
            conexion = float(conexion_str)
        except ValueError:
            raise ValueError("La conexión debe ser un número real.")

        return RelacionGenAGen.of(nombre_gen1, nombre_gen2, conexion)

# Ejemplo de uso para probar el método parse y la creación de objetos
# Función para cargar relaciones desde un fichero
def cargar_relaciones_desde_fichero(ruta_fichero: str) -> List[RelacionGenAGen]:
    relaciones = []
    with open(ruta_fichero, 'r') as fichero:
        for linea in fichero:
            linea = linea.strip()  # Elimina espacios y saltos de línea
            if linea:  # Asegúrate de que no esté vacía
                try:
                    relacion = RelacionGenAGen.parse(linea)
                    relaciones.append(relacion)
                except ValueError as e:
                    print(f"Error al parsear la línea: {linea}. Detalles: {e}")
    return relaciones

# Función principal para cargar genes
def main_genes():
    ruta_fichero = r"C:\Users\mario\git\PruebaFP\src\Practica_3\ficheros_practica3\genes.txt"
    genes = cargar_genes_desde_fichero(ruta_fichero)
    for gen in genes:
        print(gen)

# Función principal para cargar relaciones
def main_relaciones():
    ruta_fichero = r"C:\Users\mario\git\PruebaFP\src\Practica_3\ficheros_practica3\red_genes.txt"  # Cambia a la ruta de tu fichero
    relaciones = cargar_relaciones_desde_fichero(ruta_fichero)
    for relacion in relaciones:
        print(relacion)

if __name__ == "__main__":
    main_relaciones()


print("-----------------------------------------------------")



class RedGenica(Grafo):
    """
    Representa una red génica basada en un grafo.
    """
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        self.genes_por_nombre: Dict[str, Gen] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> "RedGenica":
        """
        Método de factoría para crear una nueva Red Génica.
        
        :param es_dirigido: Indica si la red génica es dirigida (True) o no dirigida (False).
        :return: Nueva red génica.
        """
        return RedGenica(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> "RedGenica":
        red_genica = RedGenica(es_dirigido)

        with open(f1, 'r') as archivo_genes:
            for linea in archivo_genes:
                linea = linea.strip()
                if linea:
                    try:
                        gen = Gen.parse(linea)
                        red_genica.agregar_vertice(gen)
                        red_genica.genes_por_nombre[gen.nombre] = gen
                    except ValueError as e:
                        print(f"Error al parsear el gen: {linea}. Detalles: {e}")

        with open(f2, 'r') as archivo_relaciones:
            for linea in archivo_relaciones:
                linea = linea.strip()
                if linea:
                    try:
                        relacion = RelacionGenAGen.parse(linea)
                        if relacion.nombre_gen1 in red_genica.genes_por_nombre and relacion.nombre_gen2 in red_genica.genes_por_nombre:
                            red_genica.agregar_arista(relacion)
                        else:
                            print(f"Relación no válida: {linea}. Alguno de los genes no está registrado.")
                    except ValueError as e:
                        print(f"Error al parsear la relación: {linea}. Detalles: {e}")

        return red_genica

# Ejemplo de uso de la clase RedGenica
def main_red():
    archivo_genes = "genes.txt"  # Cambia a la ruta de tu archivo de genes
    archivo_relaciones = "interacciones.txt"  # Cambia a la ruta de tu archivo de relaciones
    red_genica = RedGenica.parse(archivo_genes, archivo_relaciones, es_dirigido=False)

    print("Genes en la red génica:")
    for gen in red_genica.vertices:
        print(gen)

    print("\nRelaciones en la red génica:")
    for relacion in red_genica.aristas:
        print(relacion)


import networkx as nx
import matplotlib.pyplot as plt

# Paso 1: Crear una red génica no dirigida a partir de los dos ficheros
def crear_red_genica(archivo_genes, archivo_relaciones):
    red_genica = nx.Graph()

    with open(archivo_genes, 'r') as f_genes:
        for linea in f_genes:
            linea = linea.strip()
            if linea:
                gen = Gen.parse(linea)
                red_genica.add_node(gen.nombre, tipo=gen.tipo, num_mutaciones=gen.num_mutaciones, loc_cromosoma=gen.loc_cromosoma)

    with open(archivo_relaciones, 'r') as f_relaciones:
        for linea in f_relaciones:
            linea = linea.strip()
            if linea:
                relacion = RelacionGenAGen.parse(linea)
                red_genica.add_edge(relacion.nombre_gen1, relacion.nombre_gen2, conexion=relacion.conexion)

    return red_genica

# Paso 2: Aplicar un recorrido en profundidad desde el KRAS hasta el PIK3CA
def recorrido_profundidad(red_genica, inicio, fin):
    return list(nx.dfs_edges(red_genica, source=inicio))

# Paso 3: Crear un subgrafo a partir de los vértices del paso 2 y dibujarlo
def crear_subgrafo_y_dibujar(red_genica, recorrido, genes_interes):
    subgrafo = red_genica.edge_subgraph(recorrido).copy()
    subgrafo = subgrafo.subgraph(genes_interes).copy()
    pos = nx.spring_layout(subgrafo)
    nx.draw(subgrafo, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight="bold")
    labels = nx.get_edge_attributes(subgrafo, 'conexion')
    nx.draw_networkx_edge_labels(subgrafo, pos, edge_labels=labels)
    plt.show()

# Archivos de entrada
archivo_genes = r'C:\Users\mario\git\PruebaFP\src\Practica_3\ficheros_practica3\genes.txt'
archivo_relaciones = r'C:\Users\mario\git\PruebaFP\src\Practica_3\ficheros_practica3\red_genes.txt'

# Crear la red génica
red_genica = crear_red_genica(archivo_genes, archivo_relaciones)

# Realizar el recorrido en profundidad
recorrido = recorrido_profundidad(red_genica, 'KRAS', 'PIK3CA')

# Crear el subgrafo y dibujarlo solo con los genes de interés
crear_subgrafo_y_dibujar(red_genica, recorrido, ['KRAS', 'PIK3CA', 'TP53'])
