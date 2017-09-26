#Codigo Base para Analisis NO paramétrico (SDT)
#Autor: Adriana F. Chávez De la Peña
#adrifelcha@gmail.com
##########################################################

rm(list=ls())  #Limpiamos el espacio de trabajo

Hits <- 36
FA <- 2
Signals <- 100
Noise <- 100
Hit_rate <- Hits/Signals
FA_rate <- FA/Noise


#A' de acuerdo con la formula presentada por Stainslaw (1999)
if(FA_rate > Hit_rate){
  A <- 0.5+(((FA_rate-Hit_rate)*(1+(FA_rate-Hit_rate)))/(((4*FA_rate)*(1-Hit_rate))))
  print("A prima")
  print(A)  
} else {
  A <- 0.5-(((Hit_rate-FA_rate)*(1+(Hit_rate-FA_rate)))/(((4*Hit_rate)*(1-FA_rate))))
  print("A prima")
  print(A)
}


#B" de acuerdo con el metodo de Grier (Stainslaw. 1999)
if(FA_rate > Hit_rate){
  B <- (((FA_rate*(1-FA_rate))-(Hit_rate*(1-Hit_rate)))/((FA_rate*(1-FA_rate))+(Hit_rate*(1-Hit_rate))))
  print("B comillas")
  print(B)  
} else {
  B <- (((Hit_rate*(1-Hit_rate))-(FA_rate*(1-FA_rate)))/((Hit_rate*(1-Hit_rate))+(FA_rate*(1-FA_rate))))
  print("B comillas")
  print(B)
}


