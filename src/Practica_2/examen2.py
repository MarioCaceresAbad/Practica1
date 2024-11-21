'''
Created on 21 nov 2024

@author: mario
'''
from __future__ import annotations
from typing import List, Generic, TypeVar, Optional
from abc import ABC, abstractmethod

from typing import Callable
 
E = TypeVar("E")
 
class Agregado_lineal_modificado(ABC, Generic[E]):
    
    def __init__(self):
        self._elements: List[E] = []
    
    #Propiedades
    @property
    def size(self) -> int:
        return len(self._elements)
    
    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    @property
    def elements(self) -> List[E]:
        return self._elements.copy()
    
    #Métodos
    @abstractmethod
    def add(self, e: E) -> None:
        pass
    
    def add_all(self, ls: list[E]) -> None:
        for e in ls:
            self.add(e)
    
    def remove(self) -> E: 
        assert len(self._elements) > 0, "El agregado está vacío"
        return self._elements.pop(0)
    
    def remove_all(self) -> list[E]:
        elementos_eliminados = self._elements.copy()
        self._elements.clear()
        return elementos_eliminados

    def contains(self, e: E) -> bool:
        """Verifica si un elemento dado está dentro del agregado."""
        return e in self._elements
    
    def find(self, func: Callable[[E], bool]) -> Optional[E]:
        """Devuelve el primer elemento que cumple con una condición."""
        for element in self._elements:
            if func(element):
                return element
        return None
    
    def filter(self, func: Callable[[E], bool]) -> List[E]:
        """Devuelve una lista con los elementos que cumplen con una condición."""
        return [element for element in self._elements if func(element)]
 
 
class ColaConLimite(Agregado_lineal_modificado[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a cero.")
        self._capacidad = capacidad

    @property
    def capacidad(self) -> int:
        return self._capacidad

    def add(self, e: E) -> None:
        if self.size >= self.capacidad:
            raise OverflowError("La cola está llena.")
        self._elements.append(e)

    def is_full(self) -> bool:
        return self.size >= self.capacidad

    @classmethod
    def of(cls, capacidad: int) -> "ColaConLimite[E]":
        return cls(capacidad)
        
        

def pruebas_agregado_lineal_modificado():
    print("Pruebas para Agregado_lineal_modificado:")

    class MiAgregado(Agregado_lineal_modificado[int]):
        def add(self, e: int) -> None:
            self._elements.append(e)
    
    agregado = MiAgregado()

    # Prueba: propiedades básicas
    print("  Prueba: is_empty y size")
    try:
        assert agregado.is_empty
        assert agregado.size == 0
        print("    OK")
    except AssertionError:
        print("    FALLO")

    # Prueba: añadir elementos
    agregado.add(1)
    try:
        assert not agregado.is_empty
        assert agregado.size == 1
        print("    OK")
    except AssertionError:
        print("    FALLO")

    # Prueba: elementos
    print("  Prueba: elements")
    agregado.add(2)
    try:
        assert agregado.elements == [1, 2]
        print("    OK")
    except AssertionError:
        print("    FALLO")

    # Prueba: métodos avanzados
    print("  Prueba: contains")
    try:
        assert agregado.contains(2)
        assert not agregado.contains(3)
        print("    OK")
    except AssertionError:
        print("    FALLO")

    print("  Prueba: find")
    try:
        assert agregado.find(lambda x: x > 1) == 2
        assert agregado.find(lambda x: x > 3) is None
        print("    OK")
    except AssertionError:
        print("    FALLO")

    print("  Prueba: filter")
    try:
        assert agregado.filter(lambda x: x % 2 == 0) == [2]
        print("    OK")
    except AssertionError:
        print("    FALLO")


def pruebas_cola_con_limite():
    print("Pruebas para ColaConLimite:")

    cola = ColaConLimite.of(3)

    # Prueba: capacidad
    print("  Prueba: capacidad válida")
    try:
        assert cola.capacidad == 3
        print("    OK")
    except AssertionError:
        print("    FALLO")

    # Prueba: añadir elementos
    print("  Prueba: add y elementos")
    cola.add("A")
    cola.add("B")
    try:
        assert cola.elements == ["A", "B"]
        print("    OK")
    except AssertionError:
        print("    FALLO")

    # Prueba: cola llena
    print("  Prueba: overflow")
    cola.add("C")
    try:
        cola.add("D")
        print("    FALLO")
    except OverflowError:
        print("    OK")

    # Prueba: eliminar elementos
    print("  Prueba: remove")
    try:
        assert cola.remove() == "A"
        assert cola.elements == ["B", "C"]
        print("    OK")
    except AssertionError:
        print("    FALLO")

    # Prueba: eliminar de cola vacía
    print("  Prueba: remove en cola vacía")
    cola.remove()
    cola.remove()
    try:
        cola.remove()
        print("    FALLO")
    except AssertionError:
        print("    OK")

    # Prueba: is_full
    print("  Prueba: is_full")
    cola.add("X")
    cola.add("Y")
    cola.add("Z")
    try:
        assert cola.is_full()
        print("    OK")
    except AssertionError:
        print("    FALLO")


# Ejecución de pruebas
pruebas_agregado_lineal_modificado()
pruebas_cola_con_limite()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
