

#Cargamos los datos
setwd("C:/Users/Adriana/Desktop/Felisa/Proyectos/Mario_BisecciónTemporal") # Directorio de trabajo
rm(list=ls())  #Reseteamos la consola
dir()          #Imprimimos los archivos del directorio     
archive <-'Datos_Prueba.csv'  # Archivo que contiene los datos a analizar
datos <- read.csv(archive)       # Extraemos los datos del archivo

#Especificamos las variables
Sujeto <- datos$Sujeto
Condicion <- datos$Grupo
TipoSesion <- datos$Condicion
Magnitudes <- c('1v4', '2v8', '3v12', '5v2')
Dia<-datos$Día
Hits <- datos$Corto_enCorto
FA <- datos$Corto_enLargo
Signal <- datos$EnsayosCortos #Deberia ser Hits+Misses
Noise <- datos$EnsayosLargos

Magnitudes <- unique(datos$Grupo)

FA_rate<-FA/Noise
Hit_rate<-Hits/Signal




A<-Hits+FA
B<-Hits-FA

Z <- NULL
X <- NULL
W <- NULL

for(nce in sort(unique(Condicion))){
  Z <- append(Z, sum(Hits[Condicion==nce]))
  X <- (FA[Condicion==nce]*2)
  W <- Z/100
  output <- data.frame(cbind(Z,X,W))
  
  W <- round(W,1)
  
  print(nce)
  print(c('Suma:', W[length(W)]))
  print(c('Hits:', Z[length(Z)]))
  print(c('FA:', X))
}


FA <-50
Hits <- 60
Noise <- 50
Signal <- 60


if(FA==Noise){
  FA_rate<-(FA-1)/Noise
} else {
  FA_rate<-FA/Noise
}

if(Hits==Signal){
  Hit_rate<-(Hits-1)/Signal
} else {
  Hit_rate<-Hits/Signal
}

################################