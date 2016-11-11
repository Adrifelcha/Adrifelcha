setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs/Datos_Exp1")
rm(list=ls())
dir()
#####################################
#####################################
#####################################
#Classical Signal Detection Theory
#####################################
#####################################
#####################################


rm(list=ls())
layout(matrix(1:3,ncol=1))
for(archive in dir()){
  jaime <- read.csv(archive)
  fa_AN <- NULL
  hits_AN <- NULL
  fa_AS <- NULL
  fa_AS <- NULL
  hits_AN <- NULL
  hits_AS <- NULL
  hits_BS <- NULL
  hits_BN <- NULL
  { fa_AN <- sum(jaime$Falsas.alarmas[jaime$Estimulo>=161&jaime$Estimulo<=320]=='True')
  fa_AS <- sum(jaime$Falsas.alarmas[jaime$Estimulo>=1&jaime$Estimulo<=160]=='True')
  hits_AS <- sum(jaime$Hits[jaime$Estimulo>=1&jaime$Estimulo<=160]=='True')
  hits_AN <- sum(jaime$Hits[jaime$Estimulo>=161&jaime$Estimulo<=320]=='True')
  fa_BN <- sum(jaime$Falsas.alarmas[jaime$Estimulo>=481&jaime$Estimulo<=640]=='True')
  fa_BS <- sum(jaime$Falsas.alarmas[jaime$Estimulo>=321&jaime$Estimulo<=480]=='True')
  hits_BS <- sum(jaime$Hits[jaime$Estimulo>=321&jaime$Estimulo<=480]=='True')
  hits_BN <- sum(jaime$Hits[jaime$Estimulo>=481&jaime$Estimulo<=640]=='True')
  FAr_an <- fa_AN/160 
  Hr_as <- hits_AS/160
  FAr_bn <- fa_BN/160
  Hr_bs <- hits_BS/160
  print(c(fa_AN[length(fa_AN)], 
          FAr_an[length(FAr_an)], 
          fa_BN[length(fa_BN)], 
          FAr_bn[length(FAr_bn)], 
          hits_BS[length(hits_BS)], 
          Hr_bs[length(Hr_bs)], 
          hits_AS[length(hits_AS)], 
          Hr_as[length(Hr_as)]))
  k_A <- qnorm(1-FAr_an,0,1)
  d_A <- qnorm(Hr_as,0,1)-qnorm(FAr_an,0,1)
  c_A <- k_A-(d_A/2)                    
  beta_A <- dnorm(k_A,d_A,1)/dnorm(k_A,0,1)
  k_B <- qnorm(1-FAr_bn,0,1)
  d_B <-qnorm(Hr_bs,0,1)-qnorm(FAr_bn,0,1)
  c_B <-k_B-(d_B/2)                    
  beta_B <-dnorm(k_B,d_B,1)/dnorm(k_B,0,1)
  print(c(k_A[length(k_A)], 
          k_B[length(k_B)], 
          d_A[length(d_A)], 
          d_B[length(d_B)], 
          c_A[length(c_A)], 
          c_B[length(c_B)], 
          beta_A[length(hits_AS)], 
          beta_B[length(Hr_as)]))
  
  }
  soporte <- seq(-4,7,.05)
  d_AN <- dnorm(soporte,0,1)
  d_AS <- dnorm(soporte,d_A,1)
  d_BN <- dnorm(soporte,0,1)
  d_BS <- dnorm(soporte,d_B,1)
  
  d_A<-round(d_A,3)
  d_B<-round(d_B,3)
  k_A<-round(k_A,3)
  k_B<-round(k_B,3)
  c_A<-round(c_A,3)
  c_B<-round(c_B,3)
  beta_A<-round(beta_A,3)
  beta_B<-round(beta_B,3)
  Hr_as<-round(Hr_as,3)
  FAr_an<-round(FAr_an,3)
  Hr_bs<-round(Hr_bs,3)
  FAr_bn<-round(FAr_bn,3)
  
  #CLASSICAL SDT : One single Noise Distribution
  plot(soporte,d_AN,type='l', lwd=2, lty=6, col='black', yaxt='n', ann=F)
  lines(soporte,d_AS,type='l', lwd=2, col='deepskyblue2')
  abline(v=k_A,col='blue4')
  mtext(archive,3,cex=.7)
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
  text(-3.4,0.34,paste("F.A = ",FAr_bn))
  
  plot(soporte,d_BN,type='l', lwd=2, lty=1, col='black', yaxt='n', ann=F)
  lines(soporte,d_BS, type='l', lwd=2, col='darkorchid2')
  abline(v=k_B, col='purple', lwd=1, lty=3)
  abline(v=k_A, col='blue', lwd=1, lty=3)
  lines(soporte,d_AN, type='l', lwd=2, lty=6, col='gray')
  lines(soporte,d_AS, type='l', lwd=2, col='deepskyblue2')
  abline(v=k_B, col='darkorchid2')
  text(-3.7,.3,paste('AS'),cex=1,col='deepskyblue2')
  text(-3.7,.35,paste('BS'),cex=1,col='darkorchid2')
  title("Classical SDT", outer = TRUE, line = -2, cex=2)
}

