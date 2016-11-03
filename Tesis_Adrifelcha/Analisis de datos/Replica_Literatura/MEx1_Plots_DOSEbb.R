#####################################
#####################################
#####################################
#Mirror Effect

rm(list=ls())
layout(matrix(1:2,ncol=1))
for(archive in dir()){
  jaime <- read.csv(archive)
  fa <- NULL
  hits <- NULL
    for(nce in sort(unique(jaime$tipo))){
    fa <- append(fa, sum(jaime$Falsas.alarmas[jaime$tipo==nce]=='True'))
    hits <- append(hits,sum(jaime$Hits[jaime$tipo==nce]=='True'))
    rate <- (fa+hits)/200
    print(c(nce,
            fa[length(fa)],
            hits[length(hits)],
            rate[length(rate)]))
    
  }
  
  plot(rate,type='o',pch=16,col='royalblue',ylim=c(0,1),axes=F , ann=F)
  axis(1,at=1:4,labels=sort(unique(jaime$tipo)))
  axis(2,at=c(0, 0.15, 0.30, 0.45, 0.60, 0.75, 0.90, 1),labels=c("0",".15",".30",".45",".60", ".75", ".90", "1"),las=1)
  #points(hits,type='o',pch=16,col='red')
  mtext(archive,3,cex=.8)
  
  for(nce in sort(jaime$Estimulo)){
    C_AS <- sum(jaime$Confidence[jaime$tipo=='4 AS'])/200
    C_AN <- sum(jaime$Confidence[jaime$tipo=='1 AN'])/200
    C_BS <- sum(jaime$Confidence[jaime$tipo=='3 BS'])/200
    C_BN <- sum(jaime$Confidence[jaime$tipo=='2 BN'])/200
    Confidence <- c(C_AN, C_BN, C_BS, C_AS)
  }
  
  plot(Confidence,type='o',pch=16,col='maroon2',ylim=c(0,6),axes=F , ann=F)
  axis(1,at=1:4,labels=sort(unique(jaime$tipo)))
  axis(2,at=c(0, 1, 2, 3, 4, 5, 6),labels=c("0","1", "2","3","4","5","6"),las=1)
  mtext(archive,3,cex=.8)
  
}

############################
############################
############################
# Hits y Falsas alarmas x  No. Circulos externos

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$num_circulos_externos <- as.character(jaime$num_circulos_externos)
  cafe <- strsplit(as.character(jaime$num_circulos_externos),split='-')
  index <- which(jaime$facilidad=='muchos')
  
  
  for(i in index){
    jaime$num_circulos_externos[i] <- paste(as.numeric(cafe[[i]])+5,collapse = '-')
  }
  
 
  fa <- NULL
  hits <- NULL
  for(nce in sort(unique(jaime$num_circulos_externos))){
    fa <- append(fa, sum(jaime$Falsas.alarmas[jaime$num_circulos_externos==nce]=='True'))
    hits <- append(hits,sum(jaime$Hits[jaime$num_circulos_externos==nce]=='True'))
    print(c(nce,
            fa[length(fa)],
            hits[length(hits)]))
    
  }
  
  plot(hits,type='o',pch=16,col='blue',ylim=c(0,60),axes=F , ann = F )
  axis(1,at=1:8,labels=sort(unique(jaime$num_circulos_externos)))
  points(fa,type='o',pch=16,col='red')
  mtext(archive,3,cex=.8)
  

}

###################
###################
###################
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
  
  plot(hits,type='o',pch=16,col='blue',ylim=c(0,80),axes=F , ann = F )
  axis(1,at=1:5,labels=sort(unique(jaime$color)))
  points(fa,type='o',pch=16,col='red')
  mtext(archive,3,cex=.8)
  
  
}




############################
###########################
###########################
#Hits y Falsas Alarmas  x Tamaño Circulo Central


rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  jaime <- read.csv(archive)
  fa <- NULL
  hits <- NULL
  for(nce in sort(unique(jaime$tamano_centrales))){
    fa <- append(fa, sum(jaime$Falsas.alarmas[jaime$tamano_centrales==nce]=='True'))
    hits <- append(hits,sum(jaime$Hits[jaime$tamano_centrales==nce]=='True'))
    print(c(nce,
            fa[length(fa)],
            hits[length(hits)]))
    
  }
  
  plot(hits,type='o',pch=16,col='blue',ylim=c(0,80),axes=F , ann=F)
  axis(1,at=1:10,labels=sort(unique(jaime$tamano_centrales)))
  points(fa,type='o',pch=16,col='red')
  mtext(archive,3,cex=.8)
  
}


