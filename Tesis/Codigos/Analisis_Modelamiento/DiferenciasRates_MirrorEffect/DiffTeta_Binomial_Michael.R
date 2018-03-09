setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/Datos_CSVs")
rm(list=ls())
dir()
library(R2jags)
library(ggplot2)
##############################################################
##############################################################
#Diferencias en Hits y Falsas Alarmas
##############################################################
#Modelo 1 :  Diferencias entre las Tasas H y FA (parametros TauH y TauF)
##############################################################



######################################################
#Especificamos el Experimento y los Datos a analizar
experimento <- 1
#####################################################

if (experimento == 1)    #Una Figura de Ebbinghaus
{
  archive <-'Ex_1Ebb_TODOS.csv'         #El archivo que contiene los datos
  datos <- read.csv(archive)          #Jalamos los datos del archivo
  Hits_Facil <- datos$A_H       #Hits(A)
  Hits_Dificil <- datos$B_H     #Hits(B)
  FA_Facil <- datos$A_FA        #FA(A)
  FA_Dificil <- datos$B_FA      #FA(B)
  k <- 20                       #Participantes
  data <- matrix(c(FA_Facil, FA_Dificil, Hits_Dificil, Hits_Facil), nrow=k, ncol=4)   #Acomodamos datos en matriz
}

if (experimento == 2)   # Dos Figuras de Ebbinghaus
{
  archive <-'Ex_2Ebb_TODOS_Sin1.csv'  #El archivo que contiene los datos
  datos <- read.csv(archive)          #Jalamos los datos
  Hits_Facil <- datos$A_H      #Hits(A)
  Hits_Dificil <- datos$B_H    #Hits(B)
  FA_Facil <- datos$A_FA       #FA(A)
  FA_Dificil <- datos$B_FA     #FA(B)
  k <- 20                      #Participantes
  data <- matrix(c(FA_Facil, FA_Dificil, Hits_Dificil, Hits_Facil), nrow=k, ncol=4)  #Acomodamos datos en matriz
}

#Clasificamos la matriz creada (con el csv de datos seleccionado)
fa_A <- data[,1]      #La primera columna son las FA(A)
fa_B <- data[,2]      #La segunda columna son las FA(B)
h_B <- data[,3]       #La tercer columna son los Hits(B)
h_A <- data[,4]       #La cuarta columna son los Hits(A)
s <- 160       #Ensayos con Señal
n <- 160       #Ensayos con Ruido




######################################
#Preparamos y Corremos el modelo
######################################
data <- list("fa_A", "fa_B", "h_B", "h_A", "s", "n", "k")                    #Los datos que vamos a utilizar para nuestro modelo
myinits <- list(
  list(thetah_A = rep(0.5,k), thetah_B = rep(0.5,k), thetaf_A = rep(0.5,k), thetaf_B = rep(0.5,k), lam_thetah_A = 1, lam_thetaf_A = 1, lam_thetah_B = 1, lam_thetaf_B = 1, Mu_thetah = 1, Mu_thetaf = 1, Tau_H = 0, Tau_F = 0))      #Valores iniciales para las extracciones de las cadenas de Markov

#Parámetros monitoreados
parameters <- c("thetah_A", "thetaf_A", "thetah_B", "thetaf_B", "mu_thetah_A", "mu_thetaf_A", "mu_thetah_B", "mu_thetaf_B", "Mu_thetah", "Mu_thetaf", "Tau_H", "Tau_F",  "Tau_H_prior", "Tau_F_prior")

niter <- 100000    #Iteraciones
burnin <- 1000     #No. de primeros sampleos en ignorarse

#Corremos el modelo
samples <- jags(data, inits=myinits, parameters,
                model.file ="C:/Users/Alejandro/Desktop/Felisa/Tesis/Codigos/Analisis_Modelamiento/DiferenciasRates_MirrorEffect/DiffTeta_Binomial_Michael.txt",
                n.chains=1, n.iter=niter, n.burnin=burnin, n.thin=1)
#La variable 'samples' contiene los parámetros monitoreados por el modelo. (Las extracciones)

