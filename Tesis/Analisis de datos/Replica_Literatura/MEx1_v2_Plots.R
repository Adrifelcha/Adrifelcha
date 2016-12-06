####################################
# Ploteo de Datos
# EXPERIMENTO 1 (Dos Ebbinghaus)
####################################

setwd("C:/Users/Adrifelcha/Desktop/Tesis/Tesis/CSVs/Datos_Exp1")
rm(list=ls())
dir()

####################################################
####################################################
##################### Aciertos y errores x Ensayo
rm(list=ls())

pdf_name<-'Intento1.pdf'
pdf(file=pdf_name,width=8,height=8)
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$Aciertos,type='o',pch=16, col='green', lwd=.5, ylim=c(0,640),axes=F , ann = F )
  axis(1,at=1:640,labels=c(1:640))
  #axis(2,at=0:10,labels=c("0", "1","2","3","4","5","6","7","8","9","10"))
  points(jaime$Errores,type='o', lty=1, lwd=.5, pch=16, col='red')
  mtext(archive,3,cex=.8)
  text(70,500,paste('Aciertos'),cex=1,col='chartreuse4',f=2)
  text(70,400,paste('Errores'),cex=1,col='red',f=2)
  title("Aciertos y errores por ensayo", outer = TRUE, line = -2)
  
  
  plot(jaime$Exito[1:215],type='o',pch=16, col='darkgreen',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:215,labels=c(1:215))
  axis(2,at=c(0,1), labels=c('Fail', 'Success'))
  mtext('1-215',3,cex=.8)
  
  plot(jaime$Exito[216:430],type='o',pch=16, col='darkgreen',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:215,labels=c(216:430))
  axis(2,at=c(0,1), labels=c('Fail', 'Success'))
  mtext('216-430',3,cex=.8)
  
  plot(jaime$Exito[431:640],type='o',pch=16, col='darkgreen',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:210,labels=c(431:640))
  axis(2,at=c(0,1), labels=c('Fail', 'Success'))
  mtext('431-640',3,cex=.8)
}

dev.off()
#############################################
#############################################
######### Contadores x Ensayo

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$ContadorH,type='o',pch=16, col='blue',ylim=c(0,320),axes=F , ann = F )
  axis(1,at=1:640,labels=sort(unique(jaime$Ensayo)))
  #axis(2,at=0:10,labels=c("0", "1","2","3","4","5","6","7","8","9","10"))
  points(jaime$ContadorF,type='o', lty=3, pch=16, col='red')
  points(jaime$ContadorM,type='o', lty=3, pch=16, col='purple')
  points(jaime$ContadorR,type='o', lty=3, pch=16, col='green')
  text(646,jaime$ContadorF[639]+20,paste("FA"),cex=1,col='red',f=2)
  text(646,jaime$ContadorM[630]+20,paste("M"),cex=1,col='purple',f=2)
  text(646,jaime$ContadorR[639]+20,paste("R"),cex=1,col='green',f=2)
  text(646,jaime$ContadorH[639]+20,paste("H"),cex=1,col='blue',f=2)
  mtext(archive,3,cex=.8)
  title("Counters per trial", outer = TRUE, line = -2)
  
  plot(jaime$outcome[1:215],type='o',pch=16, col='deepskyblue4',ylim=c(1,4),axes=F , ann = F )
  axis(1,at=1:215,labels=c(1:215))
  axis(2,at=c(1,2,3,4), labels=c('F.Alarma', 'Miss', 'Rejection', 'Hit'))
  mtext('1-215',3,cex=.8)
  
  plot(jaime$outcome[216:430],type='o',pch=16, col='deepskyblue4',ylim=c(1,4),axes=F , ann = F )
  axis(1,at=1:215,labels=c(216:430))
  axis(2,at=c(1,2,3,4), labels=c('F.Alarma', 'Miss', 'Rejection', 'Hit'))
  mtext('216-430',3,cex=.8)
  
  plot(jaime$outcome[431:640],type='o',pch=16, col='deepskyblue4',ylim=c(1,4),axes=F , ann = F )
  axis(1,at=1:210,labels=c(431:640))
  axis(2,at=c(1,2,3,4), labels=c('F.Alarma','Miss','Rejection','Hit'))
  mtext('431-640',3,cex=.8)
  
}

