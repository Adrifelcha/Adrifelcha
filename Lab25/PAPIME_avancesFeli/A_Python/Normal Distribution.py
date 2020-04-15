# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:49:07 2016

@author: Adriana :P
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
import scipy.stats
#from scipy.stats import norm

#Dibujando una distribucion normal
mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(-6, 6, 100)
plt.plot(x,mlab.normpdf(x, mu, sigma))

plt.show()

scipy.stats.norm(0, 1)

#Obtener valores pdf y cdf para una normal
#A) Definimos los valores p y p acumulados como variables que despues imprimimos
scipy.stats.norm(0, 1)
p_values = scipy.stats.norm(0, 1).pdf(0)
print(p_values)
cumulative_p = scipy.stats.norm(0, 1).cdf(0)
print(cumulative_p)
quantile_position = scipy.stats.norm(0,1).ppf(0.5)
print(quantile_position)
#Podemos imprimir directamente el valor p y p acumulado
print(scipy.stats.norm(0, 1).pdf(2))
print(scipy.stats.norm(0, 1).cdf(2))
print(scipy.stats.norm(0,1).ppf(scipy.stats.norm(0, 1).cdf(2)))
print(scipy.stats.norm(0,1).ppf(0.9772498))

