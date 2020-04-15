#Niveles Cognitivos:
#Información sobre la dinámica del juego y los niveles de otros jugadores
#Jaime Islas Farias

library("grDevices", lib.loc="C:/Program Files/R/R-3.1.1/library") #Librería de rgb
rm(list=ls()) #Borra datos previos

#### Carga de Datos ####

setwd("D:/APLICACION/DATOS") #Indica el directorio de trabajo

#Los datos se guardan en matrices
He1_1 <- read.csv("He1_1.csv")
He1_2 <- read.csv("He1_2.csv")
He1_3 <- read.csv("He1_3.csv")
HeT_1 <- read.csv("HeT_1.csv")
HeT_2 <- read.csv("HeT_2.csv")
HeT_3 <- read.csv("HeT_3.csv")
HeT_4 <- read.csv("HeT_4.csv")
Es1_1 <- read.csv("Es1_1.csv")
Es1_2 <- read.csv("Es1_2.csv")
Es1_3 <- read.csv("Es1_3.csv")
EsT_1 <- read.csv("EsT_1.csv")
EsT_2 <- read.csv("EsT_2.csv")
EsT_3 <- read.csv("EsT_3.csv")
Ex1_1 <- read.csv("Ex1_1.csv")
Ex1_2 <- read.csv("Ex1_2.csv")
Ex1_3 <- read.csv("Ex1_3.csv")
ExT_1 <- read.csv("ExT_1.csv")
ExT_2 <- read.csv("ExT_2.csv")
ExT_3 <- read.csv("ExT_3.csv")
Pr1_1 <- read.csv("Pr1_1.csv")
PrT_1 <- read.csv("PrT_1.csv")
PrT_2 <- read.csv("PrT_2.csv")
PrT_3 <- read.csv("PrT_3.csv")

#### Variables ####

#Se crean las matrices que contendrán el desempeño total en cada condición
He1_T<-matrix(data=NA,nrow=4,ncol=1)           #Uno-Heu
  HeT_Tx<-matrix(data=NA,nrow=4,ncol=3)
HeT_T<-matrix(data=NA,nrow=4,ncol=1)           #Todos-Heu

Es1_T<-matrix(data=NA,nrow=4,ncol=1)           #Uno-Est
  EsT_Tx<-matrix(data=NA,nrow=4,ncol=3)
EsT_T<-matrix(data=NA,nrow=4,ncol=1)           #Todos-Est

Ex1_T<-matrix(data=NA,nrow=4,ncol=1)           #Uno-Exp
  ExT_Tx<-matrix(data=NA,nrow=4,ncol=3)
ExT_T<-matrix(data=NA,nrow=4,ncol=1)           #Todos-Exp
  Sin_Tx<-matrix(data=NA,nrow=4,ncol=3)
Sin_T<-matrix(data=NA,nrow=4,ncol=1)           #Prep-Exp

  SinHex<-matrix(data=NA,nrow=4,ncol=2)
SinHe<-matrix(data=NA,nrow=4,ncol=1)            #Sin-Heu

  SinEsx<-matrix(data=NA,nrow=4,ncol=2)
SinEs<-matrix(data=NA,nrow=4,ncol=1)           #Sin-Est

  SinExx<-matrix(data=NA,nrow=4,ncol=2)
SinEx<-matrix(data=NA,nrow=4,ncol=1)           #Sin-Exp

B_Ganancias<-c(1:4) #Nombre del soporte para las gráficas de ganancias

B_PrimeraTirada<-c("Uno \nHeu","Todos \nHeu", "Uno \nEst","Todos \nEst",
         "Uno \nExp","Todos \nExp") #Nombre del soporte para la grafica de PT

#Definir colores para todas las gráficas
Colores<-c("gray20","gray60")
Colores2<-c("darkorange","blue","firebrick2","deepskyblue3","red",
            "dodgerblue4","deeppink","forestgreen","darkorchid4")
Colores3<-c("Blue","Red","Orange")
ColoresTodos<-c("#006FFF4D","#00B3FF4D","#00B3FF4D","#1100FF4D","#1100FF4D","#1100FF4D",
                "#19B5294D","#21EC354D","#21EC354D","#197C234D","#197C234D","#197C234D",
                "#BF1F1F4D","#F327274D","#F327274D","#971C1C4D","#971C1C4D","#971C1C4D")
ColoresHeuT<-c("#006FFF","#00B3FF","#00B3FF","#1100FF","#1100FF","#1100FF",
               "#19B5294D","#21EC354D","#21EC354D","#197C234D","#197C234D","#197C234D",
               "#BF1F1F4D","#F327274D","#F327274D","#971C1C4D","#971C1C4D","#971C1C4D")
