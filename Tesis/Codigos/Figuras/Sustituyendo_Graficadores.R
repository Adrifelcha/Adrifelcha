############################################################
####  Tasas de ejecución 
############################################################

rm(list=ls())
for(i in 1:1){
plot(10, 20, main="", xlab="", ylab="",type='l', font.lab=2, axes = "FALSE", 
     xlim= c(-4,5),  ylim= c(0,.5))
lines(seq(1,10,.05),dnorm(seq(1,10,.05),2,1),type='l', lwd=4, col='forestgreen') #Hit
lines(seq(1,10,.05),dnorm(seq(1,10,.05),0,1),type='l', lwd=4, col='firebrick3') #FA
lines(seq(-4,1,.05),dnorm(seq(-4,1,.05),0,1),type='l', lwd=4, col='dodgerblue3') #Rej
lines(seq(-4,1,.05),dnorm(seq(-4,1,.05),2,1),type='l', lwd=4, col='darkorchid3') #Miss
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),0,1),type='l', lwd=1, lty=3, col='white') #NOISE
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),2,1),type='l', lwd=1, lty=3, col='white') #SIGNAL
axis(1,at=c(-4, -3, -2, -1, 0, 1, 2, 3, 4, 5), labels=c(-4:5), font=2)
abline(v=1, lwd=2, col='red')
text(3.1,.34,paste("Hit"), cex=1.5, col='forestgreen', f=2) 
text(-0.3,.14,paste("Omisión"), cex=1.5, col='darkorchid3', f=2) 
text(2.4,.14,paste("Falsa Alarma"), cex=1.5, col='firebrick3', f=2) 
text(-2.2,.34,paste("Rechazo Correcto"), cex=1.5, col='dodgerblue3', f=2) 
text(-0.2,.48,"Ruido",cex=3,col='black',f=2)
text(2.2,.48,"Señal",cex=3,col='black',f=2)
mtext("Evidencia",1,cex=2, line=3, f=2)
}

############################################################
### Localización del Criterio
############################################################
rm(list=ls())
for(i in 1:1){
crit <- 1
h_rate<- pnorm(crit,2,1,lower.tail=FALSE)      #Tasa de Hits relativo al total de Ensayos con Se??al
fa_rate<- pnorm(crit,0,1,lower.tail=FALSE)     #Tasa de Falsas Alarmas relativa al total de Ensayos con Ruido
k<-qnorm(1-fa_rate,0,1)   #Calculamos la localizacion del Criterio
d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)     #Calculamos d'
c<-k-(d/2)                                  #Calculamos el Sesgo c
beta<-dnorm(k,d,1)/dnorm(k,0,1)             #Calculamos el Sesgo Beta

plot(1, 0.24, main="", xlab="", ylab="",type='p', font.lab=2, axes = "FALSE", 
     xlim= c(-3.5,4.5),  ylim= c(0,.6), pch=16, color='black', cex=2)
lines(seq(1,10,.05),dnorm(seq(1,10,.05),0,1),type='l', lwd=4, col='firebrick3') #FA
lines(seq(-4,1,.05),dnorm(seq(-4,1,.05),0,1),type='l', lwd=4, col='dodgerblue3') #Rej
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),0,1),type='l', lwd=1, lty=3, col='white') #NOISE
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),2,1),type='l', lwd=1, lty=3, col='black') #SIGNAL
axis(1,at=c(-4, -3, -2, -1, 0, 1, 2, 3, 4, 5), labels=c(-4:5), font=2)
lines(c(1,1),c(-0.2,0.48), lwd=2, col='red')
lines(c(0,0),c(-0.2,0.48), lwd=2, col='black', lty=3)
lines(c(0,1),c(0.24,0.24), lwd=2, col='black')
text(2.4,.14,paste("Falsa Alarma"), cex=1.5, col='firebrick3', f=2) 
text(-2,.34,paste("Rechazo Correcto"), cex=1.5, col='dodgerblue3', f=2) 
text(2.4,.1, paste(round(pnorm(1,0,1,lower.tail=FALSE),3)), cex=1.5, col='firebrick3', f=2) 
text(-1.8,.3,paste(round(pnorm(1,0,1,lower.tail=TRUE),3)), cex=1.5, col='dodgerblue3', f=2)
text(1.7,.25,paste("Z =", round(k,2)), cex=1.5, col='black', f=2)
text(-0.2,.43,"Ruido",cex=2.5,col='black',f=2)
text(2.2,.43,"Señal",cex=2.5,col='black',f=1)
mtext("Evidencia",1,cex=2, line=2.5, f=2)
mtext("Localización del Criterio",3,cex=3, line=-2, f=2)
}

