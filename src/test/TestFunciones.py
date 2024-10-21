'''
Created on 3 oct 2024

@author: mario
'''

from math import factorial
from pickle import NONE

def funcion_uno (k:int, n:int):
    if n>k:
        resultado=1
        for i in range(0, k):
            resultado = resultado* (n-i+1)  
    return resultado
    
    
print(funcion_uno(2, 4))  
    
    
def funcion_dos(a:int, r:int, k:int):
    resultado=1
    for n in range(1, k+1):
        resultado= resultado*(a*r**(n-1))
    return resultado
        
print(funcion_dos(3, 5, 2))

def funcion_tres(n:int, k:int):
    if n>=k:
        resultado= factorial(n)/(factorial(k)*factorial(n-k))
    return resultado

print(funcion_tres(4,2))

def funcion_cuatro(n, k):
    if n>=k:
        sumatorio=0
        for i in range (0, k):
            sumatorio=sumatorio+(-1)**i * ((factorial(k+1)/(factorial(i+1)*factorial(k+1-i-1)))*((k-i)**n)) 
        return (1/factorial(k))*sumatorio
    
print(funcion_cuatro(4, 2))

def f(x):
    return 2*x**2
def df(x):
    return 4*x
def funcion_cinco(a, e):
    xn=a
    for n in range(1000):
        if abs(f(xn))<=e:
            return xn
        if df(xn)==0:
            return None
        xn=xn-f(xn)/df(xn)
    return None

print(funcion_cinco(3, 0.001)) 
