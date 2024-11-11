'''
Created on 31 oct 2024

@author: mario
'''

from Practica_2.Estructuras import *


print("TEST DE LISTA ORDENADA:")
print(" ")

lista = Lista_ordenada.of(lambda x: x)
print("Creación de una lista con criterio de orden lambda x: x")


print("Se añade en este orden: 3, 1, 2")
lista.add(3)
lista.add(1)
lista.add(2)
print(f"Resultado de la lista: {lista}")

print(" ")
print("################################################")
print(" ")
removed_element = lista.remove()
print(f"El elemento eliminado al utilizar remove(): {removed_element}")

print(" ")
print("################################################")
print(" ")

lista.add(1)
removed_all = lista.remove_all()
print(f"Elementos eliminados utilizando remove_all: {removed_all}")

print(" ")
print("################################################")
print(" ")
print("Comprobando si se añaden los números en la posición correcta...")

lista.add(1)
lista.add(2)
lista.add(3)
lista.add(0)
print(f"Lista después de añadirle el 0: {lista}")

lista.add(10)
print(f"Lista después de añadirle el 10: {lista}")

lista.add(7)
print(f"Lista después de añadirle el 7: {lista}")




print("TEST DE LISTA ORDENADA SIN REPETICIÓN:")
print(" ")
print("################################################")
print(" ")

lista = Lista_ordenada_sin_repeticion.of(lambda x: -x)
print("Creación de una lista con criterio de orden lambda x: -x")


elementos_para_añadir = [23, 47, 47, 1, 2, -3, 4, 5]
for elem in elementos_para_añadir:
    lista.add(elem)

print(f"Se añade en este orden: {', '.join(map(str, elementos_para_añadir))}")
print(f"Resultado de la lista ordenada sin repetición: {lista}")

print(" ")
print("################################################")
print(" ")


elemento_eliminado = lista.remove()
print(f"El elemento eliminado al utilizar remove(): {elemento_eliminado}")

print(" ")
print("################################################")
print(" ")

lista.add(47)
elementos_eliminados = lista.remove_all()
print(f"Elementos eliminados utilizando remove_all: {elementos_eliminados}")

print(" ")
print("################################################")
print(" ")

print("Comprobando si se añaden los números en la posición correcta...")

for elem in [23, 47, 5, 4, 2, 1, -3]:
    lista.add(elem)

lista.add(0)
print(f"Lista después de añadirle el 0: {lista}")
lista.add(0)
print(f"Lista después de añadirle el 0: {lista}")
lista.add(7)
print(f"Lista después de añadirle el 7: {lista}")



print("TEST DE COLA:")
print(" ")
print("################################################")
print(" ")

cola = Cola.of()

elementos_a_agregar = [23, 47, 1, 2, -3, 4, 5]
cola.add_all(elementos_a_agregar)

print("Creación de una cola vacía a la que luego se le añaden con un solo método los números:", elementos_a_agregar)
print("Resultado de la cola:", cola)
print(" ")
print("################################################")
print(" ") 

elementos_eliminados = cola.remove_all()
print("Elementos eliminados utilizando remove_all:", elementos_eliminados)



def test_cola_prioridad():
    cola = Cola_de_prioridad[str, int]()
    
    # Agregar pacientes 
    cola.add('Paciente A', 3)  # Dolor de cabeza leve 
    cola.add('Paciente B', 2)  # Fractura en la pierna 
    cola.add('Paciente C', 1)  # Ataque cardíaco 
    
    # Verificar el estado de la cola 
    assert cola.elements == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de la cola es incorrecto."
    
    # Atender a los pacientes y verificar el orden de atención
    atencion = []
    while not cola.is_empty:
        atencion.append(cola.remove())
    
    assert atencion == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de atención no es correcto."
    
    print("Pruebas superadas exitosamente.")

if __name__ == '__main__':
    test_cola_prioridad()




print("TEST PILA:")
print(" ")
print("Método is_empty y size al crear una lista vacia:")
pila = Pila.of()
print("Resultado de usar el metodo is_empty:", pila.is_empty) 
print("Resultado de usar el metodo size:", pila.size) 

print(" ")
print("################################################")
print(" ")

pila.add(1)
pila.add(2)
pila.add(3)

print("Añadiendo 3 elementos, probamos el metodo size y elements:")
print("Resultado del metodo size:", pila.size)
print("Resultado de usar el metodo elememts:", pila.elements)


print(" ")
print("################################################")
print(" ")
print("Ahora probamos el metodo remove y remove_all al volver a poner el elemento iniciado:")
elemento = pila.remove()
print(f"Elemento eliminado: {elemento}")

pila.add(elemento)

elementos_eliminados = pila.remove_all()
print("Los elementos eliminados son", elementos_eliminados)