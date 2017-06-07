rm(list=ls()) 


soporte <- seq(5,13,.05)        #Especificamos el Soporte de nuestras distribuciones
intensidad <- seq(5,13,0.5)
d_ruido <- dnorm(soporte,0,1)   #Definimos nuestra distribucion de Ruido de acuerdo a la teoria (Media=0 y DV=1)
d_luz <- dnorm(soporte,10,0.9)   #Definimos la distribucion de Se??al, con media en d'


plot(soporte,type='l', xlim=c(5,13),ylim=c(0,0.5), 
     axes=F, ylab="Probabilidad", xlab="Intensidad percibida", font.lab=1)             #Dibujamos la distribucion de ruido
axis(2,at=c(0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500),labels=c("0", "50", "100", "150", "200", "250", "300", "350", "400", "450", "500"),las=1)
axis(1,at=intensidad,labels=intensidad)
lines(soporte,d_luz,type='l',col='blue') #Dibujamos la distribucion de Se??al
abline(v=10,col='red', lty=2)                      #Dibujamos el criterio
text(12,0.3,"Percepción del estímulo", col="blue", font=1)
#abline(v=d/2,col='blue',lty=2)             #Se??alamos la localizacion Optima (sin sesgo) del criterio


#####################################
#####################################
#####################################

rm(list=ls()) 


soporte <- seq(1,110,.05)        #Especificamos el Soporte de nuestras distribuciones
intensidad <- seq(0,110,5)
d_ruido <- dnorm(soporte,0,1)   #Definimos nuestra distribucion de Ruido de acuerdo a la teoria (Media=0 y DV=1)
d_luz <- dnorm(soporte,75,9)   #Definimos la distribucion de Se??al, con media en d'


plot(soporte,type='l', xlim=c(1,110),ylim=c(0,0.05), 
     axes=F, ylab="Probabilidad", xlab="Puntaje en prueba clínica", font.lab=1)             #Dibujamos la distribucion de ruido
axis(2,at=c(0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500),labels=c("0", "50", "100", "150", "200", "250", "300", "350", "400", "450", "500"),las=1)
axis(1,at=intensidad,labels=intensidad)
lines(soporte,d_luz,type='l',col='blue') #Dibujamos la distribucion de Se??al
abline(v=75,col='red', lty=2)                      #Dibujamos el criterio
#abline(v=d/2,col='blue',lty=2)             #Se??alamos la localizacion Optima (sin sesgo) del criterio
text(97,0.03,"Personas con Depresión", col="blue", font=1) 



#######################################
######################################
#######################################
rm(list=ls()) 


soporte <- seq(1,110,.05)        #Especificamos el Soporte de nuestras distribuciones
intensidad <- seq(0,110,5)
d_ruido <- dnorm(soporte,50,9)   #Definimos nuestra distribucion de Ruido de acuerdo a la teoria (Media=0 y DV=1)
d_luz <- dnorm(soporte,75,9)   #Definimos la distribucion de Se??al, con media en d'


plot(soporte,type='l', xlim=c(1,110),ylim=c(0,0.05), 
     axes=F, ylab="Probabilidad", xlab="Puntaje en prueba clínica", font.lab=1)             #Dibujamos la distribucion de ruido
axis(2,at=c(0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500),labels=c("0", "50", "100", "150", "200", "250", "300", "350", "400", "450", "500"),las=1)
axis(1,at=intensidad,labels=intensidad)
lines(soporte,d_luz,type='l',col='blue') #Dibujamos la distribucion de Se??al
lines(soporte,d_ruido,type='l',col='black') #Dibujamos la distribucion de Se??al
abline(v=75,col='red', lty=2)                      #Dibujamos el criterio
#abline(v=d/2,col='blue',lty=2)             #Se??alamos la localizacion Optima (sin sesgo) del criterio
text(97,0.03,"Personas con Depresión", col="blue", font=1) 
text(28,0.03,"Personas sin Depresión", col="black", font=1) 







