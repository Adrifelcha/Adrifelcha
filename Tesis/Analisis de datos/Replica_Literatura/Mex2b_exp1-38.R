setwd("C:/Users/Adrifelcha/Dropbox/Tesis/Experimentos/Mirror Experimento 2/Data/Datos_Exp_2AFC_192x2")
rm(list=ls())
dir()

for(archive in dir()){
  felisa <- read.csv(archive)
  felisa <- felisa[1:384,]
  
  choice <- NULL
  
  choice[felisa$Respuesta=='left'] <- '0'
  choice[felisa$Respuesta=='right'] <- '1'
  
  
  felisa$choice <- choice
  head(felisa,50)
  
  
  write.csv(felisa,file=archive)
}


#################################### CHOICE por ensayo (Left or Right)

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$choice[1:96],type='o',pch=16, col='darkorchid',ylim=c(0,1), xlim=c(1,48), axes=F , ylab='Respuesta', xlab='Trial' )
  axis(1,at=1:96,labels=c(1:96))
  axis(2,at=0:1,labels=c("Left","Right"))
  text(140,9.5,paste("1-96"),cex=1,col='darkorchid',f=2)
  mtext(archive,3,cex=.8)
  
  plot(jaime$choice[97:192],type='o',pch=16, col='darkorchid3',ylim=c(0,1), xlim=c(1,48),axes=F , ann = F )
  axis(1,at=1:96,labels=c(97:192))
  axis(2,at=0:1,labels=c("Left","Right"))
  text(140,9,paste("97-192"),cex=1,col='darkorchid3',f=2)
  
  
  plot(jaime$choice[192:288],type='o',pch=16, col='darkorchid2',ylim=c(0,1), xlim=c(1,48),axes=F , ann = F )
  axis(1,at=1:96,labels=c(193:288))
  axis(2,at=0:1,labels=c("Left","Right"))
  text(140,8.5,paste("193-288"),cex=1,col='darkorchid2',f=2)
  
  
  plot(jaime$choice[289:384],type='o',pch=16, col='darkorchid1',ylim=c(0,1), xlim=c(1,48),axes=F , ann = F )
  axis(1,at=1:96,labels=c(289:384))
  axis(2,at=0:1,labels=c("Left","Right"))
  text(140,8,paste("289-384"),cex=1,col='darkorchid1',f=2)
  title( "Choice por ensayo", outer = TRUE, line = -2)
  
}

#################################Opcion Predicha por Ensayo

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$OpcionPredicha[1:192],type='o',pch=16, col='green',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:192,labels=c(1:192))
  axis(2,at=0:1,labels=c("No", "Sí"))
  text(140,8,paste("1-192"),cex=1,col='darkorchid1',f=2)
  #points(jaime$Errores,type='o', lty=3, pch=16, col='red')
  mtext(archive,3,cex=.8)
  #text(70,500,paste('Eleccion Predicha'),cex=1,col='chartreuse4',f=2)
  #text(70,400,paste('Errores'),cex=1,col='red',f=2)
  title("Opcion Predicha por Ensayo", outer = TRUE, line = -2)
  
  plot(jaime$OpcionPredicha[193:384],type='o',pch=16, col='green',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:192,labels=c(193:384))
  axis(2,at=0:1,labels=c("No", "Sí"))
  #points(jaime$Errores,type='o', lty=3, pch=16, col='red')
  mtext(archive,3,cex=.8)
  #text(70,500,paste('Eleccion Predicha'),cex=1,col='chartreuse4',f=2)
  #text(70,400,paste('Errores'),cex=1,col='red',f=2)
  title("Opcion Predicha por Ensayo", outer = TRUE, line = -2)
  text(140,8,paste("193-384"),cex=1,col='darkorchid1',f=2)
}

######################
#Response Time across trials


rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$RTime1[1:192],type='o',pch=16, col='purple',ylim=c(0,10),axes=F , ann = F )
  axis(1,at=1:192,labels=c(1:192))
  axis(2,at=c(0,2,4,6,8,10),labels=c("0","2","4","6","8","10"))
  #points(jaime$RTime2,type='o', lty=3, pch=16, col='brown')
  #text(100,14,paste('Estimulo'),cex=1,col='purple',f=2)
  #text(100,10,paste('Escala'),cex=1,col='brown',f=2)
  mtext(archive,3,cex=.8)
  text(140,8,paste("1-192"),cex=1,col='darkorchid1',f=2)
  title("Tiempo de Respuesta por Ensayo", outer = TRUE, line = -2)
  
  plot(jaime$RTime1[193:384],type='o',pch=16, col='purple',ylim=c(0,10),axes=F , ann = F )
  axis(1,at=1:192,labels=c(193:384))
  axis(2,at=c(0,2,4,6,8,10),labels=c("0","2","4","6","8","10"))
  #points(jaime$RTime2,type='o', lty=3, pch=16, col='brown')
  #text(100,14,paste('Estimulo'),cex=1,col='purple',f=2)
  #text(100,10,paste('Escala'),cex=1,col='brown',f=2)
  mtext(archive,3,cex=.8)
  text(140,8,paste("193-384"),cex=1,col='darkorchid1',f=2)
  title("Tiempo de Respuesta por Ensayo", outer = TRUE, line = -2)
}

