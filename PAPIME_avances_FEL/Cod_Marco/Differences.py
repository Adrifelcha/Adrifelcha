#!/usr/bin/env python
import math                       #Biblioteca para operaciones matematicas como raiz cuadrada, logaritmos, etc.
import numpy                      #Biblioteca para operaciones matematicas complejas
import matplotlib.pyplot as plt   #Biblioteca para desplegar graficas basicas

#A diferencia de las otras funciones, el arreglo se inicializa con un solo elemento
#y se va llenando de acuerdo con la evolucion que indica la ecuacion en diferencias.
#Estas variables son necesarias para cualquier ecuacion en diferencias
t0 = 0         #Valor inicial del tiempo. Usualmente es cero
V0 = 10         #Condicion inicial: se refiere al primer valor de la funcion
t = [0]        #Arreglo de valores de la var independiente, en este caso, tiempo
V = [0]        #Arreglo de valores de la funcion, calculada por una ecuacion en diferencias
k = 0          #Tiempo discreto actual k = 0,1,2,3....n
n = 100        #Numero de pasos (tiempos discretos) a calcular

#Las siguientes constantes son para una ecuacion en especifico:
# deltaV = r - aV
# V(k+1) = V(k) + (r - aV)
r = 50
a = 0.1

for i in range(n):
    t.append(t[k] + 1)    #Se agrega el siguiente valor de tiempo al arreglo correspondiente
    
    deltaV = r - a*V[k]   #Se calcula la diferencia. ESTA LINEA ES EN SI EL MODELO DE INTERES
                          #La caracteristica fundamental de una ecuacion en diferencias es que la
                          #diferencia calculada (el cambio en la funcion), depende del valor de la misma funcion
                          #es decir, la funcion cambia de acuerdo con su valor actual
                          
    Vk1 = V[k] + deltaV   #El siguiente valor de la funcion, es el actual, mas la diferencia calculada
    V.append(Vk1)         #Se agrega el siguiente valor al arreglo
    k = k+1               #Se incrementa el paso actual

#Estas lineas son unicamente para graficar
plt.plot(t, V)
plt.show()

########## E J E R C I C I O S ############
#1. Modificar las constantes 'r' y 'a' y observar el comportamiento de la funcion. De ser necesario,
#   cambiar los valores de las condiciones iniciales y el numero 'n' de pasos
#2. Cambiar la linea 25 de este codigo para graficar otros modelos que esten definidos
#   por una ecuacion en diferencias (p ej, Rescorla-Wagner)
