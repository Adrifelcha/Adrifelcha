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

