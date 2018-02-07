rm(list=ls())

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

############################################################

rm(list=ls())

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
text(1.7,.25,paste("Z =", round(qnorm(.841,0,1),3)), cex=1.5, col='black', f=2)
text(-0.2,.43,"Ruido",cex=2.5,col='black',f=2)
text(2.2,.43,"Señal",cex=2.5,col='black',f=1)
mtext("Evidencia",1,cex=2, line=2.5, f=2)
mtext("Localización del Criterio",3,cex=3, line=-2, f=2)




############################################################

rm(list=ls())
layout(matrix(1:2,ncol=2))

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
text(1.7,.25,paste("Z =", round(qnorm(.841,0,1),3)), cex=1.5, col='black', f=2)
text(-0.2,.43,"Ruido",cex=2.5,col='black',f=2)
text(2.2,.43,"Señal",cex=2.5,col='black',f=1)
mtext("Evidencia",1,cex=2, line=2.5, f=2)
mtext("Beta",3,cex=3, line=-2, f=2)

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
text(1.7,.25,paste("Z =", round(qnorm(.841,0,1),3)), cex=1.5, col='black', f=2)
text(-0.2,.43,"Ruido",cex=2.5,col='black',f=2)
text(2.2,.43,"Señal",cex=2.5,col='black',f=1)
mtext("Evidencia",1,cex=2, line=2.5, f=2)
mtext("C",3,cex=3, line=-2, f=2)
mtext("Sesgo Liberal",3,cex=3, line=-2, f=2, outer=TRUE)
