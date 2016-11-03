# clears workspace:  
rm(list=ls()) 

# sets working directories:
setwd("C:/Users/Alejandro/Desktop/Felisa/Mirror Experiment/Mirror Experimento 2/Data/Datos_Exp2")
library(R2jags)

#dataset <- 1

#if (dataset == 1) #Demo
#{
#  k <- 3 #number of cases
#  data <- matrix(c(70, 50, 30, 50, 7, 5, 3, 5, 10, 0, 0, 10), nrow=k, ncol=4, byrow=T)
#}

#if (dataset == 2) #Lehrner et al. (1995) data 
#{
#  k <- 3 #number of cases
#  data <- matrix(c(148, 29, 32, 151, 150, 40, 30, 140, 150, 51, 40, 139), nrow=k, ncol=4, byrow=T)
#}

#f <- data[,2]
#h <- data[,1]
#MI <- data[,3]
#CR <- data[,4]
#s <- h + MI
#n <- f + CR

k <- 20
  
for(archive in dir()){
  participante <- read.csv(archive)
  fa_AN <- NULL
  rej_AN <- NULL
  hits_AS <- NULL
  miss_AS <- NULL
  fa_BN <- NULL
  rej_BN <- NULL
  hits_BS <- NULL
  miss_BS <- NULL
{ fa_AN <- sum(participante$Falsas.alarmas[participante$Estimulo>=161&participante$Estimulo<=320]=='True')
  rej_AN <- sum(participante$Rechazos[participante$Estimulo>=161&participante$Estimulo<=320]=='True')
  hits_AS <- sum(participante$Hits[participante$Estimulo>=1&participante$Estimulo<=160]=='True')
  miss_AS <- sum(participante$Omisiones[participante$Estimulo>=1&participante$Estimulo<=160]=='True')
  fa_BN <- sum(participante$Falsas.alarmas[participante$Estimulo>=481&participante$Estimulo<=640]=='True')
  rej_BN <- sum(participante$Rechazos[participante$Estimulo>=481&participante$Estimulo<=640]=='True')
  hits_BS <- sum(participante$Hits[participante$Estimulo>=321&participante$Estimulo<=480]=='True')
  miss_BS <- sum(participante$Omisiones[participante$Estimulo>=321&participante$Estimulo<=480]=='True')
  FAr_an <- fa_AN/160 
  Hr_as <- hits_AS/160
  FAr_bn <- fa_BN/160
  Hr_bs <- hits_BS/160
  s_A <- hits_AS+miss_AS 
  s_B <- hits_BS+miss_BS
  n_A <- fa_AN+rej_AN
  n_B <- fa_BN+rej_BN
  print(c(fa_AN[length(fa_AN)], 
          FAr_an[length(FAr_an)], 
          fa_BN[length(fa_BN)], 
          FAr_bn[length(FAr_bn)], 
          hits_BS[length(hits_BS)], 
          Hr_bs[length(Hr_bs)], 
          hits_AS[length(hits_AS)], 
          Hr_as[length(Hr_as)]))
}

data <- list("hits_AS", "fa_AN", "hits_BS", "fa_BN", "s_A", "n_A", "s_B", "n_B") # to be passed on to JAGS
myinits <- list(
  list(d_A=0.5, c_A=0.5, d_B=0.5, c_B=0.5))  

# parameters to be monitored:	
parameters <- c("d_A", "d_B", "c_A", "c_B", "thetah_A", "thetah_B", "thetaf_A", "thetaf_B")

# The following command calls JAGS with specific options.
# For a detailed description see the R2jags documentation.
samples <- jags(data, inits=myinits, parameters,
	 			model.file ="C:/Users/Alejandro/Desktop/Felisa/Tesis/Codigos/MEx2_1stText.txt",
	 			n.chains=1, n.iter=10000, n.burnin=1, n.thin=1)
}

# Now the values for the monitored parameters are in the "samples" object, 
# ready for inspection.
for(d in k){
d_A <- samples$BUGSoutput$sims.list$d_A[,k]
d_B <- samples$BUGSoutput$sims.list$d_B[,k]
}

for(c in k){
  c_A <- samples$BUGSoutput$sims.list$c_A[,k]
  c_B <- samples$BUGSoutput$sims.list$c_B[,k]
}