############################################################
# SESGO Beta y C
############################################################
#Liberal
rm(list=ls())
for(i in 1:1){
layout(matrix(1:2,ncol=2))

crit <- -0.5
h_rate<- pnorm(crit,2,1,lower.tail=FALSE)      #Tasa de Hits relativo al total de Ensayos con Se??al
fa_rate<- pnorm(crit,0,1,lower.tail=FALSE)     #Tasa de Falsas Alarmas relativa al total de Ensayos con Ruido
k<-qnorm(1-fa_rate,0,1)   #Calculamos la localizacion del Criterio
d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)     #Calculamos d'
c<-k-(d/2)                                  #Calculamos el Sesgo c
beta<-dnorm(k,d,1)/dnorm(k,0,1)             #Calculamos el Sesgo Beta


plot(c(crit, crit), c(.35,.02), main="", xlab="", ylab="",type='p', font.lab=2, axes = "FALSE", 
     xlim= c(-3.5,4.5),  ylim= c(0,.53), pch=16, color='black', cex=2)
lines(seq(k,10,.05),dnorm(seq(crit,10,.05),0,1),type='l', lwd=4, col='firebrick3') #FA
lines(seq(-4,crit,.05),dnorm(seq(-4,crit,.05),0,1),type='l', lwd=4, col='dodgerblue3') #Rej
lines(seq(k,10,.05),dnorm(seq(crit,10,.05),2,1),type='l', lwd=4, col='forestgreen') #Hit
lines(seq(-4,crit,.05),dnorm(seq(-4,crit,.05),2,1),type='l', lwd=4, col='darkorchid3') #Miss
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),0,1),type='l', lwd=1, lty=3, col='white') #NOISE
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),2,1),type='l', lwd=1, lty=3, col='black') #SIGNAL
axis(1,at=c(-4, -3, -2, -1, 0, 1, 2, 3, 4, 5), labels=c(-4:5), font=2)
lines(c(crit,crit),c(-0.2,0.48), lwd=2, col='red')
text(-2.3,.45,paste("Falsa Alarma"), cex=1.2, col='firebrick3', f=2) 
text(-2.5,.41,paste("Rechazo C."), cex=1.2, col='dodgerblue3', f=2) 
text(-3.2,.37,paste("Hit"), cex=1.2, col='forestgreen', f=2) 
text(-0.2,.17,paste("K"), cex=1.2, col='red', f=2) 
text(-2.7,.33,paste("Omisión"), cex=1.2, col='darkorchid3', f=2) 
text(2.1,.35,paste("P(ruido) =", round(dnorm(crit,0,1),3)), cex=1.5, col='black', f=2)
text(2.1,.02,paste("P(señal) =", round(dnorm(crit,2,1),3)), cex=1.5, col='black', f=2)
text(-2.5, .22, expression(beta == 0.0511), cex=1.4)
mtext("Evidencia",1,cex=2, line=2.5, f=2)
mtext("Beta",3,cex=3, line=-2, f=2)

plot(1, 0.24, main="", xlab="", ylab="",type='p', font.lab=2, axes = "FALSE", 
     xlim= c(-3.5,4.5),  ylim= c(0,.53), pch=16, color='black', cex=2)
lines(seq(crit,10,.05),dnorm(seq(crit,10,.05),0,1),type='l', lwd=4, col='firebrick3') #FA
lines(seq(-4,crit,.05),dnorm(seq(-4,crit,.05),0,1),type='l', lwd=4, col='dodgerblue3') #Rej
lines(seq(crit,10,.05),dnorm(seq(crit,10,.05),2,1),type='l', lwd=4, col='forestgreen') #Hit
lines(seq(-4,crit,.05),dnorm(seq(-4,crit,.05),2,1),type='l', lwd=4, col='darkorchid3') #Miss
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),0,1),type='l', lwd=1, lty=3, col='white') #NOISE
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),2,1),type='l', lwd=1, lty=3, col='black') #SIGNAL
text(-0.2,.17,paste("K"), cex=1.2, col='red', f=2) 
axis(1,at=c(-4, -3, -2, -1, 0, 1, 2, 3, 4, 5), labels=c(-4:5), font=2)
lines(c(crit,crit),c(-0.2,0.48), lwd=2, col='red')
lines(c(1,1),c(-0.2,0.48), lwd=2, col='black', lty=3)
lines(c(1,crit),c(0.24,0.24), lwd=2, col='black')
text(2.7,.43,paste("C =", round(c,3)), cex=1.5, col='black', f=2)
mtext("Evidencia",1,cex=2, line=2.5, f=2)
mtext("C",3,cex=3, line=-2, f=2)
mtext("Sesgo Liberal",3,cex=3, line=-3, f=2, outer=TRUE)
}