ColoresEstT<-c("#006FFF4D","#00B3FF4D","#00B3FF4D","#1100FF4D","#1100FF4D","#1100FF4D",
               "#19B529","#21EC35","#21EC35","#197C23","#197C23","#197C23",
               "#BF1F1F4D","#F327274D","#F327274D","#971C1C4D","#971C1C4D","#971C1C4D")
ColoresExpT<-c("#006FFF4D","#00B3FF4D","#00B3FF4D","#1100FF4D","#1100FF4D","#1100FF4D",
               "#19B5294D","#21EC354D","#21EC354D","#197C234D","#197C234D","#197C234D",
               "#BF1F1F","#F32727","#F32727","#971C1C","#971C1C","#971C1C")
ColoresHeu1<-c("#006FFF","#00B3FF4D","#00B3FF4D","#1100FF4D","#1100FF4D","#1100FF4D",
               "#19B5291A","#21EC351A","#21EC351A","#197C231A","#197C231A","#197C231A",
               "#BF1F1F1A","#F327271A","#F327271A","#971C1C1A","#971C1C1A","#971C1C1A")
ColoresHeu2<-c("#006FFF4D","#00B3FF","#00B3FF","#1100FF4D","#1100FF4D","#1100FF4D",
               "#19B5291A","#21EC351A","#21EC351A","#197C231A","#197C231A","#197C231A",
               "#BF1F1F1A","#F327271A","#F327271A","#971C1C1A","#971C1C1A","#971C1C1A")
ColoresHeu3<-c("#006FFF4D","#00B3FF4D","#00B3FF4D","#1100FF","#1100FF","#1100FF",
               "#19B5291A","#21EC351A","#21EC351A","#197C231A","#197C231A","#197C231A",
               "#BF1F1F1A","#F327271A","#F327271A","#971C1C1A","#971C1C1A","#971C1C1A")
ColoresEst1<-c("#006FFF1A","#00B3FF1A","#00B3FF1A","#1100FF1A","#1100FF1A","#1100FF1A",
               "#19B529","#21EC354D","#21EC354D","#197C234D","#197C234D","#197C234D",
               "#BF1F1F1A","#F327271A","#F327271A","#971C1C1A","#971C1C1A","#971C1C1A")
ColoresEst2<-c("#006FFF1A","#00B3FF1A","#00B3FF1A","#1100FF1A","#1100FF1A","#1100FF1A",
               "#19B5294D","#21EC35","#21EC35","#197C234D","#197C234D","#197C234D",
               "#BF1F1F1A","#F327271A","#F327271A","#971C1C1A","#971C1C1A","#971C1C1A")
ColoresEst3<-c("#006FFF1A","#00B3FF1A","#00B3FF1A","#1100FF1A","#1100FF1A","#1100FF1A",
               "#19B5294D","#21EC354D","#21EC354D","#197C23","#197C23","#197C23",
               "#BF1F1F1A","#F327271A","#F327271A","#971C1C1A","#971C1C1A","#971C1C1A")
ColoresExp1<-c("#006FFF1A","#00B3FF1A","#00B3FF1A","#1100FF1A","#1100FF1A","#1100FF1A",
               "#19B5291A","#21EC351A","#21EC351A","#197C231A","#197C231A","#197C231A",
               "#BF1F1F","#F327274D","#F327274D","#971C1C4D","#971C1C4D","#971C1C4D")
ColoresExp2<-c("#006FFF1A","#00B3FF1A","#00B3FF1A","#1100FF1A","#1100FF1A","#1100FF1A",
               "#19B5291A","#21EC351A","#21EC351A","#197C231A","#197C231A","#197C231A",
               "#BF1F1F4D","#F32727","#F32727","#971C1C4D","#971C1C4D","#971C1C4D")
ColoresExp3<-c("#006FFF1A","#00B3FF1A","#00B3FF1A","#1100FF1A","#1100FF1A","#1100FF1A",
               "#19B5291A","#21EC351A","#21EC351A","#197C231A","#197C231A","#197C231A",
               "#BF1F1F4D","#F327274D","#F327274D","#971C1C","#971C1C","#971C1C")
Tamaños4<-c(2.5,2,1.5)
Tamaños3<-c(3,2,2)
Tipos3<-c(1,2,2)

rgb(red=0.5,green=0.5,blue=0.5,alpha=0.3)

#### Ganancias Heu1 ####
ConHeu<-(mean(c(sum(He1_1[4]),sum(He1_2[4]),sum(He1_3[4])))) #Ganancias de jugador con Heurístico
SinHeu<-(mean(c(sum(He1_1[5]),sum(He1_2[5]),sum(He1_3[5]),
                sum(He1_1[6]),sum(He1_2[6]),sum(He1_3[6])))) #Ganancias de jugador sin Heurístico
