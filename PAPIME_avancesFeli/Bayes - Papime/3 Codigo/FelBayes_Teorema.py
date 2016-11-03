# -*- coding: utf-8 -*-
"""
Created on Mon Oct 03 11:40:34 2016

@author: Felisa
"""
#Cargamos las librerias necesarias 
import matplotlib.pyplot as plt #Importamos la propiedad de gráficos desde la libreria matplotlib

#Definimos dos eventos posibles, mutuamente excluyentes.
Evento_A = 'A'
Evento_B = 'No A'
#Y los situamos dentro de un arreglo
Eventos_Posibles = [Evento_A,Evento_B]

#Definimos las Priors
Prior_A = 0.5 
Prior_B = 1-Prior_A #Tratandose de eventos excluyentes, sus probabilidades deben ser necesariamente complementarias

#Especificamos la Verosimilitud que relaciona los datos con cada escenario posible
Verosimilitud_A = 0.8 #Asumiendo que A es cierto, cual es la probabilidad de observar los datos
Verosimilitud_B = 0.3 #Asumiendo que A NO es cierto, cual es la probabilidad de observar los datos

#Calculamos la verosimilitud marginal
#Escribimos tal cual la ecuacion que define la verosimilitud marginal como la sumaatoria de los productos 
#de las prior y verosimilitudes de los distintos escenarios posibles
verosimilitud_marg = (((Prior_A)*(Verosimilitud_A))+((Prior_B)*(Verosimilitud_B)))

#Aplicamos la Regla de Bayes
#Escribimos la ecuacion sustituyendo cada termino por las variables previamente identificadas
Posterior_A = ((Prior_A)*(Verosimilitud_A))/verosimilitud_marg
Posterior_B = ((Prior_B)*(Verosimilitud_B))/verosimilitud_marg

#Obtenemos una representacion grafica de nuestros resultados posteriores
probabilidades =[Posterior_A,Posterior_B] #Creamos un arreglo que contenga las Posteriores computadas
plt.bar(0.6,probabilidades[0],facecolor='#A810CE') #dibujamos la barra correspondiente a la probabilidad posterior de A
plt.bar(1.6,probabilidades[1],facecolor='#DEAFE9')#Dibujamos la barra correspondiente a No A
plt.text(1,probabilidades[0]+0.05,'%.4f' %probabilidades[0], ha='center', va='bottom') #Escribimos el valor de la primer posterior
plt.text(2, probabilidades[1]+0.05, '%.4f' %probabilidades[1], ha='center',va='bottom') # Escribimos el valor de la segunda posterior
plt.xlabel('Escenarios posibles')
plt.ylabel('Probabilidad')
plt.title('Probabilidades Posteriores')
plt.ylim(0,1)
plt.xlim(0,3)
plt.xticks([1,2], Eventos_Posibles)
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
show()

