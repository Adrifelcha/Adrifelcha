setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs")
rm(list=ls())
dir()


experimento <- 1


if (experimento ==1)
{archive <-'Ex_1Ebb_TODOS-.csv'
datos <- read.csv(archive)}

if (experimento ==2)
{archive <-'Ex_2Ebb_TODOS-.csv'
datos <- read.csv(archive)}

############## ORDENAMOS DATOS
####  RAtes
#LLamamos los datos
FA_A <- datos$FaR_A
FA_B <- datos$FaR_B
d_A <- mean(datos$d_A)
d_B <- mean(datos$d_B)
d_a <- datos$d_A
d_b <- datos$d_B
H_B <- datos$Hr_B
H_A <- datos$Hr_A
#Ordenamos los datos
Mirror_Rates <- data.frame(cbind(FA_A,FA_B,H_B,H_A))
FA_Rates <- data.frame(cbind(FA_A,FA_B))
Hits_Rates <- data.frame(cbind(H_B,H_A))
Rates_A <- data.frame(cbind(FA_A,H_A))
Rates_B <- data.frame(cbind(FA_B,H_B))
Rates <-stack(Mirror_Rates) 
FalsasAlarmas <- stack(FA_Rates)
Hits <- stack(Hits_Rates)
d_ <- data.frame(d_a,d_b)

d_null <- 0

hits_A <- c()
falarm_A <- c()
hits_B <- c()
falarm_B <- c()
hits_na <- c()
falarm_na <- c()
c <- seq(-10,10,0.1)

for (i in 1:length(c)){
  hits_A[i] <- pnorm((-d_A/2)-c[i])
  falarm_A[i] <- pnorm((d_A/2)-c[i])
  hits_B[i] <- pnorm((-d_B/2)-c[i])
  falarm_B[i] <- pnorm((d_B/2)-c[i])
  hits_na[i] <- pnorm((d_null/2)-c[i])
  falarm_na[i] <- pnorm((-d_null/2)-c[i])
}

hits_a <- c()
hits_b <- C()
falarm_a <- c()
falarm_b <- c()

for(a in 1:length(d_a)){
for (i in 1:length(c)){
  hits_a[a] <- pnorm((-d_a[a]/2)-c[i])
  falarm_a[a] <- pnorm((d_a[a]/2)-c[i])
  hits_b[a] <- pnorm((-d_b[a]/2)-c[i])
  falarm_b[a] <- pnorm((d_b[a]/2)-c[i])
}}

#points(pnorm((-d_A/2)-0),pnorm((d_A/2)-0),pch=16)

if (experimento == 1) #Demo
{plot(Rates_A, pch=16, col='deepskyblue3', xlim=c(0,1), ylim=c(0,1), xlab='', ylab='')
points(Rates_B, lty=3, pch=16, col='darkorchid3')
lines(hits_A,falarm_A,lwd=3,col='deepskyblue3')
lines(hits_B,falarm_B,lwd=3,col='darkorchid3')
lines(hits_na,falarm_na,lwd=1,col='black', lty=2)
lines(c(0.58, 0.68),c(0.3,0.3), lwd=2, lty=1, col="deepskyblue3")
lines(c(0.58, 0.68),c(0.2,0.2), lwd=2, lty=1, col="darkorchid3")
text(0.7, 0.3, labels="Mean D' for A Condition", offset=0, cex = 0.8, pos=4)
text(0.7, 0.2, labels="Mean D' for B Condition", offset=0, cex = 0.8, pos=4)
title('ROC per Condition')
mtext('Experimento 1',3,cex=.8)


#plot(Rates_A, pch=16, col='white', xlim=c(0,1), ylim=c(0,1), xlab='', ylab='')
#lines(hits_a,falarm_a,lwd=3,col='deepskyblue3')
#lines(hits_b,falarm_b,lwd=3,col='darkorchid3')
#lines(hits_na,falarm_na,lwd=1,col='black', lty=2)
#lines(c(0.58, 0.68),c(0.3,0.3), lwd=2, lty=1, col="deepskyblue3")
#lines(c(0.58, 0.68),c(0.2,0.2), lwd=2, lty=1, col="darkorchid3")
#text(0.7, 0.3, labels="Mean D' for A Condition", offset=0, cex = 0.8, pos=4)
#text(0.7, 0.2, labels="Mean D' for B Condition", offset=0, cex = 0.8, pos=4)
#title('ROC per Condition')
#mtext('Experimento 1',3,cex=.8)

}


if (experimento == 2) #Demo
{plot(Rates_A, pch=16, col='deepskyblue3', xlim=c(0,1), ylim=c(0,1), xlab='', ylab='')
  points(Rates_B, lty=3, pch=16, col='darkorchid3')
  lines(hits_A,falarm_A,lwd=2,col='deepskyblue3')
  lines(hits_B,falarm_B,lwd=2,col='darkorchid3')
  lines(hits_na,falarm_na,lwd=1, lty=2, col='black')
  lines(c(0.58, 0.68),c(0.3,0.3), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0.58, 0.68),c(0.2,0.2), lwd=2, lty=1, col="darkorchid3")
  text(0.7, 0.3, labels="Mean D' for A Condition", offset=0, cex = 0.8, pos=4)
  text(0.7, 0.2, labels="Mean D' for B Condition", offset=0, cex = 0.8, pos=4)
  title('ROC per Condition')
  mtext('Experimento 2',3,cex=.8)
}



 #Dprima/2 - c

#FA= -dprima/2-c


