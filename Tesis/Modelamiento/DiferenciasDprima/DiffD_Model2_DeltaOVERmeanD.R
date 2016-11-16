setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs")
rm(list=ls())
dir()
library(R2jags)
######################################################
######################################################
#Diferencias en D'
#Modelo 1
######################################################
######################################################



######################################################
experimento <- 1
#####################################################


if (experimento == 1) #Demo
{
  archive <-'Ex2a_TODOS.csv'
  datos <- read.csv(archive)
  Hits_Facil <- datos$A_H
  Hits_Dificil <- datos$B_H
  FA_Facil <- datos$A_FA
  FA_Dificil <- datos$B_FA
  k <- 20 #number of cases
  data <- matrix(c(FA_Facil, FA_Dificil, Hits_Dificil, Hits_Facil), nrow=k, ncol=4)
}

if (experimento == 2) #Lehrner et al. (1995) data 
{
  archive <-'MirrEx1a_V2_TODOS.csv'
  datos <- read.csv(archive)
  Hits_Facil <- datos$A_H
  Hits_Dificil <- datos$B_H
  FA_Facil <- datos$A_FA
  FA_Dificil <- datos$B_FA
  k <- 21 #number of cases
  data <- matrix(c(FA_Facil, FA_Dificil, Hits_Dificil, Hits_Facil), nrow=k, ncol=4)
}

fa_A <- data[,1]
fa_B <- data[,2]
h_B <- data[,3]
h_A <- data[,4]
s <- 160
n <- 160

data <- list("fa_A", "fa_B", "h_B", "h_A", "s", "n", "k") # to be passed on to JAGS
myinits <- list(
  list(d_A = rep(0,k), d_B = rep(0,k), c_A = rep(0,k), c_B = rep(0,k),  muc_A = 0, lambdac_A = 1, muc_B = 0, lambdac_B = 1, mud_A = 0, lambdad_A = 1, mud_B = 0, lambdad_B = 1))


# parameters to be monitodeepskyblue3:	
parameters <- c("c_A", "c_B", "d_A", "d_B", "thetah_A", "thetah_B", "thetaf_A", "thetaf_B", "muc_A", "muc_B", "mud_A", "mud_B", "sigmac_A", "sigmac_B", "sigmad_A", "sigmad_B", "delta")


niter <- 100000
burnin <- 2000
# Corremos JAGS
samples <- jags(data, inits=myinits, parameters,
                model.file ="C:/Users/Alejandro/Desktop/Felisa/Tesis/Modelamiento/DiferenciasDprima/DiffD_Modelo2_DeltaOVERmeanD.txt",
                n.chains=1, n.iter=niter, n.burnin=burnin, n.thin=1)
# Now the values for the monitodeepskyblue3 parameters are in the "samples" object, ready for inspection.



for (a in 1:k){
  d_a <- samples$BUGSoutput$sims.list$d_A[,a]
  d_b <- samples$BUGSoutput$sims.list$d_B[,a]
  c_a <- samples$BUGSoutput$sims.list$c_A[,a]
  c_b <- samples$BUGSoutput$sims.list$c_B[,a]
  tetaH_a <- samples$BUGSoutput$sims.list$thetah_A[,a]
  tetaH_b <- samples$BUGSoutput$sims.list$thetah_B[,a]
  tetaFA_a <- samples$BUGSoutput$sims.list$thetaf_A[,a]
  tetaFA_b <- samples$BUGSoutput$sims.list$thetaf_B[,a]
}

muDA <- samples$BUGSoutput$sims.list$mud_A
muDB <- samples$BUGSoutput$sims.list$mud_B
muCA <- samples$BUGSoutput$sims.list$muc_A
muCB <- samples$BUGSoutput$sims.list$muc_B

Delta <- samples$BUGSoutput$sims.list$delta

######################################################
######### DRAWING ALL THE PLOTS
######################################################


#Four panel plot:
layout(matrix(c(1,2,3,4), 2, 2, byrow = TRUE))

