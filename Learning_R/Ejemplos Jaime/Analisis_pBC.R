#Niveles Cognitivos:
#Información sobre la dinámica del juego y los niveles de otros jugadores
#Jaime Islas
rm(list=ls())

#### Carga de Datos ####
setwd("D:/APLICACION/DATOS")
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

He1_T<-matrix(data=NA,nrow=4,ncol=1)
HeT_Tx<-matrix(data=NA,nrow=4,ncol=3)
HeT_T<-matrix(data=NA,nrow=4,ncol=1)
Es1_T<-matrix(data=NA,nrow=4,ncol=1)
EsT_Tx<-matrix(data=NA,nrow=4,ncol=3)
EsT_T<-matrix(data=NA,nrow=4,ncol=1)
Ex1_T<-matrix(data=NA,nrow=4,ncol=1)
ExT_Tx<-matrix(data=NA,nrow=4,ncol=3)
ExT_T<-matrix(data=NA,nrow=4,ncol=1)
Sin_Tx<-matrix(data=NA,nrow=4,ncol=3)
Sin_T<-matrix(data=NA,nrow=4,ncol=1)
SinHx<-matrix(data=NA,nrow=4,ncol=2)
SinH<-matrix(data=NA,nrow=4,ncol=1)
SinEsx<-matrix(data=NA,nrow=4,ncol=2)
SinEs<-matrix(data=NA,nrow=4,ncol=1)
SinExx<-matrix(data=NA,nrow=4,ncol=2)
SinEx<-matrix(data=NA,nrow=4,ncol=1)

Colores<-c("gray20","gray60")
Colores7<-c("darkorange","blue","firebrick2","deepskyblue3","red","dodgerblue4","deeppink","forestgreen","darkorchid4")

#### Ganancias Heu1 ####
ConHeu<-((sum(He1_1[4])+sum(He1_2[4])+sum(He1_3[4]))/3)
SinHeu<-((sum(He1_1[5])+sum(He1_2[5])+sum(He1_3[5])+sum(He1_1[6])+sum(He1_2[6])+sum(He1_3[6]))/6)
Heu1W<-matrix(data=NA,nrow=4,ncol=2)
Heu1W<-cbind(((He1_1[4]+He1_2[4]+He1_3[4])/3),
             ((He1_1[5]+He1_2[5]+He1_3[5]+He1_1[6]+He1_2[6]+He1_3[6])/6))
Periods<-c(1:4)
barplot(t(Heu1W),names.arg=Periods, beside=T, col=Colores,
        main="Puntos Ganados en Heu1", xlab="Periodo", ylab="Puntos Ganados", ylim=c(0,4))
lines(c(10,0),c(0,0))
rect(1.5,2.8,5.5,3.7,border=TRUE)
text(3.5,3.5,col=Colores[1],paste("Con Consejo =  ", ConHeu),cex=1, font=2)
text(3.5,3,col=Colores[2],paste("Sin Consejo =  ", SinHeu),cex=1, font=2)

#### Ganancias Est1 ####
ConEst<-((sum(Es1_1[4])+sum(Es1_2[4])+sum(Es1_3[4]))/3)
SinEst<-((sum(Es1_1[5])+sum(Es1_2[5])+sum(Es1_3[5])+sum(Es1_1[6])+sum(Es1_2[6])+sum(Es1_3[6]))/6)
Est1W<-matrix(data=NA,nrow=4,ncol=2)
Est1W<-cbind(((Es1_1[4]+Es1_2[4]+Es1_3[4])/3),
             ((Es1_1[5]+Es1_2[5]+Es1_3[5]+Es1_1[6]+Es1_2[6]+Es1_3[6])/6))
Periods<-c(1:4)
barplot(t(Est1W),names.arg=Periods, beside=T, col=Colores,
        main="Puntos Ganados en Est1", xlab="Periodo", ylab="Puntos Ganados", ylim=c(0,4))
lines(c(10,0),c(0,0))
rect(1.7,2.8,5.3,3.7,border=TRUE)
text(3.5,3.5,col=Colores[1],paste("Con Consejo =  ", ConEst),cex=1, font=2)
text(3.5,3,col=Colores[2],paste("Sin Consejo =  ", SinEst),cex=1, font=2)

#### Ganancias Exp1 ####
ConExp<-((sum(Ex1_1[4])+sum(Ex1_2[4])+sum(Ex1_3[4]))/3)
SinExp<-((sum(Ex1_1[5])+sum(Ex1_2[5])+sum(Ex1_3[5])+sum(Ex1_1[6])+sum(Ex1_2[6])+sum(Ex1_3[6]))/6)
Exp1W<-matrix(data=NA,nrow=4,ncol=2)
Exp1W<-cbind(((Ex1_1[4]+Ex1_2[4]+Ex1_3[4])/3),
             ((Ex1_1[5]+Ex1_2[5]+Ex1_3[5]+Ex1_1[6]+Ex1_2[6]+Ex1_3[6])/6))
