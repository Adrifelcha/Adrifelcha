####################################
# Figuras de Participantes incluidos en la Tesis
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
  plot(jaime$choice[1:320],type='o',pch=16, col='dodgerblue',ylim=c(0,1),axes=F, ann = FALSE)
  axis(1,at=n,labels=n)
  axis(2,at=0:1,labels=c("No","Sí"))
  mtext(archive,3,cex=2.5, f=2, line=2)
  mtext(side=1, text = "Ensayos 1-320", line=2.5, cex=1.6)
  mtext(side=2, text = "Respuesta", line=2.5, cex=1.6)
  
  plot(jaime$choice[321:640],type='o',pch=16, col='dodgerblue',ylim=c(0,1),axes=F , ann = FALSE, font.lab=2 )
  axis(1,at=n,labels=o)
  axis(2,at=0:1,labels=c("No","Sí"))
  mtext(side=1, text = "Ensayos 320-640", line=2.5, cex=1.6)
  mtext(side=2, text = "Respuesta", line=2.5, cex=1.6)
  
  ### Choice por FACIL DIFICIL
  
  layout(matrix(1:2,ncol=1))
  
  plot(jaime$choice[1:640],type='o',pch=16, col='black',ylim=c(0,1), xlim=c(0,700),axes=F ,ann=FALSE, font.lab=2 )
  axis(1,at=m,labels=m)
  axis(2,at=0:1,labels=c("No","Sí"))
  for (a in 1:640){
    if (jaime$facilidad[a] == 'pocos'){
      points(a,jaime$choice[a],pch=16,col=colp[1])}
    if (jaime$facilidad[a] == 'muchos'){
      points(a,jaime$choice[a],pch=16,col=colp[2])}}
  text(690,0.8,"Fácil (A)",cex=1.2,col=colp[1],f=2)
  text(690,0.3,"Difícil (B) ",cex=1.2,col=colp[2],f=2)
  mtext("Respuesta por Clase de Estímulo",3,cex=1.2, f=3, line=0.3)
  mtext(side=1, text = "Ensayos 1-640", line=2.5, cex=1.6)
  mtext(side=2, text = "Respuesta", line=2.5, cex=1.6)
  mtext(archive, 3, line=2, cex=2.5, f=2)
  
  ##### Choice por SENAL
  
  plot(jaime$choice[1:640],type='o',pch=16, col='black',ylim=c(0,1), xlim=c(0,700),axes=F , ann=FALSE, font.lab=2 )
  axis(1,at=m,labels=m)
  axis(2,at=0:1,labels=c("No","Sí"))
  for (a in 1:640){
    if (jaime$senal[a] == 'senal'){
      points(a,jaime$choice[a],pch=16,col=colp[3])}
    if (jaime$senal[a] == 'ruido'){
      points(a,jaime$choice[a],pch=16,col=colp[4])}}
  text(680,0.8,"Señal",cex=1.2,col='forestgreen',f=2)
  text(680,0.3,"Ruido",cex=1.2,col=colp[4],f=2)
  text(140,9.5,paste("1-160"),cex=1,col='darkorchid',f=2)
  mtext("Respuesta por Tipo de Ensayo",3,cex=1.2, line=0.3, f=3)
  mtext(side=1, text = "Ensayos 1-640", line=2.5, cex=1.6)
  mtext(side=2, text = "Respuesta", line=2.5, cex=1.6)
  
  