############################
######### Choice por ENSAYO

rm(list=ls())
layout(matrix(1:8,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')

  colp <- c('deepskyblue3','darkorchid3', 'green', 'red', 'orange')

#Choice sola
  
  plot(jaime$choice[1:160],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ylab='Respuesta', xlab='Trial' )
  axis(1,at=1:160,labels=c(1:160))
  axis(2,at=0:1,labels=c("No","S?"))
  text(140,9.5,paste("1-160"),cex=1,col='darkorchid',f=2)
  mtext(archive,3,cex=.8)
  
  plot(jaime$choice[161:320],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:160,labels=c(161:320))
  axis(2,at=0:1,labels=c("No","S?"))
  text(140,9,paste("161-320"),cex=1,col='darkorchid3',f=2)
  
  
  plot(jaime$choice[321:480],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:160,labels=c(321:480))
  axis(2,at=0:1,labels=c("No","S?"))
  text(140,8.5,paste("321-480"),cex=1,col='darkorchid2',f=2)
  
  plot(jaime$choice[481:640],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:160,labels=c(481:640))
  axis(2,at=0:1,labels=c("No","S?"))
  text(140,8,paste("481-640"),cex=1,col='darkorchid1',f=2)
  title( "Choice per trial", outer = TRUE, line = -2)
  
### Choice por FACIL DIFICIL
  
    
  plot(jaime$choice[1:160],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ylab='Respuesta', xlab='Trial' )
  axis(1,at=1:160,labels=c(1:160))
  axis(2,at=0:1,labels=c("No","S?"))
  for (a in 1:160){
    if (jaime$facilidad[a] == 'pocos'){
      points(a,jaime$choice[a],pch=16,col=colp[1])}
    if (jaime$facilidad[a] == 'muchos'){
      points(a,jaime$choice[a],pch=16,col=colp[2])}}
  text(140,9.5,paste("1-160"),cex=1,col='darkorchid',f=2)
  mtext("Facil-Dificil",3,cex=.8)
  
  plot(jaime$choice[161:320],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:160,labels=c(161:320))
  axis(2,at=0:1,labels=c("No","S?"))
  for (a in 1:160){
    if (jaime$facilidad[a] == 'pocos'){
      points(a,jaime$choice[a+160],pch=16,col=colp[1])}
    if (jaime$facilidad[a] == 'muchos'){
      points(a,jaime$choice[a+160],pch=16,col=colp[2])}}
  text(140,9,paste("161-320"),cex=1,col='darkorchid3',f=2)
  
  
  plot(jaime$choice[321:480],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:160,labels=c(321:480))
  axis(2,at=0:1,labels=c("No","S?"))
  for (a in 1:160){
    if (jaime$facilidad[a] == 'pocos'){
      points(a,jaime$choice[a+320],pch=16,col=colp[1])}
    if (jaime$facilidad[a] == 'muchos'){
      points(a,jaime$choice[a+320],pch=16,col=colp[2])}}
  text(140,8.5,paste("321-480"),cex=1,col='darkorchid2',f=2)
  
  plot(jaime$choice[481:640],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:160,labels=c(481:640))
  axis(2,at=0:1,labels=c("No","S?"))
  for (a in 1:160){
    if (jaime$facilidad[a] == 'pocos'){
      points(a,jaime$choice[a+480],pch=16,col=colp[1])}
    if (jaime$facilidad[a] == 'muchos'){
      points(a,jaime$choice[a+480],pch=16,col=colp[2])}}
  text(140,8,paste("481-640"),cex=1,col='darkorchid1',f=2)
  #title( "Choice per Trial ", outer = TRUE, line = -2)

##### Choice por SENAL
  
  plot(jaime$choice[1:160],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ylab='Respuesta', xlab='Trial' )
  axis(1,at=1:160,labels=c(1:160))
  axis(2,at=0:1,labels=c("No","S?"))
  for (a in 1:160){
    if (jaime$senal[a] == 'senal'){
      points(a,jaime$choice[a],pch=16,col=colp[3])}
    if (jaime$senal[a] == 'ruido'){
      points(a,jaime$choice[a],pch=16,col=colp[4])}}
  text(140,9.5,paste("1-160"),cex=1,col='darkorchid',f=2)
  mtext("SE?AL - RUIDO",3,cex=.8)
  
  plot(jaime$choice[161:320],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:160,labels=c(161:320))
  axis(2,at=0:1,labels=c("No","S?"))
  for (a in 1:160){
    if (jaime$senal[a] == 'senal'){
      points(a,jaime$choice[a+160],pch=16,col=colp[3])}
    if (jaime$senal[a] == 'ruido'){
      points(a,jaime$choice[a+160],pch=16,col=colp[4])}}
  text(140,9,paste("161-320"),cex=1,col='darkorchid3',f=2)
  
  
  plot(jaime$choice[321:480],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:160,labels=c(321:480))
  axis(2,at=0:1,labels=c("No","S?"))
  for (a in 1:160){
    if (jaime$senal[a] == 'senal'){
      points(a,jaime$choice[a+320],pch=16,col=colp[3])}
    if (jaime$senal[a] == 'ruido'){
      points(a,jaime$choice[a+320],pch=16,col=colp[4])}}
  text(140,8.5,paste("321-480"),cex=1,col='darkorchid2',f=2)
  
  plot(jaime$choice[481:640],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:160,labels=c(481:640))
  axis(2,at=0:1,labels=c("No","S?"))
  for (a in 1:160){
    if (jaime$senal[a] == 'senal'){
      points(a,jaime$choice[a+480],pch=16,col=colp[3])}
    if (jaime$senal[a] == 'ruido'){
      points(a,jaime$choice[a+480],pch=16,col=colp[4])}}
  text(140,8,paste("481-640"),cex=1,col='darkorchid1',f=2)
  #title( "Choice por Ensayo (Signal - Noise )", outer = TRUE, line = -2)
  

  ##### Choice por COLOR
  
  plot(jaime$choice[1:160],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ylab='Respuesta', xlab='Trial' )
  axis(1,at=1:160,labels=c(1:160))
  axis(2,at=0:1,labels=c("No","S?"))
  for (a in 1:160){
    if (jaime$Color[a] == 'Purpura'){
      points(a,jaime$choice[a],pch=16,col=colp[2])}
    if (jaime$Color[a] == 'Naranja'){
      points(a,jaime$choice[a],pch=16,col=colp[5])}
   if (jaime$Color[a] == 'Azul'){
      points(a,jaime$choice[a],pch=16,col=colp[1])}
    if (jaime$Color[a] == 'Verde'){
      points(a,jaime$choice[a],pch=16,col=colp[3])}}
  text(140,9.5,paste("1-160"),cex=1,col='darkorchid',f=2)
  mtext("COLOR",3,cex=.8)
  
  plot(jaime$choice[161:320],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:160,labels=c(161:320))
  axis(2,at=0:1,labels=c("No","S?"))
  for (a in 1:160){
    if (jaime$Color[a] == 'Purpura'){
      points(a,jaime$choice[a+160],pch=16,col=colp[2])}
    if (jaime$Color[a] == 'Naranja'){
      points(a,jaime$choice[a+160],pch=16,col=colp[5])}
  if (jaime$Color[a] == 'Azul'){
    points(a,jaime$choice[a+160],pch=16,col=colp[1])}
  if (jaime$Color[a] == 'Verde'){
    points(a,jaime$choice[a+160],pch=16,col=colp[3])}}
  text(140,9,paste("161-320"),cex=1,col='darkorchid3',f=2)
  
  
  plot(jaime$choice[321:480],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:160,labels=c(321:480))
  axis(2,at=0:1,labels=c("No","S?"))
  for (a in 1:160){
    if (jaime$Color[a] == 'Purpura'){
      points(a,jaime$choice[a+320],pch=16,col=colp[2])}
    if (jaime$Color[a] == 'Naranja'){
      points(a,jaime$choice[a+320],pch=16,col=colp[5])}
  if (jaime$Color[a] == 'Azul'){
    points(a,jaime$choice[a+320],pch=16,col=colp[1])}
  if (jaime$Color[a] == 'Verde'){
    points(a,jaime$choice[a+320],pch=16,col=colp[3])}}
  text(140,8.5,paste("321-480"),cex=1,col='darkorchid2',f=2)
  
  plot(jaime$choice[481:640],type='o',pch=16, col='black',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:160,labels=c(481:640))
  axis(2,at=0:1,labels=c("No","S?"))
  for (a in 1:160){
    if (jaime$Color[a] == 'Purpura'){
      points(a,jaime$choice[a+480],pch=16,col=colp[2])}
    if (jaime$Color[a] == 'Naranja'){
      points(a,jaime$choice[a+480],pch=16,col=colp[5])}
    if (jaime$Color[a] == 'Azul'){
      points(a,jaime$choice[a+480],pch=16,col=colp[1])}
    if (jaime$Color[a] == 'Verde'){
      points(a,jaime$choice[a+480],pch=16,col=colp[3])}}
  text(140,8,paste("481-640"),cex=1,col='darkorchid1',f=2)
  #title( "Choice por Ensayo (Color)", outer = TRUE, line = -2)
  }

##################################
######### Confidence por ENSAYO

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$Confidence[1:160],type='o',pch=16, col='darkorchid',ylim=c(1,10),axes=F , ylab='Confidence Value', xlab='Trial' )
  axis(1,at=1:160,labels=c(1:160))
  axis(2,at=1:6,labels=c("1","2","3","4","5","6"))
  text(140,9.5,paste("1-160"),cex=1,col='darkorchid',f=2)
  mtext(archive,3,cex=.8)
  
  plot(jaime$Confidence[161:320],type='o',pch=16, col='darkorchid3',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:160,labels=c(161:320))
  axis(2,at=1:6,labels=c("1","2","3","4","5","6"))
  text(140,9,paste("161-320"),cex=1,col='darkorchid3',f=2)
  
  
  plot(jaime$Confidence[321:480],type='o',pch=16, col='darkorchid2',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:160,labels=c(321:480))
  axis(2,at=1:6,labels=c("1","2","3","4","5","6"))
  text(140,8.5,paste("321-480"),cex=1,col='darkorchid2',f=2)
  
  
  plot(jaime$Confidence[481:640],type='o',pch=16, col='darkorchid1',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:160,labels=c(481:640))
  axis(2,at=1:6,labels=c("1","2","3","4","5","6"))
  text(140,8,paste("481-640"),cex=1,col='darkorchid1',f=2)
  title( "ConfidenceRate per Trial", outer = TRUE, line = -2)
  
}

