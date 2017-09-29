##########################################################
# Codigo base para el análisis de datos bajo el marco 
# de la Teoría de Detección de Señales, de acuerdo con
# los parámetros y estadísticos expuestos por Stainslaw (1999)
##########################################################
#Referencia 1: Stainslaw & Todorov (1999), Calculation of signal detection theory measures.
#Referencia 2: Gescheider, George A. (2013). "Psychophysics: The Fundamentals". 
# # # # # # # # 
#Codigo hehco por: Adriana F. Chávez De la Peña
#Contacto: adrifelcha@gmail.com
##########################################################


#Cargamos los datos
setwd("C:/Users/Alejandro/Desktop/Felisa/Proyectos/Mario_BisecciónTemporal") # Directorio de trabajo
rm(list=ls())  #Reseteamos la consola
dir()          #Imprimimos los archivos del directorio     
archive <-'Datos_Sujeto3_Dummies.csv'  # Archivo que contiene los datos a analizar
datos <- read.csv(archive)       # Extraemos los datos del archivo
#Especificamos las variables
Sujeto <- datos$Sujeto
Condicion <- datos$Grupo
TipoSesion <- datos$Condicion
Magnitudes <- c('1v4', '2v8', '3v12', '5v2')
Dia<-datos$Día
Hits <- datos$Corto_enCorto
FA <- datos$Corto_enLargo
CRej <- datos$Largo_enLargo
Signal <- datos$EnsayosCortos #Deberia ser Hits+Misses
Noise <- datos$EnsayosLargos

Magnitudes <- unique(Condicion)

FA_rate<-FA/Noise
Hit_rate<-Hits/Signal

########################
# Computo de parametros
########################

#for(nce in sort(unique(Condicion))){

#Dprima computada segun la formula presentada por Gesheider, (2013) y Stainslaw (1999)
d<-qnorm(Hit_rate,0,1)-qnorm(FA_rate,0,1)

#A-Dprima computada segun la formula de Stainslaw, (1999)

Ad<-pnorm(d/(sqrt(2)))

#A' de acuerdo con la formula presentada por Stainslaw, (1999)
if(FA_rate > Hit_rate){
  A <- 0.5- ( ((FA_rate-Hit_rate)*(1+FA_rate-Hit_rate)) / ((4*FA_rate)*(1-Hit_rate)) )
} else {
  A <- 0.5+ ( ((Hit_rate-FA_rate)*(1+Hit_rate-FA_rate)) / ((4*Hit_rate)*(1-FA_rate)) )
}

#Beta (de acuerdo a la fórmula de Gescheider, 2013)
k<-qnorm(1-FA_rate,0,1)                     #Necesitamos usar el criterio como referencia
beta<-dnorm(k,d,1)/dnorm(k,0,1)             #Calculamos el radio de la densidad de probabilidad en el criterio

#B" de acuerdo con el metodo de Grier (expuesto en Stainslaw. 1999)
if(FA_rate > Hit_rate){
  B <- (((FA_rate*(1-FA_rate))-(Hit_rate*(1-Hit_rate)))/((FA_rate*(1-FA_rate))+(Hit_rate*(1-Hit_rate))))
} else {
  B <- (((Hit_rate*(1-Hit_rate))-(FA_rate*(1-FA_rate)))/((Hit_rate*(1-Hit_rate))+(FA_rate*(1-FA_rate))))
}

#Sesgo C calculado de acuerdo con la formula de Gescheider (2013)
c<-k-(d/2)                                  


#################
#Redondeamos los valores calculados a dos dígitos
A_prima <- round(A,3)
B_biprima <- round(B,3)
Beta<-round(beta,3)
D_prima <- round(d,3)
Sesgo_C<-round(c,3)
A_dprima <- round(Ad,3)


################


################################
#Imprimimos los valores computados
valores<- data.frame(cbind(Sujeto, Condicion, TipoSesion, Dia, D_prima, A_dprima, A_prima, Beta, Sesgo_C, B_biprima))   #Acomodamos los valores en un arreglo
#Mostramos el arreglo
print(valores)

################################