#################################
######### Confidence por ENSAYO
##########################################
  rm(list=ls())
  setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs/Datos_MirrExp_2Ebb")
  dir()
  layout(matrix(1:2,ncol=1))
  archive <-'Exp2_Participante15.csv'
  jaime <- read.csv(archive)
    a <- c(1,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320)
    b <- c(321,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640)
    
    jaime <- read.csv(archive)
    jaime$Ensayo <- as.character(jaime$Ensayo)
    cafe <- strsplit(as.character(jaime$Ensayo),split='-')
    
    plot(jaime$Confidence[1:320],type='o',pch=16, col='hotpink3',ylim=c(1,6),axes=F , ann=FALSE, font.lab=2)
    axis(1,at=a,labels=a)
    axis(2,at=1:6,labels=c("1","2","3","4","5","6"))
    text(140,9.5,paste("1-160"),cex=1,col='darkorchid',f=2)
    #title( "Confidence Rating per Trial", line = 3)
    mtext(archive, 3, line=1, col='black', cex=2.5, font=2)
    mtext(side=1, text = "Ensayos 1-320", line=2.5, cex=1.6)
    mtext(side=2, text = "Puntaje", line=2.5, cex=1.6)
    
    plot(jaime$Confidence[321:640],type='o',pch=16, col='hotpink3',ylim=c(1,6), ann=FALSE, axes=F, font.lab=2 )
    axis(1,at=a,labels=b)
    axis(2,at=1:6,labels=c("1","2","3","4","5","6"))
    text(140,8.5,paste("321-480"),cex=1,col='darkorchid2',f=2)
    mtext(side=1, text = "Ensayos 321-640", line=2.5, cex=1.6)
    mtext(side=2, text = "Puntaje", line=2.5, cex=1.6)
  
  
#############################################
####            Aciertos y Errores Por Ensayo
#############################################
  rm(list=ls())
  setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs/Datos_MirrExp_2Ebb")
  dir()
  layout(matrix(1:1,ncol=1))
  archive <-'Exp2_Participante14.csv'
  jaime <- read.csv(archive)
    jaime <- read.csv(archive)
    jaime$Ensayo <- as.character(jaime$Ensayo)
    cafe <- strsplit(as.character(jaime$Ensayo),split='-')
      
    a <- c(1,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640)
    b <- c(1,30,60,90,120,150,180,210,240,270,300,330,360,390,420,450,480,510,540,570,600,630)
    
    plot(jaime$Aciertos,type='o',pch=16, col='green', lwd=.5, ylim=c(0,640),ann=FALSE ,axes=F, line=2, font.lab=2)
    axis(1,at=a,labels=a)
    axis(2,at=b, labels=b, tck=0, line=-1.3, font=2)
    points(jaime$Errores,type='o', lty=1, lwd=.5, pch=16, col='red')
    mtext(archive,3,cex=2.5, f=2)
    text(70,500,paste('Aciertos'),cex=1.2,col='chartreuse4',f=2)
    text(70,400,paste('Errores'),cex=1.2,col='red',f=2)
    #title("Aciertos y errores por ensayo", outer = TRUE, line = -2)
    mtext(side=1, text = "Ensayos 1-640", line=2.5, cex=1.3)
    mtext(side=2, text = "Frecuencia Acumulada", line=2, cex=1.6)
  
  layout(matrix(1:2,ncol=1))
    
    plot(jaime$Exito[1:320],type='o',pch=16, col='darkgreen',ylim=c(0,1),axes=F , ann = F )
    axis(1,at=1:320,labels=c(1:320))
    axis(2,at=c(0,1), labels=c('Error', 'Acierto'), f=2)
    mtext(side=1, text = "Ensayos 1-320", line=2.5, cex=1.3)
    mtext(side=2, text = "Resultado", line=2.2, cex=1.4)
    
    plot(jaime$Exito[321:640],type='o',pch=16, col='darkgreen',ylim=c(0,1),axes=F , ann = F )
    axis(1,at=1:320,labels=c(321:640))
    axis(2,at=c(0,1), labels=c('Error', 'Acierto'), f=2)
    mtext(side=1, text = "Ensayos 321-640", line=2.5, cex=1.3)
    mtext(side=2, text = "Resultado", line=2.2, cex=1.4)
  
