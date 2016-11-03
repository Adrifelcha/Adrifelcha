setwd("C:/Users/Alejandro/Desktop/Felisa/Mirror Experiment/Mirror Experimento 1/Data_Ex1a_SinSesgo1")
rm(list=ls())
dir()

#Archivo que contiene nuestros datos
archive <-'MirrEx1a_V2_TODOS.csv'
datos <- read.csv(archive)

#####################################
#Classical Signal Detection Theory
#####################################
layout(matrix(1:3,ncol=1))

fa_A <- mean(datos$A_FA)
hits_A <- mean(datos$A_H)
fa_B <- mean(datos$B_FA)
hits_B <- mean(datos$B_H)
AN <- fa_A/160
BN <- fa_B/160
BS <- hits_B/160
AS <- hits_A/160
print(c(AN,BN, BS, AS)) 

k_A <- qnorm(1-AN,0,1)
d_A <- qnorm(AS,0,1)-qnorm(AN,0,1)
c_A <- k_A-(d_A/2)                    
beta_A <- dnorm(k_A,d_A,1)/dnorm(k_A,0,1)
k_B <- qnorm(1-BN,0,1)
d_B <-qnorm(BS,0,1)-qnorm(BN,0,1)
c_B <-k_B-(d_B/2)                    
beta_B <-dnorm(k_B,d_B,1)/dnorm(k_B,0,1)
print(c(d_A,k_A,c_A,beta_A))
print(c(d_B,k_B,c_B,beta_B))

soporte <- seq(-4,5.5,.05)
d_AN <- dnorm(soporte,0,1)
d_AS <- dnorm(soporte,d_A,1)
d_BN <- dnorm(soporte,0,1)
d_BS <- dnorm(soporte,d_B,1)
  
d_A<-round(d_A,4)
d_B<-round(d_B,4)
k_A<-round(k_A,4)
k_B<-round(k_B,4)
c_A<-round(c_A,4)
c_B<-round(c_B,4)
beta_A<-round(beta_A,4)
beta_B<-round(beta_B,4)
Hr_as<-round(AS,4)
FAr_an<-round(AN,4)
Hr_bs<-round(BS,4)
FAr_bn<-round(BN,4)

#One single Noise Distribution
plot(soporte,d_AN,type='l', lwd=2, lty=6, col='black', yaxt='n', ann=F)
lines(soporte,d_AS,type='l', lwd=2, col='deepskyblue2')
abline(v=k_A,col='blue4')
text(-3.4,0.25,paste("K = ",k_A))
text(-3.4,0.20,paste("C = ",c_A))
text(-3.4,0.15,paste("D' = ",d_A))
text(-3.4,0.39,paste("Hits = ",Hr_as))
text(-3.4,0.34,paste("F.A = ",FAr_an))
  
plot(soporte,d_BN,type='l', lwd=2, lty=6, col='black', yaxt='n', ann=F)
lines(soporte,d_BS, type='l', lwd=2, col='darkorchid2')
abline(v=k_B, col='purple')
text(-3.4,0.25,paste("K = ",k_B))
text(-3.4,0.20,paste("C = ",c_B))
text(-3.4,0.15,paste("D' = ",d_B))
text(-3.4,0.39,paste("Hits = ",Hr_bs))
text(-3.4,0.34,paste("F.A = ",FAr_an))
  
plot(soporte,d_BN,type='l', lwd=2, lty=1, col='black', yaxt='n', ann=F)
lines(soporte,d_BS, type='l', lwd=2, col='darkorchid2')
abline(v=k_B, col='purple', lwd=1, lty=3)
abline(v=k_A, col='blue', lwd=1, lty=3)
lines(soporte,d_AN, type='l', lwd=2, lty=6, col='gray')
lines(soporte,d_AS, type='l', lwd=2, col='deepskyblue2')
abline(v=k_B, col='darkorchid2')
text(-3,.3,paste('AS'),cex=2,col='deepskyblue2')
text(-3,.2,paste('BS'),cex=2,col='darkorchid2')
title("Classical SDT: Mean Performance for Experiment 1", outer = TRUE, line = -2, cex=3)