for(h in k){
  h_A <- samples$BUGSoutput$sims.list$thetah_A[,k]
  h_B <- samples$BUGSoutput$sims.list$thetah_B[,k]
}

for(f in k){
  f_A <- samples$BUGSoutput$sims.list$thetaf_A[,k]
  f_B <- samples$BUGSoutput$sims.list$thetaf_B[,k]
}

c1 <- samples$BUGSoutput$sims.list$c[,1]
c2 <- samples$BUGSoutput$sims.list$c[,2]
c3 <- samples$BUGSoutput$sims.list$c[,3]

h1 <- samples$BUGSoutput$sims.list$thetah[,1]
h2 <- samples$BUGSoutput$sims.list$thetah[,2]
h3 <- samples$BUGSoutput$sims.list$thetah[,3]

f1 <- samples$BUGSoutput$sims.list$thetaf[,1]
f2 <- samples$BUGSoutput$sims.list$thetaf[,2]
f3 <- samples$BUGSoutput$sims.list$thetaf[,3]

#make the four panel plot:
layout(matrix(c(1,2,3,4), 2, 2, byrow = TRUE))
#layout.show(4)
#some plotting options to make things look better:
par(cex.main = 1.5, mar = c(5, 6, 4, 5) + 0.1, mgp = c(3.5, 1, 0), cex.lab = 1.5,
    font.lab = 2, cex.axis = 1.3, bty = "n", las=1)
# Discriminability panel:    
plot(density(d1), lwd=2, col="red", main="", ylab="", xlab="", 
     xlim=c(-2,6), axes=F)
axis(1)
axis(2, labels=F, at=c(0,24))

lines(density(d2), lwd=2, col="green", lty=2)
lines(density(d3), lwd=2, col="blue", lty=2)

mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
mtext("Discriminability", side=1, line = 2.5, cex=1.5)

# Bias panel:    
plot(density(c1), lwd=2, col="red", main="", ylab="", xlab="", 
     xlim=c(-2,2), axes=F)
axis(1)
axis(2, labels=F, at=c(0,24))

lines(density(c2), lwd=2, col="green", lty=2)
lines(density(c3), lwd=2, col="blue", lty=2)

mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
mtext("Bias", side=1, line = 2.5, cex=1.5)

# Hit Rate panel:    
plot(density(h1), lwd=2, col="red", main="", ylab="", xlab="", 
     xlim=c(0,1), axes=F)
axis(1)
axis(2, labels=F, at=c(0,24))

lines(density(h2), lwd=2, col="green", lty=2)
lines(density(h3), lwd=2, col="blue", lty=2)

if (dataset == 1)
{
  lines(c(0, 0.1),c(7,7), lwd=2, lty=1, col="red")
  lines(c(0, 0.1),c(6,6), lwd=2, lty=2, col="green")
  lines(c(0, 0.1),c(5,5), lwd=2, lty=3, col="blue")
  
  text(0.15, 7, labels="first", offset=0, cex = 1.3, pos=4)
  text(0.15, 6, labels="second", offset=0, cex = 1.3, pos=4)
  text(0.15, 5, labels="third", offset=0, cex = 1.3,pos=4)
}

if (dataset == 2)
{
  lines(c(0, 0.1),c(7,7), lwd=2, lty=1, col="red")
  lines(c(0, 0.1),c(6,6), lwd=2, lty=2, col="green")
  lines(c(0, 0.1),c(5,5), lwd=2, lty=3, col="blue")
  
  text(0.15, 7, labels="Control", offset=0, cex = 1.3, pos=4)
  text(0.15, 6, labels="Group I", offset=0, cex = 1.3, pos=4)
  text(0.15, 5, labels="Group II", offset=0, cex = 1.3,pos=4)
}

mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
mtext("Hit Rate", side=1, line = 2.5, cex=1.5)

# False-Alarm Rate panel:    
plot(density(f1), lwd=2, col="red", main="", ylab="", xlab="", 
     xlim=c(0,1), axes=F)
axis(1)
axis(2, labels=F, at=c(0,24))

lines(density(f2), lwd=2, col="green", lty=2)
lines(density(f3), lwd=2, col="blue", lty=2)

mtext("Probability Density", side=2, line = 2, cex=1.5, las=0)
mtext("False-Alarm Rate", side=1, line = 2.5, cex=1.5)



