setwd("C:/Users/Adrifelcha/Desktop/Felisa/Tesis/Datos_CSVs")
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
archive <-'Ex_1Ebb_TODOS.csv'
datos <- read.csv(archive)
layout(matrix(1:2,ncol=2, byrow=TRUE))

#Datos a plotear
Hits_Facil <- datos$Hr_A
Hits_Dificil <- datos$Hr_B
Hits_mtx<-matrix(data=c(Hits_Facil,Hits_Dificil), nrow=2, ncol=20, byrow=TRUE)
FA_Facil <- datos$FaR_A
FA_Dificil <- datos$FaR_B
FA_mtx<-matrix(data=c(FA_Facil,FA_Dificil), nrow=2, ncol=20, byrow=TRUE)

#Ploteamos diferencias en D'
matplot(Hits_mtx, type="b", lty=1, lwd=3, pch=21, col=c("green3"),
        cex=1, ylim=c(0.5,1.05), xlim=c(0.75,2.25), xlab='', ylab='',
        xaxp=c(1,2,1), las=1, labels=F, ann=F, axes=F)
mtext("Diferencias entre tasas de Hits y F.A.",3,cex=2.5, line=-2, f=2, outer=TRUE)
mtext("Experimento 1",3,cex=2, line=-4, f=2, outer=TRUE)
mtext('Diferencias en Hits',3,cex=2, col='green4', line=-1.6)
mtext("Clase de estímulo",1,cex=2, line=2.5, f=2)
mtext("Tasa de Hits",2,cex=2, line=2.5, f=2)
axis(2,at=c(0.5,0.6,0.7,0.8,0.9,1),labels=c("0.5","0.6","0.7","0.8","0.9","1"),las=1)
axis(1,at=c(1,2),labels=c("A","B"),las=1)


matplot(FA_mtx, type="b", lty=1, lwd=3, pch=21, col=c("indianred3"),
        cex=1, ylim=c(0,0.55), xlim=c(0.75,2.25), xlab='', ylab='',
        xaxp=c(1,2,1), las=1, labels=F, ann=F, axes=F)
mtext('Diferencias en F.A.',3,cex=2, col='indianred4', line=-1.6)
mtext("Clase de estímulo",1,cex=2, line=2.5, f=2)
mtext("Tasa de F.A.",2,cex=2, line=2.5, f=2)

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(0.0,0.1,0.2,0.3,0.4,0.5),labels=c("0","0.1","0.2","0.3","0.4","0.5"),las=1)


###############################################
#Experimento2
#Archivo que contiene los datos
archivo <-'Ex_2Ebb_TODOS_Sin1.csv'
data <- read.csv(archivo)
layout(matrix(1:2,ncol=2, byrow=TRUE))

#Datos que vamos a plotear
H_Facil <- data$Hr_A
H_Dificil <- data$Hr_B
H_mtx<-matrix(data=c(H_Facil,H_Dificil), nrow=2, ncol=20, byrow=TRUE)
Fa_Facil <- data$FaR_A
Fa_Dificil <- data$FaR_B
Fa_mtx<-matrix(data=c(Fa_Facil,Fa_Dificil), nrow=2, ncol=20, byrow=TRUE)

#Plot
matplot(H_mtx, type="b", lty=1, lwd=3, pch=21, col=c("olivedrab3"),
        cex=1, ylim=c(0.3,1.02), xlim=c(0.75,2.25), xlab='Tipo de Estímulos', ylab='Tasa de Hits',
        xaxp=c(1,2,1), las=1, labels=F, ann=F, axes=F)
mtext("Experimento 2",3,cex=2, line=-2.5, f=2, outer=TRUE)
mtext('Diferencias en Hits',3,cex=2, col='green4', line=-0.8)
mtext("Clase de estímulo",1,cex=2, line=2.5, f=2)
mtext("Tasa de Hits",2,cex=2, line=2.5, f=2)

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(0.3,0.4,0.5,0.6,0.7,0.8,0.9,1),labels=c("0.3","0.4","0.5","0.6","0.7","0.8","0.9","1"),las=1)


matplot(Fa_mtx, type="b", lty=1, lwd=3, pch=21, col=c("Red"),
        cex=1, ylim=c(0,0.52), xlim=c(0.75,2.25), xlab='Tipo de Estímulos', ylab='Tasa de F. Alarmas',
        xaxp=c(1,2,1), las=1, labels=F, ann=F, axes=F)
mtext('Diferencias en Hits',3,cex=2, col='brown4', line=-0.8)
mtext("Clase de estímulo",1,cex=2, line=2.5, f=2)
mtext("Tasa de F.A.",2,cex=2, line=2.5, f=2)

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(0.0,0.1,0.2,0.3,0.4,0.5),labels=c("0","0.1","0.2","0.3","0.4","0.5"),las=1)