#####################################
#####################################
#####################################
#Mirror Effect
#####################################
#####################################
#####################################

rm(list=ls())
layout(matrix(1:2,ncol=1))
for(archive in dir()){
  jaime <- read.csv(archive)
  fa_AN <- NULL
  hits_AN <- NULL
  fa_AS <- NULL
  fa_BN <- NULL
  fa_BS <- NULL
  hits_AS <- NULL
  hits_BS <- NULL
  hits_BN <- NULL
  C_AS <- NULL
  C_AN <- NULL
  C_BS <- NULL
  C_BN <- NULL
  { fa_AN <- sum(jaime$Falsas.alarmas[jaime$Estimulo>=161&jaime$Estimulo<=320]=='True')
  fa_AS <- sum(jaime$Falsas.alarmas[jaime$Estimulo>=1&jaime$Estimulo<=160]=='True')
  hits_AS <- sum(jaime$Hits[jaime$Estimulo>=1&jaime$Estimulo<=160]=='True')
  hits_AN <- sum(jaime$Hits[jaime$Estimulo>=161&jaime$Estimulo<=320]=='True')
  fa_BN <- sum(jaime$Falsas.alarmas[jaime$Estimulo>=481&jaime$Estimulo<=640]=='True')
  fa_BS <- sum(jaime$Falsas.alarmas[jaime$Estimulo>=321&jaime$Estimulo<=480]=='True')
  hits_BS <- sum(jaime$Hits[jaime$Estimulo>=321&jaime$Estimulo<=480]=='True')
  hits_BN <- sum(jaime$Hits[jaime$Estimulo>=481&jaime$Estimulo<=640]=='True')
  FAr_an <- fa_AN/160 
  Hr_as <- hits_AS/160
  FAr_bn <- fa_BN/160
  Hr_bs <- hits_BS/160
  C_AS <- sum(jaime$Confidence[jaime$tipo=='4 AS'])/160
  C_AN <- sum(jaime$Confidence[jaime$tipo=='1 AN'])/160
  C_BS <- sum(jaime$Confidence[jaime$tipo=='3 BS'])/160
  C_BN <- sum(jaime$Confidence[jaime$tipo=='2 BN'])/160
  Confidence <- c(C_AN, C_BN, C_BS, C_AS)
  #print(c(fa_AN[length(fa_AN)], 
  #        FAr_an[length(FAr_an)], 
  #        fa_BN[length(fa_BN)], 
  #        FAr_bn[length(FAr_bn)], 
  #        hits_BS[length(hits_BS)], 
  #        Hr_bs[length(Hr_bs)], 
  #        hits_AS[length(hits_AS)], 
  #        Hr_as[length(Hr_as)]))
  k <- qnorm(1-FAr_an,0,1)
  d_A <- qnorm(Hr_as,0,1)-qnorm(FAr_an,0,1)
  d_BN <- qnorm(FAr_bn,0,1)-qnorm(FAr_an,0,1)
  d_BS <- (qnorm(Hr_bs,0,1)-qnorm(FAr_bn,0,1))+d_BN
  c <- k-(d_A/2)                    
  #  beta_A <- dnorm(k_A,d_A,1)/dnorm(k_A,0,1)
  #  beta_B <-dnorm(k_B,d_B,1)/dnorm(k_B,0,1)
  print(c(k[length(k)], 
          d_A[length(d_A)], 
          d_BN[length(d_BN)], 
          d_BS[length(d_BS)], 
          c[length(c)]))
  fa_AN6 <- sum(jaime$FR6[jaime$Estimulo>=161&jaime$Estimulo<=320])/160
  fa_BN6 <- sum(jaime$FR6[jaime$Estimulo>=481&jaime$Estimulo<=640])/160
  h_AS6 <- sum(jaime$HR6[jaime$Estimulo>=1&jaime$Estimulo<=160])/160
  h_BS6 <- sum(jaime$HR6[jaime$Estimulo>=321&jaime$Estimulo<=480])/160
  fa_AN5 <- sum(jaime$FR5[jaime$Estimulo>=161&jaime$Estimulo<=320])/160
  fa_BN5 <- sum(jaime$FR5[jaime$Estimulo>=481&jaime$Estimulo<=640])/160
  h_AS5 <- sum(jaime$HR5[jaime$Estimulo>=1&jaime$Estimulo<=160])/160
  h_BS5 <- sum(jaime$HR5[jaime$Estimulo>=321&jaime$Estimulo<=480])/160
  fa_AN4 <- sum(jaime$FR4[jaime$Estimulo>=161&jaime$Estimulo<=320])/160
  fa_BN4 <- sum(jaime$FR4[jaime$Estimulo>=481&jaime$Estimulo<=640])/160
  h_AS4 <- sum(jaime$HR4[jaime$Estimulo>=1&jaime$Estimulo<=160])/160
  h_BS4 <- sum(jaime$HR4[jaime$Estimulo>=321&jaime$Estimulo<=480])/160
  fa_AN3 <- sum(jaime$FR3[jaime$Estimulo>=161&jaime$Estimulo<=320])/160
  fa_BN3 <- sum(jaime$FR3[jaime$Estimulo>=481&jaime$Estimulo<=640])/160
  h_AS3 <- sum(jaime$HR3[jaime$Estimulo>=1&jaime$Estimulo<=160])/160
  h_BS3 <- sum(jaime$HR3[jaime$Estimulo>=321&jaime$Estimulo<=480])/160
  fa_AN2 <- sum(jaime$FR2[jaime$Estimulo>=161&jaime$Estimulo<=320])/160
  fa_BN2 <- sum(jaime$FR2[jaime$Estimulo>=481&jaime$Estimulo<=640])/160
  h_AS2 <- sum(jaime$HR2[jaime$Estimulo>=1&jaime$Estimulo<=160])/160
  h_BS2 <- sum(jaime$HR2[jaime$Estimulo>=321&jaime$Estimulo<=480])/160
  fa_AN1 <- sum(jaime$FR1[jaime$Estimulo>=161&jaime$Estimulo<=320])/160
  fa_BN1 <- sum(jaime$FR1[jaime$Estimulo>=481&jaime$Estimulo<=640])/160
  h_AS1 <- sum(jaime$HR1[jaime$Estimulo>=1&jaime$Estimulo<=160])/160
  h_BS1 <- sum(jaime$HR1[jaime$Estimulo>=321&jaime$Estimulo<=480])/160
  #
  fa_AN6 <- round(fa_AN6,3)
  fa_BN6 <- round(fa_BN6,3)
  h_AS6 <- round(h_AS6,3)
  h_BS6 <- round(h_BS6,3)
  fa_AN5 <- round(fa_AN5,3)
  fa_BN5 <- round(fa_BN5,3)
  h_AS5 <- round(h_AS5,3)
  h_BS5 <- round(h_BS5,3)
  fa_AN4 <- round(fa_AN4,3)
  fa_BN4 <- round(fa_BN4,3)
  h_AS4 <- round(h_AS4,3)
  h_BS4 <- round(h_BS4,3)
  fa_AN3 <- round(fa_AN3,3)
  fa_BN3 <- round(fa_BN3,3)
  h_AS3 <- round(h_AS3,3)
  h_BS3 <- round(h_BS3,3)
  fa_AN2 <- round(fa_AN2,3)
  fa_BN2 <- round(fa_BN2,3)
  h_AS2 <- round(h_AS2,3)
  h_BS2 <- round(h_BS2,3)
  fa_AN1 <- round(fa_AN1,3)
  fa_BN1 <- round(fa_BN1,3)
  h_AS1 <- round(h_AS1,3)
  h_BS1 <- round(h_BS1,3)
  #
  print(c(h_AS6[length(h_AS6)], 
          h_AS5[length(h_AS5)], 
          h_AS4[length(h_AS4)], 
          h_AS3[length(h_AS3)],
          h_AS2[length(h_AS2)], 
          h_AS1[length(h_AS1)], 
          h_BS6[length(h_BS6)],
          h_BS5[length(h_BS5)], 
          h_BS4[length(h_BS4)], 
          h_BS3[length(h_BS3)],
          h_BS2[length(h_BS5)], 
          h_BS1[length(h_BS1)],
          fa_AN6[length(fa_AN6)],
          fa_AN5[length(fa_AN5)], 
          fa_AN4[length(fa_AN4)], 
          fa_AN3[length(fa_AN3)],
          fa_AN2[length(fa_AN2)], 
          fa_AN1[length(fa_AN1)], 
          fa_BN6[length(fa_BN6)],
          fa_BN5[length(fa_BN5)], 
          fa_BN4[length(fa_BN4)], 
          fa_BN3[length(fa_BN3)],
          fa_BN2[length(fa_BN5)]))
  k1 <- qnorm(1-fa_AN1,0,1)
  k2 <- qnorm(1-fa_AN2,0,1)
  k3 <- qnorm(1-fa_AN3,0,1)
  k4 <- qnorm(1-h_AS4,d_A,1)
  k5 <- qnorm(1-h_AS5,d_A,1)
  k6 <- qnorm(1-h_AS6,d_A,1)
  
  dif_A <-d_A-0
  dif_B <-d_BS-d_BN
  print(c(dif_A[length(dif_A)], 
          dif_B[length(dif_B)]))
  
  }
  soporte <- seq(-3.5,6.5,.05)
  dis_AN <- dnorm(soporte,0,1)
  dis_AS <- dnorm(soporte,d_A,1)
  dis_BN <- dnorm(soporte,d_BN,1)
  dis_BS <- dnorm(soporte,d_BS,1)
  
  d_A<-round(d_A,3)
  d_BN<-round(d_BN,3)
  d_BS<-round(d_BS,3)
  k<-round(k,3)
  c<-round(c,3)
  #c_B<-round(c_B,3)
  #beta_A<-round(beta_A,3)
  #beta_B<-round(beta_B,3)
  Hr_as<-round(Hr_as,3)
  FAr_an<-round(FAr_an,3)
  Hr_bs<-round(Hr_bs,3)
  FAr_bn<-round(FAr_bn,3)
  
  plot(fa_AN,type='o',pch=16,col='white',ylim=c(0,10), yaxt='n', xaxt='n', ann=F)
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
  text(.7,7.5,paste(fa_AN),cex=1,col='lightblue4')
  text(.9,7.5,paste(fa_BN),cex=1,col='lightblue4')
  text(1.1,7.5,paste(hits_BS),cex=1,col='lightblue4')
  text(1.3,7.5,paste(hits_AS),cex=1,col='lightblue4')
  title("Mirror Effect", outer = TRUE, line = -2, cex=2)
  mtext(archive,3,cex=1)
  
  
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
  text(1.3,1.5,paste(C_AN),cex=1,col='royalblue4')
  text(2.2,1.5,paste(C_BN),cex=1,col='royalblue4')
  text(2.9,1.5,paste(C_BS),cex=1,col='royalblue4')
  text(3.75,1.5,paste(C_AS),cex=1,col='royalblue4')
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
  abline(v=k2,col='forestgreen', lty=2, lwd=2)
  abline(v=k3,col='darkgreen', lty=2, lwd=2)
  abline(v=k4,col='black', lty=1, lwd=2)
  abline(v=k5,col='darkgoldenrod3', lty=2, lwd=2)
  abline(v=k6,col='orange', lty=2, lwd=2)
  text(-2.7,0.15,paste("K = ",k))
  text(-2,0.25,paste("6"), col='orange')
  text(-2,0.3,paste("5"), col='darkgoldenrod3')
  text(-2.5,0.3,paste("4"), col='black')
  text(-3,0.3,paste("3"), col='darkgreen')
  text(-3,0.35,paste("2"), col='forestgreen')
  #text(-2.5,0.35,paste("1"), col='red')
  #text(-3.4,0.15,paste("D' = ",d_B))
  #text(-3.4,0.39,paste("Hits = ",Hr_bs))
  #text(-3.4,0.34,paste("F.A = ",FAr_bn))
}
###############################
#######Confidence Rating LINEAL RELATION
################################## 
  rm(list=ls())
  layout(matrix(1:2,ncol=1))
  for(archive in dir()){
    jaime <- read.csv(archive)
    
    C_AS <- NULL
    C_AN <- NULL
    C_BS <- NULL
    C_BN <- NULL
    
    for(nce in sort(jaime$Estimulo)){
      C_AS <- sum(jaime$Confidence[jaime$tipo=='4 AS'])/160
      C_AN <- sum(jaime$Confidence[jaime$tipo=='1 AN'])/160
      C_BS <- sum(jaime$Confidence[jaime$tipo=='3 BS'])/160
      C_BN <- sum(jaime$Confidence[jaime$tipo=='2 BN'])/160
      Confidence <- c(C_AN, C_BN, C_BS, C_AS)
    }
    
    plot(Confidence,type='o',pch=16,col='white',ylim=c(0,6), yaxt='n', xaxt='n', ann=F)
    #axis(1,at=c(0,6),labels=c("AN","BN","BS","AS"), col='white')
    #axis(2,at=c(2.5,7.5),labels=c("Rate","No."),las=0)
    abline(3,c(0.1,0.1), col="black",lwd=1)
    abline(v=1.75,h=c(-10,15),col='black')
    abline(v=2.5,h=c(-10,15),col='black')
    abline(v=3.4,h=c(-10,15),col='black')
    text(1.3,1.5,paste(C_AN),cex=1,col='royalblue4')
    text(2.2,1.5,paste(C_BN),cex=1,col='royalblue4')
    text(2.9,1.5,paste(C_BS),cex=1,col='royalblue4')
    text(3.75,1.5,paste(C_AS),cex=1,col='royalblue4')
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
    axis(1,at=1:4,labels=sort(unique(jaime$tipo)))
    axis(2,at=c(0, 1, 2, 3, 4, 5, 6),labels=c("0","1", "2","3","4","5","6"),las=1)
    text(1.1,C_AN+.5,paste(C_AN),cex=.8,col='violetred',f=2)
    text(1.9,C_BN+.5,paste(C_BN),cex=.8,col='violetred',f=2)
    text(3.1,C_BS+.5,paste(C_BS),cex=.8,col='violetred',f=2)
    text(3.9,C_BS+.5,paste(C_AS),cex=.8,col='violetred',f=2)
    text(1.5,5.5,paste('Confidence Rate'),cex=1,col='violetred4',f=2)
}