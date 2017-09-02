setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs")
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



#Ploteamos diferencias en Ratings
matplot(Signal_mtx, type="b", lty=1, lwd=3, pch=21, col=c("darkslategray4"),
        cex=1, ylim=c(4,6), xlim=c(0.75,2.25), xlab="Clase de Estímulo", ylab="Puntaje promedio",
        xaxp=c(1,2,1), las=1, labels=F)
title('Experimento 1', outer = TRUE, font=3, line = -1.5)
mtext('Estímulos con Señal',3,cex=1.2, col='darkslategray4',font=2)
axis(2,at=c(4,4.5,5,5.5,6),labels=c("4","4.5","5","5.5","6"),las=1)
axis(1,at=c(1,2),labels=c("A","B"),las=1)


matplot(Noise_mtx, type="b", lty=1, lwd=3, pch=21, col=c("deepskyblue4"),
        cex=1, ylim=c(1,3.5), xlim=c(0.75,2.25), xlab='Clase de Estímulo', ylab='',
        xaxp=c(1,2,1), las=1, labels=F)
mtext('Estímulos con Ruido',3,cex=1.2, font=2, col='deepskyblue4')

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(1,1.5,2,2.5,3,3.5),labels=c("1","1.5","2","2.5","3","3.5"),las=1)


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
matplot(Signal_mtx, type="b", lty=1, lwd=3, pch=21, col=c("deeppink3"),
        cex=1, ylim=c(2.5,6), xlim=c(0.75,2.25), xlab="Clase de Estímulo", ylab="Puntaje promedio",
        xaxp=c(1,2,1), las=1, labels=F)
title('Experimento 2', outer = TRUE, font=3, line = -1.5)
mtext('Estímulos con Señal',3,cex=1.2, col='deeppink3',font=2)
axis(2,at=c(3,3.5,4,4.5,5,5.5,6),labels=c("3","3.5","4","4.5","5","5.5","6"),las=1)
axis(1,at=c(1,2),labels=c("A","B"),las=1)


matplot(Noise_mtx, type="b", lty=1, lwd=3, pch=21, col=c("deeppink4"),
        cex=1, ylim=c(1,4), xlim=c(0.75,2.25), xlab='Clase de Estímulo', ylab='',
        xaxp=c(1,2,1), las=1, labels=F)
mtext('Estímulos con Ruido',3,cex=1.2, font=2, col='deeppink4')

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(1,1.5,2,2.5,3,3.5,4),labels=c("1","1.5","2","2.5","3","3.5","4"),las=1)