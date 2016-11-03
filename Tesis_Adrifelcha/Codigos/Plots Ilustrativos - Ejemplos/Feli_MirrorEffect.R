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
soporte <- seq(-4,6,.005)
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
     xlim=c(-4,6),ylim=c(-0.05,.5))
#polygon(c(soporte[pos_inf],soporte[pos_inf:pos_sup],soporte[pos_sup]),
#        c(0,d_ruido[pos_inf:pos_sup],0),
#        col='darkorchid2',border=F)
lines(soporte,d_ruido, col='mediumvioletred',lty=1, lwd=3)
lines(soporte,d_senal,col='mediumvioletred',lty=2, lwd=1)
#CRITERIO
#abline(v=k,col='red',lty=1,lwd=3)
#CONFIDENCE CRITERIONS
#abline(v=d/2,col='dodgerblue3',lty=4,lwd=2)
#abline(v=d,col='dodgerblue3',lty=4,lwd=2)
#abline(v=0,col='dodgerblue3',lty=4,lwd=2)
#abline(v=-.5,col='dodgerblue3',lty=4,lwd=2)
#abline(v=1.5,col='dodgerblue3',lty=4,lwd=2)
#Distribuciones 'FACILES'
lines(soporte,d_ruido2,col='steelblue',lty=1, lwd=3)
lines(soporte,d_senal2,col='steelblue',lty=2, lwd=1)
axis(1,at=-4:6,pos=0)
axis(2,at=c(0,.5),pos=-4,las=1)


#text(-2.7,0.47,paste("K = ",k),col='red',cex=1)
#text(-2.7,0.43,paste("Tasa F.A. = ",fa_rate), cex=1)
#text(-2.7,0.40, paste("Tasa Hits =", h_rate),cex=1)
#text(-2.7,0.24,paste("D' = ",d),col='purple',cex=1)
#text(-2.7,0.30,paste("D'2 = ",d2),col='purple',cex=1)
#text(-2.7,0.20,paste("Beta = ",beta),col='blue',cex=1)
#text(-2.7,0.17,paste("lnBeta = ",lnB),col='blue',cex=1)
#text(-2.7,0.10,paste("C = ",c),col='blue',cex=1)
text(-0.5,0.48,paste("NUEVOS"), cex=1)
text(1.5,0.48,paste("VIEJOS"), cex=1)
text(-1.2,0.43,paste("AN"), cex=1)
text(0,0.43,paste("BN"), cex=1)
text(1,0.43,paste("BO"), cex=1)
text(2,0.43,paste("AO"), cex=1)
