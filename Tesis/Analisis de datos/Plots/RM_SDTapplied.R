#Codigo Base para Analisis Parametrico y Graficacion (SDT)
#Autor: Adriana F. Chávez De la Peña
#adrifelcha@gmail.com
##########################################################

rm(list=ls())  #Limpiamos el espacio de trabajo

#####Datos a graficar#####
h<-133  #Numero crudo de Hits
f<-13   #Numero de Falsas Alarmas
h_rate<-h/150      #Tasa de Hits relativo al total de Ensayos con Se??al
fa_rate<-f/150     #Tasa de Falsas Alarmas relativa al total de Ensayos con Ruido

#####Estimaci??n Param??trica#####
k<-qnorm(1-fa_rate,0,1)   #Calculamos la localizacion del Criterio
d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)     #Calculamos d'
c<-k-(d/2)                                  #Calculamos el Sesgo c
beta<-dnorm(k,d,1)/dnorm(k,0,1)             #Calculamos el Sesgo Beta

soporte <- seq(-4,8,.05)        #Especificamos el Soporte de nuestras distribuciones
d_ruido <- dnorm(soporte,0,1)   #Definimos nuestra distribucion de Ruido de acuerdo a la teoria (Media=0 y DV=1)
d_senal <- dnorm(soporte,d,1.4)   #Definimos la distribucion de Se??al, con media en d'

plot(soporte,d_ruido,type='l', xlim=c(-4,8),ylim=c(0,0.5), ylab="", xlab="Fuerza de Memoria", font.lab=2)             #Dibujamos la distribucion de ruido
lines(soporte,d_senal,type='l',col='blue') #Dibujamos la distribucion de Se??al
abline(v=k,col='red')                      #Dibujamos el criterio
#abline(v=d/2,col='blue',lty=2)             #Se??alamos la localizacion Optima (sin sesgo) del criterio


d<-round(d,4)   #Redondeamos el valor de d' a 5 decimales para facilitar su representacion
k<-round(k,4)   #Redondeamos el valor del criterio a 5 decimales para facilitar su representacion
c<-round(c,4)   #Redondeamos el valor del Sesgo c a 5 decimales para facilitar su representacion
beta<-round(beta,4) #Redondeamos el valor del Sesgo Beta a 5 decimales para facilitar su representacion
h_rate<-round(h_rate,4)
fa_rate<-round(fa_rate,4)

text(0.8,0.48,"Criterio", col="red")  #Imprimimos la localizacion del criterio 
text(2.7,0.33,"Señal", col="blue", font=2) 
text(4,.31,"Estímulos Conocidos", col="blue")
text(-1,0.36,"Ruido", col="black", font=2) 
text(-2.2,0.34,"Estímulos Nuevos", col="black")
#text(6,0.19,paste("Tasa de Hits = ",h_rate))            #Especificamos la Tasa de Hits
#text(6,0.15,paste("Tasa de F. Alarmas = ",fa_rate))   #Especificamos la Tasa de Falsas Alarmas