#Conservador
rm(list=ls())
for(i in 1:1){
layout(matrix(1:2,ncol=2))

crit <- 2.5
h_rate<- pnorm(crit,2,1,lower.tail=FALSE)      #Tasa de Hits relativo al total de Ensayos con Se??al
fa_rate<- pnorm(crit,0,1,lower.tail=FALSE)     #Tasa de Falsas Alarmas relativa al total de Ensayos con Ruido
k<-qnorm(1-fa_rate,0,1)   #Calculamos la localizacion del Criterio
d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)     #Calculamos d'
c<-k-(d/2)                                  #Calculamos el Sesgo c
beta<-dnorm(k,d,1)/dnorm(k,0,1)             #Calculamos el Sesgo Beta


plot(c(2.5, 2.5), c(.35,.02), main="", xlab="", ylab="",type='p', font.lab=2, axes = "FALSE", 
     xlim= c(-3.5,4.5),  ylim= c(0,.53), pch=16, color='black', cex=2)
lines(seq(2.5,10,.05),dnorm(seq(2.5,10,.05),0,1),type='l', lwd=4, col='firebrick3') #FA
lines(seq(-4,2.5,.05),dnorm(seq(-4,2.5,.05),0,1),type='l', lwd=4, col='dodgerblue3') #Rej
lines(seq(2.5,10,.05),dnorm(seq(2.5,10,.05),2,1),type='l', lwd=4, col='forestgreen') #Hit
lines(seq(-4,2.5,.05),dnorm(seq(-4,2.5,.05),2,1),type='l', lwd=4, col='darkorchid3') #Miss
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),0,1),type='l', lwd=1, lty=3, col='white') #NOISE
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),2,1),type='l', lwd=1, lty=3, col='black') #SIGNAL
axis(1,at=c(-4, -3, -2, -1, 0, 1, 2, 3, 4, 5), labels=c(-4:5), font=2)
lines(c(2.5,2.5),c(-0.2,0.48), lwd=2, col='red')
text(-2.3,.45,paste("Falsa Alarma"), cex=1.2, col='firebrick3', f=2) 
text(-2.5,.41,paste("Rechazo C."), cex=1.2, col='dodgerblue3', f=2) 
text(-3.5,.37,paste("Hit"), cex=1.2, col='forestgreen', f=2) 
text(-2.8,.33,paste("Omisión"), cex=1.2, col='darkorchid3', f=2) 
text(0.5,.35,paste("P(s) =", round(dnorm(2.5,2,1),3)), cex=1.5, col='black', f=2)
text(0.5,.02,paste("P(r) =", round(dnorm(2.5,0,1),3)), cex=1.5, col='black', f=2)
text(-2.5, .22, expression(beta == 19.555), cex=1.4)
text(2.1,.17,paste("K"), cex=1.2, col='red', f=2) 
mtext("Evidencia",1,cex=2, line=2.5, f=2)
mtext("Beta",3,cex=3, line=-2, f=2)

plot(1, 0.24, main="", xlab="", ylab="",type='p', font.lab=2, axes = "FALSE", 
     xlim= c(-3.5,4.5),  ylim= c(0,.53), pch=16, color='black', cex=2)
lines(seq(2.5,10,.05),dnorm(seq(2.5,10,.05),0,1),type='l', lwd=4, col='firebrick3') #FA
lines(seq(-4,2.5,.05),dnorm(seq(-4,2.5,.05),0,1),type='l', lwd=4, col='dodgerblue3') #Rej
lines(seq(2.5,10,.05),dnorm(seq(2.5,10,.05),2,1),type='l', lwd=4, col='forestgreen') #Hit
lines(seq(-4,2.5,.05),dnorm(seq(-4,2.5,.05),2,1),type='l', lwd=4, col='darkorchid3') #Miss
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),0,1),type='l', lwd=1, lty=3, col='white') #NOISE
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),2,1),type='l', lwd=1, lty=3, col='black') #SIGNAL
axis(1,at=c(-4, -3, -2, -1, 0, 1, 2, 3, 4, 5), labels=c(-4:5), font=2)
lines(c(2.5,2.5),c(-0.2,0.48), lwd=2, col='red')
lines(c(1,1),c(-0.2,0.48), lwd=2, col='black', lty=3)
text(2.1,.17,paste("K"), cex=1.2, col='red', f=2) 
lines(c(1,2.5),c(0.24,0.24), lwd=2, col='black')
text(-1,.43,paste("C =", round(c,3)), cex=1.5, col='black', f=2)
mtext("Evidencia",1,cex=2, line=2.5, f=2)
mtext("C",3,cex=3, line=-2, f=2)
mtext("Sesgo Conservador",3,cex=3, line=-3, f=2, outer=TRUE)
}

############################################################
# Discriminabilidad
############################################################
rm(list=ls())
for(i in 1:1){
crit <- 1.5
h_rate<- pnorm(crit,2,1,lower.tail=FALSE)      #Tasa de Hits relativo al total de Ensayos con Se??al
fa_rate<- pnorm(crit,0,1,lower.tail=FALSE)     #Tasa de Falsas Alarmas relativa al total de Ensayos con Ruido
k<-qnorm(1-fa_rate,0,1)   #Calculamos la localizacion del Criterio
d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)     #Calculamos d'
c<-k-(d/2)                                  #Calculamos el Sesgo c
beta<-dnorm(k,d,1)/dnorm(k,0,1)             #Calculamos el Sesgo Beta


