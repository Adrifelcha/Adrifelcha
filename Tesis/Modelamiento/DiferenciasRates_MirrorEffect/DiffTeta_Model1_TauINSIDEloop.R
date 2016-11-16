setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs")
rm(list=ls())
dir()
library(R2jags)
######################################################
######################################################
#Diferencias en D'
#Modelo 1
#Tenemos una variable Delta que, por cada sujeto, estima la diferencia entre las D'.
######################################################
######################################################



######################################################
experimento <- 2
#####################################################


if (experimento == 1) #Demo
{
  archive <-'Ex2a_TODOS-.csv'
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
  archive <-'MirrEx1a_V2_TODOS-.csv'
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
  list(d_A = rep(0,k), c_A = rep(0,k), d_B = rep(0,k), c_B = rep(0,k)))  

# parameters to be monitodeepskyblue3:	
parameters <- c("d_A", "c_A", "thetah_A", "thetaf_A", "d_B", "c_B", "thetah_B", "thetaf_B","Tau_H", "Tau_F")

niter <- 100000
burnin <- 1000
# Corremos JAGS
samples <- jags(data, inits=myinits, parameters,
                model.file ="C:/Users/Alejandro/Desktop/Felisa/Tesis/Modelamiento/DiferenciasRates_MirrorEffect/DiffTeta_Modelo1_TauINSIDEloop.txt",
                n.chains=1, n.iter=niter, n.burnin=burnin, n.thin=1)
# Now the values for the monitodeepskyblue3 parameters are in the "samples" object, ready for inspection.

  d_a <- samples$BUGSoutput$sims.list$d_A
  d_b <- samples$BUGSoutput$sims.list$d_B
  c_a <- samples$BUGSoutput$sims.list$c_A
  c_b <- samples$BUGSoutput$sims.list$c_B
  tetaH_a <- samples$BUGSoutput$sims.list$thetah_A
  tetaH_b <- samples$BUGSoutput$sims.list$thetah_B
  tetaFA_a <- samples$BUGSoutput$sims.list$thetaf_A
  tetaFA_b <- samples$BUGSoutput$sims.list$thetaf_B
  tauH <- samples$BUGSoutput$sims.list$Tau_H
  tauF <- samples$BUGSoutput$sims.list$Tau_F


###############################################
################## DRAWING PLOTS
###############################################

#make the four panel plot:
layout(matrix(1:2,ncol=1))
#layout(matrix(c(1,2,3,4), 2, 2, byrow = TRUE))


if (experimento ==1)
{
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
  soporte_d <- c(0,3)
  soporte_c <- c(0,6)
  soporte_h <- c(0,50)
  soporte_f <- c(0,50)
    
  # Discriminability panel:    
  plot(soporte_d, axes=F, main="", ylab="", xlab="", xlim=c(0,6), col='white')
  for(a in 1:k){
    lines(density(d_a[,a]), lwd=2, col="deepskyblue3")
    lines(density(d_b[,a]), lwd=2, col="darkorchid3", lty=1)
    axis(1)
    axis(2, labels=F, at=c(0,24))
    mtext("Probability Density", side=2, line = 2, cex=1, las=0)
    mtext("D-primes", side=1, line = 2.5, cex=1, font=2)
    }

  # Bias panel:   
  plot(soporte_c, main="", ylab="", xlab="", col='white', xlim=c(-1,1), axes=F)
  for(a in 1:k){
  axis(1)
  axis(2, labels=F, at=c(0,24))
  lines(density(c_a[,a]), lwd=2, col="deepskyblue3")
  lines(density(c_b[,a]), lwd=2, col="darkorchid3", lty=1)
  mtext("Probability Density", side=2, line = 2, cex=1, las=0)
  mtext("C (Bias)", side=1, line = 2.5, cex=1, font=2)
  }
  
  # Hit Rate panel:    
  plot(soporte_h, col="white", main="", ylab="", xlab="", xlim=c(0,1), axes=F)
  for(a in 1:k){
  axis(1)
  axis(2, labels=F, at=c(0,24))
  lines(density(tetaH_a[,a]), lwd=2, col="deepskyblue3")
  lines(density(tetaH_b[,a]), lwd=2, col="darkorchid3", lty=1)
  lines(c(0, 0.1),c(20,20), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0, 0.1),c(10,10), lwd=2, lty=1, col="darkorchid3")
  text(0.15, 20, labels="A Condition", offset=0, cex = 0.8, pos=4)
  text(0.15, 10, labels="B Condition", offset=0, cex = 0.8, pos=4)
  mtext("Probability Density", side=2, line = 2, cex=1, las=0)
  mtext("Hit Rate", side=1, line = 2.5, cex=1, font=2)
  }
  
  # False-Alarm Rate panel:    
  plot(soporte_f, col="white", main="", ylab="", xlab="", xlim=c(0,1), axes=F)
  for(a in 1:k){
  lines(density(tetaFA_a[,a]), lwd=2, col="deepskyblue3")
  lines(density(tetaFA_b[,a]), lwd=2, col="darkorchid3", lty=1)
  axis(1)
  axis(2, labels=F, at=c(0,24))
  mtext("Probability Density", side=2, line = 2, cex=1, las=0)
  mtext("False-Alarm Rate", side=1, line = 2.5, cex=1, font=2)
}}


