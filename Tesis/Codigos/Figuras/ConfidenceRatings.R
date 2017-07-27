#Ilustraci?n del c?lculo param?trico:
#?C?mo las tasas de Hits y F.A. se convierten en distribuciones?
rm(list=ls())  

#variables
h_rate<-.88
fa_rate<-.12
k<-qnorm(1-fa_rate,0,1)
d<-1
#d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)
#d2<-qnorm(1-fa_rate,0,1)-qnorm(1-h_rate,0,1)
zs<-qnorm(1-h_rate,0,1)
c<-k-(d/2)                    
beta<-dnorm(k,d,1)/dnorm(k,0,1)
lnB<-log(beta)
lnB<--.27

#Calculamos valores
d<-round(d,3)
d2<-round(d2,3)
k<-round(k,3)
c<-round(c,3)
beta<-round(beta,3)
h_rate<-round(h_rate,3)
fa_rate<-round(fa_rate,3)
lnB<-round(lnB,3)

#Distribuciones
soporte <- seq(-4,5,.005)
d_ruido <- dnorm(soporte,-0.5,1)
d_senal <- dnorm(soporte,1,1)

######################Plot 1: Criterio
valor_inf<- -.33
valor_sup<- 3
pos_inf<-which(soporte==valor_inf)
pos_sup<-which(round(soporte,2)==valor_sup)

plot(0,type='n',axes=F,
     ann = FALSE,
     xlim=c(-4,4.5),ylim=c(-0.05,.6))
axis(1,at=-4:6,pos=0)
axis(2,at=c(0,.5),pos=-4,las=1)
mtext(side=1, text = "Evidencia", line=1, cex=3.4)
mtext(side=2, text = "Probabilidad", line=-0.5, cex=3.4)
lines(soporte,d_ruido, col='mediumvioletred',lty=1, lwd=2)
lines(soporte,d_senal,col='darkgreen',lty=1, lwd=2)

#CRITERIO
#abline(v=k,col='red',lty=1,lwd=3)

#CONFIDENCE CRITERIONS
abline(v=-3.8,col='dodgerblue3',lty=4,lwd=2)
abline(v=-2.45,col='dodgerblue3',lty=4,lwd=2)
abline(v=-1.1,col='dodgerblue3',lty=4,lwd=2)
abline(v=0.25,col='dodgerblue3',lty=4,lwd=2)
abline(v=1.6,col='dodgerblue3',lty=4,lwd=2)
abline(v=2.95,col='dodgerblue3',lty=4,lwd=2)
#Etiquetas
text(-3.6,0.5,paste("1"),cex=1.7)
text(-2.25,0.5,paste("2"), cex=1.7)
text(-0.9,0.5, paste("3"),cex=1.7)
text(0.45,0.5,paste("4"),col='purple',cex=1.7)
text(1.8,0.5,paste("5"),col='purple',cex=1.7)
text(3.15,0.5,paste("6"),col='blue',cex=1.7)

text(-1.2,0.4,paste("Ruido"), col='mediumvioletred', cex=2)
text(1.8,0.4,paste("Señal"), col='darkgreen', cex=2)
