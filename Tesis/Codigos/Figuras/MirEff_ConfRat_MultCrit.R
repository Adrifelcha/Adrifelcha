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
d_ruido <- dnorm(soporte,0,1)
d_senal <- dnorm(soporte,d,1)
d_ruido2<- dnorm(soporte,-1,1)
d_senal2<- dnorm(soporte,2,1)

######################Plot 1: Criterio
valor_inf<- -.33
valor_sup<- 3
pos_inf<-which(soporte==valor_inf)
pos_sup<-which(round(soporte,2)==valor_sup)

plot(0,type='n',axes=F,
     xlab='Familiaridad',
     ylab='Probabilidad',
     cex.lab=1,
     xlim=c(-4,5),ylim=c(-0.05,.6))
lines(soporte,d_ruido, col='mediumvioletred',lty=1, lwd=2)
lines(soporte,d_senal,col='mediumvioletred',lty=1, lwd=2)

#CRITERIO
#abline(v=k,col='red',lty=1,lwd=3)

#CONFIDENCE CRITERIONS
abline(v=-3.8,col='dodgerblue3',lty=4,lwd=2)
abline(v=-2.4,col='dodgerblue3',lty=4,lwd=2)
abline(v=-0.9,col='dodgerblue3',lty=4,lwd=2)
abline(v=d/2,col='dodgerblue3',lty=4,lwd=2)
abline(v=1.8,col='dodgerblue3',lty=4,lwd=2)
abline(v=3.2,col='dodgerblue3',lty=4,lwd=2)
#Etiquetas
text(-3.6,0.57,paste("1"),cex=1)
text(-2.2,0.57,paste("2"), cex=1)
text(-0.7,0.57, paste("3"),cex=1)
text(((d/2)+.2),0.57,paste("4"),col='purple',cex=1)
text(2,0.57,paste("5"),col='purple',cex=1)
text(3.4,0.57,paste("6"),col='blue',cex=1)




#Distribuciones 'FACILES'
lines(soporte,d_ruido2,col='steelblue',lty=1, lwd=2)
lines(soporte,d_senal2,col='steelblue',lty=1, lwd=2)
axis(1,at=-4:6,pos=0)
axis(2,at=c(0,.5),pos=-4,las=1)




#text(-0.5,0.41,paste("Ruido"), cex=1)
#text(1.5,0.41,paste("Señal"), cex=1)
text(-1.2,0.43,paste("AR"), cex=1)
text(0,0.43,paste("AR"), cex=1)
text(1,0.43,paste("BS"), cex=1)
text(2,0.43,paste("BS"), cex=1)
