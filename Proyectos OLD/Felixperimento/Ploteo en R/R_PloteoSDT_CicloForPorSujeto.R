# Intento SDT a partir Jaime deteccion y JL Estimacion
rm(list=ls())  
#Borrar datos previos

#Ubicacion de la base de datos
setwd("C:/Users/Adrifelcha/Dropbox/Felixperimento/SINCA - Datos/Plots/")
Condicion_Mixta <- read.csv("Mixto_forfor.csv", header=FALSE)

for(x in 5:8){
  h_rate<-Condicion_Mixta[x,1] #La x va a tomar valores del 1 al 23, el 1 es porque es la primera columna
  fa_rate<-Condicion_Mixta[x,2] #El 2 es porque toma los valores de la segunda columna
  k<-qnorm(1-fa_rate,0,1)
  d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)
  c<-k-(d/2)                    
  beta<-dnorm(k,d,1)/dnorm(k,0,1)
  #Distribuciones
  soporte <- seq(-3.5,5,.01)
  # Jaime: soporte<-seq(-10,10,by=0.01) by?
  d_ruido <- dnorm(soporte,0,1)
  d_senal <- dnorm(soporte,d,1)
  #plots
  plot(soporte,d_ruido,type='l',lwd=2, xlab="Eje X", ylab="P")
  lines(soporte,d_senal,type='l',col='purple',lwd=2)
  lines(c(k,d/2),c(0.1,0.1),col="blue",lwd=3)           #distancia C-K
  abline(v=k,col='red',lwd=2)
  abline(v=d/2,lwd=1)
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
} 