Heu1W<-matrix(data=NA,nrow=4,ncol=2) #Se define y se llena la matriz
for(a in 1:4){Heu1W[a,1]<-mean(c(He1_1[a,4],He1_2[a,4],He1_3[a,4]))}
for(a in 1:4){Heu1W[a,2]<-mean(c(He1_1[a,5],He1_2[a,5],He1_3[a,5],
                                 He1_1[a,6],He1_2[a,6],He1_3[a,6]))}
#Se grafica
barplot(t(Heu1W),names.arg=B_Ganancias, beside=T, col=Colores,
        xlab="Periodo", ylab="Puntos Ganados", ylim=c(0,4))
lines(c(10,0.5),c(0,0))
rect(1.5,2.5,5.6,4,border=TRUE)
text(3.5,3.6,col=Colores[1],paste("Con Consejo =  ", ConHeu),cex=1, font=2)
text(3.5,2.9,col=Colores[2],paste("Sin Consejo =  ", SinHeu),cex=1, font=2)

#### Ganancias Est1 ####
ConEst<-(mean(c(sum(Es1_1[4]),sum(Es1_2[4]),sum(Es1_3[4])))) #Ganancias de jugador con Heurístico
SinEst<-(mean(c(sum(Es1_1[5]),sum(Es1_2[5]),sum(Es1_3[5]),
                sum(Es1_1[6]),sum(Es1_2[6]),sum(Es1_3[6])))) #Ganancias de jugador sin Heurístico
Est1W<-matrix(data=NA,nrow=4,ncol=2) #Se define y se llena la matriz
for(a in 1:4){Est1W[a,1]<-mean(c(Es1_1[a,4],Es1_2[a,4],Es1_3[a,4]))}
for(a in 1:4){Est1W[a,2]<-mean(c(Es1_1[a,5],Es1_2[a,5],Es1_3[a,5],
                                 Es1_1[a,6],Es1_2[a,6],Es1_3[a,6]))}
#Se grafica
barplot(t(Est1W),names.arg=B_Ganancias, beside=T, col=Colores,
        xlab="Periodo", ylab="Puntos Ganados", ylim=c(0,4))
lines(c(10,0.5),c(0,0))
rect(1.7,2.5,5.3,4,border=TRUE)
text(3.5,3.6,col=Colores[1],paste("Con Consejo =  ", ConEst),cex=1, font=2)
text(3.5,2.9,col=Colores[2],paste("Sin Consejo =  ", SinEst),cex=1, font=2)

#### Ganancias Exp1 ####
ConExp<-(mean(c(sum(Ex1_1[4]),sum(Ex1_2[4]),sum(Ex1_3[4])))) #Ganancias de jugador con Heurístico
SinExp<-(mean(c(sum(Ex1_1[5]),sum(Ex1_2[5]),sum(Ex1_3[5]),
                sum(Ex1_1[6]),sum(Ex1_2[6]),sum(Ex1_3[6])))) #Ganancias de jugador sin Heurístico
Exp1W<-matrix(data=NA,nrow=4,ncol=2) #Se define y se llena la matriz
for(a in 1:4){Exp1W[a,1]<-mean(c(Ex1_1[a,4],Ex1_2[a,4],Ex1_3[a,4]))}
for(a in 1:4){Exp1W[a,2]<-mean(c(Ex1_1[a,5],Ex1_2[a,5],Ex1_3[a,5],
                                 Ex1_1[a,6],Ex1_2[a,6],Ex1_3[a,6]))}
#Se grafica
barplot(t(Exp1W),names.arg=B_Ganancias, beside=T, col=Colores,
        xlab="Periodo", ylab="Puntos Ganados", ylim=c(0,4))
lines(c(10,0),c(0,0))
rect(6.5,2.5,10.6,4,border=TRUE)
text(8.5,3.6,col=Colores[1],paste("Con Experiencia =  ", ConExp),cex=1, font=2)
text(8.5,2.9,col=Colores[2],paste("Sin Experiencia =  ", SinExp),cex=1, font=2)

#### Primera Tirada (Mediana) ####
PTHeu1<-median(c(He1_1[1,1],He1_2[1,1],He1_3[1,1])) #Uno-Heu
PTHeuT<-median(c(HeT_1[1,1],HeT_2[1,1],HeT_3[1,1],HeT_1[1,2],HeT_2[1,2],
                 HeT_3[1,2],HeT_1[1,3],HeT_2[1,3],HeT_3[1,3])) #Todos-Heu
PTHeu<-cbind(PTHeu1,PTHeuT) #Primeras tiradas de Uno-Heu y Todos-Heu

