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
archive <-'Ex2a_TODOS.csv'
datos <- read.csv(archive)

#Datos a plotear
Hits_Facil <- datos$Hr_A
Hits_Dificil <- datos$Hr_B
Hits_mtx<-matrix(data=c(Hits_Facil,Hits_Dificil), nrow=2, ncol=20, byrow=TRUE)
FA_Facil <- datos$FaR_A
FA_Dificil <- datos$FaR_B
FA_mtx<-matrix(data=c(FA_Facil,FA_Dificil), nrow=2, ncol=20, byrow=TRUE)

#Ploteamos diferencias en D'
matplot(Hits_mtx, type="b", lty=1, lwd=3, pch=21, col=c("Blue"),
        cex=1, ylim=c(0.5,1), xlim=c(0.75,2.25), xlab='Class of stimulus', ylab='D-prime',
        xaxp=c(1,2,1), las=1, labels=F)
title('Differences on D-prime')
mtext('Hit Rate',3,cex=1, col='darkblue')

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5),labels=c("0","0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5"),las=1)

matplot(FA_mtx, type="b", lty=1, lwd=3, pch=21, col=c("Blue"),
        cex=1, ylim=c(0,0.6), xlim=c(0.75,2.25), xlab='Class of stimulus', ylab='D-prime',
        xaxp=c(1,2,1), las=1, labels=F)
mtext('F.A. Rate',3,cex=1, col='darkblue')

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5),labels=c("0","0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5"),las=1)


###############################################
#Experimento2
#Archivo que contiene los datos
archivo <-'MirrEx1a_V2_TODOS.csv'
data <- read.csv(archivo)

#Datos que vamos a plotear
H_Facil <- data$Hr_A
H_Dificil <- data$Hr_B
H_mtx<-matrix(data=c(H_Facil,H_Dificil), nrow=2, ncol=21, byrow=TRUE)
Fa_Facil <- data$FaR_A
Fa_Dificil <- data$FaR_B
Fa_mtx<-matrix(data=c(Fa_Facil,Fa_Dificil), nrow=2, ncol=21, byrow=TRUE)

#Plot
matplot(H_mtx, type="b", lty=1, lwd=3, pch=21, col=c("Red"),
        cex=1, ylim=c(0.3,1), xlim=c(0.75,2.25), xlab='Class of stimulus', ylab='D-prime',
        xaxp=c(1,2,1), las=1, labels=F)
title('Differences on D-prime')
mtext('Experiment 2',3,cex=1, col='brown4')

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5),labels=c("0","0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5"),las=1)


matplot(Fa_mtx, type="b", lty=1, lwd=3, pch=21, col=c("Red"),
        cex=1, ylim=c(0,0.6), xlim=c(0.75,2.25), xlab='Class of stimulus', ylab='D-prime',
        xaxp=c(1,2,1), las=1, labels=F)
title('Differences on D-prime')
mtext('Experiment 2',3,cex=1, col='brown4')

axis(1,at=c(1,2),labels=c("A","B"),las=1)
axis(2,at=c(0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5),labels=c("0","0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5"),las=1)