plot(10, 20, main="", xlab="", ylab="",type='l', font.lab=2, axes = "FALSE", 
     xlim= c(-4,5),  ylim= c(0,.5))
lines(seq(crit,10,.05),dnorm(seq(crit,10,.05),2,1),type='l', lwd=4, col='black', lty=3) #Hit
lines(seq(crit,10,.05),dnorm(seq(crit,10,.05),0,1),type='l', lwd=8, col='firebrick3') #FA
lines(seq(-4,crit,.05),dnorm(seq(-4,crit,.05),0,1),type='l', lwd=8, col='dodgerblue3') #Rej
lines(seq(-4,crit,.05),dnorm(seq(-4,crit,.05),2,1),type='l', lwd=4, col='black', lty=3) #Miss
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),0,1),type='l', lwd=1, lty=3, col='white') #NOISE
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),2,1),type='l', lwd=1, lty=3, col='white') #SIGNAL
axis(1,at=c(-4, -3, -2, -1, 0, 1, 2, 3, 4, 5), labels=c(-4:5), font=2)
abline(v=crit, lwd=2, col='red')
abline(v=0, lwd=3, col='black', lty=2)
lines(c(0,crit),c(0.38,0.38), lwd=5, col='black')
#text(3.1,.34,paste("Hit"), cex=1.5, col='forestgreen', f=2) 
#text(-0.3,.14,paste("Omisión"), cex=1.5, col='darkorchid3', f=2) 
text(2.5,.14,paste("Falsa Alarma"), cex=1.5, col='firebrick3', f=2) 
text(-2.2,.34,paste("Rechazo Correcto"), cex=1.5, col='dodgerblue3', f=2) 
text(0.8,.42,paste("Z =", round(qnorm(1-fa_rate,0,1),3)), cex=1.8, col='black', f=2)
text(-1.2,.48,"Ruido",cex=2.5,col='black',f=2)
text(-0.7, .12, expression(mu(ruido)), cex=1.5)
mtext("Evidencia",1,cex=2, line=3, f=2)
}

rm(list=ls())
for(i in 1:1){
crit <- 1.5
h_rate<- pnorm(crit,2,1,lower.tail=FALSE)      #Tasa de Hits relativo al total de Ensayos con Se??al
fa_rate<- pnorm(crit,0,1,lower.tail=FALSE)     #Tasa de Falsas Alarmas relativa al total de Ensayos con Ruido
k<-qnorm(1-fa_rate,0,1)   #Calculamos la localizacion del Criterio
d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)     #Calculamos d'
c<-k-(d/2)                                  #Calculamos el Sesgo c
beta<-dnorm(k,d,1)/dnorm(k,0,1)             #Calculamos el Sesgo Beta

plot(10, 20, main="", xlab="", ylab="",type='l', font.lab=2, axes = "FALSE", 
     xlim= c(-4,5),  ylim= c(0,.5))
text(3.2,.48,"Señal",cex=2.5,col='black',f=2)
mtext("Evidencia",1,cex=2, line=2.5, f=2)
lines(seq(crit,10,.05),dnorm(seq(crit,10,.05),2,1),type='l', lwd=8, col='forestgreen') #Hit
lines(seq(crit,10,.05),dnorm(seq(crit,10,.05),0,1),type='l', lwd=4, col='black', lty=3) #FA
lines(seq(-4,crit,.05),dnorm(seq(-4,crit,.05),0,1),type='l', lwd=4, col='black', lty=3) #Rej
lines(seq(-4,crit,.05),dnorm(seq(-4,crit,.05),2,1),type='l', lwd=8, col='darkorchid3') #Miss
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),0,1),type='l', lwd=1, lty=3, col='white') #NOISE
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),2,1),type='l', lwd=1, lty=3, col='white') #SIGNAL
axis(1,at=c(-4, -3, -2, -1, 0, 1, 2, 3, 4, 5), labels=c(-4:5), font=2)
abline(v=crit, lwd=2, col='red')
abline(v=d, lwd=3, col='black', lty=2)
lines(c(crit,d),c(0.38,0.38), lwd=5, col='black')
text(3.1,.34,paste("Hit"), cex=1.5, col='forestgreen', f=2) 
text(-0.3,.14,paste("Omisión"), cex=1.5, col='darkorchid3', f=2) 
#text(2.5,.14,paste("Falsa Alarma"), cex=1.5, col='firebrick3', f=2) 
#text(-2.2,.34,paste("Rechazo Correcto"), cex=1.5, col='dodgerblue3', f=2) 
text(0.8,.42,paste("z = -0.5"), cex=1.8, col='black', f=2)
text(2.7, .12, expression(mu(señal)), cex=1.5)
}