PTEst1<-median(c(Es1_1[1,1],Es1_2[1,1],Es1_3[1,1])) #Uno-Est
PTEstT<-median(c(EsT_1[1,1],EsT_2[1,1],EsT_3[1,1],EsT_1[1,2],EsT_2[1,2],
                 EsT_3[1,2],EsT_1[1,3],EsT_2[1,3],EsT_3[1,3])) #Todos-Est
PTEst<-cbind(PTEst1,PTEstT) #Primeras tiradas de Uno-Est y Todos-Est

PTExp1<-median(c(Ex1_1[1,1],Ex1_2[1,1],Ex1_3[1,1])) #Uno-Est
PTExpT<-median(c(ExT_1[1,1],ExT_2[1,1],ExT_3[1,1],ExT_1[1,2],ExT_2[1,2],
                 ExT_3[1,2],ExT_1[1,3],ExT_2[1,3],ExT_3[1,3])) #Todos-Est
PTExp<-cbind(PTExp1,PTExpT) #Primeras tiradas de Uno-Exp y Todos-Exp

PTPlot<-matrix(data=NA,nrow=3,ncol=2) #Se define la matriz
PTPlot<-rbind(PTHeu, PTEst, PTExp) #Se ingresan los datos en la matriz

#Se grafica
barplot(t(PTPlot),names.arg=B_PrimeraTirada, beside=T, col=Colores,
        main="Primer Número Elegido \n Por Jugadores Con Consejo / Experiencia",
        xlab="Condición", ylab="Número Elegido", ylim=c(0,30), las=1)
lines(c(10,0),c(0,0))

#### Matrices de Medianas Comparadas ####
#Se introducen las medianas en las matrices
for(a in 1:4){He1_T[a,1]<-median(c(He1_1[a,1],He1_2[a,1],He1_3[a,1]))}
for(a in 1:4){for(b in 1:3){HeT_Tx[a,b]<-median(c(HeT_1[a,b],HeT_2[a,b],HeT_3[a,b],HeT_4[a,b]))}}
for(a in 1:4){HeT_T[a,1]<-median(c(HeT_Tx[a,1],HeT_Tx[a,1],HeT_Tx[a,1]))}
for(a in 1:4){Es1_T[a,1]<-median(c(Es1_1[a,1],Es1_2[a,1],Es1_3[a,1]))}
for(a in 1:4){for(b in 1:3){EsT_Tx[a,b]<-median(c(EsT_1[a,b],EsT_2[a,b],EsT_3[a,b]))}}
for(a in 1:4){EsT_T[a,1]<-median(c(EsT_Tx[a,1],EsT_Tx[a,2],EsT_Tx[a,3]))}
for(a in 1:4){Ex1_T[a,1]<-median(c(Ex1_1[a,1],Ex1_2[a,1],Ex1_3[a,1]))}
for(a in 1:4){for(b in 1:3){ExT_Tx[a,b]<-median(c(ExT_1[a,b],ExT_2[a,b],ExT_3[a,b]))}}
for(a in 1:4){ExT_T[a,1]<-median(c(ExT_Tx[a,1],ExT_Tx[a,2],ExT_Tx[a,3]))}
for(a in 1:4){for(b in 1:3){Sin_Tx[a,b]<-median(c(Pr1_1[a,b],PrT_1[a,b],PrT_2[a,b],PrT_3[a,b]))}}
for(a in 1:4){Sin_T[a,1]<-median(c(Sin_Tx[a,1],Sin_Tx[a,2],Sin_Tx[a,3]))}
for(a in 1:4){for(b in 1:2){SinHex[a,b]<-median(c(He1_1[a,b+1],He1_2[a,b+1],He1_3[a,b+1]))}}
for(a in 1:4){SinHe[a,1]<-median(c(SinHex[a,1],SinHex[a,2]))}
for(a in 1:4){for(b in 1:2){SinEsx[a,b]<-median(c(Es1_1[a,b+1],Es1_2[a,b+1],Es1_3[a,b+1]))}}
for(a in 1:4){SinEs[a,1]<-median(c(SinEsx[a,1],SinEsx[a,2]))}
for(a in 1:4){for(b in 1:2){SinExx[a,b]<-median(c(Ex1_1[a,b+1],Ex1_2[a,b+1],Ex1_3[a,b+1]))}}
for(a in 1:4){SinEx[a,1]<-median(c(SinExx[a,1],SinExx[a,2]))}

#Se guarda en la matriz principal
Todos<-matrix(data=NA,nrow=4,ncol=10) 
Todos<-cbind(He1_T,HeT_T,SinHe,Es1_T,EsT_T,SinEs,Ex1_T,ExT_T,SinEx,Sin_T)

