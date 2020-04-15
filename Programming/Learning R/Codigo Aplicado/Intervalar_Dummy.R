#########################
# Para pasar una Variable Intervalar a Dummies
# por Adri ;)
##########################

rm(list=ls())   #Siempre es útil comenzar todo código con esta línea, porque borra todos los valores y variables que pudieras estar arrastrando de códigos ejecutados anteriormente

#Empezamos con una varibale intervalar
# Con fines ilustrativos, vamos a crear una variable intervalar formada por 20 números extraídos 
#aleatoriamente de una distribución normal con media en 50 y desviación estándar de 12
v_intervalar <- rnorm(20,50,12)   
print(v_intervalar) #Revisamos el contenido de nuestra variable


########## HAy muchas formas de transformar esta Variable en una Dummy, (es lo bello de la programación)
# a continuación te presento algunos ejemplillos

############################
##### FORMA 1:
##### Con un ciclo For que vaya trabajando, uno a uno, con cada elemento contenido en tu variable intervalar
### (La Forma 2 es más fácil, práctica y bonita, pero siempre es útil tener claridad sobre cómo funcionan los if y los for) 
############################

#Creamos una variable vacía, que vamos a llenar a partir de cada elemento de la variable intervalar
Dummy <- NULL
print(Dummy)

#Y llenamos nuestra dummy con un ciclo for
for(i in 1:length(v_intervalar)){    #por cada elemento "i" contenido en el intervalo del 1 al número de elementos contenidos en v_intervalar
  if(v_intervalar[i]<=40){          #va a evaluar si el elemento contenido en la posición "i" es igual o menor a 40
    Dummy[i] <- 1                    #Si sí, en esa misma posición "i" va a colocar un 1 en nuestra variable Dummy
  }else{                             #Si no
    Dummy[i] <- 0                    #Va a colocar un 0 en la posición "i" de la varibale Dummy
  }}  #Se termina el condicional y el ciclo for

print(Dummy) #Revisamos el contenido de la variable Dummy

Comparacion <-cbind(v_intervalar,Dummy)    #Con fines ilustrativos, mezclamos como columnas la variable original y su dummy
print(Comparacion)    #y las imprimimos, para poder compararlas momento a momento.

###############################
####### FORMA 2:
####### Aplicando una sola operación a toda la variable
################################
dummy <- ifelse(v_intervalar <= 40, "1", "0")      #Directamente creamos una variable donde se va a sobreescribir cada valor contenido en la v_intervalar, según si cumplen la regla o no
print(dummy)

Comparacion2 <-cbind(v_intervalar,Dummy,dummy)
print(Comparacion2)
