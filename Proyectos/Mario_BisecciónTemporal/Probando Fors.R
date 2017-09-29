

#Cargamos los datos
setwd("C:/Users/Alejandro/Desktop/Felisa/Proyectos/Mario_BisecciónTemporal") # Directorio de trabajo
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
  Z <- append(Z, sum(datos$Corto_enCorto[datos$Grupo==nce]=='True'))
  X <- append(X, sum(datos$Corto_enLargo[datos$Grupo==nce]=='True'))
  W <- Z+W
  output <- data.frame(cbind(Z,X,W))
  print(c(nce,
          'Suma:', W[length(W)],
          'Hits:', Z[length(Z)],
          'FA:', X[length(X)]))
  print(output)
}


#for(nce in sort(unique(Condicion))){
valores<- data.frame(cbind(Sujeto, Condicion, TipoSesion, A, B))   #Acomodamos los valores en un arreglo
#}
#Mostramos el arreglo
C<-mean(Hits)


D<-mean(Hits)
print(valores)

################################