#####################################
#Mirror Effect
#####################################

layout(matrix(1:2,ncol=1))

AN<- (mean(datos$A_FA)/160)
BN<- (mean(datos$B_FA)/160)
BS<- (mean(datos$B_H)/160)
AS<- (mean(datos$A_H)/160)
C_AN <- (mean(datos$R_AN))
C_BN <- (mean(datos$R_BN))
C_BS <- (mean(datos$R_BS))
C_AS <- (mean(datos$R_AS))
Confidence <- c(C_AN, C_BN, C_BS, C_AS)
Rates <- c(AN,BN,BS,AS)
print(Rates)
print(Confidence)

k <- qnorm(1-AN,0,1)
d_A <- qnorm(AS,0,1)-qnorm(AN,0,1)
d_BN <- qnorm(BN,0,1)-qnorm(AN,0,1)
d_BS <- (qnorm(BS,0,1)-qnorm(AN,0,1))
c <- k-(d_A/2)                    
print(c(k,d_A,d_BN,d_BS))

#  fa_AN6 <- sum(jaime$FR6[jaime$Estimulo>=161&jaime$Estimulo<=320])/160
#  fa_BN6 <- sum(jaime$FR6[jaime$Estimulo>=481&jaime$Estimulo<=640])/160
#  h_AS6 <- sum(jaime$HR6[jaime$Estimulo>=1&jaime$Estimulo<=160])/160
#  h_BS6 <- sum(jaime$HR6[jaime$Estimulo>=321&jaime$Estimulo<=480])/160
#  fa_AN5 <- sum(jaime$FR5[jaime$Estimulo>=161&jaime$Estimulo<=320])/160
#  fa_BN5 <- sum(jaime$FR5[jaime$Estimulo>=481&jaime$Estimulo<=640])/160
#  h_AS5 <- sum(jaime$HR5[jaime$Estimulo>=1&jaime$Estimulo<=160])/160
#  h_BS5 <- sum(jaime$HR5[jaime$Estimulo>=321&jaime$Estimulo<=480])/160
#  fa_AN4 <- sum(jaime$FR4[jaime$Estimulo>=161&jaime$Estimulo<=320])/160
#  fa_BN4 <- sum(jaime$FR4[jaime$Estimulo>=481&jaime$Estimulo<=640])/160
#  h_AS4 <- sum(jaime$HR4[jaime$Estimulo>=1&jaime$Estimulo<=160])/160
#  h_BS4 <- sum(jaime$HR4[jaime$Estimulo>=321&jaime$Estimulo<=480])/160
#  fa_AN3 <- sum(jaime$FR3[jaime$Estimulo>=161&jaime$Estimulo<=320])/160
#  fa_BN3 <- sum(jaime$FR3[jaime$Estimulo>=481&jaime$Estimulo<=640])/160
#  h_AS3 <- sum(jaime$HR3[jaime$Estimulo>=1&jaime$Estimulo<=160])/160
#  h_BS3 <- sum(jaime$HR3[jaime$Estimulo>=321&jaime$Estimulo<=480])/160
#  fa_AN2 <- sum(jaime$FR2[jaime$Estimulo>=161&jaime$Estimulo<=320])/160
#  fa_BN2 <- sum(jaime$FR2[jaime$Estimulo>=481&jaime$Estimulo<=640])/160
#  h_AS2 <- sum(jaime$HR2[jaime$Estimulo>=1&jaime$Estimulo<=160])/160
#  h_BS2 <- sum(jaime$HR2[jaime$Estimulo>=321&jaime$Estimulo<=480])/160
#  fa_AN1 <- sum(jaime$FR1[jaime$Estimulo>=161&jaime$Estimulo<=320])/160
#  fa_BN1 <- sum(jaime$FR1[jaime$Estimulo>=481&jaime$Estimulo<=640])/160
#  h_AS1 <- sum(jaime$HR1[jaime$Estimulo>=1&jaime$Estimulo<=160])/160
#  h_BS1 <- sum(jaime$HR1[jaime$Estimulo>=321&jaime$Estimulo<=480])/160
#fa_AN6 <- round(fa_AN6,3)
#fa_BN6 <- round(fa_BN6,3)
#h_AS6 <- round(h_AS6,3)
#h_BS6 <- round(h_BS6,3)
# fa_AN5 <- round(fa_AN5,3)
#fa_BN5 <- round(fa_BN5,3)
#h_AS5 <- round(h_AS5,3)
#h_BS5 <- round(h_BS5,3)
#fa_AN4 <- round(fa_AN4,3)
#fa_BN4 <- round(fa_BN4,3)
# h_AS4 <- round(h_AS4,3)
#  h_BS4 <- round(h_BS4,3)
#  fa_AN3 <- round(fa_AN3,3)
#  fa_BN3 <- round(fa_BN3,3)
#  h_AS3 <- round(h_AS3,3)
#  h_BS3 <- round(h_BS3,3)
#  fa_AN2 <- round(fa_AN2,3)
#  fa_BN2 <- round(fa_BN2,3)
#  h_AS2 <- round(h_AS2,3)
#  h_BS2 <- round(h_BS2,3)
#  fa_AN1 <- round(fa_AN1,3)
#  fa_BN1 <- round(fa_BN1,3)
#  h_AS1 <- round(h_AS1,3)
#  h_BS1 <- round(h_BS1,3)
#  print(c(h_AS6[length(h_AS6)], h_AS5[length(h_AS5)], h_AS4[length(h_AS4)],           h_AS3[length(h_AS3)],          h_AS2[length(h_AS2)],         h_AS1[length(h_AS1)],           h_BS6[length(h_BS6)],          h_BS5[length(h_BS5)],           h_BS4[length(h_BS4)],           h_BS3[length(h_BS3)],          h_BS2[length(h_BS5)],           h_BS1[length(h_BS1)],          fa_AN6[length(fa_AN6)],          fa_AN5[length(fa_AN5)], fa_AN4[length(fa_AN4)],           fa_AN3[length(fa_AN3)],          fa_AN2[length(fa_AN2)],           fa_AN1[length(fa_AN1)],           fa_BN6[length(fa_BN6)],          fa_BN5[length(fa_BN5)],           fa_BN4[length(fa_BN4)],           fa_BN3[length(fa_BN3)],          fa_BN2[length(fa_BN5)]))  
#  k1 <- qnorm(1-fa_AN1,0,1)
 # k2 <- qnorm(1-fa_AN2,0,1)
  #k3 <- qnorm(1-fa_AN3,0,1)
