# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 12:44:49 2017

@author: Cursos
"""

import math
import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider
import numpy

fig, ax=plt.subplots()
plt.subplots_adjust(left=0.15,bottom=0.25)

estimulo = numpy.linspace(0, 2.0, 100)
sensacion = numpy.zeros(len(estimulo))

k = 2.5 #constante de proporcionalidad
a = 1.2 #exponente

for i in range(len(estimulo)):
  sensacion[1] = k * math.pow(estimulo[i], a)
  
ax.plot(estimulo, sensacion,linewidth=2)
ax.axis([0,1,0,1.5])
ax.set_xlabel('Magnitud fisica del estimulo')
ax.set_ylabel('Magnitud percibida')
ax.set_title('Ley de Stevens', fontsize=25, fontweight='bold')

ax.text(0.18, 1.3, r'$\psi = k  \phi^a$', ha='center', va='bottom', fontsize=20)
ax.text(0.18, 1.25, 'a = %.2f' %a, ha='center', color='#0C2DC2', va='bottom', fontsize=8)

ax_a=plt.axes([0.15,0.1,0.56,0.03], axisbg='#9BA3C7')
slider_a=Slider (ax_a, "a",.70,2.5,facecolor='#0C2DC2',valinit=a)
plt.text(1,-1.35, 'k= %.1f' %k, fontsize=8)

def update(var):
  a = slider_a.val
  for i in range(len(estimulo)):
    sensacion[i] = k * math.pow(estimulo[i], a)
  ax.clear()
  ax.plot(estimulo,sensacion,linewidth=2)
  ax.axis([0,1,0,1.5])
  ax.set_xlabel('Magnitud fisica del estimulo')
  ax.set_ylabel('Magnitud percibida')
  ax.set_title('Ley de Stevens', fontsize=25, fontweight='bold')
  ax.text(0.18, 1.3, r'$\psi = k  \phi^a$', ha='center', va='bottom', fontsize=20)
  ax.text(0.18, 1.25, 'a = %.2f' %a, ha='center', color='#0C2DC2', va='bottom', fontsize=8)
  
slider_a.on_changed(update)

plt.show()