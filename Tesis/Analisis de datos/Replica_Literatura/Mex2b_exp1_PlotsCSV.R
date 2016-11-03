setwd("C:/Users/Adrifelcha/Dropbox/Tesis/Experimentos/Mirror Experimento 2/Data/Datos_Exp2_2AFC")
rm(list=ls())
dir()

for(archive in dir()){
  felisa <- read.csv(archive)
  felisa <- felisa[1:192,]

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
  
  plot(jaime$choice[1:48],type='o',pch=16, col='darkorchid',ylim=c(0,1), xlim=c(1,48), axes=F , ylab='Respuesta', xlab='Trial' )
  axis(1,at=1:48,labels=c(1:48))
  axis(2,at=0:1,labels=c("Left","Right"))
  text(140,9.5,paste("1-48"),cex=1,col='darkorchid',f=2)
  mtext(archive,3,cex=.8)
  
  plot(jaime$choice[49:96],type='o',pch=16, col='darkorchid3',ylim=c(0,1), xlim=c(1,48),axes=F , ann = F )
  axis(1,at=1:48,labels=c(49:96))
  axis(2,at=0:1,labels=c("Left","Right"))
  text(140,9,paste("49-96"),cex=1,col='darkorchid3',f=2)
  
  
  plot(jaime$choice[97:144],type='o',pch=16, col='darkorchid2',ylim=c(0,1), xlim=c(1,48),axes=F , ann = F )
  axis(1,at=1:48,labels=c(97:144))
  axis(2,at=0:1,labels=c("Left","Right"))
  text(140,8.5,paste("97-144"),cex=1,col='darkorchid2',f=2)
  
  
  plot(jaime$choice[145:192],type='o',pch=16, col='darkorchid1',ylim=c(0,1), xlim=c(1,48),axes=F , ann = F )
  axis(1,at=1:48,labels=c(145:192))
  axis(2,at=0:1,labels=c("Left","Right"))
  text(140,8,paste("145-192"),cex=1,col='darkorchid1',f=2)
  title( "Choice por ensayo", outer = TRUE, line = -2)
  
}

#################################Opcion Predicha por Ensayo

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$OpcionPredicha,type='o',pch=16, col='green',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:192,labels=c(1:192))
  axis(2,at=0:1,labels=c("No", "Sí"))
  #points(jaime$Errores,type='o', lty=3, pch=16, col='red')
  mtext(archive,3,cex=.8)
  #text(70,500,paste('Eleccion Predicha'),cex=1,col='chartreuse4',f=2)
  #text(70,400,paste('Errores'),cex=1,col='red',f=2)
  title("Opcion Predicha por Ensayo", outer = TRUE, line = -2)
}

######################
#Response Time across trials


rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$RTime1,type='o',pch=16, col='purple',ylim=c(0,10),axes=F , ann = F )
  axis(1,at=1:192,labels=c(1:192))
  axis(2,at=c(0,2,4,6,8,10),labels=c("0","2","4","6","8","10"))
  #points(jaime$RTime2,type='o', lty=3, pch=16, col='brown')
  #text(100,14,paste('Estimulo'),cex=1,col='purple',f=2)
  #text(100,10,paste('Escala'),cex=1,col='brown',f=2)
  mtext(archive,3,cex=.8)
  title("Tiempo de Respuesta por Ensayo", outer = TRUE, line = -2)
}

#RT en Intervalos de 150 ensayos.

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$RTime1[1:48],type='o',pch=16, col='darkorange',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:48,labels=c(1:48))
  axis(2,at=0:10,labels=c(0:10))
  text(145,9.5,paste("1-48"),cex=1,col='darkorange',f=2)
  mtext(archive,3,cex=.8)
  
  
  plot(jaime$RTime1[49:96],type='o',pch=16, col='darkorange1',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:48,labels=c(49:96))
  axis(2,at=0:10,labels=c(0:10))
  text(145,9,paste("49-96"),cex=1,col='darkorange1',f=2)
  
  
  plot(jaime$RTime1[97:144],type='o',pch=16, col='darkorange2',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:48,labels=c(97:144))
  axis(2,at=0:10,labels=c(0:10))
  text(145,8.5,paste("97-144"),cex=1,col='darkorange2',f=2)
  
  
  plot(jaime$RTime1[145:192],type='o',pch=16, col='darkorange3',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:48,labels=c(145:192))
  axis(2,at=0:10,labels=c(0:10))
  text(145,8,paste("145-192"),cex=1,col='darkorange3',f=2)
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
    C_CE2 <- sum(jaime$OpcionPredicha[jaime$Comparacion=='2 AS-BN'])/32
    C_CE4 <- sum(jaime$OpcionPredicha[jaime$Comparacion=='1 AS-AN'])/32
    C_CE1 <- sum(jaime$OpcionPredicha[jaime$Comparacion=='3 BS-BN'])/32
    C_CE3 <- sum(jaime$OpcionPredicha[jaime$Comparacion=='4 BS-AN'])/32
    C_CN1 <- sum(jaime$OpcionPredicha[jaime$Comparacion=='5 AS-BS'])/32
    C_CN2 <- sum(jaime$OpcionPredicha[jaime$Comparacion=='6 AN-BN'])/32
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

















############################3
#Hits y Falsas Alarmas x Color

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$color <- as.character(jaime$color)
  cafe <- strsplit(as.character(jaime$color),split='-')
  #index <- which(jaime$facilidad=='muchos')
  
  
  #for(i in index){
  #  jaime$num_circulos_externos[i] <- paste(as.numeric(cafe[[i]])+5,collapse = '-')
  #}
  
  
  fa <- NULL
  hits <- NULL
  for(nce in sort(unique(jaime$color))){
    fa <- append(fa, sum(jaime$Falsas.alarmas[jaime$color==nce]=='True'))
    hits <- append(hits,sum(jaime$Hits[jaime$color==nce]=='True'))
    print(c(nce,
            fa[length(fa)],
            hits[length(hits)]))
    
  }
  
  plot(hits,type='o',pch=16,col='blue',ylim=c(40,80),axes=F , ann = F )
  axis(2,at=c(40, 50, 60, 70, 80),labels=c("40", "50","60","70","80"),las=1)
  axis(1,at=1:5,labels=sort(unique(jaime$color)))
  #points(fa,type='o',pch=16,col='red')
  text(2,70,paste('Hits'),cex=1,col='blue',f=2)
  mtext(archive,3,cex=.8)
  title("Hits y F.A. por Color", outer = TRUE, line = -2)
  
  
  plot(fa,type='o',pch=16,col='red',ylim=c(0,40),axes=F , ann = F )
  axis(1,at=1:5,labels=sort(unique(jaime$color)))
  axis(2,at=c(0, 10, 20, 30, 40),labels=c("0", "10","20","30","40"),las=1)
  #points(fa,type='o',pch=16,col='red')
  text(2,30,paste('F.A.'),cex=1,col='red',f=2)
  mtext(archive,3,cex=.8) 
}