Periods<-c(1:4)
barplot(t(Exp1W),names.arg=Periods, beside=T, col=Colores,
        main="Puntos Ganados en Exp1", xlab="Periodo", ylab="Puntos Ganados", ylim=c(0,4))
lines(c(10,0),c(0,0))
rect(6.5,2.8,10.6,3.7,border=TRUE)
text(8.5,3.5,col=Colores[1],paste("Con Experiencia =  ", ConExp),cex=1, font=2)
text(8.5,3,col=Colores[2],paste("Sin Experiencia =  ", SinExp),cex=1, font=2)

#### Primera Tirada (Mediana) ####
PTHeu1<-median(c(He1_1[1,1],He1_2[1,1],He1_3[1,1]))
PTHeuT<-median(c(HeT_1[1,1],HeT_2[1,1],HeT_3[1,1],HeT_1[1,2],HeT_2[1,2],HeT_3[1,2],HeT_1[1,3],HeT_2[1,3],HeT_3[1,3]))
PTHeu<-cbind(PTHeu1,PTHeuT)
PTEst1<-median(c(Es1_1[1,1],Es1_2[1,1],Es1_3[1,1]))
PTEstT<-median(c(EsT_1[1,1],EsT_2[1,1],EsT_3[1,1],EsT_1[1,2],EsT_2[1,2],EsT_3[1,2],EsT_1[1,3],EsT_2[1,3],EsT_3[1,3]))
PTEst<-cbind(PTEst1,PTEstT)
PTExp1<-median(c(Ex1_1[1,1],Ex1_2[1,1],Ex1_3[1,1]))
PTExpT<-median(c(ExT_1[1,1],ExT_2[1,1],ExT_3[1,1],ExT_1[1,2],ExT_2[1,2],ExT_3[1,2],ExT_1[1,3],ExT_2[1,3],ExT_3[1,3]))
PTExp<-cbind(PTExp1,PTExpT)

PTPlot<-matrix(data=NA,nrow=3,ncol=2)
PTPlot<-rbind(PTHeu, PTEst, PTExp)

Tipos<-c("Heu1","HeuT", "Est1","EstT","Exp1","ExpT")
barplot(t(PTPlot),names.arg=Tipos, beside=T, col=Colores,
        main="Primer Número Elegido \n Por Jugadores Con Consejo / Experiencia",
        xlab="Condición", ylab="Número Elegido", ylim=c(0,30))
lines(c(10,0),c(0,0))

#### Comparativas Separadas ####
for(x in 1:4){He1_T[x,1]<-median(c(He1_1[x,1],He1_2[x,1],He1_3[x,1]))}
for(a in 1:4){for(b in 1:3){HeT_Tx[a,b]<-median(c(HeT_1[a,b],HeT_2[a,b],HeT_3[a,b],HeT_4[a,b]))}}
for(xx in 1:4){HeT_T[xx,1]<-median(c(HeT_Tx[xx,1],HeT_Tx[xx,1],HeT_Tx[xx,1]))}
for(y in 1:4){Es1_T[y,1]<-median(c(Es1_1[y,1],Es1_2[y,1],Es1_3[y,1]))}
for(c in 1:4){for(d in 1:3){EsT_Tx[c,d]<-median(c(EsT_1[c,d],EsT_2[c,d],EsT_3[c,d]))}}
for(yy in 1:4){EsT_T[yy,1]<-median(c(EsT_Tx[yy,1],EsT_Tx[yy,2],EsT_Tx[yy,3]))}
for(z in 1:4){Ex1_T[z,1]<-median(c(Ex1_1[z,1],Ex1_2[z,1],Ex1_3[z,1]))}
for(e in 1:4){for(f in 1:3){ExT_Tx[e,f]<-median(c(ExT_1[e,f],ExT_2[e,f],ExT_3[e,f]))}}
for(zz in 1:4){ExT_T[zz,1]<-median(c(ExT_Tx[zz,1],ExT_Tx[zz,2],ExT_Tx[zz,3]))}
for(g in 1:4){for(h in 1:3){Sin_Tx[g,h]<-median(c(Pr1_1[g,h],PrT_1[g,h],PrT_2[g,h],PrT_3[g,h]))}}
for(w in 1:4){Sin_T[w,1]<-median(c(Sin_Tx[w,1],Sin_Tx[w,2],Sin_Tx[w,3]))}
for(k in 1:4){for(l in 1:2){SinHx[k,l]<-median(c(He1_1[k,l+1],He1_2[k,l+1],He1_3[k,l+1]))}}
for(v in 1:4){SinH[v,1]<-median(c(SinHx[v,1],SinHx[v,2]))}
for(m in 1:4){for(n in 1:2){SinEsx[m,n]<-median(c(Es1_1[m,n+1],Es1_2[m,n+1],Es1_3[m,n+1]))}}
for(v in 1:4){SinEs[v,1]<-median(c(SinEsx[v,1],SinEsx[v,2]))}
for(o in 1:4){for(p in 1:2){SinExx[o,p]<-median(c(Ex1_1[o,p+1],Ex1_2[o,p+1],Ex1_3[o,p+1]))}}
for(u in 1:4){SinEx[u,1]<-median(c(SinExx[u,1],SinExx[u,2]))}

