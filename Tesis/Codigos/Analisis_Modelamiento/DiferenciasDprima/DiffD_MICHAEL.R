setwd("C:/Users/sandra/Desktop/Adrifelcha_Lab25/Tesis/Datos_CSVs")
rm(list=ls())
dir()
library(R2jags)
library(ggplot2)
##############################################################
##############################################################
#Diferencias en D'
##############################################################
#Modelo 2 :  Diferencia en el promedio de D' (parametro Delta)
##############################################################




######################################################
#Especificamos el Experimento y los Datos a analizar
experimento <- 2
#####################################################

if (experimento == 1) 
{
  archive <-'Ex_1Ebb_TODOS.csv'      #Especificamos el nombre del archivo que contiene los datos
  datos <- read.csv(archive)          #Jalamos los datos del archivo
  Hits_Facil <- datos$A_H             #Hits(A)
  Hits_Dificil <- datos$B_H           #Hits(B)
  FA_Facil <- datos$A_FA              #FA(A)
  FA_Dificil <- datos$B_FA            #FA(B)
  k <- 20              #Total Participantes
  data <- matrix(c(FA_Facil, FA_Dificil, Hits_Dificil, Hits_Facil), nrow=k, ncol=4)  #Ordenamos los datos
}

if (experimento == 2)
{
  archive <-'Ex_2Ebb_TODOS_Sin1.csv'          #Especificamos el nombre del archivo que contiene los datos
  datos <- read.csv(archive)              #Jalamos los datos
  Hits_Facil <- datos$A_H                 #H(A)
  Hits_Dificil <- datos$B_H               #H(B)
  FA_Facil <- datos$A_FA                  #FA(A)
  FA_Dificil <- datos$B_FA                #FA(B)
  k <- 20    #Total de participantes
  data <- matrix(c(FA_Facil, FA_Dificil, Hits_Dificil, Hits_Facil), nrow=k, ncol=4)  #Ordenamos los datos
}

#De acuerdo con la matriz creada (con el csv de datos seleccionado)
fa_A <- data[,1]    #La primera columna son las FA(A)
fa_B <- data[,2]    #La primera columna son las FA(B)
h_B <- data[,3]     #La primera columna son las H(B)
h_A <- data[,4]     #La primera columna son las H(A)
s <- 160    # Número Total de ensayos con Señal
n <- 160    # Número Total de ensayos con Ruido




######################################
#Preparamos y Corremos el modelo
######################################
data <- list("fa_A", "fa_B", "h_B", "h_A", "s", "n", "k") # Datos a analizar con JAGS
myinits <- list(
  list(d_A = rep(0,k), d_B = rep(0,k), c = rep(0,k), lambdad_A = 1,  lambdad_B = 1, delta = 0, MuD = 0))

# Parametros monitoreados
parameters <- c("c", "d_A", "d_B", "thetah_A", "thetah_B", "thetaf_A", "mud_A", "mud_B", "thetaf_B", "sigmad_A", "sigmad_B", "delta", "MuD", "delta_prior", "MuD_prior")

niter <- 200000     #Iteraciones
burnin <- 2000      #Numero de extracciones iniciales ignoradas

# Corremos el modelo
samples <- jags(data, inits=myinits, parameters,
                model.file ="C:/Users/Alejandro/Desktop/Felisa/Tesis/Codigos/Analisis_Modelamiento/DiferenciasDprima/DiffD_Michael.txt",
                n.chains=1, n.iter=niter, n.burnin=burnin, n.thin=1)

#La variable 'samples' contiene los parámetros monitoreados por el modelo. (Las extracciones)


####################################################################
# Jalamos los resultados de correr el modelo (Inferencias)
# a.k.a.:
#Le ponemos una etiqueta a cada elemento contenido en Samples
####################################################################

d_a <- samples$BUGSoutput$sims.list$d_A
d_b <- samples$BUGSoutput$sims.list$d_B

c <- samples$BUGSoutput$sims.list$c

