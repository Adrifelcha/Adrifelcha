setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/Datos_CSVs")
rm(list=ls())
dir()
library(R2jags)
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
  list(thetah_A = rep(0,k), thetah_B = rep(0,k), thetaf_A = rep(0,k), thetaf_B = rep(0,k), sigmath_A = 1, sigmath_B = 1, sigmatf_A = 1, sigmatf_B = 1, Mu_thetah = 1, Mu_thetaf = 1, Tau_H = 0, Tau_F = 0))      #Valores iniciales para las extracciones de las cadenas de Markov

#Parámetros monitoreados
parameters <- c("thetah_A", "thetaf_A", "thetah_B", "thetaf_B", "mu_thetah_A", "mu_thetaf_A", "mu_thetah_B", "mu_thetaf_B", "Mu_thetah", "Mu_thetaf", "Tau_H", "Tau_F")

niter <- 100000    #Iteraciones
burnin <- 1000     #No. de primeros sampleos en ignorarse

#Corremos el modelo
samples <- jags(data, inits=myinits, parameters,
                model.file ="C:/Users/Alejandro/Desktop/Felisa/Tesis/Codigos/Analisis_Modelamiento/DiferenciasRates_MirrorEffect/DiffTeta_Binomial_Michael_Sigma.txt",
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
  lines(density(tetaH_b[,a]), lwd=2, col="darkorchid3", lty=1)
  lines(c(0.35, 0.4),c(60,60), lwd=3, lty=1, col="deepskyblue3")
  lines(c(0.35, 0.4),c(50,50), lwd=3, lty=1, col="darkorchid3")
  text(0.45, 60, labels="Estímulos A", offset=0, cex = 1.8, pos=4)
  text(0.45, 50, labels="Estímulos B", offset=0, cex = 1.8, pos=4)
  mtext("Densidad Posterior", 2, line = 2, cex=2.1, las=0)
  mtext(expression(paste(theta, "H")), side=1, line = 2.8, cex=2.5, font=2)}
  
  # THETA F.A:
  plot(soporte_f, col="white", main="", cex.main=3, ylab="", xlab="", xlim=c(0,0.7), axes=F)
  for(a in 1:k){
  lines(density(tetaFA_a[,a]), lwd=2, col="deepskyblue3")
  lines(density(tetaFA_b[,a]), lwd=2, col="darkorchid3", lty=1)
  axis(1)
  axis(2, labels=F, at=c(0,94))
  mtext("Densidad Posterior", side=2, line = 2.1, cex=2, las=0)
  mtext(expression(paste(theta, "F")), side=1, line = 2.8, cex=2.5, font=2)}
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
    lines(density(tetaH_b[,a]), lwd=2, col="darkorchid3", lty=1)
    lines(c(0.25, 0.3),c(55,55), lwd=3, lty=1, col="deepskyblue3")
    lines(c(0.25, 0.3),c(45,45), lwd=3, lty=1, col="darkorchid3")
    text(0.35, 55, labels="Estímulos A", offset=0, cex = 1.8, pos=4)
    text(0.35, 45, labels="Estímulos B", offset=0, cex = 1.8, pos=4)
    mtext("Densidad Posterior", side=2, line = 2, cex=2.1, las=0)
    mtext(expression(paste(theta, "H")), side=1, line = 2.8, cex=2.5, font=2)}
  
  # Theta F.A.:    
  plot(soporte_f, col="white", main="", cex.main=3,  ylab="", xlab="", xlim=c(0,0.7), axes=F)
  for(a in 1:k){
    lines(density(tetaFA_a[,a]), lwd=2, col="deepskyblue3")
    lines(density(tetaFA_b[,a]), lwd=2, col="darkorchid3", lty=1)
    axis(1)
    axis(2, labels=F, at=c(0,94))
    mtext("Densidad Posterior", side=2, line = 2, cex=2.1, las=0)
    mtext(expression(paste(theta, "F")), side=1, line = 2.8, cex=2.5, font=2)}
  }
  
  ###################################################################################
  # Gráficos de Dispersión
  # Interacción entre parámetros (TauH y TauFA; D' y C)
  ###################################################################################

#Preparamos los datos
keep_ <- (1000)   #Numero de extracciones a incluir en el Gráfico
keep <- sample(niter, keep_)    #De las 'niter' extracciones, sacamos 'keep' muestras
#
d.FA_a <- density(tetaFA_a)
d.FA_b <- density(tetaFA_b)
d.H_a <- density(tetaH_a)
d.H_b <- density(tetaH_b)
d.TauH <- density(tauH)
d.TauF <- density(tauF)


