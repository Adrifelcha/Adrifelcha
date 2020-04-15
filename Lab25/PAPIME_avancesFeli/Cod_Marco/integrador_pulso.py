#Librerias necesarias para crear ventanas y graficas a la vez
import matplotlib
import math
import numpy
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from Tkinter import *
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import Tkinter as tk
import ttk


LARGE_FONT = ("Verdana", 14) 



root = Tk()
var = DoubleVar()

f = Figure(figsize=(5,5), dpi=100)
graph = f.add_subplot(111)


### FUNCION MATEMATICA
a = 0.1

x = [0]*50
y = [0]*50
V_ant = 0
y_max = 0.0
R = 1
x[0] = 0.0
y[0] = 0.0
for i in range(1,50):
    x[i] = i
    y[i] = a*V_ant + (1-a)*R

    V_ant = y[i]

    if i < 20:
        R = 1
    else: 
        R = 0
 
    
    if y[i] < 0:
        y[i] = 0
    
    print "R: " + str(R) + " - " + " y: "+ str(y[i]) + " a: " + str(a) + " V_ant: " + str(V_ant)


graph.clear()
graph.plot(x,y)

label = tk.Label(root, text="Ventana temporal (Estimulo unico)", font=LARGE_FONT)
label.pack(pady=10,padx=10)

canvas = FigureCanvasTkAgg(f, root)
canvas.show()
canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

label = tk.Label(root, text="a = 0.1", font=LARGE_FONT)
label.pack(pady=10,padx=10)

scale = Scale( root, from_=0, to=1, orient="horizontal", variable = var )
scale.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()