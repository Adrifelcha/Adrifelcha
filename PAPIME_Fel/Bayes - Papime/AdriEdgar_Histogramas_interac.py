####
###   Codigo hecho por Adriana Feliza
###

from matplotlib.widgets import Slider, Button  #Importar la propiedad de histograma y mostrar, desde la libreria matplotlib
import matplotlib.pyplot as plt
import numpy #Libreria para matematicas (numeros) en Python
import random 


A = 0.5
NoA = 1-A
prob =[A,NoA]


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.25)

b1 = ax.bar(0.6, prob[0], facecolor='#9999FF')
b2 = ax.bar(1.6, prob[1], facecolor='#4846FF')

ax.text(1.0, prob[0]+0.05, '%.4f' %prob[0], ha='center', va='bottom')
ax.text(2.0, prob[1]+0.05, '%.4f' %prob[1], ha='center', va='bottom')

labels = ['Evento A','Evento B']
ax.set_xticks([1, 2], labels)

ax.set_title('Probabilidad Posterior')
ax.set_xlabel('Escenarios Posibles')
ax.set_ylabel('Probabilidad')

ax.axis([0.0, 3.0, 0.0, 1.5])

ax_probA = plt.axes([0.15, 0.1, 0.65, 0.03], axisbg='lightgoldenrodyellow')
s_prob = Slider(ax_probA, 'Prior(A)', 0.01, 1.0, valinit=A)

def update(var):
	prob[0] = s_prob.val
	prob[1] = 1-prob[0]
	ax.clear()
	ax.bar(0.6, prob[0], facecolor='#9999FF')
	ax.bar(1.6, prob[1], facecolor='#4846FF')
	ax.text(1.0, prob[0]+0.05, '%.4f' %prob[0], ha='center', va='bottom')
	ax.text(2.0, prob[1]+0.05, '%.4f' %prob[1], ha='center', va='bottom')
	ax.axis([0.0, 3.0, 0.0, 1.5])
	ax.set_xticks([1, 2], labels)
	ax.set_title('Edgar')
	ax.set_xlabel('Lo que sea')
	ax.set_ylabel('Hola')
s_prob.on_changed(update)

plt.show()
