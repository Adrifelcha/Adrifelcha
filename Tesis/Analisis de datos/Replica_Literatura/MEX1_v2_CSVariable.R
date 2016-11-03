setwd("C:/Users/Adrifelcha/Dropbox/Tesis/Experimentos/Mirror Experimento 1/Data_Ex1a_SinSesgo1")
rm(list=ls())
dir()

#archive <-'MirrorEx1a_Elias_2016-05-05_Y_N+R.csv'

for(archive in dir()){
  felisa <- read.csv(archive)
  felisa <- felisa[1:640,]
  # Codificacion Estimulos
  # Estimulo 1-200 senalfacil/AS
  # Estimulo 201-400 ruidofacil/AN
  # Estimulo 401-600 senaldificil/BS
  # Estimulo 601-800 ruidodificil/BN
  
  
  facilidad <- NULL
  signal <- NULL
  tamano_central <- NULL
  num_ext <- NULL
  tam_ext <- NULL
  tipo <- NULL
  choice <- NULL
  outcome <- NULL
  Exito <- NULL
  
  facilidad[felisa$Estimulo<=320] <- 'pocos'
  facilidad[felisa$Estimulo>320] <- 'muchos'
  
  choice[felisa$Respuesta=='n'] <- '0'
  choice[felisa$Respuesta=='s'] <- '1'
  
  signal[(felisa$Estimulo>=1&felisa$Estimulo<=160)|(felisa$Estimulo>=321&felisa$Estimulo<=480)] <- 'senal'
  signal[(felisa$Estimulo>=161&felisa$Estimulo<=320)|(felisa$Estimulo>=481&felisa$Estimulo<=640)] <- 'ruido'
  

  tipo[(felisa$Estimulo>=1&felisa$Estimulo<=160)] <- '4 AS'
  tipo[(felisa$Estimulo>=321&felisa$Estimulo<=480)] <- '3 BS'
  tipo[(felisa$Estimulo>=161&felisa$Estimulo<=320)] <- '1 AN'
  tipo[(felisa$Estimulo>=481&felisa$Estimulo<=640)] <- '2 BN'
  
  Exito[felisa$Correcto=='True'] <- '1'
  Exito[felisa$Correcto=='False'] <- '0'
  
  outcome[felisa$Rechazos=='True'] <- 3
  outcome[felisa$Hits=='True'] <- 4
  outcome[felisa$Falsas.alarmas=='True'] <- 1
  outcome[felisa$Omisiones=='True'] <-2
  
  felisa$facilidad <- facilidad
  felisa$senal <- signal
  felisa$tipo <- tipo
  felisa$choice <- choice
  felisa$outcome <- outcome
  felisa$Exito <- Exito
  head(felisa,50)
  
  
  write.csv(felisa,file=archive)
}


#########

rm(list=ls())
dir()

