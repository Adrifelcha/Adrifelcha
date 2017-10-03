##########################################################
# Codigo base para el análisis de datos obtenidos en el experimento presentado por Pérez et al (2017)
# con los parámetros y estadísticos expuestos por Stainslaw (1999) y Gescheider (2013)
##########################################################
#Referencia 1: Stainslaw & Todorov (1999), Calculation of signal detection theory measures.
#Referencia 2: Gescheider, George A. (2013). "Psychophysics: The Fundamentals". 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#Codigo hecho por: Adriana F. Chávez De la Peña
#Contacto: adrifelcha@gmail.com
##########################################################
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # 


####################################
# # # # # # # #  Parte I
# # # # # # # #  Cargamos los datos
####################################
setwd("C:/Users/Adriana/Desktop/Felisa/Proyectos/Mario_BisecciónTemporal") # Directorio de trabajo
rm(list=ls())  #Reseteamos la consola
dir()          #Imprimimos los archivos contenidos en el directorio en la consola
archive <-'Datos_Sujeto3_Dummies.csv'  #Señalamos el archivo que contiene los datos a analizar
datos <- read.csv(archive)             #Extraemos los datos del archivo


########################################
# # # # # # # #  Parte II
# # # # # # # #  Especificamos variables
########################################
Sujeto <- datos$Sujeto         #Del archivo 'datos', identificamos los datos en la columna 'Sujeto' como variable Sujeto
Condicion <- datos$Grupo       #Del archivo 'datos', identificamos los datos en la columna 'Grupo' como variable Condición
TipoSesion <- datos$Condicion  #etc, etc, etc
Dia<-datos$Día
Hits <- datos$Corto_enCorto
FA <- datos$Corto_enLargo
CRej <- datos$Largo_enLargo
Signal <- datos$EnsayosCortos 
Noise <- datos$EnsayosLargos

Magnitudes <- c('1v4', '2v8', '3v12', '5v2')
# Preveemos una solución para los casos donde
# FalsasAlarmas = NumeroTotalDeEnsayosConRuido  ó
# Hits = NumeroTotalDeEnsayosConSeñal, 
# en cuyo caso, la tasa de Hits y FA sería = 1 y
# no permitiría continuar con la estimación paramétrica

FA_rate <- NULL
Hit_rate <- NULL
A <- NULL
B <- NULL

for(i in 1:length(FA)){
  if(FA[i]==Noise[i]){
    FA_rate[i]<-(FA[i]-1)/Noise[i]
  } else {
    FA_rate[i]<-FA[i]/Noise[i]}

  if(Hits[i]==Signal[i]){
    Hit_rate[i]<-(Hits[i]-1)/Signal[i]
  } else {
    Hit_rate[i]<-Hits[i]/Signal[i]}


############################################
# # # # # # # #  Parte III
# # # # # # # #  Computamos los parámetros
############################################


#Dprima computada segun la formula presentada por Gesheider, (2013) y Stainslaw (1999)
d<- qnorm(Hit_rate,0,1)-qnorm(FA_rate,0,1)
#D' = Distancia en unidades de desviación estándar (puntajes Z) entre las distribuciones de Ruido y Señal
#D' forma parte del análisis paramétrico e implica que se acepta que hay distribuciones normales equivariantes involucradas

#A-Dprima computada segun la formula de Stainslaw, (1999)
Ad<-pnorm(d/(sqrt(2)))
#A_D'= Area bajo la curva ROC computada aceptando los supuestos de normalidad y equivarianza en las distribuciones R y S

#A' de acuerdo con la formula presentada por Stainslaw, (1999) de manera diferencial para los casos donde H<FA y H>FA
if(FA_rate[i] > Hit_rate[i]){
  A[i] <- 0.5- ( ((FA_rate[i]-Hit_rate[i])*(1+FA_rate[i]-Hit_rate[i])) / ((4*FA_rate[i])*(1-Hit_rate[i])) )
  } else {
  A[i] <- 0.5+ ( ((Hit_rate[i]-FA_rate[i])*(1+Hit_rate[i]-FA_rate[i])) / ((4*Hit_rate[i])*(1-FA_rate[i])) )}
#A' = Medida NO paramétrica de sensibilidad, definida como el area bajo la curva ROC trazada SIN asumir normalidad o
#equivarianza en las distribuciones de Ruido y Señal

#Criterio (K) de acuerdo con la fórmula de Gescheider, (2013)
k<-qnorm(1-FA_rate,0,1)               
#K = La localización, en unidades de desviaciones estándar, del criterio de elección sobre el eje de decisión
#que determina la emisión de juicios a favor, o en contra, de la detección de la Señal

#Beta (de acuerdo a la fórmula de Gescheider, 2013)
beta<-dnorm(k,d,1)/dnorm(k,0,1)             
#Beta = Medida paramétrica de sesgo que calcula el radio de la densidad de probabilidad en el criterio

#Sesgo C calculado de acuerdo con la formula de Gescheider (2013)
c<-k-(d/2)                                
#C = Medida paramétrica de sesgo que computa la distancia entre la localización del criteiro y el punto en que se
#intercectan las distribuciones S y R (cuando el sesgo es nulo)


#B" de acuerdo con el metodo de Grier (expuesto en Stainslaw. 1999), para los casos en que H>FA o H<FA
if(FA_rate[i] > Hit_rate[i]){
  B[i] <- (((FA_rate[i]*(1-FA_rate[i]))-(Hit_rate[i]*(1-Hit_rate[i])))/((FA_rate[i]*(1-FA_rate[i]))+(Hit_rate[i]*(1-Hit_rate[i]))))
} else {
  B[i] <- (((Hit_rate[i]*(1-Hit_rate[i]))-(FA_rate[i]*(1-FA_rate[i])))/((Hit_rate[i]*(1-Hit_rate[i]))+(FA_rate[i]*(1-FA_rate[i]))))}
#B" = Medida NO paramétrica que computa la distancia entre la localización del criterio en el espacio ROC y 
# la diagonal negativa, que define la localización esperada en un criterio sin sesgo alguno.


# # # # # # # # Redondeamos los valores computados a 3 dígitos

A_prima <- round(A,3)
B_biprima <- round(B,3)
Beta<-round(beta,3)
D_prima <- round(d,2)
Sesgo_C<-round(c,3)
A_dprima <- round(Ad,3)
}

