######################
######################
#Response Time (1 y 2) across trials


rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  plot(jaime$RTime1,type='o',pch=16, col='purple',ylim=c(0,16),axes=F , ann = F )
  axis(1,at=1:640,labels=sort(unique(jaime$Ensayo)))
  axis(2,at=c(0,2,4,6,8,10,12,14,16),labels=c("0","2","4","6","8","10","12","14","16"))
  points(jaime$RTime2,type='o', lty=3, pch=16, col='brown')
  text(100,14,paste('Estimulo'),cex=1,col='purple',f=2)
  text(100,10,paste('Escala'),cex=1,col='brown',f=2)
  mtext(archive,3,cex=.8)
  title("Tiempo de Respuesta por Ensayo", outer = TRUE, line = -2)
}

################################
################################
#RT en Intervalos de 150 ensayos.

rm(list=ls())

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  {plot(jaime$RTime1[1:160],type='o',pch=16, col='darkorange',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:160,labels=c(1:160))
  axis(2,at=0:20,labels=c(0:20))
  text(145,9.5,paste("1-160"),cex=1,col='darkorange',f=2)
  mtext(archive,3,cex=.8)
  
  
  plot(jaime$RTime1[161:320],type='o',pch=16, col='darkorange1',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:160,labels=c(161:320))
  axis(2,at=0:20,labels=c(0:20))
  text(145,9,paste("161-320"),cex=1,col='darkorange1',f=2)
  
  
  plot(jaime$RTime1[321:480],type='o',pch=16, col='darkorange2',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:160,labels=c(321:480))
  axis(2,at=0:20,labels=c(0:20))
  text(145,8.5,paste("321-480"),cex=1,col='darkorange2',f=2)
  
  
  plot(jaime$RTime1[481:640],type='o',pch=16, col='darkorange3',ylim=c(1,10),axes=F , ann = F )
  axis(1,at=1:160,labels=c(481:640))
  axis(2,at=0:20,labels=c(0:20))
  text(145,8,paste("481-640"),cex=1,col='darkorange3',f=2)
  # text(170,7.5,paste("5"),cex=1,col='violet',f=2)
  title("Tiempo de Respuesta al Estimulo", outer = TRUE, line = -2)
  
  }  
  {plot(jaime$RTime2[1:160],type='o',pch=16, col='violetred1',ylim=c(0,10),axes=F , ann = F )
  axis(1,at=1:160,labels=c(1:160))
  axis(2,at=0:20,labels=c(0:20))
  text(145,9.5,paste("1-160"),cex=1,col='violetred1',f=2)
  mtext(archive,3,cex=.8)
  
  
  plot(jaime$RTime2[161:320],type='o',pch=16, col='violetred2',ylim=c(0,10),axes=F , ann = F )
  axis(1,at=1:160,labels=c(161:320))
  axis(2,at=0:20,labels=c(0:20))
  text(145,9,paste("161-320"),cex=1,col='violetred2',f=2)
  
  
  plot(jaime$RTime2[321:480],type='o',pch=16, col='violetred3',ylim=c(0,10),axes=F , ann = F )
  axis(1,at=1:160,labels=c(321:480))
  axis(2,at=0:20,labels=c(0:20))
  text(145,8.5,paste("321-480"),cex=1,col='violetred3',f=2)
  
  
  plot(jaime$RTime2[481:640],type='o',pch=16, col='violetred4',ylim=c(0,10),axes=F , ann = F )
  axis(1,at=1:160,labels=c(481:640))
  axis(2,at=0:20,labels=c(0:20))
  text(145,8,paste("481-640"),cex=1,col='violetred4',f=2)
  # text(170,7.5,paste("5"),cex=1,col='violet',f=2)
  title( "Tiempo de Respuesta a la Escala", outer = TRUE, line = -2)
  
  }}

