setwd("C:/Users/Alejandro/Desktop/Felisa/Tesis/CSVs")
rm(list=ls())
dir()
library(R2jags)
######################################################
######################################################
#Estimando Parametros D y C con nuestro experimento
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
  list(d_A = rep(0,k), c_A = rep(0,k), d_B = rep(0,k), c_B = rep (0,k), mud_A = 0, muc_A = 0, lambdad_A = 1, lambdac_A = 1, mud_B = 0, muc_B = 0, lambdad_B = 1, lambdac_B = 1))  

# parameters to be monitodeepskyblue3:	
parameters <- c("d_A", "c_A", "thetah_A", "thetaf_A", "d_B", "c_B", "thetah_B", "thetaf_B", "mud_A", "muc_A", "sigmad_A", "sigmac_A", "mud_B", "muc_B", "sigmad_B", "sigmac_B")

# Corremos JAGS
samples <- jags(data, inits=myinits, parameters,
                model.file ="C:/Users/Alejandro/Desktop/Felisa/Tesis/Modelamiento/Aprendiendo_EnsayoError/Ap_3_SDTME_2ndAtt.txt",
                n.chains=1, n.iter=20000, n.burnin=100, n.thin=100)
# Now the values for the monitodeepskyblue3 parameters are in the "samples" object, ready for inspection.

MU_dA <- samples$BUGSoutput$sims.list$mud_A
MU_dB <- samples$BUGSoutput$sims.list$mud_B
MU_cA <- samples$BUGSoutput$sims.list$muc_A
MU_cB <- samples$BUGSoutput$sims.list$muc_B
SIG_dA <- samples$BUGSoutput$sims.list$sigmad_A
SIG_dB <- samples$BUGSoutput$sims.list$sigmad_B
SIG_cA <- samples$BUGSoutput$sims.list$sigmac_A
SIG_cB <- samples$BUGSoutput$sims.list$sigmac_B

print(c(mean(MU_dA), mean(MU_dB), mean(MU_cA), mean(MU_cB), mean(SIG_dA), mean(SIG_dB), mean(SIG_cA), mean(SIG_cB)))


#make the four panel plot:
#layout(matrix(c(1,2,3,4), 2, 2, byrow = TRUE))
layout(matrix(1:2,ncol=1))


if (experimento == 1) #Demo
{
#layout.show(4)
#some plotting options to make things look better:
par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
    font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
# Discriminability panel:    
plot(density(MU_dA), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
     xlim=c(1,4), ylim=c(0,2.3), axes=F)
lines(density(MU_dB), lwd=2, col="darkorchid3", lty=1)
axis(1)
axis(2, labels=F, at=c(0,24))
mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
mtext("D-primes", side=1, line = 2.5, cex=1.5)


# Bias panel:    
plot(density(MU_cA), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
     xlim=c(-0.5,0.5), ylim=c(0,4.5), axes=F)
axis(1)
axis(2, labels=F, at=c(0,24))
lines(density(MU_cB), lwd=2, col="darkorchid3", lty=1)
mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
mtext("C", side=1, line = 2.5, cex=1.5)
}

if (experimento == 2) #Demo
{
  par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
      font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
  # Discriminability panel:    
  # D primes (means)
  plot(density(MU_dA), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
       xlim=c(-0.2,2.7), ylim=c(0,2.2), axes=F)
  lines(density(MU_dB), lwd=2, col="darkorchid3", lty=1)
  axis(1)
  axis(2, labels=F, at=c(0,24))
  mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
  mtext("D-primes", side=1, line = 2.5, cex=1.5)
  
  
  # Bias panel:    
  plot(density(MU_cA), lwd=2, col="deepskyblue3", main="", ylab="", xlab="", 
       xlim=c(-0.7,0.51), ylim=c(0,5.5), axes=F)
  axis(1)
  axis(2, labels=F, at=c(0,24))
  lines(density(MU_cB), lwd=2, col="darkorchid3", lty=1)
  mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
  mtext("C", side=1, line = 2.5, cex=1.5)
}