if (experimento ==2)
{
par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
    font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
  
# Discriminability panel:    
plot(density(d_a), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
     xlim=c(0,3), axes=F)
lines(density(d_b), lwd=2, col="darkorchid3", lty=1)
axis(1)
axis(2, labels=F, at=c(0,24))
mtext("Probability Density", side=2, line = 2, cex=1, las=0)
mtext("D-primes", side=1, line = 2.5, cex=1, font=2)
# Bias panel:    
plot(density(c_a), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
     xlim=c(-1,1), axes=F)
axis(1)
axis(2, labels=F, at=c(0,24))
lines(density(c_b), lwd=2, col="darkorchid3", lty=1)
mtext("Probability Density", side=2, line = 2, cex=1, las=0)
mtext("C (Bias)", side=1, line = 2.5, cex=1, font=2)
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
mtext("Probability Density", side=2, line = 2, cex=1, las=0)
mtext("Hit Rate", side=1, line = 2.5, cex=1, font=2)
# False-Alarm Rate panel:    
plot(density(tetaFA_a), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
     xlim=c(0,1), axes=F)
lines(density(tetaFA_b), lwd=2, col="darkorchid3", lty=1)
axis(1)
axis(2, labels=F, at=c(0,24))
mtext("Probability Density", side=2, line = 2, cex=1, las=0)
mtext("False-Alarm Rate", side=1, line = 2.5, cex=1, font=2)
}



############################### Interaccion entre parametros
######## Marginales y Densidad
keep_ <- (1000)
keep <- sample(niter, keep_)
d.FA_a <- density(tetaFA_a)
d.FA_b <- density(tetaFA_b)
d.H_a <- density(tetaH_a)
d.H_b <- density(tetaH_b)
d.D_a <- density(d_a)
d.D_b <- density(d_b)
d.C_a <- density(c_a)
d.C_b <- density(c_b)
d.TauH <- density(tauH)
d.TauF <- density(tauF)


layout(matrix(c(1,2,3,0),2,2,byrow=T), width=c(2/3, 1/3), heights=c(2/3,1/3))
#layout.show()

if (experimento ==1)
{
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
  
  # D' y C
  
  par(mar=c(2,2,1,0))
  plot(d_a[keep],c_a[keep], col="deepskyblue3", xlab="", ylab="", axes=F,xlim=c(0,5), ylim=c(-1,1))
  points(d_b[keep],c_b[keep], col="darkorchid3")
  lines(c(0.2, 0.6),c(0.9,0.9), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0.2, 0.6),c(0.7,0.7), lwd=2, lty=1, col="darkorchid3")
  text(0.65, 0.9, labels="A Condition", offset=0, cex = 0.8, pos=4)
  text(0.65, 0.7, labels="B Condition", offset=0, cex = 0.8, pos=4)
  box(lty=1)
  
  par(mar=c(2,1,1,4))
  plot(d.C_a$y, d.C_a$x, xlim=rev(c(0,5)),type='l', col="deepskyblue3", axes=F, xlab="", ylab="",ylim=c(-1,1))
  lines(d.C_b$y, d.C_b$x, col="darkorchid3")
  axis(4)
  mtext(expression(paste("C (Bias)")), side=4,line=2.3, cex=0.9, font=2, las=0)
  box(lty=1)
  
  par(mar=c(6,2,0,0))
  plot(density(d_a),zero.line=F ,main="", col="deepskyblue3", ylab="", xlab="", cex.lab=1.3, axes=F, xlim=c(0,5),ylim=c(0,3))
  lines(density(d_b), col="darkorchid3")
  axis(1, at=c(0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4, 4.5, 5))
  mtext(expression(paste("D prime")), side=1.2,line=2, cex=0.9, font=2)
  box(lty=1)
}