####################################################################
# Jalamos los resultados de correr el modelo (Inferencias)
# a.k.a.:
#Le ponemos una etiqueta a cada elemento contenido en Samples
####################################################################
  tetaH_a <- samples$BUGSoutput$sims.list$thetah_A
  tetaH_b <- samples$BUGSoutput$sims.list$thetah_B
  tetaFA_a <- samples$BUGSoutput$sims.list$thetaf_A
  tetaFA_b <- samples$BUGSoutput$sims.list$thetaf_B
  
  tauH <- samples$BUGSoutput$sims.list$Tau_H
  tauF <- samples$BUGSoutput$sims.list$Tau_F
  
  p_tauH <- samples$BUGSoutput$sims.list$Tau_H_prior
  p_tauF <- samples$BUGSoutput$sims.list$Tau_F_prior
  
  mu_tH <- samples$BUGSoutput$sims.list$Mu_thetah
  mu_tF <- samples$BUGSoutput$sims.list$Mu_thetaf
##########################################################
##########################################################
##########################################################
################## DRAWING PLOTS
##########################################################

  
  ###################################################################################
  # Paneles separados
  # Las posteriores de los parámetros INDVIDUALES estimados (D'y C; ThetaH y ThetaFA)
  ###################################################################################
  
layout(matrix(1:2,ncol=1))  #Dos paneles
#layout(matrix(c(1,2,3,4), 2, 2, byrow = TRUE))  #Cuatro paneles


if (experimento ==1)
{
  #par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5, font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
  soporte_d <- c(0,3)      
  soporte_c <- c(0,6)
  soporte_h <- c(0,70)
  soporte_f <- c(0,60)
    
  # THETA HITS:    
  plot(soporte_h, col="white", main="Experimento 1", cex.main=3, ylab="", xlab="", xlim=c(0.3,1), axes=F)
  for(a in 1:k){
  axis(1)
  axis(2, labels=F, at=c(0,94))
  lines(density(tetaH_a[,a]), lwd=2, col="deepskyblue3")
  lines(density(tetaH_b[,a]), lwd=2, col="darkorchid3", lty=1)}
  lines(c(0.35, 0.4),c(60,60), lwd=3, lty=1, col="deepskyblue3")
  lines(c(0.35, 0.4),c(50,50), lwd=3, lty=1, col="darkorchid3")
  text(0.45, 60, labels="Estímulos A", offset=0, cex = 1.8, pos=4)
  text(0.45, 50, labels="Estímulos B", offset=0, cex = 1.8, pos=4)
  mtext("Densidad Posterior", 2, line = 2, cex=2.1, las=0)
  mtext(expression(paste(theta, "H")), side=1, line = 2.8, cex=2.5, font=2)
  
  # THETA F.A:
  plot(soporte_f, col="white", main="", cex.main=3, ylab="", xlab="", xlim=c(0,0.7), axes=F)
  for(a in 1:k){
  lines(density(tetaFA_a[,a]), lwd=2, col="deepskyblue3")
  lines(density(tetaFA_b[,a]), lwd=2, col="darkorchid3", lty=1)}
  axis(1)
  axis(2, labels=F, at=c(0,94))
  mtext("Densidad Posterior", side=2, line = 2.1, cex=2, las=0)
  mtext(expression(paste(theta, "F")), side=1, line = 2.8, cex=2.5, font=2)
  }


if (experimento ==2)
{
  #par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
  #    font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
  soporte_d <- c(0,3)
  soporte_c <- c(0,6)
  soporte_h <- c(0,62)
  soporte_f <- c(0,25)

    # Theta HITS:    
  plot(soporte_h, col="white", main="Experimento 2", cex.main=3,  ylab="", xlab="", xlim=c(0.18,1), axes=F)
  for(a in 1:k){
    axis(1)
    axis(2, labels=F, at=c(0,94))
    lines(density(tetaH_a[,a]), lwd=2, col="deepskyblue3")
    lines(density(tetaH_b[,a]), lwd=2, col="darkorchid3", lty=1)}
    lines(c(0.25, 0.3),c(55,55), lwd=3, lty=1, col="deepskyblue3")
    lines(c(0.25, 0.3),c(45,45), lwd=3, lty=1, col="darkorchid3")
    text(0.35, 55, labels="Estímulos A", offset=0, cex = 1.8, pos=4)
    text(0.35, 45, labels="Estímulos B", offset=0, cex = 1.8, pos=4)
    mtext("Densidad Posterior", side=2, line = 2, cex=2.1, las=0)
    mtext(expression(paste(theta, "H")), side=1, line = 2.8, cex=2.5, font=2)
  
  # Theta F.A.:    
  plot(soporte_f, col="white", main="", cex.main=3,  ylab="", xlab="", xlim=c(0,0.7), axes=F)
  for(a in 1:k){
    lines(density(tetaFA_a[,a]), lwd=2, col="deepskyblue3")
    lines(density(tetaFA_b[,a]), lwd=2, col="darkorchid3", lty=1)}
    axis(1)
    axis(2, labels=F, at=c(0,94))
    mtext("Densidad Posterior", side=2, line = 2, cex=2.1, las=0)
    mtext(expression(paste(theta, "F")), side=1, line = 2.8, cex=2.5, font=2)
  }
  
