####################################
# Ploteo de Datos
# EXPERIMENTO 1 (Dos Ebbinghaus)
####################################

setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs/Datos_Exp1")
rm(list=ls())
dir()


#####################################
#####################################
#     Evaluando/ GRaficando         #
#        Mirror Effect              #
#####################################
#####################################
#####################################


#####################################
####            HITS Y FALSAS ALARMAS
#####################################


rm(list=ls())
layout(matrix(1:2,ncol=1))
for(archive in dir()){
  jaime <- read.csv(archive)
  fa <- NULL
  hits <- NULL
  conf <- NULL
  for(nce in sort(unique(jaime$tipo))){
    fa <- append(fa, sum(jaime$Falsas.alarmas[jaime$tipo==nce]=='True'))
    hits <- append(hits, sum(jaime$Hits[jaime$tipo==nce]=='True'))
    rate <- (fa+hits)/160
    total <- (fa+hits)
    print(c(nce,
            fa[length(fa)],
            hits[length(hits)],
            rate[length(rate)],
            total[length(total)]))
  }
  
  barplot(total, main = "", xlab = "", ylab = "Cumulative Frequency", font.lab=2, ylim = c(0, 160), axes = FALSE, col =c("deepskyblue3", "darkorchid3", "darkorchid3", "deepskyblue3"))
  #axis(1,at=1:4,labels=sort(unique(jaime$tipo)))
  axis(1,at=c(0.72,1.9,3.1,4.3),labels=c("Fa(AN)", "Fa(BN)", "H(BS)", "H(AS)"), font=2)
  axis(2,at=c(0, 20, 40, 60, 80, 100, 120, 140, 160),labels=c("0","20","40","60", "80", "100", "120", "140", "160"),las=1)
  text(0.72,total[1]+12,paste(total[1]),cex=.8,col='black',f=2)
  text(1.9,total[2]+12,paste(total[2]),cex=.8,col='black',f=2)
  text(3.1,total[3]-12,paste(total[3]),cex=.8,col='black',f=2)
  text(4.3,total[4]-12,paste(total[4]),cex=.8,col='black',f=2)
  text(1.5,100,paste('Hits & F.A.'),cex=1,col='black',f=2)
  mtext(archive,3,cex=.8, line=1)
  title("Mirror Effect: Yes/No Responses", outer = TRUE, line = -2)  
  
  plot(rate, main = "", type='o', pch=16, xlab = "", ylab = "Rate", font.lab=2, ylim = c(0, 1), axes = FALSE, col ='royalblue')
  axis(1,at=1:4,labels=c("Fa(AN)", "Fa(BN)", "H(BS)", "H(AS)"), font=2)
  axis(2,at=c(0, 0.15, 0.30, 0.45, 0.60, 0.75, 0.90, 1),labels=c("0",".15",".30",".45",".60", ".75", ".90", "1"),las=1)
  text(1.1,rate[1]+.1,paste(rate[1]),cex=1,col='blue',f=2)
  text(1.9,rate[2]+.1,paste(rate[2]),cex=1,col='blue',f=2)
  text(3.1,rate[3]-.1,paste(rate[3]),cex=1,col='blue',f=2)
  text(3.9,rate[4]-.1,paste(rate[4]),cex=1,col='blue',f=2)
  text(1.5,.8,paste('Hits & F.A. rates'),cex=1,col='black',f=2)
}  

#####################################
####            Confidence Rating
#####################################

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
  text(1.3,4.5,paste('R(AN)'),cex=1,col='royalblue4')
  text(2.2,4.5,paste('R(BN)'),cex=1,col='royalblue4')
  text(2.9,4.5,paste('R(BS)'),cex=1,col='royalblue4')
  text(3.75,4.5,paste('R(AS)'),cex=1,col='royalblue4')
  mtext(archive,3,cex=.8)
  #text(1.5,.8,paste('Hits & F.A. rate'),cex=1,col='blue',f=2)
  #mtext(archive,3,cex=.8)
  title("Confidence Rating", outer = TRUE, line = -2)
  #points(hits,type='o',pch=16,col='black')
  
  plot(Confidence,type='o',pch=16,col='maroon2',ylim=c(0,6),axes=F , ylab="Confidence Rating", xlab="", font.lab=2)
  axis(1,at=1:4,labels=c("R(AN)", "R(BN)", "R(BS)", "R(AS)"), font=2)
  axis(2,at=c(0, 1, 2, 3, 4, 5, 6),labels=c("0","1", "2","3","4","5","6"),las=1)
  text(1.1,C_AN+.5,paste(C_AN),cex=1,col='violetred',f=2)
  text(1.9,C_BN+.5,paste(C_BN),cex=1,col='violetred',f=2)
  text(3.1,C_BS-.6,paste(C_BS),cex=1,col='violetred',f=2)
  text(3.9,C_AS-.5,paste(C_AS),cex=1,col='violetred',f=2)
  text(1.5,5.5,paste('Mean Confidence Rating'),cex=1,col='violetred4',f=2)
}