#### Matrices de Medias Comparadas ####
#Se introducen las medias en las matrices
for(a in 1:4){He1_T[a,1]<-mean(c(He1_1[a,1],He1_2[a,1],He1_3[a,1]))}
for(a in 1:4){for(b in 1:3){HeT_Tx[a,b]<-mean(c(HeT_1[a,b],HeT_2[a,b],HeT_3[a,b],HeT_4[a,b]))}}
for(a in 1:4){HeT_T[a,1]<-mean(c(HeT_Tx[a,1],HeT_Tx[a,1],HeT_Tx[a,1]))}
for(a in 1:4){Es1_T[a,1]<-mean(c(Es1_1[a,1],Es1_2[a,1],Es1_3[a,1]))}
for(a in 1:4){for(b in 1:3){EsT_Tx[a,b]<-mean(c(EsT_1[a,b],EsT_2[a,b],EsT_3[a,b]))}}
for(a in 1:4){EsT_T[a,1]<-mean(c(EsT_Tx[a,1],EsT_Tx[a,2],EsT_Tx[a,3]))}
for(a in 1:4){Ex1_T[a,1]<-mean(c(Ex1_1[a,1],Ex1_2[a,1],Ex1_3[a,1]))}
for(a in 1:4){for(b in 1:3){ExT_Tx[a,b]<-mean(c(ExT_1[a,b],ExT_2[a,b],ExT_3[a,b]))}}
for(a in 1:4){ExT_T[a,1]<-mean(c(ExT_Tx[a,1],ExT_Tx[a,2],ExT_Tx[a,3]))}
for(a in 1:4){for(b in 1:3){Sin_Tx[a,b]<-mean(c(Pr1_1[a,b],PrT_1[a,b],PrT_2[a,b],PrT_3[a,b]))}}
for(a in 1:4){Sin_T[a,1]<-mean(c(Sin_Tx[a,1],Sin_Tx[a,2],Sin_Tx[a,3]))}
for(a in 1:4){for(b in 1:2){SinHex[a,b]<-mean(c(He1_1[a,b+1],He1_2[a,b+1],He1_3[a,b+1]))}}
for(a in 1:4){SinHe[a,1]<-mean(c(SinHex[a,1],SinHex[a,2]))}
for(a in 1:4){for(b in 1:2){SinEsx[a,b]<-mean(c(Es1_1[a,b+1],Es1_2[a,b+1],Es1_3[a,b+1]))}}
for(a in 1:4){SinEs[a,1]<-mean(c(SinEsx[a,1],SinEsx[a,2]))}
for(a in 1:4){for(b in 1:2){SinExx[a,b]<-mean(c(Ex1_1[a,b+1],Ex1_2[a,b+1],Ex1_3[a,b+1]))}}
for(a in 1:4){SinEx[a,1]<-mean(c(SinExx[a,1],SinExx[a,2]))}

#Se guarda en la matriz principal
Todos<-matrix(data=NA,nrow=4,ncol=10) 
Todos<-cbind(He1_T,HeT_T,SinHe,Es1_T,EsT_T,SinEs,Ex1_T,ExT_T,SinEx,Sin_T)

#### Comparaciones Heurístico ####

#Se grafica
matplot(Todos[,1:3], type="b", lty=c(2,1,3), lwd=4, pch=21, col=Colores2[1:3], cex=1,
        ylim=c(0,55), xaxp=c(1, 4, 3), yaxp=c(0, 50, 5), las=1)
for(a in 1:4){
  for(b in 1:3){
    points(a,Todos[a,b],col=Colores2[b],pch=21, bg=Colores2[b], cex=1.5)
  }
}
rect(3.55,37.2,4.12,57.3,border=TRUE)
text(3.84,54.5,labels="Uno-Heu      ",col=Colores2[1],cex=0.9, font=2)
text(3.84,47,labels="Todos-Heu   ",col=Colores2[2],cex=0.9, font=2)
text(3.84,40.5,labels="Sin Uno-Heu",col=Colores2[3],cex=0.9, font=2)

#### Comparaciones Estratégico ####

#Se grafica
matplot(Todos[,4:6], type="b", lty=c(2,1,3), lwd=4, pch=21, col=Colores2[4:6], cex=1,
        ylim=c(0,55), xaxp=c(1, 4, 3), yaxp=c(0, 50, 5), las=1)
for(a in 1:4){
  for(b in 4:6){
    points(a,Todos[a,b],col=Colores2[b],pch=21, bg=Colores2[b], cex=1.5)
  }
}
rect(3.55,37.2,4.12,57.3,border=TRUE)
text(3.84,54.5,labels="Uno-Est      ",col=Colores2[4],cex=0.9, font=2)
text(3.84,47,labels="Todos-Est   ",col=Colores2[5],cex=0.9, font=2)
text(3.84,40.5,labels="Sin Uno-Est",col=Colores2[6],cex=0.9, font=2)

