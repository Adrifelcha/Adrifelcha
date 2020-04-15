#!/usr/bin/env python
import math                       #Biblioteca para operaciones matematicas como raiz cuadrada, logaritmos, etc.
import numpy                      #Biblioteca para operaciones matematicas complejas
import matplotlib.pyplot as plt   #Biblioteca para desplegar graficas basicas

#Se inicializa el arreglo de valores 'x'
#La funcion 'linspace' inicializa un arreglo con n puntos en un intervalo [a,b)
#El primer parametro es el limite inferior 'a'
#El segundo parametro es el limite superior 'b'
#El tercer parametro indica el numero de valores 'n' que tendra el arreglo
x = numpy.linspace(0.001, 5.0, 1000)

#Se inicializan tres arreglos para cada una de las funciones: potencia, exponencial y logaritimica.
#El numero de ceros es igual al numero de elementos en 'x'
pow_x = numpy.zeros(len(x))
exp_x = numpy.zeros(len(x))
log_x = numpy.zeros(len(x))

#El siguiente ciclo asigna un valor a cada uno de los arreglos para cada valor de 'x'
a1 = 1.0 #Potencia a la que se elevara cada valor de x
a2 = 1.0 #Constante que multplica al valor de x (exponente de e)
a3 = 1.0 #Constante que multplica al valor de x dentro del argumento del logaritmo
k1 = 1.0 #Constante de proporcionalidad para la funcion de potencia
k2 = 1.0 #Constante de proporcionalidad para la funcion exponencial
k3 = 1.0 #Constante de proporcionalidad para la funcion logaritmica
for i in range(len(x)):
    pow_x[i] = k1*math.pow(x[i], a1)     #Calcula k*(x^a)
    exp_x[i] = k2*math.exp(a2*x[i])      #Calcula k*exp(ax)
    if x[i] > 0:                       #Calcula el logaritmo natural de x: k*ln(ax)
        log_x[i] = k3*math.log(a3*x[i])  #Es importante notar que el logaritmo natural solo esta definido
    else:                              #para valores estrictamente mayores que cero
        log_x[i] = 0

#Despliegue de la grafica
fig,sub = plt.subplots()
plt.plot(x, pow_x, label='Potencia')
plt.plot(x, exp_x, label='Exponencial')
plt.plot(x, log_x, label='Logaritmica')
plt.xlim(0, 5.0) #Estas lineas fijan los limites maximo y minimo de los ejes
plt.ylim(0, 5.0) #Estas lineas fijan los limites maximo y minimo de los ejes
plt.xlabel('Valor de la variable independiente')
plt.ylabel('Valor de la funcion')
plt.title('Funciones de potencia, exponencial y logaritmica')
plt.legend(loc='lower right')
plt.show()

########## E J E R C I C I O  ############
#1. Modificar las constantes de proporcionalidad y discutir los cambios cuando dicha constante es negativa,
#   cuando tiene valores entre cero y uno, y cuando es mayor que uno.
#2. Modificar las constantes 'a' y observar que sucede con las funciones para valores negativos,
#   entre cero y uno, y mayores que uno.
#3. Modificar el dominio de la funcion y observar que sucede con valores negativos, entre cero y uno, y mayores que uno
#4. Modificar el dominio, las constantes 'a' y 'k' y los limites de los ejes para obtener graficas similares
#   a las que se muestran en la fig 1.1 capitulo 1, del Handbook of Computational and Mathematical Psychology