rm(list=ls())
for(i in 1:1){
crit <- 1.5
h_rate<- pnorm(crit,2,1,lower.tail=FALSE)      #Tasa de Hits relativo al total de Ensayos con Se??al
fa_rate<- pnorm(crit,0,1,lower.tail=FALSE)     #Tasa de Falsas Alarmas relativa al total de Ensayos con Ruido
k<-qnorm(1-fa_rate,0,1)   #Calculamos la localizacion del Criterio
d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)     #Calculamos d'
c<-k-(d/2)                                  #Calculamos el Sesgo c
beta<-dnorm(k,d,1)/dnorm(k,0,1)             #Calculamos el Sesgo Beta

plot(10, 20, main="", xlab="", ylab="",type='l', font.lab=2, axes = "FALSE", 
     xlim= c(-4,5),  ylim= c(0,.5))
text(3,.48,"Señal",cex=2.5,col='black',f=1)
mtext("Evidencia",1,cex=2, line=3, f=2)
lines(seq(crit,10,.05),dnorm(seq(crit,10,.05),2,1),type='l', lwd=8, col='forestgreen') #Hit
lines(seq(crit,10,.05),dnorm(seq(crit,10,.05),0,1),type='l', lwd=8, col='firebrick3') #FA
lines(seq(-4,crit,.05),dnorm(seq(-4,crit,.05),0,1),type='l', lwd=8, col='dodgerblue3') #Rej
lines(seq(-4,crit,.05),dnorm(seq(-4,crit,.05),2,1),type='l', lwd=8, col='darkorchid3') #Miss
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),0,1),type='l', lwd=1, lty=3, col='white') #NOISE
lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),2,1),type='l', lwd=1, lty=3, col='white') #SIGNAL
axis(1,at=c(-4, -3, -2, -1, 0, 1, 2, 3, 4, 5), labels=c(-4:5), font=2)
abline(v=crit, lwd=2, col='red')
abline(v=d, lwd=3, col='black', lty=2)
abline(v=0, lwd=3, col='black', lty=2)
#lines(c(0,d),c(0.38,0.38), lwd=5, col='black')
lines(c(crit,d),c(0.43,0.43), lwd=5, col='black')
lines(c(0,crit),c(0.42,0.42), lwd=5, col='black')
#text(3.1,.34,paste("Hit"), cex=1.5, col='forestgreen', f=2) 
#text(-0.3,.14,paste("Omisión"), cex=1.5, col='darkorchid3', f=2) 
#text(2.5,.14,paste("Falsa Alarma"), cex=1.5, col='firebrick3', f=2) 
#text(-2.2,.34,paste("Rechazo Correcto"), cex=1.5, col='dodgerblue3', f=2) 
text(-2.1,.37,paste("d' = 1.5 + 0.5 = 2"), cex=1.8, col='black', f=2)
text(-1.2,.48,"Ruido",cex=2.5,col='black',f=1)
text(2.7, .12, expression(mu(señal)), cex=1.5)
text(-0.7, .12, expression(mu(ruido)), cex=1.5)
}

############################################################
# R O C
############################################################

