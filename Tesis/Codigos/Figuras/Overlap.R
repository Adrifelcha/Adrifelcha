rm(list=ls()) 
#layout(matrix(1:2,ncol=1))

######################################
#######################################
rm(list=ls()) 


soporte <- seq(1,90,.05)        #Especificamos el Soporte de nuestras distribuciones
intensidad <- seq(0,90,5)
d_ruido <- dnorm(soporte,30,9)   #Definimos nuestra distribucion de Ruido de acuerdo a la teoria (Media=0 y DV=1)
d_1 <- dnorm(soporte,45,9)   #Definimos la distribucion de Se??al, con media en d'
d_2 <- dnorm(soporte,65,9)

plot(soporte,type='l', xlim=c(1,90),ylim=c(0,0.05), 
     axes=F, ylab="Probabilidad", xlab="Evidencia", font.lab=1)             #Dibujamos la distribucion de ruido
axis(2,at=c(0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500),labels=c("0", "50", "100", "150", "200", "250", "300", "350", "400", "450", "500"),las=1)
axis(1,at=intensidad,labels=intensidad)
lines(soporte,d_1,type='l',col='blue') #Dibujamos la distribucion de Se??al
lines(soporte,d_ruido,type='l',col='black') #Dibujamos la distribucion de Se??al
#abline(v=75,col='red', lty=2)                      #Dibujamos el criterio
#abline(v=d/2,col='blue',lty=2)             #Se??alamos la localizacion Optima (sin sesgo) del criterio
text(60,0.03,"Señal", col="blue", font=1) 
text(15,0.03,"Ruido", col="black", font=1) 
text(85,0.047,"a)", col="black", font=1) 


plot(soporte,type='l', xlim=c(1,90),ylim=c(0,0.05), 
     axes=F, ylab="Probabilidad", xlab="Evidencia", font.lab=1)             #Dibujamos la distribucion de ruido
axis(2,at=c(0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500),labels=c("0", "50", "100", "150", "200", "250", "300", "350", "400", "450", "500"),las=1)
axis(1,at=intensidad,labels=intensidad)
lines(soporte,d_2,type='l',col='blue') #Dibujamos la distribucion de Se??al
lines(soporte,d_ruido,type='l',col='black') #Dibujamos la distribucion de Se??al
#abline(v=75,col='red', lty=2)                      #Dibujamos el criterio
#abline(v=d/2,col='blue',lty=2)             #Se??alamos la localizacion Optima (sin sesgo) del criterio
text(50,0.03,"Señal", col="blue", font=1) 
text(15,0.03,"Ruido", col="black", font=1) 
text(85,0.047,"b)", col="black", font=1) 





