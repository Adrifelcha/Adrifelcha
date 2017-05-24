# Gráficas 
#Autor: Adriana F. Chávez De la Peña
#adrifelcha@gmail.com
##########################################################

rm(list=ls())  #Limpiamos el espacio de trabajo

# Grafica de Barras
a <- 75
b <- 63
c <- 60

Candidatos <- c(a,b,c)

barplot(Candidatos,  main = "", xlab = "", ylab = " ", ylim = c(0, 100), axes = FALSE, col = c("red", "dodgerblue3", "forestgreen"))
axis(2,at=c(0, 20, 40, 60, 80, 100),labels=c("0", "20", "40","60","80","100"),las=1)
axis(1,at=c(0.7,1.9,3.1),labels=c("Palin","Huckabee", "Romney"), font= 1)
text(0.7,Candidatos[1]+5,paste(Candidatos[1], '%'),cex=3,col='black',f=1)
text(1.9,Candidatos[2]+5,paste(Candidatos[2], '%'),cex=3,col='black',f=1)
text(3.1,Candidatos[3]+5,paste(Candidatos[3], '%'),cex=3,col='black',f=1)
mtext("Candidato", side = 1, line = 3, cex = 2, font = 2)
mtext("Proporción de -Favorable-", side = 4, line = 0, cex = 2, font = 2, las = 0)
mtext("2012 Presidential Run: GOP Candidates",3,cex=2.5, font=2)
#title("2012 Presidential Run: GOP Candidates", outer = TRUE,cex=3, line = -2)