if (experimento == 1) #Demo
{
par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
    font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
# Discriminability panel:    
plot(density(muDA), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
     xlim=c(0,5), axes=F)
lines(density(muDB), lwd=2, col="darkorchid3", lty=1)
axis(1)
axis(2, labels=F, at=c(0,24))
mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
mtext("D-primes", side=1, line = 2.5, cex=1.5)

# Bias panel:    
plot(density(muCA), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
     xlim=c(-1,1), axes=F)
axis(1)
axis(2, labels=F, at=c(0,24))
lines(density(muCB), lwd=2, col="darkorchid3", lty=1)
mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
mtext("C", side=1, line = 2.5, cex=1.5)

# Hit Rate panel:    
plot(density(tetaH_a), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
     xlim=c(0,1), axes=F)
axis(1)
axis(2, labels=F, at=c(0,24))
lines(density(tetaH_b), lwd=2, col="darkorchid3", lty=1)

lines(c(0, 0.1),c(12,12), lwd=2, lty=1, col="deepskyblue3")
lines(c(0, 0.1),c(10,10), lwd=2, lty=1, col="darkorchid3")
text(0.15, 12, labels="A Condition", offset=0, cex = 0.8, pos=4)
text(0.15, 10, labels="B Condition", offset=0, cex = 0.8, pos=4)


mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
mtext("Hit Rate", side=1, line = 2.5, cex=1.5)

# False-Alarm Rate panel:    
plot(density(tetaFA_a), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
     xlim=c(0,1), axes=F)
lines(density(tetaFA_b), lwd=2, col="darkorchid3", lty=1)
axis(1)
axis(2, labels=F, at=c(0,24))
mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
mtext("False-Alarm Rate", side=1, line = 2.5, cex=1.5)
}


if (experimento == 2) #Demo
{
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
  # Discriminability panel:    
  plot(density(d_a), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
       xlim=c(-1,3), axes=F)
  lines(density(d_b), lwd=2, col="darkorchid3", lty=1)
  axis(1)
  axis(2, labels=F, at=c(0,24))
  mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
  mtext("D-primes", side=1, line = 2.5, cex=1.5)
  
  # Bias panel:    
  plot(density(c_a), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
       xlim=c(-1,1), axes=F)
  axis(1)
  axis(2, labels=F, at=c(0,24))
  lines(density(c_b), lwd=2, col="darkorchid3", lty=1)
  mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
  mtext("C", side=1, line = 2.5, cex=1.5)
  
  # Hit Rate panel:    
  plot(density(tetaH_a), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
       xlim=c(0,1), axes=F)
  axis(1)
  axis(2, labels=F, at=c(0,24))
  lines(density(tetaH_b), lwd=2, col="darkorchid3", lty=1)
  
  lines(c(0, 0.1),c(12,12), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0, 0.1),c(10,10), lwd=2, lty=1, col="darkorchid3")
  text(0.15, 12, labels="A Condition", offset=0, cex = 0.8, pos=4)
  text(0.15, 10, labels="B Condition", offset=0, cex = 0.8, pos=4)
  
  
  mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
  mtext("Hit Rate", side=1, line = 2.5, cex=1.5)
  
  # False-Alarm Rate panel:    
  plot(density(tetaFA_a), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
       xlim=c(0,1), axes=F)
  lines(density(tetaFA_b), lwd=2, col="darkorchid3", lty=1)
  axis(1)
  axis(2, labels=F, at=c(0,24))
  mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
  mtext("False-Alarm Rate", side=1, line = 2.5, cex=1.5)
}


##########
############################### Interaccion entre parametros
######## Marginales y Densidad
keep_ <- (1000)
keep <- sample(niter, keep_)
d.FA_a <- density(tetaFA_a)
d.FA_b <- density(tetaFA_b)
d.H_a <- density(tetaH_a)
d.H_b <- density(tetaH_b)
mu.Da <- density(muDA)
mu.Db <- density(muDB)
mu.Ca <- density(muCA)
mu.Cb <- density(muCB)

layout(matrix(c(1,2,3,0),2,2,byrow=T), width=c(2/3, 1/3), heights=c(2/3,1/3))
#layout.show()

if (experimento ==1)
{
 # D' y C
  
  par(mar=c(0.7,1,3,0))
  plot(muDA[keep],muCA[keep], col="deepskyblue3", xlab="", main="Experiment 1", cex.main=2, ylab="", axes=F,xlim=c(0,5), ylim=c(-1,1))
  points(muDB[keep],muCB[keep], col="darkorchid3")
  lines(c(0.2, 0.6),c(0.85,0.85), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0.2, 0.6),c(0.7,0.7), lwd=2, lty=1, col="darkorchid3")
  text(0.65, 0.85, labels="Condition A", offset=0, cex = 1, pos=4)
  text(0.65, 0.7, labels="Condition B", offset=0, cex = 1, pos=4)
  box(lty=1)
  
  par(mar=c(0.7,0.5,3,6))
  plot(mu.Ca$y, mu.Ca$x, xlim=rev(c(0,5)),type='l', col="deepskyblue3", axes=F, xlab="", ylab="",ylim=c(-1,1), lwd=2)
  lines(mu.Cb$y, mu.Cb$x, col="darkorchid3", lwd=2)
  axis(4)
  mtext(expression(paste(mu, "C")), side=4,line=5, cex=1.5, font=2, las=0)
  box(lty=1)
  
  par(mar=c(6,1,0,0))
  plot(density(muDA),zero.line=F ,main="", col="deepskyblue3", ylab="", xlab="", cex.lab=1.3, axes=F, xlim=c(0,5),ylim=c(0,3), lwd=2)
  lines(density(muDB), col="darkorchid3", lwd=2)
  axis(1, at=c(0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4, 4.5, 5))
  mtext(expression(paste(mu, "D")), side=1.2,line=4, cex=1.5, font=2)
  box(lty=1)
}


