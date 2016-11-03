#!/usr/bin/env python
import math                       #Biblioteca para operaciones matematicas como raiz cuadrada, logaritmos, etc.
import numpy                      #Biblioteca para operaciones matematicas complejas
import matplotlib.pyplot as plt   #Biblioteca para desplegar graficas basicas

#Se inicializa el arreglo de valores 'x'
#La funcion 'linspace' inicializa un arreglo con n puntos en un intervalo [a,b]
#El primer parametro es el limite inferios 'a'
#El segundo parametro es el limite superior 'b'
#El tercer parametro indica el numero de valores 'n' que tendra el arreglo
x = numpy.linspace(0, 1.0, 100)

#Se inicializa un arreglo 'y' como arreglo de puros ceros.
#El numero de ceros es igual al numero de elementos en 'x'
y = numpy.zeros(len(x))

#El siguiente ciclo asigna un valor en el arreglo 'y' para cada valor de 'x'
#de acuerdo con la ley de Stevens. En este caso, los valores de 'x' representan la magnitud fisica
#del estimulo, y los valores de 'y', la magnitud percibida
k = 1.0      #Constante de proporcionalidad
a = 1.2      #Exponente
for i in range(len(x)):
    y[i] = k * math.pow(x[i], a)


#Despliegue de la grafica
plt.plot(x, y)
plt.xlabel('Magnitud fisica del estimulo')
plt.ylabel('Magnitud percibida')
plt.title('Ley de Stevens')
plt.show()

########## E J E R C I C I O  ############
#1. Modificar la constante de proporcionalidad y observar los cambios en la grafica
#2. Modificar el intervalo de valores de 'x'. Probar con [0.0, 2.0], [0.0, 10.0] y [0.0, 0.5]
#3. En la pagina 'https://en.wikipedia.org/wiki/Stevens%27_power_law' se presenta una tabla con
#   valores del exponente para distintos fenomenos de percepcion.
#   Graficar los diferentes valores y observar los cambios en la grafica