###############
############################3
#Hits y Falsas Alarmas x Color

rm(list=ls())
layout(matrix(1:4,ncol=2))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Color <- as.character(jaime$Color)
  cafe <- strsplit(as.character(jaime$Color),split='-')
  #index <- which(jaime$facilidad=='muchos')
  
  
  
  fa <- NULL
  hits <- NULL
  for(nce in sort(unique(jaime$Color))){
    fa <- append(fa, sum(jaime$Falsas.alarmas[jaime$Color==nce]=='True'))
    hits <- append(hits,sum(jaime$Hits[jaime$Color==nce]=='True'))
    print(c(nce,
            fa[length(fa)],
            hits[length(hits)]))
    
  }
  
  plot(hits,type='o',pch=16,col='blue',ylim=c(40,80),axes=F , ann = F )
  axis(2,at=c(40, 50, 60, 70, 80),labels=c("40", "50","60","70","80"),las=1)
  axis(1,at=1:4,labels=sort(unique(jaime$Color)))
  #points(fa,type='o',pch=16,col='red')
  text(2,70,paste('Hits'),cex=1,col='blue',f=2)
  mtext(archive,3,cex=.8)
  title("Hits y F.A. por Color", outer = TRUE, line = -2)
  
  
  plot(fa,type='o',pch=16,col='red',ylim=c(0,40),axes=F , ann = F )
  axis(1,at=1:4,labels=sort(unique(jaime$Color)))
  axis(2,at=c(0, 10, 20, 30, 40),labels=c("0", "10","20","30","40"),las=1)
  #points(fa,type='o',pch=16,col='red')
  text(2,30,paste('F.A.'),cex=1,col='red',f=2)
  mtext(archive,3,cex=.8) 
}