# -*- coding: utf-8 -*-
"""
Autor: Uriel O. Gonzalez Bravo
Curso: 'Un laboratorio virtual en Python para modelos del comportamiento'
	 Introducción a python.
		
"""
""" /////////////////////   STRINGS    /////////////////////// """


#%%
""" Variables y sus asignaciones"""
print("Hello python world") #Utilizando la función print()
#%%
message="Hello python world" #Asignemos la cadena a message
print(message) 

#%%
"""Strings"""
name="uriel gonzalez"
print(name.title()) #Pone en mayúsculas el inicio de cada palabra en una cadena
print(name.upper()) #Pone en mayúsculas a toda la cadena
print(name.lower()) #Pone en minúsculas a toda la cadena
print(name.capitalize()) #Pone en mayúscula solo la primera letra de la cadena
    
#%%
#Imaginemos que queremos guardar el apeido y el nombre en variables separadas
first_name="uriel"
last_name="gonzalez"
full_name = first_name+" "+last_name
print(full_name)
print("Hello, "+ full_name.title()+"!")

#%%
"""Removiendo los espacios en blanco"""
#Sobre todo sirve cuando queremos comparar que dos variables contengan lo mismo.
favorite_language= " python "
favorite_language
#%%
favorite_language.rstrip()  #rstrip elimina los espacios en blanco de la derecha
#%%
favorite_language=" python "
favorite_language=favorite_language.rsplit()
favorite_language
#%%
favorite_language= " python "
favorite_language.lstrip() #Quita los espacios de la izquierda
favorite_language.rstrip() #Quita los espacios de la derecha
favorite_language.strip() #Quita todos los espacios del extremo

#%%
""" ///////////////////   NUMEROS   ////////////////////////"""

#Enteros
2+2 #Suma
5-2 #Resta
2-5 #Resta

3*2 #Multiplicación
3**2 #Exponenciación
# Para la exponenciación no hay que utilizar NUNCA ^

5/3 #???? #Algunos detalles de python 2.7 

#Flotantes 
5/3.0
5.0/3
5.0/3.0

#Los flotantes son como la gripe, se contagian
(5/3)*2.0
(5/3.0)*2

#Ahora asignemos un número a una variable
edad = 22
 #Dará error
print("El promedio de edad de la gente que toma el curso es "+edad+" años")
#Correcto
print("El promedio de edad de la gente que toma el curso es "+str(edad)+" años")

#Ahora sumemos variables que representan números
a=5
a-3
a+a

a=10
b=2
a+b

a=2
b=a

print(9-1)
print(4+4)
print(2**3)
print(16/2)
dia=15
print("Mi cumpleaños es el"+" " +str(dia)+" "+"de enero.")

#%%
""" /////////////////////////  BOOLEANOS  /////////////////   """
a=1
b=1

a == b  #Aqui preguntamos si a es igual a b

a=1
b=2
a == b
a != b

#########
a = True
b = False
c = True

"""con "and" hacemos una comparación de valores que resultará en True
solamente cuando ambos elementos a comparar son True"""
a&b
a and b
a&c 
a and c

""" con "or" hacemos una comparación de valores que resultará en True en 
tanto uno de los elementos sea True o ambos sean True"""
a|b
a or b

#### Veamos porque ^ no se utiliza en exponenciación
a = True
b = False
c = True
""" con "^" hacemos una comparación de valores que resultará en True en 
tanto uno de los elementos sea True pero si ambos son True la comparacion
será False"""
a^b
a^c

#%%
"""    //////////////////// LISTAS  //////////// """
numeros = ["uno","dos","tres","cuatro","cinco"]
print(numeros)
print(numeros[0]) #Accediendo al primer elemento de la lista
print(numeros[2]) #Accediendo al tercer elemente de la lista
print(numeros[-1]) #Accediendo al último elemento de la lista
print(numeros[-2]) #De atrás para adelante
print(numeros[0:3]) #Extrayendo el primer elemento al que ocupa el tercer index sin incluirlo


#%%
meses = ["enero","febrero","marzo","abril","mayo","junio"]
message = "Mi cumpleaños es el " +str(15)+" de " + meses[0].title()+"."
print(message)