#############################################
####            Aciertos y Errores Por Ensayo
#############################################
rm(list=ls())

#pdf_name<-'Intento1.pdf'
#pdf(file=pdf_name,width=8,height=8)
layout(matrix(1:3,ncol=1))
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Ensayo <- as.character(jaime$Ensayo)
  cafe <- strsplit(as.character(jaime$Ensayo),split='-')
  
  a <- c(1,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600,620,640)
  b <- c(1,30,60,90,120,150,180,210,240,270,300,330,360,390,420,450,480,510,540,570,600,630)
  
  plot(jaime$Aciertos,type='o',pch=16, col='green', lwd=.5, ylim=c(0,640), ylab="Cumulative Frequency",axes=F, line=2, xlab="Trial", font.lab=2)
  axis(1,at=a,labels=a)
  axis(2,at=b, labels=b, tck=0, line=-1.3, font=2)
  points(jaime$Errores,type='o', lty=1, lwd=.5, pch=16, col='red')
  mtext(archive,3,cex=1, f=2)
  text(70,500,paste('Aciertos'),cex=1,col='chartreuse4',f=2)
  text(70,400,paste('Errores'),cex=1,col='red',f=2)
  #title("Aciertos y errores por ensayo", outer = TRUE, line = -2)
  
  
  plot(jaime$Exito[1:320],type='o',pch=16, col='darkgreen',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:320,labels=c(1:320))
  axis(2,at=c(0,1), labels=c('Fail', 'Success'), f=2)
  mtext('Trials 1-320',3,cex=.8, font=2)
  
  plot(jaime$Exito[321:640],type='o',pch=16, col='darkgreen',ylim=c(0,1),axes=F , ann = F )
  axis(1,at=1:320,labels=c(321:640))
  axis(2,at=c(0,1), labels=c('Fail', 'Success'), f=2)
  mtext('Trials 321-640',3,cex=.8, font=2)}

#dev.off()
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


####################################
####################################
######       ROC curves     ########
####################################
####################################


rm(list=ls())
layout(matrix(1:1,ncol=1))
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
  }
  
  hits_A <- c()
  falarm_A <- c()
  hits_B <- c()
  falarm_B <- c()
  hits_na <- c()
  falarm_na <- c()
  c <- seq(-10,10,0.1)
  d_null <- 0
  
  for (i in 1:length(c)){
    hits_A[i] <- pnorm((-d_A/2)-c[i])
    falarm_A[i] <- pnorm((d_A/2)-c[i])
    hits_B[i] <- pnorm((-d_B/2)-c[i])
    falarm_B[i] <- pnorm((d_B/2)-c[i])
    hits_na[i] <- pnorm((d_null/2)-c[i])
    falarm_na[i] <- pnorm((-d_null/2)-c[i])
  }
  
  plot(FAr_an,Hr_as, pch=16, col='deepskyblue4', xlim=c(0,1), ylim=c(0,1), xlab='F.A. Rate', ylab='Hit Rate', font.lab=2)
  points(FAr_bn,Hr_bs, lty=3, pch=16, col='darkorchid4')
  lines(hits_A,falarm_A,lwd=2,col='deepskyblue3')
  lines(hits_B,falarm_B,lwd=2,col='darkorchid3')
  lines(hits_na,falarm_na,lwd=1,col='black', lty=2)
  lines(c(0.58, 0.68),c(0.3,0.3), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0.58, 0.68),c(0.2,0.2), lwd=2, lty=1, col="darkorchid3")
  text(FAr_an, Hr_as+.04, paste("D'(A)=", round(d_A,2)), offset=0, cex = 0.8, pos=4, col='deepskyblue4', font=2)
  text(FAr_bn, Hr_bs-.04, paste("D'(B)=", round(d_B,2)), offset=0, cex = 0.8, pos=4, col='darkorchid4', font=2)
  text(0.7, 0.3, labels="D' for A Condition", offset=0, cex = 0.8, pos=4)
  text(0.7, 0.2, labels="D' for B Condition", offset=0, cex = 0.8, pos=4)
  title('ROC per Condition')
  mtext(archive,3,cex=.8)
}