layout(matrix(c(1,2,3,0),2,2,byrow=T), width=c(2/3, 1/3), heights=c(2/3,1/3))
#layout.show()

if (experimento ==1)
{ soporte_d <- c(0,3)
  soporte_c <- c(0,6)
  soporte_h <- c(0,62)
  soporte_f <- c(0,25)
  par(mar=c(2,2,1,0))
  plot(tetaFA_a[keep],tetaH_a[keep], col="deepskyblue3", xlab="", ylab="", axes=F,xlim=c(0,0.5), ylim=c(0.5,1))
  points(tetaFA_b[keep],tetaH_b[keep], col="darkorchid3")
  lines(c(0.36, 0.41),c(0.60,0.60), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0.36, 0.41),c(0.55,0.55), lwd=2, lty=1, col="darkorchid3")
  text(0.42, 0.60, labels="A Condition", offset=0, cex = 0.8, pos=4)
  text(0.42, 0.55, labels="B Condition", offset=0, cex = 0.8, pos=4)
  box(lty=1)
  
  par(mar=c(2,1,1,4))
  plot(d.H_a$y, d.H_a$x, xlim=rev(c(0,16)),type='l', col="deepskyblue3", axes=F, xlab="", ylab="",ylim=c(0.5,1))
  lines(d.H_b$y, d.H_b$x, col="darkorchid3")
  axis(4)
  mtext(expression(paste("Hits")), side=4,line=2.3, cex=0.9, las=0)
  box(lty=1)
  
  par(mar=c(6,2,0,0))
  plot(density(tetaFA_a),zero.line=F ,main="", col="deepskyblue3", ylab="", xlab="", cex.lab=1.3, axes=F, xlim=c(0,0.5),ylim=c(0,26))
  lines(density(tetaFA_b), col="darkorchid3")
  axis(1, at=c(0, 0.1, 0.2, 0.3, 0.4, 0.5))
  mtext(expression(paste("False Alarms")), side=1.2,line=2, cex=0.9)
  box(lty=1)
}


if (experimento ==2)
{
  soporte_d <- c(0,3)
  soporte_c <- c(0,6)
  soporte_h <- c(0,62)
  soporte_f <- c(0,25)

  #Density Plot
  par(mar=c(2,2,1,0))  
  plot(tetaFA_a[keep],tetaH_a[keep], col="deepskyblue3", xlab="", ylab="", axes=F,xlim=c(0,0.5), ylim=c(0.45,1))
  points(tetaFA_b[keep],tetaH_b[keep], col="darkorchid3")
  lines(c(0.02, 0.07),c(0.90,0.90), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0.02, 0.07),c(0.85,0.85), lwd=2, lty=1, col="darkorchid3")
  text(0.08, 0.90, labels="A Condition", offset=0, cex = 0.8, pos=4)
  text(0.08, 0.85, labels="B Condition", offset=0, cex = 0.8, pos=4)
  box(lty=1)
  
  par(mar=c(2,1,1,4))
  plot(d.H_a$y, d.H_a$x, xlim=rev(c(0,17)),type='l', col="deepskyblue3", axes=F, xlab="", ylab="",ylim=c(0.45,1))
  lines(d.H_b$y, d.H_b$x, col="darkorchid3")
  axis(4)
  mtext(expression(paste("Hits")), side=4,line=2.3, cex=0.9, las=0)
  box(lty=1)
  
  par(mar=c(6,2,0,0))
  plot(density(tetaFA_a),zero.line=F ,main="", col="deepskyblue3", ylab="", xlab="", cex.lab=1.3, axes=F, xlim=c(0,0.5),ylim=c(0,16))
  lines(density(tetaFA_b), col="darkorchid3")
  axis(1, at=c(0, 0.1, 0.2, 0.3, 0.4, 0.5))
  mtext(expression(paste("False Alarms")), side=1.2,line=2, cex=0.9)
  box(lty=1)
  
  }


###################################################################################
# Tau
# Posteriores individuales para Tau por sujeto
# ###################################################################################
layout(matrix(1:2,ncol=1))