###########################################################################################################
###########################################################################################################
# # # # # # # #  Parte IV
# # # # # # # #  Imprimimos los valores computados
##########################################################################################################

############################
#OPCION 1:  TODOS LOS DATOS
#Imprimimos TODOS los parámetros computados, distinguiendo con Variables Dummies 1) El sujeto a presentar;
#2) La magnitud probada #3) El tipo de sesión (LB o M) y 4) El día
valores<- data.frame(cbind(Sujeto, Condicion, TipoSesion, Dia, D_prima, A_dprima, A_prima, Beta, Sesgo_C, B_biprima))   #Acomodamos los valores en un arreglo
print(valores)


########################################
# OPCION 2: Datos por Sujeto y Magnitud, días por separado
#Imprimimos los parámetros computados por cada sujeto, para cada una de las magnitudes probadas
#Es decir, por cada sujeto, se mostrarán 4 arreglos de datos que presenten las estimaciones para
#los ensayos en LB y Magnitud, a lo largo de 10 días
for(a in sort(unique(datos$Sujeto))){
  print('---------------------------------------------------')
  print(c('Sujeto:', a))
  print('---------------------------------------------------')
  for(nce in sort(unique(Condicion))){
    print(c('Magnitud:', nce,'=============='))
    valores<- data.frame(cbind(TipoSesion[Condicion==nce], D_prima[Condicion==nce], A_dprima[Condicion==nce], A_prima[Condicion==nce], Beta[Condicion==nce], Sesgo_C[Condicion==nce], B_biprima[Condicion==nce]))   #Acomodamos los valores en un arreglo
    colnames(valores) <- c("Sesion","D'","A_d'","A'","Beta","C","B''")
    print(valores) }}


########################################
# OPCION 3: Datos por Sujeto y Magnitud, promediando LB y M
#Imprimimos los parámetros computados por cada sujeto, para cada una de las magnitudes probadas
#Es decir, por cada sujeto, se mostrarán 4 arreglos de datos que presenten las estimaciones para
#los ensayos en LB y Magnitud, de acuerdo a la ejecución promedio de los participantes.
layout(matrix(1:2,ncol=2, byrow=TRUE))