tetaH_a <- samples$BUGSoutput$sims.list$thetah_A
tetaH_b <- samples$BUGSoutput$sims.list$thetah_B
tetaFA_a <- samples$BUGSoutput$sims.list$thetaf_A
tetaFA_b <- samples$BUGSoutput$sims.list$thetaf_B

muDA <- samples$BUGSoutput$sims.list$mud_A
muDB <- samples$BUGSoutput$sims.list$mud_B

Delta <- samples$BUGSoutput$sims.list$delta
MuD <- samples$BUGSoutput$sims.list$MuD

p_Delta <- samples$BUGSoutput$sims.list$delta_prior
p_MuD <- samples$BUGSoutput$sims.list$MuD_prior



######################################################
######################################################
######################################################
######### Dibujamos los plots
######################################################

###################################################################################
# Cuatro Panels
# Las posteriores de los parámetros INDVIDUALES estimados (D'; C; ThetaH y ThetaFA)
###################################################################################
layout(matrix(c(1,2,3,4), 2, 2, byrow = TRUE)) 
#layout(matrix(1:1,ncol=1))

if (experimento == 1){   ### EXPERIMENTO 1
par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5, 
     font.lab = 2, cex.axis = 1.3, bty = "n", las=1, cex.main=3)
  
############### D':    
  soporte_d <- c(0,2.8)
  plot(soporte_d, axes=F, main="Experimento 1", ylab="", xlab="", xlim=c(0,6.5), col='white')
  for(a in 1:k){
    lines(density(d_a[,a]), lwd=2, col="dodgerblue2", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)
    lines(density(d_b[,a]), lwd=2, col="darkorchid2", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)}  
  lines(density(muDB), lwd=5, col="darkorchid4", lty=1)
  lines(density(muDA), lwd=5, col="dodgerblue4", lty=1)
  axis(1)
  axis(2, labels=F, at=c(0,210))
  #mtext("Differences on Hit Rates", side=3, line = 0.2, cex=1.2, font=1)
  mtext("d'", side=1, line = 3, cex=1.5, f=2)
  mtext("Densidad", side=2, line = 2, cex=1.8, las=0, f=2)

################ C:    
  soporte_c <- c(0,5.5)
  plot(soporte_c, axes=F, main="", ylab="", xlab="", xlim=c(-2,2), col='white')
  for(a in 1:k){
    lines(density(c[,a]), lwd=2, col="dodgerblue2", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)}  
  axis(1)
  axis(2, labels=F, at=c(0,210))
  mtext("C", side=1, line = 3, cex=1.5, f=2)
  mtext("Densidad", side=2, line = 2, cex=1.8, las=0, f=2) 

############## Theta Hits:
soporte_t <- c(0,90)
plot(soporte_t, axes=F, main="", ylab="", xlab="", xlim=c(0.4,1), col='white')
for(a in 1:k){
  lines(density(tetaH_a[,a]), lwd=1, col="dodgerblue3", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)
  lines(density(tetaH_b[,a]), lwd=1, col="darkorchid3", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)}  
axis(1)
axis(2, labels=F, at=c(0,210))
#mtext("Differences on Hit Rates", side=3, line = 0.2, cex=1.2, font=1)
mtext(expression(paste(theta, "H")), side=1, line = 3, cex=1.5)
mtext("Densidad", side=2, line = 2, cex=1.8, las=0, f=2)

lines(c(0, 0.1),c(60,60), lwd=2, lty=1, col="deepskyblue3")
lines(c(0, 0.1),c(50,50), lwd=2, lty=1, col="darkorchid3")
text(0.15, 60, labels="Estímulos A", offset=0, cex = 0.8, pos=4)
text(0.15, 50, labels="Estímulos B", offset=0, cex = 0.8, pos=4)

############### Theta F.A.
plot(soporte_t, axes=F, main="", ylab="", xlab="", xlim=c(0,0.7), col='white')
for(a in 1:k){
  lines(density(tetaFA_a[,a]), lwd=1, col="dodgerblue3", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)
  lines(density(tetaFA_b[,a]), lwd=1, col="darkorchid3", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)}  