####Un color diferente por sujeto
coltaufa <- c('chocolate', 'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'firebrick4', 'coral1', 'coral2', 'coral3', 'coral4','darkgoldenrod', 'brown', 'brown4', 'darkgoldenrod3', 'darkgoldenrod4','darkorange','coral4', 'darkorange2', 'darkorange3', 'darkorange4', 'goldenrod3')
coltauh <- c('darkolivegreen', 'darkolivegreen1', 'darkolivegreen2', 'darkolivegreen3', 'darkolivegreen4', 'darkseagreen', 'darkseagreen1', 'darkseagreen2', 'darkseagreen3', 'darkseagreen4','chartreuse4', 'chartreuse3', 'chartreuse2', 'aquamarine4', 'aquamarine3','aquamarine2','darkgreen', 'forestgreen', 'darkcyan', 'darkgoldenrod4', 'darkkhaki')

#####Tres colores diferentes por Tau: Ayuda a distinguir los colores sin cargar demasiado la gráfica
taucolfa <- c('chocolate3','firebrick4','goldenrod2','chocolate3','firebrick4','goldenrod2','chocolate3','firebrick4','goldenrod2','chocolate3','firebrick4','goldenrod2','chocolate3','firebrick4','goldenrod2','chocolate3','firebrick4','goldenrod2','chocolate3','firebrick4','goldenrod2')
taucolh <- c('darkgreen','forestgreen','chartreuse3', 'darkgreen','forestgreen','chartreuse3','darkgreen','forestgreen','chartreuse3','darkgreen','forestgreen','chartreuse3','darkgreen','forestgreen','chartreuse3','darkgreen','forestgreen','chartreuse3','darkgreen','forestgreen','chartreuse3')

if (experimento ==1)
{ soporte_t <- c(0,35)
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1, cex.main=3)
  
  plot(soporte_t, axes=F, main="", ylab="", xlab="", xlim=c(-0.15,0.3), col='white')
  for(a in 1:k){
  title("Experimento 1", line=2.2)
  lines(density(tauH), lwd=2.5, col=taucolh[a], ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)}
  axis(1)
  abline(v=0, col='black', lty=2, lwd=3)
  #axis(2, labels=F, at=c(0,24))
  #mtext("Density", side=2, line = 0, cex=1, las=0)
  mtext("Diferencias en Tasas de Hits", side=3, line = 0.2, cex=1.5, font=1)
  mtext("Tau-H", side=1, line = 3, cex=2, font=2)

  
  plot(soporte_t, axes=F, main="", ylab="", xlab="", xlim=c(-0.1,0.35), col='white')
  for (a in 1:k){
  lines(density(tauF), lwd=2.5, col=taucolfa[a], ylab="", main="", xlab="", xlim=c(-0.5,0.5), axes=F)
  }
  axis(1) 
  abline(v=0, col='black', lty=2, lwd=3)
  #axis(2, labels=F, at=c(0,24))
  #mtext("Density", side=2, line = 2, cex=1, las=0)
  mtext("Tau-F", side=1, line = 3, cex=2, font=2)
  mtext("Diferencias en Tasas de F.A.", side=3, line = 0.2, cex=1.5, font=1)
}

if (experimento ==2)
{
  soporte_t <- c(0,35)
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1, cex.main=3)
  
  plot(soporte_t, axes=F, main="", ylab="", xlab="", xlim=c(-0.1,0.55), col='white')
  for(a in 1:k){
    title("Experimento 2", line=2.2)
    lines(density(tauH[,a]), lwd=2.5, col=taucolh[a], ylab="", xlab="", 
          xlim=c(-0.5,0.5), axes=F)
  }
  axis(1)
  abline(v=0, col='black', lty=2, lwd=3)
  #axis(2, labels=F, at=c(0,24))
  #mtext("Density", side=2, line = 2, cex=1, las=0)
  mtext("Diferencias entre Tasas de Hits", side=3, line = 0.2, cex=1.5, font=1)
  mtext("Tau-H", side=1, line = 3, cex=2, font=2)

  
  plot(soporte_t, axes=F, main="", ylab="", xlab="", xlim=c(-0.15,0.35), col='white')
  for (a in 1:k){
    lines(density(tauF[,a]), lwd=2.5, col=taucolfa[a], ylab="", main="", xlab="", xlim=c(-0.5,0.5), axes=F)
  }
  axis(1) 
  abline(v=0, col='black', lty=2, lwd=3)
  #axis(2, labels=F, at=c(0,24))
  mtext("Tau-F", side=1, line = 3, cex=2, font=2)
  mtext("Diferencias entre Tasas de F.A.", side=3, line = 0.2, cex=1.5, font=1)
}