#### Comparaciones Experiencia ####

matplot(Todos[,7:9], type="b", lty=c(2,1,3), lwd=4, pch=21, col=Colores2[7:9], cex=1,
        ylim=c(0,55), xaxp=c(1, 4, 3), yaxp=c(0, 50, 5), las=1)
for(a in 1:4){
  for(b in 7:9){
    points(a,Todos[a,b],col=Colores2[b],pch=21, bg=Colores2[b], cex=1.5)
  }
}
rect(3.55,37.2,4.12,57.3,border=TRUE)
text(3.84,54.3,labels="Uno-Exp      ",col=Colores2[7],cex=0.9, font=2)
text(3.84,47,labels="Todos-Exp   ",col=Colores2[8],cex=0.9, font=2)
text(3.84,40.3,labels="Sin Uno-Exp",col=Colores2[9],cex=0.9, font=2)

#### Comparaciones Uno ####

matplot(Todos[,c(1,4,7)], type="b", lty=1, lwd=4, pch=21, col=Colores2[c(1,4,7)], cex=1,
        ylim=c(0,30), xaxp=c(1, 4, 3), yaxp=c(0, 30, 6), las=1)
for(a in 1:4){
  for(b in c(1,4,7)){
    points(a,Todos[a,b],col=Colores2[b],pch=21, bg=Colores2[b], cex=1.3)
  }
}
rect(3.55,20,4.12,30,border=TRUE)
text(3.84,28.3,labels="Uno-Heu",col=Colores2[1],cex=0.9, font=2)
text(3.84,25,labels="Uno-Est",col=Colores2[4],cex=0.9, font=2)
text(3.84,22,labels="Uno-Exp",col=Colores2[7],cex=0.9, font=2)

#### Comparaciones Todos ####

matplot(Todos[,c(2,5,8)], type="b", lty=1, lwd=4, pch=21, col=Colores2[c(2,5,8)], cex=1,
        ylim=c(0,30), xaxp=c(1, 4, 3), yaxp=c(0, 30, 6), las=1)
for(a in 1:4){
  for(b in c(2,5,8)){
    points(a,Todos[a,b],col=Colores2[b],pch=21, bg=Colores2[b], cex=1.3)
  }
}
rect(3.55,20,4.12,30,border=TRUE)
text(3.84,28.3,labels="Todos-Heu",col=Colores2[2],cex=0.9, font=2)
text(3.84,25,labels="Todos-Est",col=Colores2[5],cex=0.9, font=2)
text(3.84,22,labels="Todos-Exp",col=Colores2[8],cex=0.9, font=2)

#### Comparación Individual Prueba ####

matplot(ExT_Tx, type="b", lty=1, lwd=4, pch=21, col=Colores3[1:3], cex=1,
        ylim=c(0,30), xaxp=c(1, 4, 3), yaxp=c(0, 30, 6), las=1)
for(a in 1:4){
  for(b in 1:3){
    points(a,ExT_Tx[a,b],col=Colores3[b],pch=21, bg=Colores3[b], cex=1.3)
  }
}
rect(3.55,20,4.12,30,border=TRUE)
text(3.84,28.3,labels="Todos-Exp 1",col=Colores3[1],cex=0.9, font=2)
text(3.84,25,labels="Todos-Exp 2",col=Colores3[2],cex=0.9, font=2)
text(3.84,22,labels="Todos-Exp 3",col=Colores3[3],cex=0.9, font=2)

#### Iniciar PDF ####

pdf_name<-'Graficas.pdf'
pdf(file=pdf_name,width=9,height=9)
layout(matrix(1:6,ncol=2))

#### Todas las gráficas Uno-Heu ####

matplot(He1_1[1:3], type="b", lty=Tipos3, lwd=Tamaños3, pch=21, col=Colores3[1:3],
        main="One-Heu 1", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(He1_1[a,b] > 0){
points(a,He1_1[a,b-3],col=Colores3[b-3],pch=21, bg=Colores3[b-3], cex=Tamaños4[b-3])}}}
rect(3,90,4.12,110,border=TRUE)
text(3.5,100,labels="Heuristic Yes",col=Colores3[1],cex=0.9, font=2)
text(3.5,95,labels="Heuristic No",col=Colores3[2],cex=0.9, font=2)


matplot(He1_2[1:3], type="b", lty=Tipos3, lwd=Tamaños3, pch=21, col=Colores3[1:3],
        main="One-Heu 2", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(He1_2[a,b] > 0){
  points(a,He1_2[a,b-3],col=Colores3[b-3],pch=21, bg=Colores3[b-3], cex=Tamaños4[b-3])}}}