#%%
meses=["enero","febrero","marzo","abril","mayo","junio"]
print(meses)
meses[0]="julio"
print(meses) #Reempazamos el primer valor de la lista por "julio"
#%%
meses=["enero","febrero","marzo","abril","mayo","junio"]
meses.append("julio")
print(meses)
#%%
numeros = ["dos","tres","cuatro","cinco"]
numeros.append("uno")
print(numeros)
#%%
numeros = ["dos","tres","cuatro","cinco"]
numeros.insert(0,"uno")
print(numeros)
#%%
numeros = ["uno","dos","tres","cuatro","cinco"]
del numeros[0]
print(numeros)
#%%
#Imaginemos que compramos unas motocicletas
motocicletas = ["honda","yamaha","suzuki"]
first = motocicletas.pop()
print("Mi primer motocicleta fue una "+first.title()+".")
print(motocicletas)
#%%
motocicletas = ["honda","yamaha","ducati","suzuki"]
second = motocicletas.pop(1)
print("Mi segunda motocicleta fue una "+second.title()+".")
print(motocicletas)
#%%
#Que pasa cuando no sabemos el indice pero si lo que queremos borrar
motocicletas = ["honda","yamaha","ducati","suzuki"]
print(motocicletas)
motocicletas.remove("yahama")
print(motocicletas)
#%%
motocicletas = ["honda","yamaha","ducati","suzuki"]
too_expensive="YAMAHA".lower()
print(too_expensive)
motocicletas.remove(too_expensive)
print("La moto mas cara es una "+too_expensive.title()+".")
print(motocicletas)
#%%
#¿Qué hacer cuando queremos trabajar de igual manera con cada elemento de una lista?
#Print cada elemento de la lista
magos=["alice","david","carolina"]
for mago in magos: #Primero el nombre de la nueva variable y después el de la lista
    print(mago.title())
"""Primero creamos una lista (magicians), después hacemos un ciclo for donde tomamos un elemento de la lista magicians para almacenarla
en la variable magician y luego pedimos imprimirla. Esto lo hace con cada elemento de la lista"""
#%%
#Hagamos un poco más
magos=["alice","david","carolina"]
for mago in magos:
    print(mago.title()+", ese fue un gran truco!")
    print("No puedo esperar a ver el proximo, "+mago.title()+".\n")
#%% 
#Haciendo algo después del loop, por ejemplo un mensaje cuando los mensajes del loop hayan aparecido completos
magos=["alice","david","carolina"]
for mago in magos:
    print(mago.title()+", ese fue un gran truco!")
    print("No puedo esperar a ver el proximo, "+mago.title()+".\n")
print("Gracias a todos! Ese fue un gran show!")
#%%
"""PERO COMO NOSOTROS TRABAJAREMOS CON NUMEROS"""
#Ahora trabajando con una lista numérica
for value in range(1,6):
    print(value)
#%%
#Convirtamos el rango directamente a una lista
numbers=list(range(1,6))
print(numbers)
#%%
even_numbers=list(range(2,11,2)) #range(inicio,final,de dos en dos)
print(even_numbers)
#%%
#Hagamos un ciclo for para la lista del 1 al 10 elevado al cuadrado
#Primera versión
for value in range(1,11):
    value=value**2
    print(value)
#%%
#Version mejorada
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
#%%
#Ahora hagámoslo más preciso
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
#%%
#List Comprehensions (generando todo en una sola línea)
squares=[value**2 for value in range(1,11)]
print(squares)
"""Expliquémoslo un poco. Se inicia con un nombre descriptivo de la lista (squares). En seguida
abrimos los corchetes cuadrados y definimos la expresión que queremos guardar en nuestra nueva lista. 
En este ejemplo fue que elevemos al cuadrado cada elemento value que es tomado del rango del 1 al 10. Notar que
no se usaron los dos puntos para la función"""

#%%
""" ///// UTILIZANDO NUMPY   ///////"""
a = [1,2,3]
a+1 #Nos dará error todo esto
a-1
a*2
a**2
#%%
#podriamos hacer esto
a = [1,2,3]
a[0]+1
#Para trabajar con listas como si fueran vectores necesitaremos de una libreria Numpy
#%% 
#Pero esto es mejor
import numpy
a = [1,2,3,4,5]
b = numpy.array(a)
b+1 
b*2
b**2
#%%
player=["charles","martina","michael","florence","eli"]
print(player[1:4])
print(player[:4])
print(player[2:])
print(player[-3:])
#%%
players=["charles","martina","michael","florence","eli"]
print("Here are the first three players on my team:")
for player in players[:3]:
    print("\t"+player.title())