#RT en Intervalos de 150 ensayos.

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$RTime1[1:96],type='o',pch=16, col='darkorange',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:96,labels=c(1:96))
  axis(2,at=0:10,labels=c(0:10))
  text(145,9.5,paste("1-96"),cex=1,col='darkorange',f=2)
  mtext(archive,3,cex=.8)
  
  
  plot(jaime$RTime1[97:192],type='o',pch=16, col='darkorange1',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:96,labels=c(97:192))
  axis(2,at=0:10,labels=c(0:10))
  text(145,9,paste("97-192"),cex=1,col='darkorange1',f=2)
  
  
  plot(jaime$RTime1[193:288],type='o',pch=16, col='darkorange2',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:96,labels=c(193:288))
  axis(2,at=0:10,labels=c(0:10))
  text(145,8.5,paste("193-289"),cex=1,col='darkorange2',f=2)
  
  
  plot(jaime$RTime1[289:384],type='o',pch=16, col='darkorange3',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:96,labels=c(289:384))
  axis(2,at=0:10,labels=c(0:10))
  text(145,8,paste("289-384"),cex=1,col='darkorange3',f=2)
  # text(170,7.5,paste("5"),cex=1,col='violet',f=2)
  title("Tiempo de Respuesta", outer = TRUE, line = -2)
  
}


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
  
  C_CE1 <- NULL
  C_CE2 <- NULL
  C_CE3 <- NULL
  C_CE4 <- NULL
  C_CN1 <- NULL
  C_CN2 <- NULL
  
  for(nce in sort(jaime$Estimulo)){
    C_CE2 <- sum(jaime$OpcionPredicha[jaime$Comparacion=='2 AS-BN'])/64
    C_CE4 <- sum(jaime$OpcionPredicha[jaime$Comparacion=='1 AS-AN'])/64
    C_CE1 <- sum(jaime$OpcionPredicha[jaime$Comparacion=='3 BS-BN'])/64
    C_CE3 <- sum(jaime$OpcionPredicha[jaime$Comparacion=='4 BS-AN'])/64
    C_CN1 <- sum(jaime$OpcionPredicha[jaime$Comparacion=='5 AS-BS'])/64
    C_CN2 <- sum(jaime$OpcionPredicha[jaime$Comparacion=='6 AN-BN'])/64
    Preference <- c(C_CE1, C_CE2, C_CE3, C_CE4)
  }
  
  plot(Preference,type='o',pch=16,col='white',ylim=c(0,6), yaxt='n', xaxt='n', ann=F)
  #axis(1,at=c(0,6),labels=c("BSAN","BSAN","ASBN","ASAN"), col='black')
  #axis(2,at=c(2.5,7.5),labels=c("Rate","No."),las=0)
  abline(3,c(0.1,0.1), col="black",lwd=1)
  abline(v=1.75,h=c(-10,15),col='black')
  abline(v=2.5,h=c(-10,15),col='black')
  abline(v=3.4,h=c(-10,15),col='black')
  text(1.3,1.5,paste(C_CE1),cex=1,col='royalblue4')
  text(2.2,1.5,paste(C_CE2),cex=1,col='royalblue4')
  text(2.9,1.5,paste(C_CE3),cex=1,col='royalblue4')
  text(3.75,1.5,paste(C_CE4),cex=1,col='royalblue4')
  text(1.3,4.5,paste('P(BS>BN)'),cex=1,col='royalblue4')
  text(2.1,4.5,paste('P(AS>BN)'),cex=1,col='royalblue4')
  text(2.9,4.5,paste('P(BS>AN)'),cex=1,col='royalblue4')
  text(3.75,4.5,paste('P(AS>AN)'),cex=1,col='royalblue4')
  mtext(archive,3,cex=.8)
  #text(1.5,.8,paste('Hits & F.A. rate'),cex=1,col='blue',f=2)
  #mtext(archive,3,cex=.8)
  title("Preferencia Predicha", outer = TRUE, line = -2)
  #points(hits,type='o',pch=16,col='black')
  
  plot(Preference,type='o',pch=16,col='maroon2',ylim=c(0.6,1),axes=F , ann=F)
  axis(1,at=1:4,labels=c('BSBN', 'ASBN', 'BSAN', 'ASAN'))
  axis(2,at=c(0.6, .7, .8, .9, 1),labels=c(".6", ".7",".8",".9","1"),las=1)
  text(1.1,C_CE1+.1,paste(C_CE1),cex=1,col='maroon4',f=2)
  text(1.9,C_CE2+.1,paste(C_CE2),cex=1,col='maroon4',f=2)
  text(3.1,C_CE3+.1,paste(C_CE3),cex=1,col='maroon4',f=2)
  text(3.9,C_CE4+.1,paste(C_CE4),cex=1,col='maroon4',f=2)
  text(1.5,1,paste('Preference'),cex=1,col='maroon4',f=2)
  
  
}



