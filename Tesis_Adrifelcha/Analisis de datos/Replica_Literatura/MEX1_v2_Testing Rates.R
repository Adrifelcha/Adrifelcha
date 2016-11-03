#Calculando Miss Rates, FA Rates y H Rates por separado

setwd("C:/Users/Adrifelcha/Dropbox/Tesis/Experimentos/Mirror Experimento 1/Data_Ex1a_SinSesgo1")
rm(list=ls())
dir()

data <- read.csv("Ex1aV2_S101_Frida.csv")

layout(matrix(1:3,ncol=1))
#for(archive in dir()){
#data <- read.csv("Ex1aV2_S101_Frida.csv")
for(archive in dir()){
  data <- read.csv(archive)
  Hits_AS <- NULL
  Hits_BS <- NULL
  Miss_AN <- NULL
  Miss_BN <- NULL
  Rej_AN <- NULL
  Rej_BN <- NULL
  FA_AN <- NULL
  FA_BN <- NULL
  Hits_AS <- mean(data$Confidence[data$Hits=='True'&data$facilidad=='pocos'])
  Hits_BS <- mean(data$Confidence[data$Hits=='True'&data$facilidad=='muchos'])
  Miss_AN <- mean(data$Confidence[data$Omisiones=='True'&data$facilidad=='pocos'])
  Miss_BN <- mean(data$Confidence[data$Omisiones=='True'&data$facilidad=='muchos'])
  Rej_AN <- mean(data$Confidence[data$Rechazos=='True'&data$facilidad=='pocos'])
  Rej_BN <- mean(data$Confidence[data$Rechazos=='True'&data$facilidad=='muchos'])
  FA_AN <- mean(data$Confidence[data$Falsas.alarmas=='True'&data$facilidad=='pocos'])
  FA_BN <- mean(data$Confidence[data$Falsas.alarmas=='True'&data$facilidad=='muchos'])
  print(c(archive))
  print(c('H_AS','H_BS','M_AS','M_BS','Rej_AN','Rej_BN','FA_AN','FA_BN'))
  print(c(Hits_AS, Hits_BS, Miss_AN, Miss_BN, Rej_AN, Rej_BN, FA_AN, FA_BN))}
  

setwd("C:/Users/Adrifelcha/Dropbox/Tesis/Experimentos/Mirror Experimento 2/Data/Datos_Exp2")
rm(list=ls())
dir()

#data <- read.csv("Ex1aV2_S101_Frida.csv")

layout(matrix(1:3,ncol=1))
#for(archive in dir()){
#data <- read.csv("Ex1aV2_S101_Frida.csv")
for(archive in dir()){
  data <- read.csv(archive)
  Hits_AS <- NULL
  Hits_BS <- NULL
  Miss_AN <- NULL
  Miss_BN <- NULL
  Rej_AN <- NULL
  Rej_BN <- NULL
  FA_AN <- NULL
  FA_BN <- NULL
  Hits_AS <- mean(data$Confidence[data$Hits=='True'&data$facilidad=='pocos'])
  Hits_BS <- mean(data$Confidence[data$Hits=='True'&data$facilidad=='muchos'])
  Miss_AN <- mean(data$Confidence[data$Omisiones=='True'&data$facilidad=='pocos'])
  Miss_BN <- mean(data$Confidence[data$Omisiones=='True'&data$facilidad=='muchos'])
  Rej_AN <- mean(data$Confidence[data$Rechazos=='True'&data$facilidad=='pocos'])
  Rej_BN <- mean(data$Confidence[data$Rechazos=='True'&data$facilidad=='muchos'])
  FA_AN <- mean(data$Confidence[data$Falsas.alarmas=='True'&data$facilidad=='pocos'])
  FA_BN <- mean(data$Confidence[data$Falsas.alarmas=='True'&data$facilidad=='muchos'])
  print(c(archive))
  print(c('H_AS','H_BS','M_AS','M_BS','Rej_AN','Rej_BN','FA_AN','FA_BN'))
  print(c(Hits_AS, Hits_BS, Miss_AN, Miss_BN, Rej_AN, Rej_BN, FA_AN, FA_BN))}