########################################
####                   Contadores por Ensayo
#############################################
  rm(list=ls())
  setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs/Datos_MirrExp_2Ebb")
  dir()
  layout(matrix(1:2,ncol=1))
  archive <-'Exp2_Participante14.csv'
  jaime <- read.csv(archive)
    jaime$Ensayo <- as.character(jaime$Ensayo)
    cafe <- strsplit(as.character(jaime$Ensayo),split='-')
        
    a <- c(1,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640)
    b <- c(1,30,60,90,120,150,180,210,240,270,300,330,360,390,420,450,480,510,540,570,600,630)
    
    plot(jaime$ContadorH,type='o',pch=16, col='blue',ylim=c(0,320),axes=F , ann=FALSE)
    axis(1,at=a,labels=a)
    axis(2,at=b, labels=b, tck=0, line=-1.3, font=2)
    points(jaime$ContadorF,type='o', lty=3, pch=16, col='red')
    points(jaime$ContadorM,type='o', lty=3, pch=16, col='purple')
    points(jaime$ContadorR,type='o', lty=3, pch=16, col='green')
    text(646,jaime$ContadorF[639]+20,paste("FA"),cex=1,col='red',f=2)
    text(646,jaime$ContadorM[630]+20,paste("M"),cex=1,col='purple',f=2)
    text(646,jaime$ContadorR[639]+20,paste("R"),cex=1,col='green',f=2)
    text(646,jaime$ContadorH[639]+20,paste("H"),cex=1,col='blue',f=2)
    mtext(archive,3,cex=2.5, f=2)
    mtext(side=1, text = "Ensayos 1-640", line=2.5, cex=1.3)
    mtext(side=2, text = "Acumulado", line=2.2, cex=1.4)
    #title("Counters per trial", outer = TRUE, line = -2)
  
    plot(jaime$outcome[1:640],type='o',pch=16, col='deepskyblue4',ylim=c(1,4),axes=F , ann=FALSE)
    axis(1,at=a,labels=a)
    axis(2,at=c(1,2,3,4), labels=c('FA', 'O', 'R', 'H'),f=2)
    mtext(side=1, text = "Ensayos 1-640", line=2.5, cex=1.3)
    mtext(side=2, text = "Resultado", line=2.2, cex=1.4)
  
###########################################
#               Hits y Falsas Alarmas x Color
#############################################
  rm(list=ls())
  setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs/Datos_MirrExp_1Ebb")
  dir()
  layout(matrix(1:2,ncol=2, byrow = TRUE))
  archive <-'Exp1_Participante14.csv'
  jaime <- read.csv(archive)
    jaime$color <- as.character(jaime$color)
    cafe <- strsplit(as.character(jaime$color),split='-')
    fa <- NULL
    hits <- NULL
    for(nce in sort(unique(jaime$color))){
      fa <- append(fa, sum(jaime$Falsas.alarmas[jaime$color==nce]=='True'))
      hits <- append(hits,sum(jaime$Hits[jaime$color==nce]=='True'))
      print(c(nce,
              'F.A.', fa[length(fa)],
              'Hits', hits[length(hits)]))}
          
    barplot(hits, main = "", ylim = c(0, 100), axes = FALSE, col = c("dodgerblue3","firebrick3", "chocolate3", "darkorchid4", "forestgreen"))
    axis(2,at=c(0, 20, 40, 60, 80, 100),labels=c("0", "20", "40","60","80","100"),las=1)
    axis(1,at=c(0.7,1.9,3.1,4.3,5.5),labels=c("Azul","Rojo", "Anaranjado", "Púrpura", "Verde"))
    text(0.7,hits[1]+5,paste(hits[1]),cex=1,col='black',f=1)
    text(1.9,hits[2]+5,paste(hits[2]),cex=1,col='black',f=1)
    text(3.1,hits[3]+5,paste(hits[3]),cex=1,col='black',f=1)
    text(4.3,hits[4]+5,paste(hits[4]),cex=1,col='black',f=1)
    text(5.5,hits[5]+5,paste(hits[5]),cex=1,col='black',f=1)
    mtext("Color", side = 1, line = 2.5, cex = 1, font = 2)
    mtext("Hits", side = 2, line = 3, cex = 1, font = 2, las = 0)
    mtext('Hits por color',3,cex=1.5, font=2)
    mtext(archive, outer = TRUE, line = -2, cex=2.4, font=2)
          
    barplot(fa, main = "", xlab = "", ylab = " ", ylim = c(0, 100), axes = FALSE, col =c("dodgerblue3","firebrick3", "chocolate3", "darkorchid4", "forestgreen"))
    axis(2,at=c(0, 20, 40, 60, 80, 100),labels=c("0", "20", "40","60","80","100"),las=1)
    axis(1,at=c(0.7,1.9,3.1,4.3,5.5),labels=c("Azul","Rojo", "Naranja", "Púrpura", "Verde"))
    text(0.7,fa[1]+5,paste(fa[1]),cex=1,col='black',f=1)
    text(1.9,fa[2]+5,paste(fa[2]),cex=1,col='black',f=1)
    text(3.1,fa[3]+5,paste(fa[3]),cex=1,col='black',f=1)
    text(4.3,fa[4]+5,paste(fa[4]),cex=1,col='black',f=1)
    text(5.5, fa[5]+5,paste(fa[5]), cex=1,col='black',f=1)
    mtext("Color", side = 1, line = 2.5, cex = 1, font = 2)
    mtext("Falsas Alarmas", side = 2, line = 3, cex = 1, font = 2, las = 0)
    mtext('F. Alarmas por Color',3,cex=1.5, font=2)
    