#####################################
#####################################
#####################################
#Hits y FA por Tamaño Central; across No. Circulos externos


rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  # archive <- dir()[3]
  jaime <- read.csv(archive)
  jaime$num_circulos_externos <- as.character(jaime$num_circulos_externos)
  cafe <- strsplit(as.character(jaime$num_circulos_externos),split='-')
  index <- which(jaime$facilidad=='muchos')
  
  for(i in index){
    jaime$num_circulos_externos[i] <- paste(as.numeric(cafe[[i]])+5,collapse = '-')
  }
  
  
  fa <- array(dim=c(10,8))
  hits <- array(dim=c(10,8))
  c_nce <- 0
  for(nce in sort(unique(jaime$num_circulos_externos))){
    c_nce <- c_nce+1
    c_tc <- 0
    for(tc in sort(unique(jaime$tamano_centrales))){
      c_tc <- c_tc+1
      
      fa[c_tc,c_nce] <- sum(jaime$Falsas.alarmas[jaime$num_circulos_externos==nce&jaime$tamano_centrales==tc]=='True')
      hits[c_tc,c_nce] <- sum(jaime$Hits[jaime$num_circulos_externos==nce&jaime$tamano_centrales==tc]=='True')
      
    } 
  }
  
  plot(0,type='n',xlim=c(-1,10),ylim=c(0,10),axes=F, ann=F)
  axis(1,at=1:8,labels=sort(unique(jaime$num_circulos_externos)))
  for(f in 1:nrow(fa)){
    lines(1:8,fa[f,],col='red',type='o',pch=16)
    text(0,fa[f,1],sort(unique(jaime$tamano_centrales))[f],col='red')
    text(9,fa[f,8],sort(unique(jaime$tamano_centrales))[f],col='red')
  }  
  for(h in 1:nrow(hits)){
    lines(1:8,hits[h,],col='blue',type='o',pch=16)
#     text(0,hits[h,1],sort(unique(jaime$tamano_centrales))[h],col='blue')
#     text(9,hits[h,8],sort(unique(jaime$tamano_centrales))[h],col='blue')
  } 
  mtext(archive,3,cex=.8)
}


#######################
######################
######################
#Response Time (1 y 2) across trials


rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$RTime1,type='o',pch=16, col='purple',ylim=c(0,10),axes=F , ann = F )
  axis(1,at=1:800,labels=sort(unique(jaime$Ensayo)))
  axis(2,at=0:10,labels=c("0", "1","2","3","4","5","6","7","8","9","10"))
  points(jaime$RTime2,type='o', lty=3, pch=16, col='brown')
  mtext(archive,3,cex=.8)
}

################################
################################
#RT en Intervalos de 200 ensayos.

rm(list=ls())

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')

plot(jaime$RTime1[1:200],type='o',pch=16, col='darkorchid',ylim=c(1,10),axes=F , ann = F )
axis(1,at=1:200,labels=c(1:200))
axis(2,at=1:10,labels=c("1","2","3","4","5","6","7","8","9","10"))
text(170,9.5,paste("1-200"),cex=1,col='darkorchid',f=2)
mtext(archive,3,cex=.8)

plot(jaime$RTime1[201:400],type='o',pch=16, col='darkorchid3',ylim=c(1,10),axes=F , ann = F )
axis(1,at=1:200,labels=c(201:400))
axis(2,at=1:10,labels=c("1","2","3","4","5","6","7","8","9","10"))
text(170,9,paste("201-400"),cex=1,col='darkorchid3',f=2)


plot(jaime$RTime1[401:600],type='o',pch=16, col='darkorchid2',ylim=c(1,10),axes=F , ann = F )
axis(1,at=1:200,labels=c(401:600))
axis(2,at=1:10,labels=c("1","2","3","4","5","6","7","8","9","10"))
text(170,8.5,paste("401-600"),cex=1,col='darkorchid2',f=2)


plot(jaime$RTime1[601:800],type='o',pch=16, col='darkorchid1',ylim=c(1,10),axes=F , ann = F )
axis(1,at=1:200,labels=c(601:800))
axis(2,at=1:10,labels=c("1","2","3","4","5","6","7","8","9","10"))
text(170,8,paste("601-800"),cex=1,col='darkorchid1',f=2)

