# Intento SDT a partir Jaime deteccion y JL Estimacion

rm(list=ls())  
#Borrar datos previos

#variables
h<-125
f<-13
h_rate<-h/168
fa_rate<-f/168
k<-qnorm(1-fa_rate,0,1)
d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)
c<-k-(d/2)                    
beta<-dnorm(k,d,1)/dnorm(k,0,1)


#Distribuciones
soporte <- seq(-3.5,6,.01)
# Jaime: soporte<-seq(-10,10,by=0.01) by?
d_ruido <- dnorm(soporte,0,1)
d_senal <- dnorm(soporte,d,1)

#plots
plot(soporte,d_ruido,type='l',lwd=2)
lines(soporte,d_senal,type='l',col='purple',lwd=2)
lines(c(k,d/2),c(0.1,0.1),col="blue",lwd=3)           #distancia C-K
abline(v=k,col='red',lwd=2)
abline(v=d/2,lwd=1)

#Si agregaramos el argumento 'lwd=2' las líneas se engrosarían
#Lines es horizontal y Abline es vertical

#Redondeamos valores
d<-round(d,3)
k<-round(k,3)
c<-round(c,3)
beta<-round(beta,3)
h_rate<-round(h_rate,3)
fa_rate<-round(fa_rate,3)

#textos
text(-2.5,0.39,paste("Hit Rate = ",h_rate),cex=1.2)
text(-2.5,0.36,paste("F. alarm Rate = ",fa_rate),cex=1.2)
text(-2.5,0.33,paste("K = ",k),cex=1.2,col='red',f=2)
text(-2.5,0.30,paste("C = ",c),cex=1.2,col='blue',f=2)
text(-2.5,0.27,paste("D' = ",d),cex=1.2)