#%%
cars=["audi","bmw","subaru","toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
#%%
answer=17
if answer != 42:
    print("That is not the correct answer. Please try again!")
#%%
#La forma más simple del if
"""if conditional_test:
    do something
    """
age=19
if age>=18:
    print("Bien, usted puede votar")
    print("¿Ya se ha registrado?")
#%%
"""IF, ELSE Statements"""
#Sirve cuando queremos realizar una acción en un caso particular pero otra en todos los demás casos
age=17
if age>=18:
    print("Bien, usted puede votar")
    print("¿Ya se ha registrado?")
else:
    print("Lo siento, no puede votar:")
    print("Por favor, regístrese en cuanto tenga 18")
#%%
"""La cadena If, elif, else"""
#Cuando queremos evaluar más de una sola situación.
#Veamos un ejemplo donde el precio de la entrada varía en función de la edad
age=20
if age<4:
    print("Su presicio de admision es de $0")
elif age<18:
    print("Su presicio de admision es de $5")
else:
    print("Su presicio de admision es de $10")
#%%
#Otra forma de poner lo de arriba
age=20

if age<4:
    price=0
elif age<18:
    price=5
else:
    price=10
print("Su precio de admision es de $"+str(price)+".")
#%%
#También se puede omitir el bloque else
age=64
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=11
elif age>=65:
    price=70 
print("Su precio de admision es $"+str(price)+".")
#%%
#Imaginemos a un alien le acaban de disparar en nuestro juego. 
#Hay que crear una variable para asignarle el color
alien_color="green"
if alien_color=="green":
    print("Haz ganado 5 puntos")
else:
    print("Lo siento, estuviste cerca")
 
#%%
alien_color="red"
if alien_color=="green":
    print("Haz ganado 5 puntos")
elif alien_color=="yellow":
    print("Haz ganado 3 puntos")
else:
    print("Haz ganado un punto")
#%%
alien_color="red"
if alien_color=="green":
    print("haz ganado 5 puntos")
if alien_color=="red":
    print("haz ganado 1 punto")
#%%
"""           FUNCIONES    """
def saludo_usuario():
    """Mostrando un saludo"""
    print("Hola!")
saludo_usuario()
#%%
def saludo_usuario(usuario):
    print("Hola, "+usuario.title()+"!")
    
saludo_usuario("uriel")

#%%
def describe_mascota(animal_tipo,nombre_mascota):
    print("\nYo tengo un "+animal_tipo+ ", su nombre es "+nombre_mascota.title())
    
describe_mascota("perro","Maia")
describe_mascota("Maia","perro")
describe_mascota(nombre_mascota="maia",animal_tipo="perro")
#%%
"""Default arguments"""
def describe_mascota(animal_tipo,nombre_mascota="maia"):
    print("\nYo tengo un "+animal_tipo+ ", su nombre es "+nombre_mascota.title())

describe_mascota("raton")
#%%
#%%
def make_shirt(size,text):
    print("Quiero una playera tamaño "+size)
    print("El texto debe de decir "+'"'+text.capitalize()+'".')
 
make_shirt("grande","Cool Life")
#%%
def make_shirt(size,text="I love python"):
    print("\nQuiero una playera tamaño "+size)
    print("El texto debe de decir "+'"'+text.capitalize()+'".')
 
make_shirt(size="grande")
make_shirt("mediana")
make_shirt("chica")
#%%
#Regresando argumentos
def nombre_completo(first_name,last_name):
    """Regresando el nombre completo en una bonita forma"""
    full_name = first_name+" "+last_name
    return full_name.title()

musicos = nombre_completo("jimmy","hendrix")
print(musicos)
#%%
def make_album(artist,album,tracks=""):
    if tracks:
        album="artista: "+artist.title()+", album: "+album.title()+", tracks: "+str(tracks)
    else:
        album="artista: "+artist.title()+", album: "+album.title()
    return album
 
music=make_album("shakira","piesdes",12)
print(music)
music=make_album("shakira","pies")
print(music)
#%%
magicians=["uriel","felisa","nino"]
def show_magicians(magics):
    print("Estos son los magos: ")
    for magic in magics:
        print(magic.title())
 
show_magicians(magicians)
#%%
magicians=["uriel","felisa","nino"]
def show_magicians(magics):
    print("Estos son los magos: ")
    for magic in magics:
        print(magic.title())
 
show_magicians(magicians)
#%%
magicians=["uriel","felisa","nino"]
def make_great(magics):
    print("\n")
    for magic in magics:
        if magic == "felisa":
            print("La gran "+magic.title()+" en persona!")
        else:
            print("El gran "+magic.title()+" en persona!")
         
make_great(magicians[:])

#%%
"""                          PLOTS                   """
import matplotlib.pyplot as plt
squares = [1,4,9,16,25]
plt.plot(squares)
plt.show()

#%%
import matplotlib.pyplot as plt
squares = [1,4,9,16,25]
plt.plot(squares,linewidth=5)
#Agregando ejes
plt.title("Numeros al cuadrado",fontsize=24)
plt.xlabel("Valor",fontsize=14)
plt.ylabel("Valor al cuadrado",fontsize=14)
#Estableciendo detalles de las etiquetas
plt.tick_params(axis="both",labelsize=14)
plt.show()
#%%
#Corrigiendo lo de arriba
import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)
#Agregando ejes
plt.title("Numeros al cuadrado",fontsize=24)
plt.xlabel("Valor",fontsize=14)
plt.ylabel("Valor al cuadrado",fontsize=14)
#Estableciendo detalles de las etiquetas
plt.tick_params(axis="both",labelsize=14)
plt.show()
#%%
#Hagamos scatterplot
import matplotlib.pyplot as plt
plt.scatter(2,4)
plt.show()
#%%
import matplotlib.pyplot as plt
plt.scatter(2,4,s=200)
#Estableciendo titulo y ejes
plt.title("Numeros al cuadrado",fontsize=24)
plt.xlabel("Valor",fontsize=14)
plt.ylabel("Valor al cuadrado",fontsize=14)
#Estableciendo detalles de las etiquetas
plt.tick_params(axis="both",labelsize=14)
plt.show()
#%%
import matplotlib.pyplot as plt
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values,y_values,s=100)
#Estableciendo titulo y ejes
plt.title("Numeros al cuadrado",fontsize=24)
plt.xlabel("Valor",fontsize=14)
plt.ylabel("Valor al cuadrado",fontsize=14)
#Estableciendo detalles de las etiquetas
plt.tick_params(axis="both",labelsize=14)
plt.show()