axis(1)
axis(2, labels=F, at=c(0,200))
#mtext("Differences on Hit Rates", side=3, line = 0.2, cex=1.2, font=1)
mtext(expression(paste(theta, "F")), side=1, line = 3, cex=1.5)
mtext("Densidad", side=2, line = 2, cex=1.8, las=0, f=2)
}

######### EXPERIMENTO 2
if (experimento == 2){
par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1, cex.main=3)
  
############### D'
  soporte_d <- c(0,2.8)
  plot(soporte_d, axes=F, main="Experimento 2", ylab="", xlab="", xlim=c(-0.5,5), col='white')
  for(a in 1:k){
    lines(density(d_a[,a]), lwd=2, col="dodgerblue2", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)
    lines(density(d_b[,a]), lwd=2, col="darkorchid2", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)}  
    lines(density(muDB), lwd=5, col="darkorchid4", lty=1)
    lines(density(muDA), lwd=5, col="dodgerblue4", lty=1)
  axis(1)
  axis(2, labels=F, at=c(0,210))
  #mtext("Differences on Hit Rates", side=3, line = 0.2, cex=1.2, font=1)
  mtext("d'", side=1, line = 3, cex=1.5, f=2)
  mtext("Densidad", side=2, line = 2, cex=1.8, las=0, f=2) 
  

################ C:
  soporte_c <- c(0,5.5)
  
  plot(soporte_c, axes=F, main="", ylab="", xlab="", xlim=c(-2,2), ylim = c(0,6), col='white')
  for(a in 1:k){
    lines(density(c[,a]), lwd=2, col="dodgerblue2", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)}
  axis(1)
  axis(2, labels=F, at=c(0,250))
  mtext("C", side=1, line = 3, cex=1.5, f=2)
  mtext("Densidad", side=2, line = 2, cex=1.8, las=0, f=2) 
  
################ Theta Hits:
  soporte_t <- c(0,50)
  
  plot(soporte_t, axes=F, main="", ylab="", xlab="", xlim=c(0.2,1), col='white')
  for(a in 1:k){
    lines(density(tetaH_a[,a]), lwd=1, col="dodgerblue3", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)
    lines(density(tetaH_b[,a]), lwd=1, col="darkorchid3", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)}  
  axis(1)
  axis(2, labels=F, at=c(0,210))
  #mtext("Differences on Hit Rates", side=3, line = 0.2, cex=1.2, font=1)
  mtext(expression(paste(theta, "H")), side=1, line = 3, cex=1.5)
  mtext("Densidad", side=2, line = 2, cex=1.8, las=0, f=2)
  
  lines(c(.2, 0.3),c(45,45), lwd=2, lty=1, col="deepskyblue3")
  lines(c(.2, 0.3),c(35,35), lwd=2, lty=1, col="darkorchid3")
  text(0.4, 45, labels="Estímulos A", offset=0, cex = 0.8, pos=4)
  text(0.4, 35, labels="Estímulos B", offset=0, cex = 0.8, pos=4)
  
################### Theta FA:    
  plot(soporte_t, axes=F, main="", ylab="", xlab="", ylim=c(0,25), xlim=c(0,0.7), col='white')
  for(a in 1:k){
    lines(density(tetaFA_a[,a]), lwd=1, col="dodgerblue3", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)
    lines(density(tetaFA_b[,a]), lwd=1, col="darkorchid3", ylab="", xlab="", xlim=c(-0.5,0.5), axes=F)}  
  axis(1)
  axis(2, labels=F, at=c(0,200))
  #mtext("Differences on Hit Rates", side=3, line = 0.2, cex=1.2, font=1)
  mtext(expression(paste(theta, "F")), side=1, line = 3, cex=1.5)
  mtext("Densidad", side=2, line = 2, cex=1.8, las=0, f=2)
}





############################
######### DIFFERENCES ON D'