###################################################################################
# Tau
# Posteriores individuales para Tau por sujeto
# ###################################################################################
layout(matrix(1:2,ncol=1))

#layout(matrix(1,ncol=1))

soporte <- seq(-10,10,.01)
SavageDickey_F <- dnorm(0,mean(tauF),sd(tauF))/dnorm(0,0,1)
SavageDickey_H <- dnorm(0,mean(tauH),sd(tauH))/dnorm(0,0,1)

if (experimento ==1)
{ soporte_t <- c(0,35)
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1, cex.main=3)
  
  plot(density(tauH), axes=F, main="", ylab="", xlab="", xlim=c(-0.5,0.5), col='forestgreen', lwd=2, ylim=c(0,14))
  lines(soporte, dnorm(soporte,0,1), lwd=1, col="darkorchid3")
  axis(1)
  abline(v=0, col='black', lty=2, lwd=3)
  #mtext("Density", side=2, line = 0, cex=1, las=0)
  mtext("Experimento 1", side=3, line = -0.3, cex=1.5, font=1)
  mtext("Tau-H", side=1, line = 3, cex=2, font=2)
  text(-0.2,3,paste(round(SavageDickey_H,3)))  
  text(-0.2,5,paste("Bayes Factor"))  
  title(expression(paste(theta, "H(A) - ", theta, "H(B)")), line=2.2)
  
  #ZOOM
  plot(density(tauH), axes=F, main="", ylab="", xlab="", xlim=c(-2,0.2), col='forestgreen', lwd=2, ylim=c(0,0.8))
  lines(soporte, dnorm(soporte,0,1), lwd=1, col="darkorchid3")
  axis(1)
  abline(v=0, col='black', lty=2, lwd=3)
  lines(c(-1.5, -1.3),c(0.70,0.70), lwd=2, lty=1, col="darkorchid3")
  lines(c(-1.5, -1.3),c(0.50,0.50), lwd=2, lty=1, col="forestgreen")
  text(-1.25, 0.70, labels="Tau F - Prior", offset=0, cex = 0.8, pos=4)
  text(-1.25, 0.50, labels="Tau F - Posterior", offset=0, cex = 0.8, pos=4)
  mtext("(zoom)", side=1, line = 3, cex=2, font=2)
  

  plot(density(tauF), axes=F, main="", ylab="", xlab="", xlim=c(-0.5,0.5), col='red', lwd=2,  ylim=c(0,10.5))
  lines(seq(-1,1,.05), dnorm(seq(-1,1,.05), 0,1), lwd=1, col="darkorchid3")
  axis(1) 
  abline(v=0, col='black', lty=2, lwd=3)
  text(-0.2,3,paste(round(SavageDickey_F,3)))  
  text(-0.2,5,paste("Bayes Factor"))  
  #axis(2, labels=F, at=c(0,24))
  #mtext("Density", side=2, line = 2, cex=1, las=0)
  mtext("Tau-F", side=1, line = 3, cex=2, font=2)
  mtext("Experimento 1", side=3, line = -0.3, cex=1.5, font=1)
  title(expression(paste(theta, "FA(B) - ", theta, "FA(A)")), line=2.2)
  
  #ZOOM
  plot(density(tauF), axes=F, main="", ylab="", xlab="", xlim=c(-2,0.2), col='red', lwd=2, ylim=c(0,0.8))
  lines(soporte, dnorm(soporte,0,1), lwd=1, col="darkorchid3")
  axis(1)
  abline(v=0, col='black', lty=2, lwd=3)
  lines(c(-1.5, -1.3),c(0.70,0.70), lwd=2, lty=1, col="darkorchid3")
  lines(c(-1.5, -1.3),c(0.50,0.50), lwd=2, lty=1, col="red")
  text(-1.25, 0.70, labels="Tau F - Prior", offset=0, cex = 0.8, pos=4)
  text(-1.25, 0.50, labels="Tau F - Posterior", offset=0, cex = 0.8, pos=4)
  mtext("(zoom)", side=1, line = 3, cex=2, font=2)
}

