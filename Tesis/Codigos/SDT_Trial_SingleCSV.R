# clears workspace:  
rm(list=ls()) 

# sets working directories:
setwd("C:/Users/Alejandro/Desktop/Felisa/Mirror Experiment/Mirror Experimento 2/Data")
library(R2jags)

#Archivo que contiene todos los datos
archive <-'Ex2a_TODOS.csv'
datos <- read.csv(archive)

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

for(row in archive){{
  fa_AN <- datos$A_FA
  hits_AS <- datos$A_H
  fa_BN <- datos$B_FA
  hits_BS <- datos$B_H
  FAr_an <- fa_AN/160 
  Hr_as <- hits_AS/160
  FAr_bn <- fa_BN/160
  Hr_bs <- hits_BS/160
  n <-160
#  scores <- c(fa_AN, FAr_an, hits_AS, Hr_as, fa_BN, FAr_bn, hits_BS, Hr_bs)
  }
#  print(c(fa_AN[length(fa_AN)], 
#        FAr_an[length(FAr_an)], 
#        fa_BN[length(fa_BN)], 
#        FAr_bn[length(FAr_bn)], 
#        hits_BS[length(hits_BS)], 
#        Hr_bs[length(Hr_bs)], 
#        hits_AS[length(hits_AS)], sampl
#       Hr_as[length(Hr_as)])) 
  
  data <- list("hits_AS", "fa_AN", "hits_BS", "fa_BN", "n") # to be passed on to JAGS
  myinits <- list(
    list(d_A=0, c_A=0.5, d_B=0, c_B=0))  
  
  # parameters to be monitored:	
  parameters <- c("d_A", "d_B", "c_A", "c_B", "thetah_A", "thetah_B", "thetaf_A", "thetaf_B")
  
  # The following command calls JAGS with specific options.
  # For a detailed description see the R2jags documentation.
  samples <- jags(data, inits=myinits, parameters,
                  model.file ="C:/Users/Alejandro/Desktop/Felisa/Tesis/Codigos/MEx2_2ndText.txt",
                  n.chains=1, n.iter=10000, n.burnin=1, n.thin=1)
}