rect(3,90,4.12,110,border=TRUE)
text(3.5,100,labels="Heuristic Yes",col=Colores3[1],cex=0.9, font=2)
text(3.5,95,labels="Heuristic No",col=Colores3[2],cex=0.9, font=2)

matplot(He1_3[1:3], type="b", lty=Tipos3, lwd=Tamaños3, pch=21, col=Colores3[1:3],
        main="One-Heu 3", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(He1_3[a,b] > 0){
  points(a,He1_3[a,b-3],col=Colores3[b-3],pch=21, bg=Colores3[b-3], cex=Tamaños4[b-3])}}}
rect(3,90,4.12,110,border=TRUE)
text(3.5,100,labels="Heuristic Yes",col=Colores3[1],cex=0.9, font=2)
text(3.5,95,labels="Heuristic No",col=Colores3[2],cex=0.9, font=2)

#### Todas las gráficas Todos-Heu ####

matplot(HeT_1[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="All-Heu 1", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(HeT_1[a,b] > 0){
  points(a,HeT_1[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños4[b-3])}}}

matplot(HeT_2[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="All-Heu 2", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(HeT_2[a,b] > 0){
  points(a,HeT_2[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños4[b-3])}}}

matplot(HeT_3[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="All-Heu 3", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(HeT_3[a,b] > 0){
  points(a,HeT_3[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños4[b-3])}}}

#### Todas las gráficas Uno-Est ####

matplot(Es1_1[1:3], type="b", lty=Tipos3, lwd=Tamaños3, pch=21, col=Colores3[1:3],
        main="One-Str 1", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(Es1_1[a,b] > 0){
  points(a,Es1_1[a,b-3],col=Colores3[b-3],pch=21, bg=Colores3[b-3], cex=Tamaños4[b-3])}}}
rect(3,90,4.12,110,border=TRUE)
text(3.5,100,labels="Strategic Yes",col=Colores3[1],cex=0.9, font=2)
text(3.5,95,labels="Strategic No",col=Colores3[2],cex=0.9, font=2)

matplot(Es1_2[1:3], type="b", lty=Tipos3, lwd=Tamaños3, pch=21, col=Colores3[1:3],
        main="One-Str 2", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(Es1_2[a,b] > 0){
  points(a,Es1_2[a,b-3],col=Colores3[b-3],pch=21, bg=Colores3[b-3], cex=Tamaños4[b-3])}}}
rect(3,90,4.12,110,border=TRUE)
text(3.5,100,labels="Strategic Yes",col=Colores3[1],cex=0.9, font=2)
text(3.5,95,labels="Strategic No",col=Colores3[2],cex=0.9, font=2)

matplot(Es1_3[1:3], type="b", lty=Tipos3, lwd=Tamaños3, pch=21, col=Colores3[1:3],
        main="One-Str 3", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(Es1_3[a,b] > 0){
  points(a,Es1_3[a,b-3],col=Colores3[b-3],pch=21, bg=Colores3[b-3], cex=Tamaños4[b-3])}}}
rect(3,90,4.12,110,border=TRUE)
text(3.5,100,labels="Strategic Yes",col=Colores3[1],cex=0.9, font=2)
text(3.5,95,labels="Strategic No",col=Colores3[2],cex=0.9, font=2)

#### Todas las gráficas Todos-Est ####

matplot(EsT_1[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="All-Str 1", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(EsT_1[a,b] > 0){
  points(a,EsT_1[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños4[b-3])}}}

matplot(EsT_2[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="All-Str 2", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(EsT_2[a,b] > 0){
  points(a,EsT_2[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños4[b-3])}}}

matplot(EsT_3[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="All-Str 3", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(EsT_3[a,b] > 0){
  points(a,EsT_3[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños4[b-3])}}}

#### Todas las gráficas Uno-Exp ####

matplot(Ex1_1[1:3], type="b", lty=Tipos3, lwd=Tamaños3, pch=21, col=Colores3[1:3],
        main="One-Exp 1", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(Ex1_1[a,b] > 0){
  points(a,Ex1_1[a,b-3],col=Colores3[b-3],pch=21, bg=Colores3[b-3], cex=Tamaños4[b-3])}}}
rect(3,90,4.12,110,border=TRUE)
text(3.5,100,labels="Experience Yes",col=Colores3[1],cex=0.9, font=2)
text(3.5,95,labels="Experience No",col=Colores3[2],cex=0.9, font=2)

matplot(Ex1_2[1:3], type="b", lty=Tipos3, lwd=Tamaños3, pch=21, col=Colores3[1:3],
        main="One-Exp 2", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(Ex1_2[a,b] > 0){
  points(a,Ex1_2[a,b-3],col=Colores3[b-3],pch=21, bg=Colores3[b-3], cex=Tamaños4[b-3])}}}
rect(3,90,4.12,110,border=TRUE)
text(3.5,100,labels="Experience Yes",col=Colores3[1],cex=0.9, font=2)
text(3.5,95,labels="Experience No",col=Colores3[2],cex=0.9, font=2)

matplot(Ex1_3[1:3], type="b", lty=Tipos3, lwd=Tamaños3, pch=21, col=Colores3[1:3],
        main="One-Exp 3", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(Ex1_3[a,b] > 0){
  points(a,Ex1_3[a,b-3],col=Colores3[b-3],pch=21, bg=Colores3[b-3], cex=Tamaños4[b-3])}}}