Todos<-matrix(data=NA,nrow=4,ncol=10) 
Todos<-cbind(He1_T,HeT_T,SinH,Es1_T,EsT_T,SinEs,Ex1_T,ExT_T,SinEx,Sin_T)

matplot(Todos[,1:3], type="b", lty=c(2,1,3), lwd=4, pch=21, col=Colores7[1:3], cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,30), xaxp=c(1, 4, 3),
        yaxp=c(0, 30, 6))
title(main="Comparación de desempeño \n Consejo Heurístico", cex.main=0.9)
for(i in 1:4){
  for(j in 1:3){
    points(i,Todos[i,j],col=Colores7[j],pch=21, bg=Colores7[j], cex=1.5)
  }
}
rect(3.2,24,3.8,30,border=TRUE)
text(3.5,29.2,labels="Heu1",col=Colores7[1],cex=0.9, font=2)
text(3.5,25.2,labels="HeuTodos",col=Colores7[2],cex=0.9, font=2)
text(3.5,27.2,labels="Sin Heu",col=Colores7[3],cex=0.9, font=2)

matplot(Todos[,4:6], type="b", lty=c(2,1,3), lwd=4, pch=21, col=Colores7[4:6], cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,55), xaxp=c(1, 4, 3),
        yaxp=c(0, 55, 11))
title(main="Comparación de desempeño \n Consejo Estratégico", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    points(i,Todos[i,j],col=Colores7[j],pch=21, bg=Colores7[j], cex=1.5)
  }
}
rect(3.2,35,3.8,45,border=TRUE)
text(3.5,43,labels="Est1",col=Colores7[4],cex=0.9, font=2)
text(3.5,37,labels="EstTodos",col=Colores7[5],cex=0.9, font=2)
text(3.5,40,labels="Sin Est",col=Colores7[6],cex=0.9, font=2)

matplot(Todos[,7:9], type="b", lty=c(2,1,3), lwd=4, pch=21, col=Colores7[7:9], cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,30), xaxp=c(1, 4, 3),
        yaxp=c(0, 30, 6))
title(main="Comparación de desempeño \n Experiencia", cex.main=0.9)
for(i in 1:4){
  for(j in 7:9){
    points(i,Todos[i,j],col=Colores7[j],pch=21, bg=Colores7[j], cex=1.5)
  }
}
rect(3.2,24,3.8,30,border=TRUE)
text(3.5,29.2,labels="Exp1",col=Colores7[7],cex=0.9, font=2)
text(3.5,25.2,labels="ExpTodos",col=Colores7[8],cex=0.9, font=2)
text(3.5,27.2,labels="Sin Exp",col=Colores7[9],cex=0.9, font=2)

matplot(Todos[,c(1,4,7)], type="b", lty=1, lwd=4, pch=21, col=Colores7[c(1,4,7)], cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,30), xaxp=c(1, 4, 3),
        yaxp=c(0, 30, 6))
title(main="Comparación de desempeño \n Condiciones donde solo un jugador tiene consejo / experiencia", cex.main=0.9)
for(i in 1:4){
  for(j in c(1,4,7)){
    points(i,Todos[i,j],col=Colores7[j],pch=21, bg=Colores7[j], cex=1.3)
  }
}
rect(3.2,24,3.8,30,border=TRUE)
text(3.5,29,labels="Heu1",col=Colores7[1],cex=0.9, font=2)
text(3.5,27,labels="Est1",col=Colores7[4],cex=0.9, font=2)
text(3.5,25,labels="Exp1",col=Colores7[7],cex=0.9, font=2)

matplot(Todos[,c(2,5,8)], type="b", lty=1, lwd=4, pch=21, col=Colores7[c(2,5,8)], cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,30), xaxp=c(1, 4, 3),
        yaxp=c(0, 30, 6))
title(main="Comparación de desempeño \n Condiciones donde todos tienen consejo / experiencia", cex.main=0.9)
for(i in 1:4){
  for(j in c(2,5,8)){
    points(i,Todos[i,j],col=Colores7[j],pch=21, bg=Colores7[j], cex=1.3)
  }
}
rect(3.2,24,3.8,30,border=TRUE)
text(3.5,29,labels="HeuTodos",col=Colores7[2],cex=0.9, font=2)
text(3.5,27,labels="EstTodos",col=Colores7[5],cex=0.9, font=2)
text(3.5,25,labels="ExpTodos",col=Colores7[8],cex=0.9, font=2)