# d' nula
rm(list=ls())
for(i in 1:1){
layout(matrix(1:2,ncol=2))
  
  h_rate<- 0.5
  fa_rate<- 0.5
  
  k<-qnorm(1-fa_rate,0,1)   #Calculamos la localizacion del Criterio
  d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)     #Calculamos d'
  c<-k-(d/2)                                  #Calculamos el Sesgo c
  beta<-dnorm(k,d,1)/dnorm(k,0,1)             #Calculamos el Sesgo Beta
  
  
  plot(c(k, k), c(35,35), main="", xlab="", ylab="",type='p', font.lab=2, axes = "FALSE", 
       xlim= c(-3.5,4.5),  ylim= c(0,.53), pch=16, color='black', cex=2)
  lines(seq(k,10,.05),dnorm(seq(k,10,.05),0,1),type='l', lwd=4, col='firebrick3') #FA
  lines(seq(-4,k,.05),dnorm(seq(-4,k,.05),0,1),type='l', lwd=4, col='dodgerblue3') #Rej
  lines(seq(k,10,.05),dnorm(seq(k,10,.05),d,1),type='l', lwd=4, col='forestgreen') #Hit
  lines(seq(-4,k,.05),dnorm(seq(-4,k,.05),d,1),type='l', lwd=4, col='darkorchid3') #Miss
  lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),0,1),type='l', lwd=1, lty=3, col='white') #NOISE
  lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),d,1),type='l', lwd=1, lty=3, col='black') #SIGNAL
  axis(1,at=c(-4, -3, -2, -1, 0, 1, 2, 3, 4, 5), labels=c(-4:5), font=2)
  lines(c(k,k),c(-0.2,0.48), lwd=2, col='red')
  text(-2.3,.45,paste("Falsa Alarma"), cex=1.2, col='firebrick3', f=2) 
  text(-2.5,.41,paste("Rechazo C."), cex=1.2, col='dodgerblue3', f=2) 
  text(-3.2,.37,paste("Hit"), cex=1.2, col='forestgreen', f=2) 
  text(-0.2,.17,paste("K"), cex=1.2, col='red', f=2) 
  text(-2.7,.33,paste("Omisión"), cex=1.2, col='darkorchid3', f=2) 
  mtext("Evidencia",1,cex=2, line=2.5, f=2)
  mtext("d' = 0",3,cex=3, line=-2, f=2)
  
  
  
  hits <- c()   #Creamos un arreglo vacío, que vamos a ir llenando con el Ciclo For, para las tasas de Hits
  falarms <- c()  #Creamos un arreglo vacío para las tasas de Falsas Alarmas
  bias_c <- seq(-10,10,0.1) 
  d_null <- 0  #Como referencia, vamos a incluir una curva ROC para una d' de 0. El sistema a evaluar será juzgado como 'más preciso' conforme su ROC se aleje de ésta función de identidad.
  hits_na <- c()     #Creamos un arreglo vacío para los hits en  d' 0
  falarms_na <- c()  # Creamos un arreglo vacío para las falsas alarmas en d' 0
  
  
  for (i in 1:length(bias_c)){                     #Creamos un For donde, para cada posible valor del sesgo C (que relaciona directamente d' con el criterio)
    hits[i] <- pnorm((-d/2)-bias_c[i])             #se compute la proporción de la distribución de señal que cae sobre el criterio
    falarms[i] <- pnorm((d/2)-bias_c[i])           # y la proporción de la distribución de ruido.
    hits_na[i] <- pnorm((d_null/2)-bias_c[i])      #Para referencia, realizamos el mismo cómputo para la d' de 0
    falarms_na[i] <- pnorm((-d_null/2)-bias_c[i])
  }
  
  plot(fa_rate,h_rate, axes=F, ann=F,  pch=16, col='deepskyblue4', xlim=c(0,1), ylim=c(0,1.1), xlab='F.A. Rate', ylab='Hit Rate')     #Ploteamos las tasas de hits y falsas alarmas obervadas como un punto en el espacio
  axis(1,at=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), labels=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), font=2)
  axis(2,at=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), labels=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), font=2)
  lines(hits,falarms,lwd=2,col='deepskyblue2')        #Dibujamos la curva ROC correspondiente a la d' de nuestro sistema evaluado
  lines(hits_na,falarms_na,lwd=1,col='black', lty=2)  #Dibujamos la función de identidad, que corresponde a una d' de 0 (Donde las distribuciones de ruido y señal se empalman por completo)
  #lines(c(0.3, 0.38),c(0.25,0.25), lwd=2, lty=1, col="deepskyblue3")      
  #text(0.3, 0.2, labels="Relaciones posibles entre Hits-F.A., dada la d'", offset=0, cex = 0.7, pos=4)
  #text(0.3, 0.1, labels="Relación Hits-F.A. registrada", offset=0, cex = 0.7, pos=4)
  #points(.25,0.1, lty=3, pch=16, col='deepskyblue4')
  text(fa_rate-0.13, h_rate+0.02, paste("d' =", d), offset=0, cex = 0.8, pos=4)
  mtext("ROC",3,cex=3, line=-2, f=2)
  mtext("Tasa F.A.",1,cex=2, line=2.5, f=2)
  mtext("Tasa Hits",2,cex=2, line=2.5, f=2)
  mtext("Discriminabilidad nula",3,cex=3, line=-3, f=2, outer=TRUE)
}