plot(jaime$RTime2[1:200],type='o',pch=16, col='firebrick4',ylim=c(0,10),axes=F , ann = F )
axis(1,at=1:200,labels=c(1:200))
axis(2,at=0:10,labels=c("0", "1","2","3","4","5","6","7","8","9","10"))
text(170,9.5,paste("1-200"),cex=1,col='firebrick4',f=2)
mtext(archive,3,cex=.8)

plot(jaime$RTime2[201:400],type='o',pch=16, col='firebrick3',ylim=c(0,10),axes=F , ann = F )
axis(1,at=1:200,labels=c(201:400))
axis(2,at=0:10,labels=c("0", "1","2","3","4","5","6","7","8","9","10"))
text(170,9,paste("201-400"),cex=1,col='darkorchid3',f=2)


plot(jaime$RTime2[401:600],type='o',pch=16, col='firebrick2',ylim=c(0,10),axes=F , ann = F )
axis(1,at=1:200,labels=c(401:600))
axis(2,at=0:10,labels=c("0", "1","2","3","4","5","6","7","8","9","10"))
text(170,8.5,paste("401-600"),cex=1,col='darkorchid2',f=2)


plot(jaime$RTime2[601:800],type='o',pch=16, col='firebrick1',ylim=c(0,10),axes=F , ann = F )
axis(1,at=1:200,labels=c(601:800))
axis(2,at=0:10,labels=c("0", "1","2","3","4","5","6","7","8","9","10"))
text(170,8,paste("601-800"),cex=1,col='darkorchid1',f=2)

}


####################################################
####################################################
##################### Aciertos y errores x Ensayo
rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$Aciertos,type='o',pch=16, col='green',ylim=c(0,800),axes=F , ann = F )
  axis(1,at=1:800,labels=sort(unique(jaime$Ensayo)))
  #axis(2,at=0:10,labels=c("0", "1","2","3","4","5","6","7","8","9","10"))
  points(jaime$Errores,type='o', lty=3, pch=16, col='red')
  mtext(archive,3,cex=.8)
}

#############################################
#############################################
######### Contadores x Ensayo

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$ContadorH,type='o',pch=16, col='blue',ylim=c(0,400),axes=F , ann = F )
  axis(1,at=1:800,labels=sort(unique(jaime$Ensayo)))
  #axis(2,at=0:10,labels=c("0", "1","2","3","4","5","6","7","8","9","10"))
  points(jaime$ContadorF,type='o', lty=3, pch=16, col='red')
  points(jaime$ContadorM,type='o', lty=3, pch=16, col='purple')
  points(jaime$ContadorR,type='o', lty=3, pch=16, col='green')
  text(810,jaime$ContadorF[799]+20,paste("FA"),cex=1,col='red',f=2)
  text(810,jaime$ContadorM[799]+20,paste("M"),cex=1,col='purple',f=2)
  text(810,jaime$ContadorR[799]+20,paste("R"),cex=1,col='green',f=2)
  text(810,jaime$ContadorH[799]+20,paste("H"),cex=1,col='blue',f=2)
  mtext(archive,3,cex=.8)
}
############################
############################
######### Confidence por ENSAYO

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$Confidence[1:200],type='o',pch=16, col='darkorchid',ylim=c(1,10),axes=F , ylab='Confidence Value', xlab='Trial' )
  axis(1,at=1:200,labels=c(1:200))
  axis(2,at=1:6,labels=c("1","2","3","4","5","6"))
  text(170,9.5,paste("1-200"),cex=1,col='darkorchid',f=2)
  mtext(archive,3,cex=.8)
  
  plot(jaime$Confidence[201:400],type='o',pch=16, col='darkorchid3',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:200,labels=c(201:400))
  axis(2,at=1:6,labels=c("1","2","3","4","5","6"))
  text(170,9,paste("201-400"),cex=1,col='darkorchid3',f=2)
  
  
  plot(jaime$Confidence[401:600],type='o',pch=16, col='darkorchid2',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:200,labels=c(401:600))
  axis(2,at=1:6,labels=c("1","2","3","4","5","6"))
  text(170,8.5,paste("401-600"),cex=1,col='darkorchid2',f=2)
  
  
  plot(jaime$Confidence[601:800],type='o',pch=16, col='darkorchid1',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:200,labels=c(601:800))
  axis(2,at=1:6,labels=c("1","2","3","4","5","6"))
  text(170,8,paste("601-800"),cex=1,col='darkorchid1',f=2)
  
  
  
}