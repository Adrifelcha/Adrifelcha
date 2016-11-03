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
  list(d_A = rep(0,k), c_A = rep(0,k), d_B = rep(0,k), c_B = rep (0,k)))  

# parameters to be monitodeepskyblue3:	
parameters <- c("d_A", "c_A", "thetah_A", "thetaf_A", "d_B", "c_B", "thetah_B", "thetaf_B")

niter <- 10000
burnin <- 1000
# Corremos JAGS
samples <- jags(data, inits=myinits, parameters,
                model.file ="C:/Users/Alejandro/Desktop/Felisa/Tesis/Modelamiento/Aprendiendo_EnsayoError/Ap_2_SDTME_1stAtt.txt",
                n.chains=1, n.iter=niter, n.burnin=burnin, n.thin=1)
# Now the values for the monitodeepskyblue3 parameters are in the "samples" object, ready for inspection.

for (a in 1:k){
  d_a <- samples$BUGSoutput$sims.list$d_A
  }

for (b in 1:k){
  d_b <- samples$BUGSoutput$sims.list$d_B
}

for (c in 1:k){
  c_a <- samples$BUGSoutput$sims.list$c_A
}

for (d in 1:k){
  c_b <- samples$BUGSoutput$sims.list$c_B
}

for (e in 1:k){
  tetaH_a <- samples$BUGSoutput$sims.list$thetah_A[,e]
}

for (f in 1:k){
  tetaH_b <- samples$BUGSoutput$sims.list$thetah_B[,f]
}

for (g in 1:k){
  tetaFA_a <- samples$BUGSoutput$sims.list$thetaf_A[,g]
}

for (h in 1:k){
  tetaFA_b <- samples$BUGSoutput$sims.list$thetaf_B[,h]
}

print(c(d_a[length(d_a)], 
        d_b[length(d_b)], 
        c_a[length(c_a)], 
        c_b[length(c_b)], 
        tetaFA_a[length(tetaFA_a)], 
        tetaFA_b[length(tetaFA_b)], 
        tetaH_a[length(tetaH_a)], 
        tetaH_b[length(tetaH_b)]))



#make the four panel plot:
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




######## Marginales y Densidad
keep_ <- (1000)
keep <- sample(niter, keep_)
d.FA_a <- density(tetaFA_a)
d.FA_b <- density(tetaFA_b)
d.H_a <- density(tetaH_a)
d.H_b <- density(tetaH_b)

layout(matrix(c(1,2,3,0),2,2,byrow=T), width=c(2/3, 1/3), heights=c(2/3,1/3))
#layout.show()

if (experimento == 1)
{
par(mar=c(2,2,1,0))
plot(tetaFA_a[keep],tetaH_a[keep], col="deepskyblue3", xlab="", ylab="", axes=F,xlim=c(0,0.5), ylim=c(0.5,1))
points(tetaFA_b[keep],tetaH_b[keep], col="darkorchid3")
lines(c(0.36, 0.41),c(0.60,0.60), lwd=2, lty=1, col="deepskyblue3")
lines(c(0.36, 0.41),c(0.55,0.55), lwd=2, lty=1, col="darkorchid3")
text(0.43, 0.60, labels="A Condition", offset=0, cex = 0.8, pos=4)
text(0.43, 0.55, labels="B Condition", offset=0, cex = 0.8, pos=4)
box(lty=1)

par(mar=c(2,1,1,4))
plot(d.H_a$y, d.H_a$x, xlim=rev(c(0,16)),type='l', col="deepskyblue3", axes=F, xlab="", ylab="",ylim=c(0.5,1))
lines(d.H_b$y, d.H_b$x, col="darkorchid3")
axis(4)
mtext(expression(paste(mu, "Hits")), side=4,line=2.3, cex=0.9)
box(lty=1)

par(mar=c(6,2,0,0))
plot(density(tetaFA_a),zero.line=F ,main="", col="deepskyblue3", ylab="", xlab="", cex.lab=1.3, axes=F, xlim=c(0,0.5),ylim=c(0,26))
lines(density(tetaFA_b), col="darkorchid3")
axis(1, at=c(0, 0.1, 0.2, 0.3, 0.4, 0.5))
mtext(expression(paste(mu, "False Alarms")), side=1.2,line=2, cex=0.9)
box(lty=1)
}

if (experimento == 2){
  
  par(mar=c(2,2,1,0))
  plot(tetaFA_a[keep],tetaH_a[keep], xlab="", ylab="", col="deepskyblue3",axes=F,xlim=c(0,0.5), ylim=c(0.5,1))
  points(tetaFA_b[keep],tetaH_b[keep], col="darkorchid3")
  lines(c(0, 0.05),c(0.9,0.9), lwd=2, lty=1, col="deepskyblue3")
  lines(c(0, 0.05),c(0.85,0.85), lwd=2, lty=1, col="darkorchid3")
  text(0.08, 0.9, labels="A Condition", offset=0, cex = 0.8, pos=4)
  text(0.08, 0.85, labels="B Condition", offset=0, cex = 0.8, pos=4)
  box(lty=1)
  
  par(mar=c(2,1,1,4))
  plot(d.H_a$y, d.H_a$x, xlim=rev(c(0,13)), col= 'deepskyblue3', type='l', axes=F, xlab="", ylab="",ylim=c(0.5,1))
  lines(d.H_b$y, d.H_b$x, col="darkorchid3")
  axis(4)
  mtext(expression(paste(mu, "Hits")), side=4,line=2.3, cex=0.9)
  box(lty=1)
  
  par(mar=c(6,2,0,0))
  plot(density(tetaFA_a),zero.line=F , col="deepskyblue3", main="", ylab="", xlab="", cex.lab=1.3, axes=F, xlim=c(0,0.5),ylim=c(0,12))
  lines(density(tetaFA_b), col="darkorchid3")
  axis(1, at=c(0, 0.1, 0.2, 0.3, 0.4, 0.5))
  mtext(expression(paste(mu, "False Alarms")), side=1.2,line=2, cex=0.9)
  box(lty=1)
}