# d' pequeña
rm(list=ls())
for(i in 1:1){
  layout(matrix(1:2,ncol=2))
  
  h_rate<- 0.84
  fa_rate<- 0.49
  
  k<-qnorm(1-fa_rate,0,1)   #Calculamos la localizacion del Criterio
  d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)     #Calculamos d'
  c<-k-(d/2)                                  #Calculamos el Sesgo c
  beta<-dnorm(k,d,1)/dnorm(k,0,1)             #Calculamos el Sesgo Beta
  
  
  plot(c(k, k), c(35,35), main="", xlab="", ylab="",type='p', font.lab=2, axes = "FALSE", 
       xlim= c(-3.5,4.5),  ylim= c(0,.53), pch=16, color='black', cex=2)
  lines(seq(k,10,.05),dnorm(seq(k,10,.05),0,1),type='l', lwd=4, col='firebrick3') #FA
  lines(seq(-4,k,.05),dnorm(seq(-4,k,.05),0,1),type='l', lwd=4, col='dodgerblue3') #Rej
  lines(seq(k,10,.05),dnorm(seq(k,10,.05),d,1),type='l', lwd=4, col='forestgreen') #Hit
  lines(seq(-4,k,.05),dnorm(seq(-4,k,.05),d,1),type='l', lwd=4, col='darkorchid3') #Miss
  lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),0,1),type='l', lwd=1, lty=3, col='white') #NOISE
  lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),d,1),type='l', lwd=1, lty=3, col='black') #SIGNAL
  axis(1,at=c(-4, -3, -2, -1, 0, 1, 2, 3, 4, 5), labels=c(-4:5), font=2)
  lines(c(k,k),c(-0.2,0.48), lwd=2, col='red')
  text(-2.3,.45,paste("Falsa Alarma"), cex=1.2, col='firebrick3', f=2) 
  text(-2.5,.41,paste("Rechazo C."), cex=1.2, col='dodgerblue3', f=2) 
  text(-3.2,.37,paste("Hit"), cex=1.2, col='forestgreen', f=2) 
  text(0.5,.17,paste("K"), cex=1.2, col='red', f=2) 
  text(-2.7,.33,paste("Omisión"), cex=1.2, col='darkorchid3', f=2) 
  mtext("Evidencia",1,cex=2, line=2.5, f=2)
  mtext("d' = 1",3,cex=3, line=-2, f=2)
  
  
  
  hits <- c()   #Creamos un arreglo vacío, que vamos a ir llenando con el Ciclo For, para las tasas de Hits
  falarms <- c()  #Creamos un arreglo vacío para las tasas de Falsas Alarmas
  bias_c <- seq(-10,10,0.1) 
  d_null <- 0  #Como referencia, vamos a incluir una curva ROC para una d' de 0. El sistema a evaluar será juzgado como 'más preciso' conforme su ROC se aleje de ésta función de identidad.
  hits_na <- c()     #Creamos un arreglo vacío para los hits en  d' 0
  falarms_na <- c()  # Creamos un arreglo vacío para las falsas alarmas en d' 0
  
  
  for (i in 1:length(bias_c)){                     #Creamos un For donde, para cada posible valor del sesgo C (que relaciona directamente d' con el criterio)
    hits[i] <- pnorm((-d/2)-bias_c[i])             #se compute la proporción de la distribución de señal que cae sobre el criterio
    falarms[i] <- pnorm((d/2)-bias_c[i])           # y la proporción de la distribución de ruido.
    hits_na[i] <- pnorm((d_null/2)-bias_c[i])      #Para referencia, realizamos el mismo cómputo para la d' de 0
    falarms_na[i] <- pnorm((-d_null/2)-bias_c[i])
  }
  
  plot(fa_rate,h_rate, axes=F, ann=F,  pch=16, col='deepskyblue4', xlim=c(0,1), ylim=c(0,1.1), xlab='F.A. Rate', ylab='Hit Rate')     #Ploteamos las tasas de hits y falsas alarmas obervadas como un punto en el espacio
  axis(1,at=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), labels=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), font=2)
  axis(2,at=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), labels=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), font=2)
  lines(hits,falarms,lwd=2,col='deepskyblue2')        #Dibujamos la curva ROC correspondiente a la d' de nuestro sistema evaluado
  lines(hits_na,falarms_na,lwd=1,col='black', lty=2)  #Dibujamos la función de identidad, que corresponde a una d' de 0 (Donde las distribuciones de ruido y señal se empalman por completo)
  #lines(c(0.3, 0.38),c(0.25,0.25), lwd=2, lty=1, col="deepskyblue3")      
  #text(0.3, 0.2, labels="Relaciones posibles entre Hits-F.A., dada la d'", offset=0, cex = 0.7, pos=4)
  #text(0.3, 0.1, labels="Relación Hits-F.A. registrada", offset=0, cex = 0.7, pos=4)
  #points(.25,0.1, lty=3, pch=16, col='deepskyblue4')
  text(fa_rate-0.23, h_rate+0.02, paste("d' =", round(d,4)), offset=0, cex = 0.8, pos=4)
  mtext("ROC",3,cex=3, line=-2, f=2)
  mtext("Tasa F.A.",1,cex=2, line=2.5, f=2)
  mtext("Tasa Hits",2,cex=2, line=2.5, f=2)
  mtext("Discriminabilidad baja",3,cex=3, line=-3, f=2, outer=TRUE)
}

