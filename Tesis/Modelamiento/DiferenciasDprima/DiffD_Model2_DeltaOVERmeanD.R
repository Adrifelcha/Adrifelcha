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
experimento <- 2
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
  list(d_A = rep(0,k), c_A = rep(0,k), d_B = rep(0,k), c_B = rep (0,k)))  

# parameters to be monitodeepskyblue3:	
parameters <- c("d_A", "c_A", "thetah_A", "thetaf_A", "d_B", "c_B", "thetah_B", "thetaf_B","delta")

# Corremos JAGS
samples <- jags(data, inits=myinits, parameters,
                model.file ="C:/Users/Alejandro/Desktop/Felisa/Tesis/Modelamiento/DiferenciasDprima/DiffD_Modelo2_DeltaOVERmeanD.txt",
                n.chains=1, n.iter=10000, n.burnin=1, n.thin=1)
# Now the values for the monitodeepskyblue3 parameters are in the "samples" object, ready for inspection.



for (a in 1:k){
  d_a <- samples$BUGSoutput$sims.list$d_A[,a]
  d_b <- samples$BUGSoutput$sims.list$d_B[,a]
  c_a <- samples$BUGSoutput$sims.list$c_A[,a]
  c_b <- samples$BUGSoutput$sims.list$c_B[,a]
}

for (b in 1:k){
  tetaH_a <- samples$BUGSoutput$sims.list$thetah_A[,b]
  tetaH_b <- samples$BUGSoutput$sims.list$thetah_B[,b]
  tetaFA_a <- samples$BUGSoutput$sims.list$thetaf_A[,b]
  tetaFA_b <- samples$BUGSoutput$sims.list$thetaf_B[,b]
  Delta <- samples$BUGSoutput$sims.list$delta[,k]
}


print(c(d_a[length(d_a)], 
        d_b[length(d_b)], 
        c_a[length(c_a)], 
        c_b[length(c_b)], 
        tetaFA_a[length(tetaFA_a)], 
        tetaFA_b[length(tetaFA_b)], 
        tetaH_a[length(tetaH_a)], 
        tetaH_b[length(tetaH_b)],
        Delta[length(Delta)]))


#make the four panel plot:
#layout(matrix(1:2,ncol=1))
layout(matrix(c(1,2,3,4), 2, 2, byrow = TRUE))




#layout.show(4)
#some plotting options to make things look better:
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


if (experimento == 1)
{
  lines(c(0, 0.1),c(12,12), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0, 0.1),c(10,10), lwd=2, lty=1, col="darkorchid3")
  
  text(0.15, 12, labels="A Condition", offset=0, cex = 0.8, pos=4)
  text(0.15, 10, labels="B Condition", offset=0, cex = 0.8, pos=4)
}

if (experimento == 2)
{
  lines(c(0, 0.1),c(12,12), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0, 0.1),c(10,10), lwd=2, lty=1, col="darkorchid3")
  
  text(0.15, 12, labels="A Condition", offset=0, cex = 0.8, pos=4)
  text(0.15, 10, labels="B Condition", offset=0, cex = 0.8, pos=4)
}

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



