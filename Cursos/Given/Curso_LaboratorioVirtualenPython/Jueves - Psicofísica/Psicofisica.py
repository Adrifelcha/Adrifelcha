# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 10:14:16 2017

@author: Cursos
"""

import numpy #operaciones matematicas complejas
import matplotlib.pyplot as plt #graficas basicas
from matplotlib.widgets import Slider


"""cuantas veces presentamos el estimulo y cuantas veces el sujeto responde al estimulo"""

ensayos = 60
estimulo = numpy.linspace (0, ensayos, ensayos)
valor_ud = numpy.zeros(len(estimulo)) #len dice longitud

"""parametros de la ley de weber"""

k=1
c=[k]*ensayos #constante de Weber repitela cuantas veces ensayos haya
S0 = 10 #umbral debajo del cual el estimulo es percibido

"""plots"""
fig, ax = plt.subplots(2)
plt.subplots_adjust(left=0.15, bottom=0.25)

ax_k=plt.axes([0.15,0.1,0.65,0.03], axisbg='lightgoldenrodyellow')
slider_k=Slider(ax_k, 'k',.5,1.5,valinit=k)

for i in range(len(estimulo)):
  if estimulo[i] <= S0:
    valor_ud[i] = 0
  else: 
    valor_ud[i] = S0 + k*estimulo[i-S0]
    
def update (var):
  k = slider_k.val 
  c=[k]*ensayos
  for i in range(len(estimulo)):
    if estimulo[i] <=S0:
      valor_ud[i]=0
    else:
      valor_ud[i] = S0 + k*estimulo[i-S0]

  ax[0].clear()
  ax[0].plot(estimulo, valor_ud, 'ro')
  ax[0].set_ylabel ('Umbral diferencial')
  ax[0].set_title('Ley de Weber')
  ax[0].axis([0,ensayos,0,60])
  
  ax[1].clear()
  ax[1].plot(estimulo, c, 'ro')
  ax[1].set_xlabel ('Intensidad del estimulo')
  ax[1].set_ylabel ('Fraccion de Weber')
  ax[1].axis ([10, ensayos, 0.0,2])
  
"""desplegamos la grafica"""

ax[0].plot(estimulo, valor_ud, 'ro')
ax[0].axis([0,ensayos,0,60])
ax[0].set_ylabel ('Umbral diferencial')
ax[0].set_title('Ley de Weber')

ax[1].plot(estimulo, c, 'ro')
ax[1].axis ([10, ensayos, 0.0,2])
ax[1].set_xlabel ('Intensidad del estimulo')
ax[1].set_ylabel ('Fraccion de Weber')

slider_k.on_changed(update)

plt.show()


      
  
      
    
  