#%%
"""Calculando datos automaticamente"""
import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s=40)
#Estableciendo titulo y ejes
plt.title("Numeros al cuadrado",fontsize=24)
plt.xlabel("Valor",fontsize=14)
plt.ylabel("Valor al cuadrado",fontsize=14)
#Estableciendo el rango de nuestros ejes
plt.axis([0,1100,0,1100000])
plt.show()

#%%
#Haciendo todo super cool
import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s=40,c="red",edgecolor="none")
#Estableciendo titulo y ejes
plt.title("Numeros al cuadrado",fontsize=24)
plt.xlabel("Valor",fontsize=14)
plt.ylabel("Valor al cuadrado",fontsize=14)
#Estableciendo el rango de nuestros ejes
plt.axis([0,1100,0,1100000])
plt.show()

#%%
import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s=40,c=y_values,cmap=plt.cm.Blues,
            edgecolor="none")
#Estableciendo titulo y ejes
plt.title("Numeros al cuadrado",fontsize=24)
plt.xlabel("Valor",fontsize=14)
plt.ylabel("Valor al cuadrado",fontsize=14)
#Estableciendo el rango de nuestros ejes
plt.axis([0,1100,0,1100000])
plt.show()
#%%
import numpy
numpy.random.rand() #Generamos numeros aleatorios
numpy.random.rand()
#%%
noise = numpy.random.rand(5,5)
print(noise)
noise.shape
#%%
import numpy
from matplotlib import pyplot

noise = numpy.random.rand(500,500,3)
pyplot.imshow(noise)
pyplot.show()
#%%
#Zen of python
import this