if (experimento ==2)
{
  soporte_t <- c(0,35)
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1, cex.main=3)
  
  plot(density(tauH), axes=F, main="", ylab="", xlab="", xlim=c(-0.5,0.5), col='forestgreen', lwd=2, ylim=c(0,14))
  lines(soporte, dnorm(soporte,0,1), lwd=1, col="darkorchid3")
  axis(1)
  abline(v=0, col='black', lty=2, lwd=3)
  points(0,dnorm(0,0,1), pch=16, type='p', col='red', cex=1)
  points(0,dnorm(0,mean(tauH), sd(tauH)), pch=16, type='p', col='red', cex=1)
  #mtext("Density", side=2, line = 0, cex=1, las=0)
  text(-0.2,3,paste(round(SavageDickey_H,3)))  
  text(-0.2,5,paste("Bayes Factor"))  
  mtext("Experimento 2", side=3, line = -0.3, cex=1.5, font=1)
  mtext("Tau-H", side=1, line = 3, cex=2, font=2)
  title(expression(paste(theta, "H(A) - ", theta, "H(B)")), line=2.2)
  
  #ZOOM
  plot(density(tauH), axes=F, main="", ylab="", xlab="", xlim=c(-2,0.2), col='forestgreen', lwd=2, ylim=c(0,0.8))
  lines(soporte, dnorm(soporte,0,1), lwd=1, col="darkorchid3")
  points(0,dnorm(0,0,1), pch=16, type='p', col='red', cex=1.5)
  points(0,dnorm(0,mean(tauH), sd(tauH)), pch=16, type='p', col='red', cex=1.5)
  lines(c(-1.5, -1.3),c(0.70,0.70), lwd=2, lty=1, col="darkorchid3")
  lines(c(-1.5, -1.3),c(0.50,0.50), lwd=2, lty=1, col="forestgreen")
  text(-1.25, 0.70, labels="Tau F - Prior", offset=0, cex = 0.8, pos=4)
  text(-1.25, 0.50, labels="Tau F - Posterior", offset=0, cex = 0.8, pos=4)
  axis(1)
  abline(v=0, col='black', lty=2, lwd=3)
  mtext("(zoom)", side=1, line = 3, cex=2, font=2)
  
  
  plot(density(tauF), axes=F, main="", ylab="", xlab="", xlim=c(-0.5,0.5), col='red', lwd=2,  ylim=c(0,10.5))
  lines(seq(-1,1,.05), dnorm(seq(-1,1,.05), 0,1), lwd=1, col="darkorchid3")
  axis(1) 
  abline(v=0, col='black', lty=2, lwd=3)
  points(0,dnorm(0,0,1), pch=16, type='p', col='blue', cex=1)
  points(0,dnorm(0,mean(tauF), sd(tauF)), pch=16, type='p', col='blue', cex=1)
  lines(c(0,0), c(dnorm(0,0,1), dnorm(0,mean(tauF), sd(tauF))), lwd=3, col="blue", lty=1)
  text(-0.2,3,paste(round(SavageDickey_F,3)))  
  text(-0.2,5,paste("Bayes Factor"))  
  #axis(2, labels=F, at=c(0,24))
  #mtext("Density", side=2, line = 2, cex=1, las=0)
  mtext("Tau-F", side=1, line = 3, cex=2, font=2)
  mtext("Experimento 2", side=3, line = -0.3, cex=1.5, font=1)
  title(expression(paste(theta, "FA(B) - ", theta, "FA(A)")), line=2.2)
  
  #ZOOM
  plot(density(tauF), axes=F, main="", ylab="", xlab="", xlim=c(-1.7,0.2), col='red', lwd=2, ylim=c(0,2.8))
  lines(soporte, dnorm(soporte,0,1), lwd=1, col="darkorchid3")
  points(0,dnorm(0,0,1), pch=16, type='p', col='blue', cex=1.5)
  points(0,dnorm(0,mean(tauF), sd(tauF)), pch=16, type='p', col='blue', cex=1.5)
  axis(1)
  lines(c(-1.5, -1.3),c(2.60,2.60), lwd=2, lty=1, col="darkorchid3")
  lines(c(-1.5, -1.3),c(1.60,1.60), lwd=2, lty=1, col="red")
  text(-1.25, 2.60, labels="Tau F - Prior", offset=0, cex = 0.8, pos=4)
  text(-1.25, 1.60, labels="Tau F - Posterior", offset=0, cex = 0.8, pos=4)
  abline(v=0, col='black', lty=2, lwd=3)
  mtext("(zoom)", side=1, line = 3, cex=2, font=2)}