for(x in sort(unique(datos$Sujeto))){
  print('===================================================')
  print(c('Sujeto:', x))
  print('===================================================')
    for(a in sort(unique(Condicion))){
    print(c('========> Magnitud:', a))
      for(b in sort(unique(TipoSesion))){
      Sesion <- b
      Hits_TS <- sum(Hits[Condicion==a & TipoSesion==b])
      FA_TS <- sum(FA[Condicion==a & TipoSesion==b]) 
      Signal_TS <- sum(Signal[Condicion==a & TipoSesion==b])
      Noise_TS <- sum(Noise[Condicion==a & TipoSesion==b])
      Hit_rateTS <- Hits_TS/Signal_TS
      FA_rateTS <- FA_TS/Noise_TS
      d_TS<- qnorm(Hit_rateTS,0,1)-qnorm(FA_rateTS,0,1)
      Ad_TS<-pnorm(d_TS/(sqrt(2)))
      if(FA_rateTS > Hit_rateTS){
        A_TS <- 0.5- ( ((FA_rateTS-Hit_rateTS)*(1+FA_rateTS-Hit_rateTS)) / ((4*FA_rateTS)*(1-Hit_rateTS)) )
      } else {
        A_TS <- 0.5+ ( ((Hit_rateTS-FA_rateTS)*(1+Hit_rateTS-FA_rateTS)) / ((4*Hit_rateTS)*(1-FA_rateTS)) )}
      k_TS<-qnorm(1-FA_rateTS,0,1)               
      beta_TS<-dnorm(k_TS,d_TS,1)/dnorm(k_TS,0,1)             
      c_TS<-k_TS-(d_TS/2)                                
      if(FA_rateTS > Hit_rateTS){
        B_TS <- (((FA_rateTS*(1-FA_rateTS))-(Hit_rateTS*(1-Hit_rateTS)))/((FA_rateTS*(1-FA_rateTS))+(Hit_rateTS*(1-Hit_rateTS))))
      } else {
        B_TS <- (((Hit_rateTS*(1-Hit_rateTS))-(FA_rateTS*(1-FA_rateTS)))/((Hit_rateTS*(1-Hit_rateTS))+(FA_rateTS*(1-FA_rateTS))))}
      A_primaTS <- round(A_TS,3)
      B_biprimaTS <- round(B_TS,3)
      Beta_TS<-round(beta_TS,3)
      D_primaTS <- round(d_TS,2)
      Sesgo_CTS<-round(c_TS,3)
      A_dprimaTS <- round(Ad_TS,3)
      Hit_rateTS <- round(Hit_rateTS,3)
      FA_rateTS <- round(FA_rateTS,3)
      valoresTS<- data.frame(cbind(Sesion, Hit_rateTS, FA_rateTS, D_primaTS, A_dprimaTS, A_primaTS, Beta_TS, Sesgo_CTS, B_biprimaTS))   #Acomodamos los valores en un arreglo
      colnames(valoresTS) <- c("Sesion",'Hits', 'FA', "D'","A_d'","A'","Beta", "C", "B''")
      print(valoresTS)
      
      Barras <- c(A_primaTS, B_biprimaTS)
      
      barplot(Barras, main = "", xlab = "", ylab = "", font.lab=2, ylim = c(-1,1), axes = FALSE, col =c("dodgerblue4", "deeppink4"))
      axis(1,at=c(0.72,1.9),labels=c("A'", "B''"), font=2)
      axis(2,at=c(0, -1, 1),labels=c("0","-1","1"),las=1)
      text(0.72,(A_primaTS/2),paste(A_primaTS),cex=.9,col='white',f=3)
      text(1.9,(B_biprimaTS/2),paste(B_biprimaTS),cex=.9,col='white',f=3)
      text(0.72,(A_primaTS/2)-.1,"A'",cex=1.2,col='white',f=3)
      text(1.9,(B_biprimaTS/2)-.1,"B''",cex=1.2,col='white',f=3)
      mtext(b,3,cex=2.5, line=1, f=2)
      title(a, outer = TRUE, line = -2)
      }}}






















###########################################################################################################
###########################################################################################################
# # # # # # # #  Parte V
# # # # # # # #  Graficamos los datos
##########################################################################################################
layout(matrix(1:2,ncol=1, byrow=TRUE))

TotalDatos <- (length(unique(Condicion))*length(unique(TipoSesion)))*length(unique(Sujeto))

for(barras in 1:(length(unique(Condicion))*length(unique(TipoSesion)))*length(unique(Sujeto))){
  barplot(c(A_primaTS[barras], B_biprimaTS[barras]))}
