setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs")
rm(list=ls())
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
layout(matrix(1:2,ncol=2))
#Datos a plotear
d_Facil <- datos$d_A
d_Dificil <- datos$d_B
d_mtx<-matrix(data=c(d_Facil,d_Dificil), nrow=2, ncol=20, byrow=TRUE)

#Ploteamos diferencias en D'
matplot(d_mtx, type="b", lty=1, lwd=3, pch=21, col=c("orange3"),
        cex=1, ylim=c(0,5), xlim=c(0.75,2.25), xlab='Tipo de Estímulo', ylab='D-prima', font.lab=2, cex.lab=1,
        las=1, labels=F)
mtext('Experimento 1',3,cex=1.7, col='orange4')

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5),labels=c("0","0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5"),las=1)



###############################################
#Experimento2
#Archivo que contiene los datos
archivo <-'Ex_2Ebb_TODOS_No1.csv'
data <- read.csv(archivo)

#Datos que vamos a plotear
D_Facil <- data$d_A
D_Dificil <- data$d_B
D_mtx<-matrix(data=c(D_Facil,D_Dificil), nrow=2, ncol=20, byrow=TRUE)

#Plot
matplot(D_mtx, type="b", lty=1, lwd=3, pch=21, col=c("lightsalmon3"),
        cex=1, ylim=c(0,5), xlim=c(0.75,2.25), xlab='Tipo de Estimulo', ylab='D-prima', font.lab=2, cex.lab=1,
        las=1, labels=F)
mtext('Experimento 2',3,cex=1.7, col='lightsalmon4')

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5),labels=c("0","0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5"),las=1)
