###################################################
# Teo�a de las muestras grandes
# por Adriana F. Chávez
# adrifelcha@gmail.com
###################################################

#La teor��a de las muestras grandes est� compuesta por la Ley de los Grandes N�meros y 
#el Teorema del L�mite Central. Segun los cuales: 
#a) El valor de la media muestral se aproxima al valor de la media poblacional conforme n se acerca al infinito
#b) Los estimadores obtenidos en N muestras, presentan valores que se distribuyen normalmente cuando N tiende a infinito.



#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
# PARTE UNO: Ley de los grandes N�meros



# Distribuci�n  N O R M A L
####################################
####################################

#Generamos tres muestras aleatorias [ rnorm() ] con distinto tamaño de muestra (primer argumento), pero con la misma media (0) y desviación (1)
n_peque <- rnorm(5,0,1)  
n_media <- rnorm(20,0,1)
n_grande <- rnorm(300,0,1)

#Revisemos cuál es la media computada para cada una de estas muestras y prestemos atención en cuál se acerca más al valor real de la población de donde se extrajeron (0)
ns <- data.frame(round(cbind(mean(n_peque),mean(n_media), mean(n_grande)),3))
colnames(ns) <- c("Peque�a","Media","Grande")
print(ns)

#Repitamos el mismo ejercicio con al menos 10 muestras diferentes por cada tama�o probado

#Para ello empezamos por crear tres objetos vacíos que después llenaremos con un ciclo for
peques<- c(NULL)
medias<- c(NULL)
grandes<- c(NULL)

#Por cada elemento (arbitrariamente identificado como 'i') contenido en el intervalo 1-10
for(i in 1:10){
peques[i]<- mean(rnorm(5,0,1))     #Voy a escribir en el espacio i del objeto "peques" la media de una muestra aleatoria de 5 elementos extraidos de una normal con media 0 y desviacion 1
medias[i]<- mean(rnorm(20,0,1))    #de igual forma, lleno los objetos "medias" y "grandes" con las medias de muestras generadas en cada una de las 10 repeticiones del ciclo, con distintos tamaños de muestra
grandes[i]<- mean(rnorm(300,0,1))
}

cbind(peques,medias,grandes)    #Agrupo los arreglos de medias generados en una tabla, y los imprimo. 
#Podemos apreciar que, en general, las medias computadas en el grupo Grandes tienden a acercarse más a 0

cbind(mean(peques),mean(medias),mean(grandes))
#Computamos la media de las medias estimadas para verificar que, en promedio, los grupos más grandes tuvieron valores promedios más cercanos a 0.






# Distribuci�n  P O I S S O N
####################################
####################################
#En una distribución poisson, la media poblacional se captura por el parámetro Lambda

#Generamos tres muestras de distinto tamaño y misma parametrización.
n_peque <- rpois(5,10)
n_media <- rpois(20,10)
n_grande <- rpois(300,10)

#Agrupamos los promedios de las tres muestras generadas en una sola tabla, para comprobar que es la muestra de mayor tamaño quien presenta el valor promedio más cercano a la media poblacional (el parámetro lambda previamente definido para la población)
ns <- data.frame(round(cbind(mean(n_peque),mean(n_media), mean(n_grande)),3))
colnames(ns) <- c("Pequeña","Media","Grande")
print(ns)

#Una vez más, repetimos este ejercicio generando 10 muestras -computando su respectiva media- por cada tamaño muestral propuesto

#generamos tres objetos vacíos
peques<- c(NULL)
medias<- c(NULL)
grandes<- c(NULL)

#Llenamos cada objeto con 10 medias muestrales generadas a partir de cada una de las repeticiones del siguiente ciclo for:
for(i in 1:10){
  peques[i]<- mean(rpois(5,10)) 
  medias[i]<- mean(rpois(20,10))
  grandes[i]<- mean(rpois(300,10))
}

#Imprimimos las diez medias muestrales computadas por grupo
cbind(peques,medias,grandes)
#Imprimimos la media de las medias muestrales computadas
cbind(mean(peques),mean(medias),mean(grandes))




# Distribución  Exponencial
####################################
####################################
#En una distribución exponencial, el Valor esperado se computa como 1/omega

#Generamos tres muestras de distinto tamaño, pero mismo valor de Omega
n_peque <- rexp(5,10)
n_media <- rexp(20,10)
n_grande <- rexp(300,10)

#Organizamos las medias de las muestras generadas en un arreglo de datos
ns <- data.frame(round(cbind(mean(n_peque),mean(n_media), mean(n_grande)),3))
colnames(ns) <- c("Pequeña","Media","Grande")
print(ns)

#Repetimos el proceso, computando las medias de 10 muestras distintas por cada tamaño de la muestra propuesto
peques<- c(NULL)
medias<- c(NULL)
grandes<- c(NULL)

for(i in 1:10){
  peques[i]<- mean(rexp(5,10))
  medias[i]<- mean(rexp(20,10))
  grandes[i]<- mean(rexp(300,10))
}

#Presentamos las 10 medias generadas con el ciclo for por cada Tamaño propuesto
cbind(peques,medias,grandes)

#Computamos el promedio de las medias muestrales generadas
cbind(mean(peques),mean(medias),mean(grandes))

#Establecemos la media poblacional, según la Omega definida :
1/10


#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
# Teorema del Lìmite central

#Segun el teorema del Límite Central, si yo observo las estimaciones que podría hacer sobre el valor de mi parámetro poblacional (a.k.a. estimadores) a partir de un número infinito de muestras extraídas de cierta población, encontraría que
# dichos valores estimados se distribuirían de acuerdo a una Distribución Normal con una varianza cada vez más pequeña y media en el valor real del parámetro.

####### Variable aleatoria (~Normal)
v_normal <- c(NA)   #Creamos un arreglo vacío
for(i in 1:5000){   #Que vamos a llenar con 5000 valores (que representan el número de muestras extraídas) 
v_normal[i] <- mean(rnorm(500,0,1))      #Por cada una de esas 5000 muestras, voy a computar la media de 500 valores extraídos aleatoriamente de una distribución normal con media en 0 y desviación 1
}
#Si graficamos un histograma con todas las medias muestrales computadas, encontramos una distribución normal cuya media se encuentra en el valor real del parámetro a estimar (en este caso, la media poblacional previamente establecida como 0)
hist(v_normal,breaks=20, xlim=c(-0.2,0.2), main="Variable Normal", col="turquoise") 




#La misma lógica aplica para cualquier otro tipo de distribución:

####### Variable aleatoria (~Binom)
v_binom <- c(NA)
for(i in 1:5000){
v_binom[i] <- mean(rbinom(500,500,0.5))  
}
hist(v_binom, main="Variable Binomial", breaks=20, col="pink")

###### Variable aleatoria (~Poisson)
v_pois <- c(NA)
for(i in 1:5000){
v_pois[i] <- mean(rpois(500,10))
}
hist(v_pois, main="Variable Poisson", breaks=50, col="lightgreen")

###### Variable aleatoria (~Exponencial)
v_exp <- c(NA)
for(i in 1:50000){
v_exp[i] <- mean(rexp(500,10))
}
hist(v_exp, main="Variable Exponencial", breaks=50, col="indianred3")
