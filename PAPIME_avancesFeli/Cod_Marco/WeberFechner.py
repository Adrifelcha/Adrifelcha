#!/usr/bin/env python
import math                       #Biblioteca para operaciones matematicas como raiz cuadrada, logaritmos, etc.
import numpy                      #Biblioteca para operaciones matematicas complejas
import matplotlib.pyplot as plt   #Biblioteca para desplegar graficas basicas

#Se inicializa el arreglo de valores 'x'
#La funcion 'linspace' inicializa un arreglo con n puntos en un intervalo [a,b]
#El primer parametro es el limite inferior 'a'
#El segundo parametro es el limite superior 'b'
#El tercer parametro indica el numero de valores 'n' que tendra el arreglo
x = numpy.linspace(0.01, 1.0, 100)

#Se inicializa un arreglo 'y' como arreglo de puros ceros.
#El numero de ceros es igual al numero de elementos en 'x'
y = numpy.zeros(len(x))

#El siguiente ciclo asigna un valor en el arreglo 'y' para cada valor de 'x'
#de acuerdo con la ley de Weber-Fechner. En este caso, los valores de 'x' representan la magnitud fisica
#del estimulo, y los valores de 'y', la magnitud percibida
k  = 1.0      #Constante de proporcionalidad
S0 = 0.2      #Umbral debajo del cual el estimulo no es percibido
for i in range(len(x)):
    y[i] = k * math.log(x[i]/S0)
    if x[i] < S0:
        y[i] = 0


#Despliegue de la grafica
plt.plot(x, y)
plt.xlabel('Magnitud fisica del estimulo')
plt.ylabel('Magnitud percibida')
plt.title('Ley de Weber-Fechner')
plt.show()

########## E J E R C I C I O S ############
#1. Modificar la constante de proporcionalidad y observar los cambios en la grafica
#2. Modificar el valor de S0 y observar que pasa con la grafica.
#3. Comentar las lineas 24 y 25 de este codigo, observar que pasa con la grafica y discutir
#   Por que no tienen sentido los valores de 'x' menores que 'S0'?