from matplotlib.pylab import hist, show  #Importar la propiedad de histograma y mostrar, desde la libreria matplotlib
import matplotlib.pyplot as plt
import numpy #Libreria para matematicas (numeros) en Python
import random 

edgar = range(1,101)

adri =[]
for i in range(1000):
    adri.append(random.choice(edgar))

#hist(marco, 100, (0,101)) 
#plt.xlabel('Lo que sea')
#plt.ylabel('Hola')
#plt.title('Edgar')
#show

#El primer argumento, son los datos
#El segundo, es la cantidad de vlores diferentes

A = 0.78
NoA = 1-A

prob =[A,NoA]
plt.bar(1,prob[0],facecolor='#9999FF')
plt.bar(2,prob[1],facecolor='#4846FF')
plt.text(1.3,prob[0]+0.05,prob[0], ha='center', va='bottom')
plt.text(2.3, prob[1]+0.05, prob[1], ha='center',va='bottom')
plt.xlabel('Lo que sea')
plt.ylabel('Hola')
plt.title('Edgar')
plt.ylim(0,2)
plt.xlim(0,3)

show()
