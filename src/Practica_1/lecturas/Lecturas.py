'''
Created on 21 oct 2024

@author: mario
'''



import re
from typing import Optional

#6
def funcion_seis(fichero: str, sep: str, cad: str):
    try:
        contador = 0
        with open(fichero, 'r', encoding='utf-8') as f:
            for linea in f:
                cad = (cad.lower()).capitalize()
                palabras = re.split(sep, linea)
                palabras = [palabra.lower() for palabra in palabras]
                palabras = [palabra.capitalize() for palabra in palabras]
                for palabra in palabras:
                    if palabra == cad:
                        contador += 1
        return contador

    except IOError as e:
        return f"Error al intentar leer el archivo: {e}"
    except Exception as i:
        return f"Error inesperado: {i}"
    
      
#7
def funcion_siete(fichero: str, cad: str):
    try:
        lineas_encontradas = []
        with open(fichero, 'r', encoding='utf-8') as f:
            for linea in f:
                if cad.lower() in linea.lower():
                    lineas_encontradas.append(linea.strip())
        return lineas_encontradas

    except IOError as e:
        return f"Error al intentar leer el archivo: {e}"
    except Exception as i:
        return f"Error inesperado: {i}"
    

#8
def funcion_ocho(fichero: str):
    try:
        palabras_unicas = set()
        with open(fichero, 'r', encoding='utf-8') as f:
            for linea in f:
                palabras = linea.split()  # separa por espacios
                palabras_unicas.update(palabras)  # añade palabras únicas al conjunto
        return list(palabras_unicas)

    except IOError as e:
        return f"Error al intentar leer el archivo: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"
    


#9
def funcion_nueve(file_path: str) -> Optional[float]:
    try:
        total_longitud = 0
        total_lineas = 0
        with open(file_path, 'r', encoding='utf-8') as f:
            for linea in f:
                lineas = linea.split(",")
                total_longitud += len(lineas)
                total_lineas += 1
        return total_longitud / total_lineas if total_lineas > 0 else None

    except IOError:
        return None
    except Exception:
        return None


if _name_ == '_main_':
    pass  