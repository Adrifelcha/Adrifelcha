####################################
# Ploteo de Datos
# EXPERIMENTO 2 (Dos Ebbinghaus)
####################################
rm(list=ls())

####################
#################### 1   Participante 1 Exp 2 - > Elecciones por ensayo
####################
rm(list=ls())
setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs/Datos_MirrExp_2Ebb")
dir()
archive <-'Exp2_Participante1.csv'
jaime <- read.csv(archive)
jaime$Ensayo <- as.character(jaime$Ensayo)
cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  m <- c(1,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640)
  n <- c(1,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320)
  o <- c(321,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640)
  
  
  colp <- c('deepskyblue3','darkorchid3', 'green', 'red', 'orange')
  
  #Choice sola
  layout(matrix(1:2,ncol=1))
  plot(jaime$choice[1:320],type='o',pch=16, col='dodgerblue',ylim=c(0,1),axes=F , ylab='Respuesta', xlab='Trials 1-320', font.lab=2 )
  axis(1,at=n,labels=n)
  axis(2,at=0:1,labels=c("No","Sí"))
  text(140,9.5,paste("1-160"),cex=1,col='darkorchid',f=2)
  mtext(archive,3,cex=1.2, f=2, line=2)
  
  plot(jaime$choice[321:640],type='o',pch=16, col='dodgerblue',ylim=c(0,1),axes=F , ylab='Respuesta', xlab='Trials 321-640', font.lab=2 )
  axis(1,at=n,labels=o)
  axis(2,at=0:1,labels=c("No","Sí"))
  text(140,9.5,paste("1-160"),cex=1,col='darkorchid',f=2)
  
  
  
  ### Choice por FACIL DIFICIL
  
  layout(matrix(1:2,ncol=1))
  
  plot(jaime$choice[1:640],type='o',pch=16, col='black',ylim=c(0,1), xlim=c(0,700),axes=F , ylab='Respuesta', xlab='Trial', font.lab=2 )
  axis(1,at=m,labels=m)
  axis(2,at=0:1,labels=c("No","Sí"))
  for (a in 1:640){
    if (jaime$facilidad[a] == 'pocos'){
      points(a,jaime$choice[a],pch=16,col=colp[1])}
    if (jaime$facilidad[a] == 'muchos'){
      points(a,jaime$choice[a],pch=16,col=colp[2])}}
  text(670,0.8,"Fácil",cex=1,col=colp[1],f=2)
  text(670,0.3,"Difícil",cex=1,col=colp[2],f=2)
  mtext("Respuesta Registrada por Condición",3,cex=0.8, f=3)
  mtext(archive, 3, line=2, cex=1.2, f=2)
  
  
  ##### Choice por SENAL
  
  plot(jaime$choice[1:640],type='o',pch=16, col='black',ylim=c(0,1), xlim=c(0,700),axes=F , ylab='Respuesta', xlab='Trial', font.lab=2 )
  axis(1,at=m,labels=m)
  axis(2,at=0:1,labels=c("No","Sí"))
  for (a in 1:640){
    if (jaime$senal[a] == 'senal'){
      points(a,jaime$choice[a],pch=16,col=colp[3])}
    if (jaime$senal[a] == 'ruido'){
      points(a,jaime$choice[a],pch=16,col=colp[4])}}
  text(670,0.8,"Señal",cex=1,col='forestgreen',f=2)
  text(670,0.3,"Ruido",cex=1,col=colp[4],f=2)
  text(140,9.5,paste("1-160"),cex=1,col='darkorchid',f=2)
  mtext("Respuesta Registrada por Estímulo",3,cex=.8, f=3)
  