rm(list=ls()) 


soporte <- seq(1,110,.05)        #Especificamos el Soporte de nuestras distribuciones
intensidad <- seq(0,110,5)
d_ruido <- dnorm(soporte,50,9)   #Definimos nuestra distribucion de Ruido de acuerdo a la teoria (Media=0 y DV=1)
d_luz <- dnorm(soporte,75,9)   #Definimos la distribucion de Se??al, con media en d'


plot(soporte,type='l', xlim=c(1,110),ylim=c(0,0.055), 
     axes=F, ann = FALSE)             #Dibujamos la distribucion de ruido
axis(1,at=intensidad,labels=intensidad, line=-0.5)
lines(soporte,d_luz,type='l',col='blue', lwd=3) #Dibujamos la distribucion de Se??al
lines(soporte,d_ruido,type='l',col='black', lwd=3) #Dibujamos la distribucion de Se??al
abline(v=55,col='black', lty=2, lwd=3)                      #Dibujamos el criterio
text(94,0.052,"Depredador", col="blue", font=1, cex=2) 
text(31,0.052,"No depredador", col="black", font=1, cex=2) 
mtext(side=1, text = "Decibeles", line=2.9, cex=2.4)
#abline(v=75,col='red', lty=2, lwd=2.5)                      #Dibujamos el criterio
#text(72,0.047,expression(mu), col="red", font=1, cex=2)