# d' grande
rm(list=ls())
for(i in 1:1){
  layout(matrix(1:2,ncol=2))
  
  h_rate<- 0.97
  fa_rate<- 0.1
  
  k<-qnorm(1-fa_rate,0,1)   #Calculamos la localizacion del Criterio
  d<-qnorm(h_rate,0,1)-qnorm(fa_rate,0,1)     #Calculamos d'
  c<-k-(d/2)                                  #Calculamos el Sesgo c
  beta<-dnorm(k,d,1)/dnorm(k,0,1)             #Calculamos el Sesgo Beta
  
  
  plot(c(k, k), c(35,35), main="", xlab="", ylab="",type='p', font.lab=2, axes = "FALSE", 
       xlim= c(-3.5,6.5),  ylim= c(0,.53), pch=16, color='black', cex=2)
  lines(seq(k,10,.05),dnorm(seq(k,10,.05),0,1),type='l', lwd=4, col='firebrick3') #FA
  lines(seq(-4,k,.05),dnorm(seq(-4,k,.05),0,1),type='l', lwd=4, col='dodgerblue3') #Rej
  lines(seq(k,10,.05),dnorm(seq(k,10,.05),d,1),type='l', lwd=4, col='forestgreen') #Hit
  lines(seq(-4,k,.05),dnorm(seq(-4,k,.05),d,1),type='l', lwd=4, col='darkorchid3') #Miss
  lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),0,1),type='l', lwd=1, lty=3, col='white') #NOISE
  lines(seq(-4,10,.05),dnorm(seq(-4,10,.05),d,1),type='l', lwd=1, lty=3, col='black') #SIGNAL
  axis(1,at=c(-4, -3, -2, -1, 0, 1, 2, 3, 4, 5), labels=c(-4:5), font=2)
  lines(c(k,k),c(-0.2,0.48), lwd=2, col='red')
  text(-3.2,.33,paste("F.A."), cex=1.2, col='firebrick3', f=2) 
  text(-3.15,.41,paste("R. C."), cex=1.2, col='dodgerblue3', f=2) 
  text(-3.45,.37,paste("Hit"), cex=1.2, col='forestgreen', f=2) 
  text(0.5,.15,paste("K"), cex=1.2, col='red', f=2) 
  text(-2.6,.45,paste("Omisión"), cex=1.2, col='darkorchid3', f=2) 
  mtext("Evidencia",1,cex=2, line=2.5, f=2)
  mtext("d' = 3",3,cex=3, line=-2, f=2)
  
  
  
  hits <- c()   #Creamos un arreglo vacío, que vamos a ir llenando con el Ciclo For, para las tasas de Hits
  falarms <- c()  #Creamos un arreglo vacío para las tasas de Falsas Alarmas
  bias_c <- seq(-10,10,0.1) 
  d_null <- 0  #Como referencia, vamos a incluir una curva ROC para una d' de 0. El sistema a evaluar será juzgado como 'más preciso' conforme su ROC se aleje de ésta función de identidad.
  hits_na <- c()     #Creamos un arreglo vacío para los hits en  d' 0
  falarms_na <- c()  # Creamos un arreglo vacío para las falsas alarmas en d' 0
  
  
  for (i in 1:length(bias_c)){                     #Creamos un For donde, para cada posible valor del sesgo C (que relaciona directamente d' con el criterio)
    hits[i] <- pnorm((-d/2)-bias_c[i])             #se compute la proporción de la distribución de señal que cae sobre el criterio
    falarms[i] <- pnorm((d/2)-bias_c[i])           # y la proporción de la distribución de ruido.
    hits_na[i] <- pnorm((d_null/2)-bias_c[i])      #Para referencia, realizamos el mismo cómputo para la d' de 0
    falarms_na[i] <- pnorm((-d_null/2)-bias_c[i])
  }
  
  plot(fa_rate,h_rate, axes=F, ann=F,  pch=16, col='deepskyblue4', xlim=c(0,1), ylim=c(0,1.1), xlab='F.A. Rate', ylab='Hit Rate')     #Ploteamos las tasas de hits y falsas alarmas obervadas como un punto en el espacio
  axis(1,at=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), labels=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), font=2)
  axis(2,at=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), labels=c(0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), font=2)
  lines(hits,falarms,lwd=2,col='deepskyblue2')        #Dibujamos la curva ROC correspondiente a la d' de nuestro sistema evaluado
  lines(hits_na,falarms_na,lwd=1,col='black', lty=2)  #Dibujamos la función de identidad, que corresponde a una d' de 0 (Donde las distribuciones de ruido y señal se empalman por completo)
  #lines(c(0.3, 0.38),c(0.25,0.25), lwd=2, lty=1, col="deepskyblue3")      
  #text(0.3, 0.2, labels="Relaciones posibles entre Hits-F.A., dada la d'", offset=0, cex = 0.7, pos=4)
  #text(0.3, 0.1, labels="Relación Hits-F.A. registrada", offset=0, cex = 0.7, pos=4)
  #points(.25,0.1, lty=3, pch=16, col='deepskyblue4')
  text(fa_rate+0.04, h_rate-0.02, paste("d' =", round(d,4)), offset=0, cex = 0.8, pos=4)
  mtext("ROC",3,cex=3, line=-2, f=2)
  mtext("Tasa F.A.",1,cex=2, line=2.5, f=2)
  mtext("Tasa Hits",2,cex=2, line=2.5, f=2)
  mtext("Discriminabilidad alta",3,cex=3, line=-3, f=2, outer=TRUE)
}