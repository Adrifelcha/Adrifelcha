setwd("C:/Users/Adriana/Desktop/Felisa") #Directorio de trabajo
rm(list=ls())  #Reseteamos  el espacio de trabajo
archive <-'Batería_iPhone6s.csv'  #Señalamos el archivo que contiene los datos
datos <- read.csv(archive)    #'Leemos' el archivo

Tiempo <- datos$Tiempo
Carga_1 <- datos$Carga_1
Carga_2 <- datos$Carga_2
Delta <- datos$Delta
Zero <- rep('0',length(Tiempo))


#Todos los datos registrados
plot(-3, xlim= c(0,18), ylim=c(0,100), col='white', xlab="", ylab="", axes=FALSE)
for(a in 1:length(Tiempo)){
  if(Carga_1[a] > Carga_2[a]){   #si el Sujeto aparece en el grupo donde Largo es Señal 
    lines(c(Zero[a],Tiempo[a]),c(Carga_1[a],Carga_2[a]), lwd=2, lty=1, col="red")
    } else {
    lines(c(Zero[a],Tiempo[a]),c(Carga_1[a],Carga_2[a]), lwd=2, lty=1, col="forestgreen")}}
lines(c(3,3),c(0,100), lwd=2, lty=2, col="black")
axis(2,at=c(0,10,20,30,40,50,60,70,80,90,100),labels=c("0%","10","20","30","40","50","60","70","80","90","100%"), font=2)
axis(1,at=c(0,2,4,6,8,10,12,14,16,18),labels=c("0","2","4","6","8","10","12","14","16","18"),las=1)
#mtext("Carga (%)",1,cex=1.3, line=3, f=2)
#mtext("Tiempo (hrs)",2,cex=1.3, line=3, f=2)
title("Cambios en la batería", outer = TRUE, line = -2)

#Tiempos de CARGA
plot(-3, xlim= c(0,4), ylim=c(0,100), col='white', xlab="", ylab="", axes=FALSE)
for(a in 1:length(Tiempo)){
  if(Carga_1[a] > Carga_2[a]){   #si el Sujeto aparece en el grupo donde Largo es Señal 
    lines(c(100,100),c(100,100), lwd=2, lty=1, col="white")
  } else {
    lines(c(Zero[a],Tiempo[a]),c(Carga_1[a],Carga_2[a]), lwd=2, lty=1, col="forestgreen")}}
lines(c(3,3),c(0,100), lwd=2, lty=2, col="black")
lines(c(2,2),c(0,100), lwd=2, lty=2, col="black")
lines(c(2.33,2.33),c(0,100), lwd=2, lty=2, col="darkgray")
lines(c(1,1),c(0,100), lwd=2, lty=2, col="black")
axis(2,at=c(0,10,20,30,40,50,60,70,80,90,100),labels=c("0%","10","20","30","40","50","60","70","80","90","100%"), font=2)
axis(1,at=c(0,1,2,3,4),labels=c("0","1","2","3","4"),las=1)
mtext("Carga (%)",2,cex=1.3, line=3, f=2)
mtext("Tiempo (hrs)",1,cex=1.3, line=3, f=2)
title("Cargas registradas", outer = TRUE, line = -2)

#Tiempos de Descarga
plot(-3, xlim= c(0,18), ylim=c(0,100), col='white', xlab="", ylab="", axes=FALSE)
for(a in 1:length(Tiempo)){
  if(Carga_1[a] > Carga_2[a]){ 
    if(datos$Bluetooth[a] == 'Sí'){ 
      lines(c(Zero[a],Tiempo[a]),c(Carga_1[a],Carga_2[a]), lwd=2, lty=1, col="blue")
    } else {
      lines(c(Zero[a],Tiempo[a]),c(Carga_1[a],Carga_2[a]), lwd=2, lty=1, col="green")}
  } else {
    lines(c(100,100),c(100,100), lwd=2, lty=1, col="white")}}
lines(c(7,7),c(0,100), lwd=2, lty=2, col="black")
axis(2,at=c(0,10,20,30,40,50,60,70,80,90,100),labels=c("0%","10","20","30","40","50","60","70","80","90","100%"), font=2)
axis(1,at=c(0,2,4,6,8,10,12,14,16,18),labels=c("0","2","4","6","8","10","12","14","16","18"),las=1)
#mtext("Carga (%)",1,cex=1.3, line=3, f=2)
#mtext("Tiempo (hrs)",2,cex=1.3, line=3, f=2)
title("Descargas registradas", outer = TRUE, line = -2)

barplot(Tiempo[datos$Direccion=='Descarga'], ylim= c(0,18), axes = FALSE, horiz = TRUE)
axis(1,at=c(0,2,4,6,8,10,12,14,16,18),labels=c("0","2","4","6","8","10","12","14","16","18"),las=1)
mtext("Registros",2,cex=1.3, line=1, f=2)
title("Descargas registradas", outer = TRUE, line = -2)