for(archive in dir()){
  felisa <- read.csv(archive)
  felisa <- felisa[1:640,]
  
  HR6 <- NULL
  FR6 <- NULL
  HR5 <- NULL
  FR5 <- NULL
  HR4 <- NULL
  FR4 <- NULL
  HR3 <- NULL
  FR3 <- NULL
  HR2 <- NULL
  FR2 <- NULL
  HR1 <- NULL
  FR1 <- NULL
  
  HR6[felisa$Confidence=='6'& felisa$senal=='senal'] <- '1'
  HR6[felisa$Confidence=='6'& felisa$senal=='ruido'] <- '0'
  HR6[(felisa$Confidence=='5')|(felisa$Confidence=='4')|(felisa$Confidence=='3')|(felisa$Confidence=='2')|(felisa$Confidence=='1')] <- '0'
  
  HR5[(felisa$Confidence=='6'& felisa$senal=='senal')|(felisa$Confidence=='5'& felisa$senal=='senal')] <- '1'
  HR5[(felisa$Confidence=='6'& felisa$senal=='ruido')|(felisa$Confidence=='5'& felisa$senal=='ruido')|(felisa$Confidence=='4')|(felisa$Confidence=='3')|(felisa$Confidence=='2')|(felisa$Confidence=='1')] <- '0'
  
  HR4[(felisa$Confidence=='6'& felisa$senal=='senal')|(felisa$Confidence=='5'& felisa$senal=='senal')|(felisa$Confidence=='4'& felisa$senal=='senal')] <- '1'
  HR4[(felisa$Confidence=='6'& felisa$senal=='ruido')|(felisa$Confidence=='5'& felisa$senal=='ruido')|(felisa$Confidence=='4'& felisa$senal=='ruido')|(felisa$Confidence=='3')|(felisa$Confidence=='2')|(felisa$Confidence=='1')] <- '0'
  
  HR3[(felisa$Confidence=='6'& felisa$senal=='senal')|(felisa$Confidence=='5'& felisa$senal=='senal')|(felisa$Confidence=='4'& felisa$senal=='senal')|(felisa$Confidence=='3'& felisa$senal=='senal')] <-'1'
  HR3[(felisa$Confidence=='6'& felisa$senal=='ruido')|(felisa$Confidence=='5'& felisa$senal=='ruido')|(felisa$Confidence=='4'& felisa$senal=='ruido')|(felisa$Confidence=='3'& felisa$senal=='ruido')|(felisa$Confidence=='2')|(felisa$Confidence=='1')] <-'0'
  
  HR2[(felisa$Confidence=='6'& felisa$senal=='senal')|(felisa$Confidence=='5'& felisa$senal=='senal')|(felisa$Confidence=='4'& felisa$senal=='senal')|(felisa$Confidence=='3'& felisa$senal=='senal')|(felisa$Confidence=='2'& felisa$senal=='senal')] <-'1' <-'1'
  HR2[(felisa$Confidence=='6'& felisa$senal=='ruido')|(felisa$Confidence=='5'& felisa$senal=='ruido')|(felisa$Confidence=='4'& felisa$senal=='ruido')|(felisa$Confidence=='3'& felisa$senal=='ruido')|(felisa$Confidence=='2'& felisa$senal=='ruido')|(felisa$Confidence=='1')] <-'0'
  
  HR1[(felisa$Confidence=='6'& felisa$senal=='senal')|(felisa$Confidence=='5'& felisa$senal=='senal')|(felisa$Confidence=='4'& felisa$senal=='senal')|(felisa$Confidence=='3'& felisa$senal=='senal')|(felisa$Confidence=='2'& felisa$senal=='senal')|(felisa$Confidence=='1'& felisa$senal=='senal')] <-'1'
  HR1[(felisa$Confidence=='6'& felisa$senal=='ruido')|(felisa$Confidence=='5'& felisa$senal=='ruido')|(felisa$Confidence=='4'& felisa$senal=='ruido')|(felisa$Confidence=='3'& felisa$senal=='ruido')|(felisa$Confidence=='2'& felisa$senal=='ruido')|(felisa$Confidence=='1'& felisa$senal=='ruido')] <- '0'
  
  FR6[felisa$Confidence=='6'& felisa$senal=='senal'] <- '0'
  FR6[felisa$Confidence=='6'& felisa$senal=='ruido'] <- '1'
  FR6[(felisa$Confidence=='5')|(felisa$Confidence=='4')|(felisa$Confidence=='3')|(felisa$Confidence=='2')|(felisa$Confidence=='1')] <- '0'
  
  FR5[(felisa$Confidence=='6'& felisa$senal=='senal')|(felisa$Confidence=='5'& felisa$senal=='senal')] <- '0'
  FR5[(felisa$Confidence=='6'& felisa$senal=='ruido')|(felisa$Confidence=='5'& felisa$senal=='ruido')] <- '1'
  FR5[(felisa$Confidence=='4')|(felisa$Confidence=='3')|(felisa$Confidence=='2')|(felisa$Confidence=='1')] <- '0'
  
  FR4[(felisa$Confidence=='6'& felisa$senal=='senal')|(felisa$Confidence=='5'& felisa$senal=='senal')|(felisa$Confidence=='4'& felisa$senal=='senal')] <- '0'
  FR4[(felisa$Confidence=='6'& felisa$senal=='ruido')|(felisa$Confidence=='5'& felisa$senal=='ruido')|(felisa$Confidence=='4'& felisa$senal=='ruido')] <- '1'
  FR4[(felisa$Confidence=='3')|(felisa$Confidence=='2')|(felisa$Confidence=='1')] <- '0'
  
  FR3[(felisa$Confidence=='6'& felisa$senal=='senal')|(felisa$Confidence=='5'& felisa$senal=='senal')|(felisa$Confidence=='4'& felisa$senal=='senal')|(felisa$Confidence=='3'& felisa$senal=='senal')] <-'0'
  FR3[(felisa$Confidence=='6'& felisa$senal=='ruido')|(felisa$Confidence=='5'& felisa$senal=='ruido')|(felisa$Confidence=='4'& felisa$senal=='ruido')|(felisa$Confidence=='3'& felisa$senal=='ruido')] <-'1'
  FR3[(felisa$Confidence=='2')|(felisa$Confidence=='1')] <- '0'
  
  FR2[(felisa$Confidence=='6'& felisa$senal=='senal')|(felisa$Confidence=='5'& felisa$senal=='senal')|(felisa$Confidence=='4'& felisa$senal=='senal')|(felisa$Confidence=='3'& felisa$senal=='senal')|(felisa$Confidence=='2'& felisa$senal=='senal')] <-'0' 
  FR2[(felisa$Confidence=='6'& felisa$senal=='ruido')|(felisa$Confidence=='5'& felisa$senal=='ruido')|(felisa$Confidence=='4'& felisa$senal=='ruido')|(felisa$Confidence=='3'& felisa$senal=='ruido')|(felisa$Confidence=='2'& felisa$senal=='ruido')] <-'1'
  FR2[(felisa$Confidence=='1')] <- '0'
  
  FR1[(felisa$Confidence=='6'& felisa$senal=='senal')|(felisa$Confidence=='5'& felisa$senal=='senal')|(felisa$Confidence=='4'& felisa$senal=='senal')|(felisa$Confidence=='3'& felisa$senal=='senal')|(felisa$Confidence=='2'& felisa$senal=='senal')|(felisa$Confidence=='1'& felisa$senal=='senal')] <-'0'
  FR1[(felisa$Confidence=='6'& felisa$senal=='ruido')|(felisa$Confidence=='5'& felisa$senal=='ruido')|(felisa$Confidence=='4'& felisa$senal=='ruido')|(felisa$Confidence=='3'& felisa$senal=='ruido')|(felisa$Confidence=='2'& felisa$senal=='ruido')|(felisa$Confidence=='1'& felisa$senal=='ruido')] <- '1'
  
  felisa$HR6 <- HR6
  felisa$FR6 <- FR6
  felisa$HR5 <- HR5
  felisa$FR5 <- FR5
  felisa$HR4 <- HR4
  felisa$FR4 <- FR4
  felisa$HR3 <- HR3
  felisa$FR3 <- FR3
  felisa$HR2 <- HR2
  felisa$FR2 <- FR2
  felisa$HR1 <- HR1
  felisa$FR1 <- FR1
  
  
  write.csv(felisa,file=archive)
}
#is.recursive(felisa)