rect(3,90,4.12,110,border=TRUE)
text(3.5,100,labels="Experience Yes",col=Colores3[1],cex=0.9, font=2)
text(3.5,95,labels="Experience No",col=Colores3[2],cex=0.9, font=2)

#### Todas las gráficas Todos-Exp ####

matplot(ExT_1[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="All-Exp 1", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(ExT_1[a,b] > 0){
  points(a,ExT_1[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños4[b-3])}}}

matplot(ExT_2[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="All-Exp 2", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(ExT_2[a,b] > 0){
  points(a,ExT_2[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños4[b-3])}}}

matplot(ExT_3[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="All-Exp 3", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
for(a in 1:4){for(b in 4:6){if(ExT_3[a,b] > 0){
  points(a,ExT_3[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños4[b-3])}}}

#### Terminar PDF ####

dev.off()

#### Preparación ####

pdf_name<-'Graficas2.pdf'
pdf(file=pdf_name,width=9,height=9)
layout(matrix(1:4,ncol=2))

matplot(Pr1_1[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="Preparation \n One-Exp 123", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10), las=1)
for(a in 1:4){for(b in 4:6){if(Pr1_1[a,b] > 0){
  points(a,Pr1_1[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños4[b-3])}}}

matplot(PrT_1[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="Preparation \n All-Exp 1", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10), las=1)
for(a in 1:4){for(b in 4:6){if(PrT_1[a,b] > 0){
  points(a,PrT_1[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños4[b-3])}}}

matplot(PrT_2[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="Preparation \n All-Exp 2", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10), las=1)
for(a in 1:4){for(b in 4:6){if(PrT_2[a,b] > 0){
  points(a,PrT_2[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños2[b-3])}}}

matplot(PrT_3[1:3], type="b", lty=2, lwd=2, pch=21, col=Colores2[1:3],
        main="Preparation \n All-Exp 3", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10), las=1)
for(a in 1:4){for(b in 4:6){if(PrT_3[a,b] > 0){
  points(a,PrT_3[a,b-3],col=Colores2[b-3],pch=21, bg=Colores2[b-3], cex=Tamaños2[b-3])}}}

dev.off()

#### Todos ####
TodosI<-matrix(data=NA,nrow=4,ncol=36)
TodosI<-cbind(He1_1[1:3],HeT_1[1:3],Es1_1[1:3],EsT_1[1:3],Ex1_1[1:3],ExT_1[1:3],
              He1_2[1:3],HeT_2[1:3],Es1_2[1:3],EsT_2[1:3],Ex1_2[1:3],ExT_2[1:3],
              He1_3[1:3],HeT_3[1:3],Es1_3[1:3],EsT_3[1:3],Ex1_3[1:3],ExT_3[1:3])

pdf_name<-'Graficas3.pdf'
pdf(file=pdf_name,width=9,height=9)
layout(matrix(1:4,ncol=2))

matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresTodos,
        main="All", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresHeuT,
        main="Heuristic", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresEstT,
        main="Strategic", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresExpT,
        main="Experience", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)

matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresHeuT,
        main="Heuristic", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresHeu1,
        main="One Heuristic", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresHeu2,
        main="None Heuristic", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresHeu3,
        main="All Heuristic", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)

matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresEstT,
        main="Estrategic", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresEst1,
        main="One Estrategic", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresEst2,
        main="None Estrategic", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresEst3,
        main="All Estrategic", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)

matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresExpT,
        main="Experience", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresExp1,
        main="One Experience", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresExp2,
        main="None Experience", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)
matplot(TodosI, type="b", lty=1, lwd=3, pch=21, col=ColoresExp3,
        main="All Experience", cex=1, ylim=c(0,100), xaxp=c(1, 4, 3), yaxp=c(0, 100, 10),
        las=1)

dev.off()