####################################################
#               Yes/No por Color
####################################################
  rm(list=ls())
  setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs/Datos_MirrExp_2Ebb")
  dir()
  layout(matrix(1:2,ncol=1))
  archive <-'Exp1_Participante13.csv'
  jaime <- read.csv(archive)
    cafe <- strsplit(as.character(jaime$color),split='-')
    print(c(archive))
    yes <- NULL
    no <- NULL
    for(nce in sort(unique(jaime$color))){
      yes<- append(yes, sum(jaime$Respuesta[jaime$color==nce]=='s'))
      no <- append(no,sum(jaime$Respuesta[jaime$color==nce]=='n'))
      print(c(nce,
              'Sí', yes[length(yes)],
              'No', no[length(no)]))}
    barplot(yes, main = "", xlab = "", horiz=T, ylab = " ", ylim = c(0, 6),xlim = c(0,128), axes = FALSE, col = c("deepskyblue3","firebrick2", "darkorange2", "darkorchid1", "chartreuse3"))
    lines(c(yes[1], 128),c(0.7,0.7), lwd=2, lty=1, col="deepskyblue3")
    lines(c(yes[2], 128),c(1.9,1.9), lwd=2, lty=1, col="firebrick2")
    lines(c(yes[3], 128),c(3.1,3.1), lwd=2, lty=1, col="darkorange2")
    lines(c(yes[4], 128),c(4.3,4.3), lwd=2, lty=1, col="darkorchid1")
    lines(c(yes[5], 128),c(5.5,5.5), lwd=2, lty=1, col="chartreuse3")
    axis(1,at=c(0, 32, 64, 96, 128),labels=c("0", "32", "64", "96","128"), las=1)
    axis(2,at=c(0.7,1.9,3.1,4.3,5.5),labels=c("Azul","Rojo", "Naranja", "Púrpura", "Verde"), las=3)
    text(yes[1]-5, 0.7,paste(yes[1]),cex=1,col='black',f=2)
    text(yes[2]-5, 1.9,paste(yes[2]),cex=1,col='black',f=2)
    text(yes[3]-5,3.1,paste(yes[3]),cex=1,col='black',f=2)
    text(yes[4]-5,4.3,paste(yes[4]),cex=1,col='black',f=2)
    text(yes[5]-5,5.5,paste(yes[5]),cex=1,col='black',f=2)
    text(yes[1]+5, 0.85,paste(no[1]),cex=1,col='black',f=2)
    text(yes[2]+5, 2.05,paste(no[2]),cex=1,col='black',f=2)
    text(yes[3]+5,3.25,paste(no[3]),cex=1,col='black',f=2)
    text(yes[4]+5,4.45,paste(no[4]),cex=1,col='black',f=2)
    text(yes[5]+5,5.65,paste(no[5]),cex=1,col='black',f=2)
    text(yes[3]/2,3.1,'Sí',cex=3,col='black',f=3)
    text(yes[3]+no[3]/2,3.1,'No',cex=3,col='black',f=3)
    mtext("Número de Respuestas", side = 1, line = 2.5, cex = 2, font = 2)
    mtext("Color", side = 4, line=0.8, cex = 2, font = 1, las = 3)
    #mtext('Sí por color',3,cex=1.5, font=2)
    title(archive, outer = TRUE, line = -3.5)