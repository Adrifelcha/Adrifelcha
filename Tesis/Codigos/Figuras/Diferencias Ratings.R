setwd("C:/Users/Adrifelcha/Desktop/Felisa/Tesis/CSVs")
rm(list=ls())
#layout(matrix(1:2,ncol=1))
dir()
######################################################
######################################################
#PLOT: Diferencias en D'
#Comprobando la existencia de dos condiciones DIFERENTES



########################################################
#Experimento 1
#Archivo que contiene todos los datos
archive <-'Ex_1Ebb_TODOS-.csv'
datos <- read.csv(archive)
layout(matrix(1:2,ncol=2, byrow=TRUE))

#Datos a plotear
C_AS <- datos$R_AS
C_BS <- datos$R_BS
Signal_mtx <-matrix(data=c(C_AS,C_BS), nrow=2, ncol=20, byrow=TRUE)
C_AN <- datos$R_AN
C_BN <- datos$R_BN
Noise_mtx <-matrix(data=c(C_AN,C_BN), nrow=2, ncol=20, byrow=TRUE)
Confidence <- c(C_AN, C_BN, C_BS, C_AS)



#Ploteamos diferencias en D'
matplot(Signal_mtx, type="b", lty=1, lwd=3, pch=21, col=c("green3"),
        cex=1, ylim=c(2,6), xlim=c(0.75,2.25), xlab='Tipo de Estímulo', ylab='Tasa de Hits',
        xaxp=c(1,2,1), las=1, labels=F)
title('Experimento 1', outer = TRUE, font=1, line = -1.5)
mtext('Diferencias en Hits',3,cex=1.2, col='green4')
axis(2,at=c(0.5,0.6,0.7,0.8,0.9,1),labels=c("0.5","0.6","0.7","0.8","0.9","1"),las=1)
axis(1,at=c(1,2),labels=c("A","B"),las=1)


matplot(Noise_mtx, type="b", lty=1, lwd=3, pch=21, col=c("indianred3"),
        cex=1, ylim=c(1,4), xlim=c(0.75,2.25), xlab='Tipo de Estímulo', ylab='Tasa de F. Alarmas',
        xaxp=c(1,2,1), las=1, labels=F)
mtext('Diferencias en F. Alarmas',3,cex=1.2, col='Red')

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(0.0,0.1,0.2,0.3,0.4,0.5),labels=c("0","0.1","0.2","0.3","0.4","0.5"),las=1)


###############################################
#Experimento2
#Archivo que contiene los datos
archivo <-'Ex_2Ebb_TODOS_No1.csv'
data <- read.csv(archivo)
layout(matrix(1:2,ncol=2, byrow=TRUE))

#Datos que vamos a plotear
C_AS <- data$R_AS
C_BS <- data$R_BS
Signal_mtx <-matrix(data=c(C_AS,C_BS), nrow=2, ncol=20, byrow=TRUE)
C_AN <- data$R_AN
C_BN <- data$R_BN
Noise_mtx <-matrix(data=c(C_AN,C_BN), nrow=2, ncol=20, byrow=TRUE)
Confidence <- c(C_AN, C_BN, C_BS, C_AS)

#Plot
matplot(Signal_mtx, type="b", lty=1, lwd=3, pch=21, col=c("olivedrab3"),
        cex=1, ylim=c(3,6), xlim=c(0.75,2.25), xlab='Tipo de Estímulos', ylab='Tasa de Hits',
        xaxp=c(1,2,1), las=1, labels=F)
mtext('Diferencias en Hits',3,cex=1, col='olivedrab4')

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(0.3,0.4,0.5,0.6,0.7,0.8,0.9,1),labels=c("0.3","0.4","0.5","0.6","0.7","0.8","0.9","1"),las=1)


matplot(Noise_mtx, type="b", lty=1, lwd=3, pch=21, col=c("Red"),
        cex=1, ylim=c(0,4), xlim=c(0.75,2.25), xlab='Tipo de Estímulos', ylab='Tasa de F. Alarmas',
        xaxp=c(1,2,1), las=1, labels=F)
title('Experimento 2', outer = TRUE, font=1, line = -1.5)
mtext('Diferencias en F. Alarmas',3,cex=1, col='brown4')

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(0.0,0.1,0.2,0.3,0.4,0.5),labels=c("0","0.1","0.2","0.3","0.4","0.5"),las=1)