layout(matrix(1:1,ncol=1))
if (experimento ==1)
{
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
  
  prior_delta <- dnorm(0,1)
  SavageDickey <- dnorm(0,0,1)/dnorm(0,mean(Delta),sd(Delta))
  
  plot(density(Delta), col='blue4', main="Experimento 1", cex.main=2, lwd=3.5, ylab="", xlab="", axes=F, xlim=c(-0.5,2))
  lines(seq(-100,100,.05), dnorm(seq(-100,100,.05), 0,1), lwd=1, col="darkorchid3")
  axis(1)
  axis(2, labels=F, at=c(0,24))
  mtext("Densidad de probabilidad", side=2, line=2, cex=2, las=0, font=2)
  mtext("Delta", side=1, line=2.5, cex=2, font=2)
  points(0,0.03226, pch=16, type='p', col='red', cex=1.5)
  points(0,0.3989423, pch=16, type='p', col='red', cex=1.5)
  lines(c(0,0), c(0.0403, 0.4003), lwd=1, col="red", lty=2)
  lines(c(0.57,0.57), c(0, 14), lwd=1, col="red", lty=2)
  text(0,0.8,paste(round(SavageDickey,3)))  
  text(0,0.9,paste("Bayes Factor"))  
  
}

if (experimento ==2)
{
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
  
  prior_delta <- dnorm(0,1)
  SavageDickey <- dnorm(0,0,1)/dnorm(0,mean(Delta),sd(Delta))
  
  plot(density(Delta), col='blue4', main="Experimento 2", cex.main=2, lwd=3.5, ylab="", xlab="", axes=F, xlim=c(-0.5,2))
  lines(seq(-100,100,.05), dnorm(seq(-100,100,.05), 0,1), lwd=1, col="darkorchid3")
  axis(1)
  axis(2, labels=F, at=c(0,24))
  mtext("Densidad de probabilidad", side=2, line=2, cex=2, las=0, font=2)
  mtext("Delta", side=1, line=2.5, cex=2, font=2)
  points(0,0.01995232, pch=16, type='p', col='red', cex=1.5)
  points(0,0.3989423, pch=16, type='p', col='red', cex=1.5)
  lines(c(0,0), c(0.0403, 0.4003), lwd=1, col="red", lty=2)
  text(0,0.8,paste(round(SavageDickey,3)))  
  text(0,0.9,paste("Bayes Factor"))  
}




############################
######### Normalized
############################
prior_delta <- rnorm(100000,0,1)
posterior_delta <- sample(Delta,100000)
dat1 = data.frame(x=prior_delta, group="Prior")
dat2 = data.frame(x=posterior_delta, group="Posterior")
dat = rbind(dat1, dat2)

if (experimento ==1)
{
ggplot(dat, aes(x, fill=group, colour=group)) +
  geom_histogram(breaks=seq(-2,2,.05), alpha=0.6, 
                 position="identity", lwd=0.2) +
  geom_density(col=2) + 
  ggtitle("Unormalized - Experiment 1")

ggplot(dat, aes(x, fill=group, colour=group)) +
  geom_histogram(aes(y=..density..), breaks=seq(-2,2,.05), alpha=0.6, 
                 position="identity", lwd=0.2) +
  geom_density(col=2) + 
  ggtitle("Normalized - Experiment 1")
}



if (experimento ==2)
{
  ggplot(dat, aes(x, fill=group, colour=group)) +
    geom_histogram(breaks=seq(-2,2,.05), alpha=0.6, 
                   position="identity", lwd=0.2) +
    geom_density(col=2) + 
    ggtitle("Unormalized - Experiment 2")
  
  ggplot(dat, aes(x, fill=group, colour=group)) +
    geom_histogram(aes(y=..density..), breaks=seq(-2,2,.05), alpha=0.6, 
                   position="identity", lwd=0.2) +
    geom_density(col=2) + 
    ggtitle("Normalized - Experiment 2")
  
  ggplot(dat, aes(x, fill=group, colour=group)) +
    geom_density(alpha=0.4, lwd=0.8, adjust=0.5) +
  ggtitle("Normalized - Experiment 2")
}