if (experimento ==2)
{
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
  
  # D' y C
  
  par(mar=c(2,2,1,0))
  plot(d_a[keep],c_a[keep], col="deepskyblue3", xlab="", ylab="", axes=F,xlim=c(0,3), ylim=c(-1,1))
  points(d_b[keep],c_b[keep], col="darkorchid3")
  lines(c(0.2, 0.6),c(0.90,0.90), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0.2, 0.6),c(0.80,0.80), lwd=2, lty=1, col="darkorchid3")
  text(0.7, 0.90, labels="A Condition", offset=0, cex = 0.8, pos=4)
  text(0.7, 0.80, labels="B Condition", offset=0, cex = 0.8, pos=4)
  box(lty=1)
  
  par(mar=c(2,1,1,4))
  plot(d.C_a$y, d.C_a$x, xlim=rev(c(0,6)),type='l', col="deepskyblue3", axes=F, xlab="", ylab="",ylim=c(-1,1))
  lines(d.C_b$y, d.C_b$x, col="darkorchid3")
  axis(4)
  mtext(expression(paste(mu, "C (Bias)")), side=4,line=2.3, cex=0.9, font=2, las=0)
  box(lty=1)
  
  par(mar=c(6,2,0,0))
  plot(density(d_a),zero.line=F ,main="", col="deepskyblue3", ylab="", xlab="", cex.lab=1.3, axes=F, xlim=c(0,3),ylim=c(0,3))
  lines(density(d_b), col="darkorchid3")
  axis(1, at=c(0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0))
  mtext(expression(paste("D prime")), font=2, side=1.2,line=2, cex=0.9)
  box(lty=1)
}


layout(matrix(1:2,ncol=1))
if (experimento ==1)
{
  soporte_t <- c(0,35)
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
  
  plot(soporte_t, axes=F, main="", ylab="", xlab="", xlim=c(-0.5,0.5), col='white')
  for(a in 1:k){
  title("Experiment 1", line=2.5)
  lines(density(tauH[,a]), lwd=1, col="dodgerblue3", ylab="", xlab="", 
       xlim=c(-0.5,0.5), axes=F)
}
  axis(1)
  abline(v=0, col='black', lty=2, lwd=3)
  #axis(2, labels=F, at=c(0,24))
  #mtext("Density", side=2, line = 0, cex=1, las=0)
  mtext("Differences on Hit Rates", side=3, line = 0.2, cex=1.2, font=1)
  mtext("Tau-H", side=1, line = 3, cex=1.5, font=2)

  
  plot(soporte_t, axes=F, main="", ylab="", xlab="", xlim=c(-0.5,0.5), col='white')
  for (a in 1:k){
  lines(density(tauF[,a]), lwd=1, col="dodgerblue3", ylab="", main="", xlab="", xlim=c(-0.5,0.5), axes=F)
  }
  axis(1) 
  abline(v=0, col='black', lty=2, lwd=3)
  #axis(2, labels=F, at=c(0,24))
  #mtext("Density", side=2, line = 2, cex=1, las=0)
  mtext("Tau-F", side=1, line = 3, cex=1.5, font=2)
  mtext("Differences on FA Rates", side=3, line = 0.2, cex=1.2, font=1)
}

if (experimento ==2)
{
  soporte_t <- c(0,35)
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
  
  plot(soporte_t, axes=F, main="", ylab="", xlab="", xlim=c(-0.5,0.5), col='white')
  for(a in 1:k){
    title("Experiment 2", line=2.5)
    lines(density(tauH[,a]), lwd=1, col="dodgerblue3", ylab="", xlab="", 
          xlim=c(-0.5,0.5), axes=F)
  }
  axis(1)
  abline(v=0, col='black', lty=2, lwd=3)
  #axis(2, labels=F, at=c(0,24))
  #mtext("Density", side=2, line = 2, cex=1, las=0)
  mtext("Differences on Hit Rates", side=3, line = 0.2, cex=1.2, font=1)
  mtext("Tau-H", side=1, line = 3, cex=1.5, font=2)

  
  plot(soporte_t, axes=F, main="", ylab="", xlab="", xlim=c(-0.5,0.5), col='white')
  for (a in 1:k){
    lines(density(tauF[,a]), lwd=1, col="dodgerblue3", ylab="", main="", xlab="", xlim=c(-0.5,0.5), axes=F)
  }
  axis(1) 
  abline(v=0, col='black', lty=2, lwd=3)
  #axis(2, labels=F, at=c(0,24))
  mtext("Tau-F", side=1, line = 3, cex=1.5, font=2)
  mtext("Differences on FA Rates", side=3, line = 0.2, cex=1.2, font=1)
}