#  k4 <- qnorm(1-h_AS4,d_A,1)
#  k5 <- qnorm(1-h_AS5,d_A,1)
#  k6 <- qnorm(1-h_AS6,d_A,1)
  
  dif_A <-d_A-0
  dif_B <-d_BS-d_BN
  print(c(dif_A, dif_B))
  
  soporte <- seq(-4,5.5,.05)
  dis_AN <- dnorm(soporte,0,1)
  dis_AS <- dnorm(soporte,d_A,1)
  dis_BN <- dnorm(soporte,d_BN,1)
  dis_BS <- dnorm(soporte,d_BS,1)
  
  d_A<-round(d_A,4)
  d_BN<-round(d_BN,4)
  d_BS<-round(d_BS,4)
  k<-round(k,4)
  c<-round(c,4)
  #c_B<-round(c_B,3)
  #beta_A<-round(beta_A,3)
  #beta_B<-round(beta_B,3)
  Hr_as<-round(AS,4)
  FAr_an<-round(AN,4)
  Hr_bs<-round(BS,4)
  FAr_bn<-round(BN,4)
  Y_AN <-round((AN*160),4)
  Y_BN <-round((BN*160),4)
  Y_BS <-round((BS*160),4)
  Y_AS <-round((AS*160),4)
  CR_AN <-round(C_AN,4)
  CR_BN <-round(C_BN,4)
  CR_BS <-round(C_BS,4)
  CR_AS <-round(C_AS,4)
  
  plot(AN,type='o',pch=16,col='white',ylim=c(0,10), yaxt='n', xaxt='n', ann=F)
  axis(1,at=c(0.7,0.9,1.1,1.3),labels=c("AN","BN","BS","AS"))
  axis(2,at=c(2.5,7.5),labels=c("Rate","No."),las=0)
  abline(5,c(0.1,0.1), col="black",lwd=1)
  abline(v=.8,h=c(-10,15),col='black')
  abline(v=1,h=c(-10,15),col='black')
  abline(v=1.2,h=c(-10,15),col='black')
  text(.7,2.5,paste(FAr_an),cex=1,col='royalblue4')
  text(.9,2.5,paste(FAr_bn),cex=1,col='royalblue4')
  text(1.1,2.5,paste(Hr_bs),cex=1,col='royalblue4')
  text(1.3,2.5,paste(Hr_as),cex=1,col='royalblue4')
  text(.7,7.5,paste(Y_AN),cex=1,col='lightblue4')
  text(.9,7.5,paste(Y_BN),cex=1,col='lightblue4')
  text(1.1,7.5,paste(Y_BS),cex=1,col='lightblue4')
  text(1.3,7.5,paste(Y_AS),cex=1,col='lightblue4')
  title("Mirror Effect", outer = TRUE, line = -2, cex=2)
  mtext('Mean Performance for Experiment 1',cex=0.8)
  
  
  plot(soporte,dis_AN,type='l', lwd=2, lty=1, col='deepskyblue3', yaxt='n', ann=F)
  lines(soporte,dis_AS,type='l', lwd=2, col='deepskyblue2')
  lines(soporte,dis_BN,type='l', lwd=2, lty=1, col='darkorchid3')
  lines(soporte,dis_BS, type='l', lwd=2, col='darkorchid2')
  abline(v=k,col='black', lwd=2)
  #abline(v=k1,col='red', lty=6, lwd=2)
  text(-3,0.15,paste("K = ",k))
  #text(-2.5,0.35,paste("1"), col='red')
  #text(-3.4,0.15,paste("D' = ",d_B))
  #text(-3.4,0.39,paste("Hits = ",Hr_bs))
  #text(-3.4,0.34,paste("F.A = ",FAr_bn))
  
  ####### Confidence Rating
  
  plot(Confidence,type='o',pch=16,col='white',ylim=c(0,6), yaxt='n', xaxt='n', ann=F)
  #axis(1,at=c(0,6),labels=c("AN","BN","BS","AS"), col='white')
  #axis(2,at=c(2.5,7.5),labels=c("Rate","No."),las=0)
  abline(3,c(0.1,0.1), col="black",lwd=1)
  abline(v=1.75,h=c(-10,15),col='black')
  abline(v=2.5,h=c(-10,15),col='black')
  abline(v=3.4,h=c(-10,15),col='black')
  text(1.3,1.5,paste(CR_AN),cex=1,col='royalblue4')
  text(2.2,1.5,paste(CR_BN),cex=1,col='royalblue4')
  text(2.9,1.5,paste(CR_BS),cex=1,col='royalblue4')
  text(3.75,1.5,paste(CR_AS),cex=1,col='royalblue4')
  text(1.3,4.5,paste('R(AN)'),cex=1,col='royalblue4')
  text(2.2,4.5,paste('R(BN)'),cex=1,col='royalblue4')
  text(2.9,4.5,paste('R(BS)'),cex=1,col='royalblue4')
  text(3.75,4.5,paste('R(AS)'),cex=1,col='royalblue4')
  mtext(archive,3,cex=.8)
  #text(1.5,.8,paste('Hits & F.A. rate'),cex=1,col='blue',f=2)
  #mtext(archive,3,cex=.8)
  title("Confidence Rating", outer = TRUE, line = -2)
  #points(hits,type='o',pch=16,col='black')
  
  plot(soporte,dis_AN,type='l', lwd=1.5, lty=1, col='black', yaxt='n', ann=F)
  lines(soporte,dis_AS,type='l', lwd=1.5, col='black')
  lines(soporte,dis_BN,type='l', lwd=1.5, lty=1, col='black')
  lines(soporte,dis_BS, type='l', lwd=1.5, col='black')
  #abline(v=k,col='black', lwd=2)
  #abline(v=k1,col='red', lty=6, lwd=2)
  #abline(v=k2,col='forestgreen', lty=2, lwd=2)
  #abline(v=k3,col='darkgreen', lty=2, lwd=2)
  #abline(v=k4,col='black', lty=1, lwd=2)
  #abline(v=k5,col='darkgoldenrod3', lty=2, lwd=2)
  #abline(v=k6,col='orange', lty=2, lwd=2)
  text(-3.7,0.15,paste("K = ",k))
  #text(-2,0.25,paste("6"), col='orange')
  #text(-2,0.3,paste("5"), col='darkgoldenrod3')
  #text(-2.5,0.3,paste("4"), col='black')
  #text(-3,0.3,paste("3"), col='darkgreen')
  #text(-3,0.35,paste("2"), col='forestgreen')
  #text(-2.5,0.35,paste("1"), col='red')
  #text(-3.4,0.15,paste("D' = ",d_B))
  text(-3,0.39,paste("Hits = ",Hr_bs))
  text(-3,0.34,paste("F.A = ",FAr_bn))


  plot(Confidence,type='o',pch=16,col='white',ylim=c(0,6), yaxt='n', xaxt='n', ann=F)
  #axis(1,at=c(0,6),labels=c("AN","BN","BS","AS"), col='white')
  #axis(2,at=c(2.5,7.5),labels=c("Rate","No."),las=0)
  abline(3,c(0.1,0.1), col="black",lwd=1)
  abline(v=1.75,h=c(-10,15),col='black')
  abline(v=2.5,h=c(-10,15),col='black')
  abline(v=3.4,h=c(-10,15),col='black')
  text(1.3,1.5,paste(CR_AN),cex=1,col='royalblue4')
  text(2.2,1.5,paste(CR_BN),cex=1,col='royalblue4')
  text(2.9,1.5,paste(CR_BS),cex=1,col='royalblue4')
  text(3.75,1.5,paste(CR_AS),cex=1,col='royalblue4')
  text(1.3,4.5,paste('R(AN)'),cex=1,col='maroon2')
  text(2.2,4.5,paste('R(BN)'),cex=1,col='maroon2')
  text(2.9,4.5,paste('R(BS)'),cex=1,col='maroon2')
  text(3.75,4.5,paste('R(AS)'),cex=1,col='maroon2')
  mtext(archive,3,cex=.8)
  #text(1.5,.8,paste('Hits & F.A. rate'),cex=1,col='blue',f=2)
  #mtext(archive,3,cex=.8)
  title("Confidence Rating", outer = TRUE, line = -2)
  #points(hits,type='o',pch=16,col='black')
  
  plot(Confidence,type='o',pch=16,col='maroon2',ylim=c(0,6),axes=F , ann=F)
  axis(1,at=1:4,labels=c('AN','BN','BS','BN'))
  axis(2,at=c(0, 1, 2, 3, 4, 5, 6),labels=c("0","1", "2","3","4","5","6"),las=1)
  text(1.1,C_AN+.5,paste(CR_AN),cex=.8,col='violetred',f=2)
  text(1.9,C_BN+.5,paste(CR_BN),cex=.8,col='violetred',f=2)
  text(3.1,C_BS+.5,paste(CR_BS),cex=.8,col='violetred',f=2)
  text(3.9,C_BS+.5,paste(CR_AS),cex=.8,col='violetred',f=2)
  text(1.5,5.5,paste('Confidence Rate'),cex=1,col='violetred4',f=2)
