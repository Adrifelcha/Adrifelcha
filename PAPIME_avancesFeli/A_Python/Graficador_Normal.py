# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 19:17:41 2017

@author: Adriana
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:47:32 2016
@author: Adriana Felisa
"""

#########################################
#Cargamos las librerias necesarias
#########################################
from matplotlib.widgets import Slider   #Libreria para hacer Sliders
import matplotlib.pyplot as plt         #Libreria para hacer graficas
import numpy as np                      #Librería para hacer operaciones matematicas
import matplotlib.mlab as mlab	      #Libreria para personalizar graficas
import math			                  #Librería matematica
import scipy			            #Librería para hacer distribuciones de probabilidad
import scipy.stats			      #Librerias para hacer operaciones estadisticas

###########################################################
# Ajustamos el Output
###########################################################
fig, ax = plt.subplots()                       #Ampliamos nuestro espacio para generar dos areas independientes para la grafica principal y los sliders
plt.subplots_adjust(left=0.1, bottom=0.25)     #Especificamos la relación en el espacio entre dichas areas


###########################################################
#Definimos nuestra distribución
###########################################################
mu = 0               #La media de la distribucion
variance = 1         #Definimos una varianza de 1.
sigma = math.sqrt(variance)        #Calculamos la desviación estándar a partir de la varianza
x = np.arange(-6.0, 6.0, 0.01)     #Especificamos la longitud del soporte de las distribuciones (El Eje X)
i = 0    #Iniciamos el graficador con un valor en x cualquiera (lo ponemos en la media por conveniencia)

above = np.arange(i, 6.0, 0.01)      #El área de la curva por encima de i
below = np.arange(-6.0, i, 0.01)     #El área de la curva por debajo de i
 
dist_norm = ax.plot(x,mlab.normpdf(x, mu, sigma), 'black')      #Dibujamos la primer distribucion (Ruido)

ax.plot([i,i],[0,0.55], 'red')   #Dibujamos una línea vertical que indique dódne cae i

ax.fill_between(above, 0, (scipy.stats.norm(0,1).pdf(above)), facecolor='#CBECF4', alpha=0.5)     #Coloreamos las Falsas Alarmas
ax.fill_between(below, 0, scipy.stats.norm(0,1).pdf(below), facecolor='#741D97', alpha=0.5)         #Coloreamos los Rechazos Correctos
     
ax.plot([-3,3],[0.6,0.6], 'k', linewidth=1)      #Insertamos una línea horizontal en la parte superior de la grafica
ax.text(-2.3, 0.61, 'PDF', color='black', ha='center', va='bottom', fontsize=10, fontweight='bold')   #Escribimos los nombres de los cuatro posibles Outcomes a obtener, dependiendo la correspondencia entre la respuesta dada y la distribucion de origen del estimulo.
ax.text(0, 0.61, 'CDF', color='#741D97', ha='center', va='bottom', fontsize=10, fontweight='bold')   
ax.text(2.3, 0.61, 'Puntaje Z', color='red', ha='center', va='bottom', fontsize=10, fontweight='bold')   
ax.text(-2.3, 0.56, '(%.2f)' %scipy.stats.norm(0,1).pdf(i), color='black', ha='center', va='bottom', fontsize=10)     #Calculamos y escribimos cuál es el área bajo la curva que corresponde a los Rechazos
ax.text(0, 0.56, '(%.2f)' %scipy.stats.norm(0,1).cdf(i), color='#741D97', ha='center', va='bottom', fontsize=10)      #Especificamos el área bajo la curva que corresponde a las Omisiones
ax.text(2.3, 0.56, '(%.2f)' %scipy.stats.norm(0,1).ppf(scipy.stats.norm(0, 1).cdf(i)), color='red', ha='center', va='bottom', fontsize=10)  #Especificamos el área bajo la curva que corresponde a las Falsas Alarmas

ax.set_title('Distribucion Normal', fontsize=18, fontweight='bold')  #Añadimos un titulo a la grafica
ax.set_xlabel('Valores X')                                                      #Damos un nombre al eje de las abscisas
ax.set_ylabel('Probabilidad')                                                   #Damos un nombre al eje de las ordenadas
ax.axis([-4.0, 4.0, 0.0, 0.7])                                                  #Especificamos las dimensiones de la grafica principal: (rango en x, rango en y)
 
rect_i = plt.axes([0.10, 0.12, 0.80, 0.03], axisbg='white')                    #Dibujamos un rectangulo especificando sus coordenadas
slider_i = Slider(rect_i, 'Valor x', -3.0, 4.0, facecolor='white', valinit=i)      #Asignamos la funcionalidad de slider al rectángulo; especificamos los valores entre los que puede variar y asignamos como valor inicial el calculado al principio del codigo

def update(adri):          # Creamos una funcion para actualizar nuestra grafica 
    i_ = slider_i.val           #El criterio se va a obtener directamente del slider
    above = np.arange(i_, 6.0, 0.01)       #A partir de la ubicacion del slider, definimos cual es el espacio de ‘respuestas afirmatorias’
    below = np.arange(-6.0, i_, 0.01)       #y definimos el espacio de ‘respuestas negativas’ antes del slider
    ax.clear()                           #Limpiamos la grafica para poder dibujar sobre ella
    ax.plot(x,mlab.normpdf(x, mu, sigma), 'black')         #Volvemos a dibujar la distribucion de Ruido
    ax.plot([-3,3],[0.6,0.6], 'k', linewidth=1)        #Dibujamos la línea arriba de la grafica
    ax.text(-2.3, 0.61, 'PDF', color='black', ha='center', va='bottom', fontsize=10, fontweight='bold')   #Escribimos los nombres de los cuatro posibles Outcomes a obtener, dependiendo la correspondencia entre la respuesta dada y la distribucion de origen del estimulo.
    ax.text(0, 0.61, 'CDF', color='#741D97', ha='center', va='bottom', fontsize=10, fontweight='bold')   
    ax.text(2.3, 0.61, 'Puntaje Z', color='red', ha='center', va='bottom', fontsize=10, fontweight='bold')   
    ax.text(-2.3, 0.56, '(%.2f)' %scipy.stats.norm(0,1).pdf(i_), color='black', ha='center', va='bottom', fontsize=10)     #Calculamos y escribimos cuál es el área bajo la curva que corresponde a los Rechazos
    ax.text(0, 0.56, '(%.2f)' %scipy.stats.norm(0,1).cdf(i_), color='#741D97', ha='center', va='bottom', fontsize=10)      #Especificamos el área bajo la curva que corresponde a las Omisiones
    ax.text(2.3, 0.56, '(%.2f)' %scipy.stats.norm(0,1).ppf(scipy.stats.norm(0, 1).cdf(i_)), color='red', ha='center', va='bottom', fontsize=10)  #Especificamos el área bajo la curva que corresponde a las Falsas Alarmas
    ax.plot([i_,i_],[0,0.55], 'red') #Dibujamos el criterio
    ax.fill_between(above, 0, (scipy.stats.norm(0,1).pdf(above)), facecolor='#CBECF4', alpha=0.5)   #Coloreamos las falsas alarmas
    ax.fill_between(below, 0, scipy.stats.norm(0,1).pdf(below), facecolor='#741D97', alpha=0.5)       #Coloreamos los Rechazos correctos
    ax.axis([-4.0, 4.0, 0.0, 0.7])                            #Mantenemos las dimensiones de la grafica 
    ax.set_title('Distribucion Normal', fontsize=18, fontweight='bold') #Reiteramos el titulo
    ax.set_xlabel('Valores X')                                                      #Reiteramos el nombre del eje de las abscisas
    ax.set_ylabel('Probabilidad')                                                    #Reiteramos el nombre del eje de las ordenadas
slider_i.on_changed(update)                    #Llamamos la funcion de actualizacion por cada movimiento en el Slider 
plt.show() #Imprimimos la grafica

