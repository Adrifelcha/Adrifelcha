setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs/Datos_MirrExp_2Ebb")
rm(list=ls())
dir()


##########
#               YES x Color
#############################################

rm(list=ls())
for(archive in dir()){
  
  jaime <- read.csv(archive)
  jaime$Color <- as.character(jaime$Color)
  cafe <- strsplit(as.character(jaime$Color),split='-')
    print(c(archive))
  
  yes <- NULL
  no <- NULL
  for(nce in sort(unique(jaime$Color))){
    yes<- append(yes, sum(jaime$Respuesta[jaime$Color==nce]=='s'))
    no <- append(no,sum(jaime$Respuesta[jaime$Color==nce]=='n'))
    print(c(nce,
            'Sí', yes[length(yes)],
            'No', no[length(no)]))}
  
  barplot(yes, main = "", xlab = "", horiz=T, ylab = " ", ylim = c(0, 5),xlim = c(0,160), axes = FALSE, col = c("deepskyblue3", "darkorange2", "darkorchid1", "chartreuse3"))
  lines(c(yes[1], 160),c(0.7,0.7), lwd=2, lty=1, col="deepskyblue3")
  lines(c(yes[2], 160),c(1.9,1.9), lwd=2, lty=1, col="darkorange2")
  lines(c(yes[3], 160),c(3.1,3.1), lwd=2, lty=1, col="darkorchid1")
  lines(c(yes[4], 160),c(4.3,4.3), lwd=2, lty=1, col="chartreuse3")
  axis(1,at=c(0, 32, 64, 96, 128, 160),labels=c("0", "32", "64", "96","128", "160"), las=1)
  axis(2,at=c(0.7,1.9,3.1,4.3),labels=c("Azul","Naranja", "Purpura", "Verde"), las=3)
  text(yes[1]-5, 0.7,paste(yes[1]),cex=1,col='black',f=2)
  text(yes[2]-5, 1.9,paste(yes[2]),cex=1,col='black',f=2)
  text(yes[3]-5,3.1,paste(yes[3]),cex=1,col='black',f=2)
  text(yes[4]-5,4.3,paste(yes[4]),cex=1,col='black',f=2)
  text(yes[1]+5, 0.85,paste(no[1]),cex=1,col='black',f=2)
  text(yes[2]+5, 2.05,paste(no[2]),cex=1,col='black',f=2)
  text(yes[3]+5,3.25,paste(no[3]),cex=1,col='black',f=2)
  text(yes[4]+5,4.45,paste(no[4]),cex=1,col='black',f=2)
  text(yes[3]/2,3.1,'Sí',cex=3,col='black',f=3)
  text(yes[3]+no[3]/2,3.1,'No',cex=3,col='black',f=3)
  mtext("Número de Respuestas", side = 1, line = 2.5, cex = 2, font = 2)
  mtext("Color", side = 4, line=0.8, cex = 2, font = 1, las = 3)
  #mtext('Sí por Color',3,cex=1.5, font=2)
  title(archive, outer = TRUE, line = -3.5)}