if (experimento ==2)
{
  # D' y C
  
  par(mar=c(0.7,1,3,0))
  plot(muDA[keep],muCA[keep], col="deepskyblue3", xlab="", main="Experiment 2", cex.main=2, ylab="", axes=F,xlim=c(0,5), ylim=c(-1,1))
  points(muDB[keep],muCB[keep], col="darkorchid3")
  lines(c(0.2, 0.6),c(0.85,0.85), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0.2, 0.6),c(0.7,0.7), lwd=2, lty=1, col="darkorchid3")
  text(0.65, 0.85, labels="Condition A", offset=0, cex = 1, pos=4)
  text(0.65, 0.7, labels="Condition B", offset=0, cex = 1, pos=4)
  box(lty=1)
  
  par(mar=c(0.7,0.5,3,6))
  plot(mu.Ca$y, mu.Ca$x, xlim=rev(c(0,6)),type='l', col="deepskyblue3", axes=F, xlab="", ylab="",ylim=c(-1,1), lwd=2)
  lines(mu.Cb$y, mu.Cb$x, col="darkorchid3", lwd=2)
  axis(4)
  mtext(expression(paste(mu, "C")), side=4,line=5, cex=1.5, font=2, las=0)
  box(lty=1)
  
  par(mar=c(6,1,0,0))
  plot(density(muDA),zero.line=F ,main="", col="deepskyblue3", ylab="", xlab="", cex.lab=1.3, axes=F, xlim=c(0,5),ylim=c(0,3), lwd=2)
  lines(density(muDB), col="darkorchid3", lwd=2)
  axis(1, at=c(0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4, 4.5, 5))
  mtext(expression(paste(mu, "D")), side=1.2,line=4, cex=1.5, font=2)
  box(lty=1)
}


########## DIFFERENCES ON D'

layout(matrix(1:1,ncol=1))
if (experimento ==1)
{
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
  
  plot(density(Delta), col='blue4', main="", cex.main=2, lwd=3.5, ylab="", xlab="", axes=F, xlim=c(-0.5,2))
  #text(1.5, 1.2, labels="Delta", offset=0, cex = 1, col='red', pos=4)
  axis(1)
  axis(2, labels=F, at=c(0,24))
  mtext("Density", side=2, line=2, cex=2, las=0, font=2)
  mtext("Delta", side=1, line=2.5, cex=2, font=2)
  points(0,0.03032, pch=16, type='p', col='red', cex=1.5)
  
  
  
  plot(density(Delta), lwd=3.5, col="blue4", main="", cex.main=2,  ylab="", xlab="", 
       xlim=c(-3,3), axes=F)
  axis(1)
  mtext("Delta", side=1, line = 3, cex=2, font=2)
  points(0,0.03032, pch=16, type='p', col='red', cex=1.5)
  
}

if (experimento ==2)
{
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
  
  plot(density(Delta), col='blue4', main="", cex.main=2, lwd=3.5, ylab="", xlab="", axes=F, xlim=c(-0.5,2))
#  text(1.5, 1.2, labels="Delta", offset=0, cex = 1, col='red', pos=4)
  axis(1)
  axis(2, labels=F, at=c(0,24))
  mtext("Density", side=2, line=2, cex=2, las=0, font=2)
  mtext("Delta", side=1, line=2.5, cex=2, font=2)
  points(0,0.007229, pch=16, type='p', col='red', cex=1.5)
  
  #     
  plot(density(Delta), lwd=3.5, col="blue4", main="", cex.main=2, ylab="", xlab="", 
       xlim=c(-3,3), axes=F)
  axis(1)
  mtext("Delta", side=1, line = 3, cex=2, font=2)
  points(0,0.007229, pch=16, type='p', col='red', cex=1.5)
}
