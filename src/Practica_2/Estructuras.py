'''
Created on 31 oct 2024

@author: mario
'''

from __future__ import annotations
from typing import List, Generic, TypeVar
from abc import ABC, abstractmethod


E = TypeVar("E") 

class Agregado_lineal(ABC, Generic[E]):
    
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
    
from typing import Callable

R = TypeVar("R")


class Lista_ordenada(Agregado_lineal[E], Generic[E,R]):
    
    def __init__(self, order: Callable[[E], R]):
        self._order = order
        self._elements: List[E] = []
        
    @staticmethod
    def of(order: Callable[[E], R]) -> "Lista_ordenada[E, R]":
        return Lista_ordenada(order)

    def _index_order(self, e: E) -> int:
        for i, current in enumerate(self._elements):
            if self._order(e) < self._order(current):
                return i
        return len(self._elements)  

    def add(self, e: E) -> None:
        index = self._index_order(e)
        self._elements.insert(index, e)

    def __str__(self) -> str:
        return "Lista_ordenada(" + ", ".join(str(e) for e in self._elements) + ")"





class Lista_ordenada_sin_repeticion(Agregado_lineal[E], Generic[E, R]):

    def __init__(self, order: Callable[[E], R]):
        self._order = order
        self._elements: List[E] = []

    @staticmethod
    def of(order: Callable[[E], R]) -> 'Lista_ordenada_sin_repeticion[E, R]':
        return Lista_ordenada_sin_repeticion(order)

    def __index_order(self, e: E) -> int:
        for i, elem in enumerate(self._elements):
            if self._order(e) < self._order(elem):
                return i
        return len(self._elements)

    def add(self, e: E) -> None:
        if e not in self._elements: 
            index = self.__index_order(e)
            self._elements.insert(index, e)

    def __repr__(self) -> str:
        elements_str = ', '.join(repr(e) for e in self._elements)
        return f"ListaOrdenadaSinRepeticion({elements_str})"





class Cola(Agregado_lineal[E]):

    @staticmethod
    def of() -> 'Cola[E]':
        return Cola()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __str__(self) -> str:
        elementos = ', '.join(str(e) for e in self._elements)
        return f"Cola({elementos})"
      
P = TypeVar('P')  

class Cola_de_prioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[E] = []      
        self._priorities: List[P] = []    

    @staticmethod
    def of() -> 'Cola_de_prioridad[E, P]':
        return Cola_de_prioridad()

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0
    
    @property
    def elements(self) -> List[E]:
        return self._elements.copy()

    def _index_order(self, priority: P) -> int:
        pos = 0
        while pos < len(self._priorities) and self._priorities[pos] <= priority:
            pos += 1
        return pos

    def add(self, e: E, priority: P) -> None:
        pos = self._index_order(priority)  
        self._elements.insert(pos, e)
        self._priorities.insert(pos, priority)

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        for e, priority in ls:
            self.add(e, priority)

    def remove(self) -> E:
        assert len(self._elements) > 0, "El agregado está vacío"
        self._priorities.pop(0)
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        elementos_eliminados = []
        while not self.is_empty:
            elementos_eliminados.append(self.remove())
        return elementos_eliminados

    def decrease_priority(self, e: E, new_priority: P) -> None:
        index = self.index_of(e)
        if index != -1 and new_priority < self._priorities[index]:
            self._elements.pop(index)
            self._priorities.pop(index)
            self.add(e, new_priority)

    def __str__(self) -> str:
        elementos = ', '.join(f"({e}, {p})" for e, p in zip(self._elements, self._priorities))
        return f"ColaPrioridad[{elementos}]"



class Pila(Agregado_lineal[E]):
    
    def __init__(self):
        super().__init__()
    
    @staticmethod
    def of() -> Pila[E]:
        return Pila()

    def add(self, e: E) -> None:
        self._elements.insert(0, e)  

 
 
