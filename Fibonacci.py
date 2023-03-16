# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 16:28:59 2016

@author: Diego

Creamos un programa que calcule la lista de numeros para cualquier n.

"""
#Imprimimos datos por pantalla

z = eval(raw_input('Dame el valor de z: '))

#Creamos la lista

Fibonacci = []

#Empleamos el bucle for in

for n in range(0, z):
    if n == 0 :
        Fibonacci.append(0)
        
    elif n == 1:
        Fibonacci.append(1)
        
    if n > 1:
        f = Fibonacci[n - 1] + Fibonacci[n - 2]
        Fibonacci.append(f)
        
print(Fibonacci)        