##########################################################
# Codigo base para el análisis de paty obtenidos en el experimento presentado por Pérez et al (2017)
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
# # # # # # # #  Cargamos los paty
####################################
setwd("C:/Users/Adriana/Desktop/Felisa/Proyectos/Mario_BisecciónTemporal") # Directorio de trabajo
rm(list=ls())  #Reseteamos la consola
dir()          #Imprimimos los archivos contenidos en el directorio en la consola
archive <-'Datos_Paty.csv'  
paty <- read.csv(archive) #Extraemos los paty del archivo




########################################
# # # # # # # #  Parte II
# # # # # # # #  Especificamos variables
########################################
Sujeto <- paty$sujeto         #Del archivo 'paty', identificamos los paty en la columna 'Sujeto' como variable Sujeto
Condicion <- paty$grupo       #Del archivo 'paty', identificamos los paty en la columna 'Grupo' como variable Condición
TipoSesion <- paty$condición  #etc, etc, etc
Dia<- paty$dia
Hits <- paty$hit
FA <- paty$fa
CRej <- paty$rechazo
Miss <- paty$miss
Noise <- paty$ensayos_largo
Signal <- paty$ensayos_cortos

Signal_Is <- c(rep('Corto', length(Sujeto)))
TotalSujetos <- length(unique(Sujeto))
Sesiones <- c(rep('LB',10), rep('M',10))
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
  if(FA[i]==0){
    FA_rate[i]<-.01
    #FA_rate[i]<-(FA[i]+1)/Noise[i]
  } else {
    FA_rate[i]<-FA[i]/Noise[i]}
  
  if(Hits[i]==Signal[i]){
    Hit_rate[i]<-0.99
    #Hit_rate[i]<-(Hits[i]-1)/Signal[i]
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
  Hit_rate <- round(Hit_rate,3)
  FA_rate <- round(FA_rate,3)
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
#valores<- data.frame(cbind(Sujeto, Magnitudes, Sesiones, Dia, D_prima, A_dprima, A_prima, Beta, Sesgo_C, B_biprima))   #Acomodamos los valores en un arreglo
valores<- data.frame(cbind(Sujeto, Signal_Is, Condicion, Sesiones, Dia, Hit_rate, FA_rate, D_prima, A_dprima, A_prima, Beta, Sesgo_C, B_biprima))   #Acomodamos los valores en un arreglo
colnames(valores) <- c("Sujeto","Señal","Condicion", "Sesion", "Día","Tasa Hits","Tasa F.A.","D'","A_d'","A'","Beta","C","B''")
options(max.print=10000000)
print(valores)


########################################
# OPCION 2: Datos por Sujeto y Magnitud, días por separado
#Imprimimos los parámetros computados por cada sujeto, para cada una de las magnitudes probadas
#Es decir, por cada sujeto, se mostrarán 4 arreglos de datos que presenten las estimaciones para
#los ensayos en LB y Magnitud, a lo largo de 10 días
for(a in sort(unique(paty$sujeto))){
  print('---------------------------------------------------')
  print(c('Sujeto:', a, '==== La Señal es:', Signal_Is[Sujeto==a & Dia=='1' &Condicion=='1v4' & TipoSesion=='LB']))
  print('---------------------------------------------------')
  for(nce in sort(unique(Condicion))){
    print(c('============================ > Magnitud:', nce))
    valor<- data.frame(cbind(Sesiones, Hit_rate[Sujeto==a&Condicion==nce], FA_rate[Sujeto==a&Condicion==nce], D_prima[Sujeto==a&Condicion==nce], A_dprima[Sujeto==a&Condicion==nce], A_prima[Sujeto==a&Condicion==nce], Beta[Sujeto==a&Condicion==nce], Sesgo_C[Sujeto==a&Condicion==nce], B_biprima[Sujeto==a&Condicion==nce]))   #Acomodamos los valores en un arreglo
    colnames(valor) <- c("Sesion","Hits","FA","D'","A_d'","A'","Beta","C","B''")
    print(valor) }}


########################################
# OPCION 3: Datos por Sujeto y Magnitud, promediando LB y M
#Imprimimos los parámetros computados por cada sujeto, para cada una de las magnitudes probadas
#Es decir, por cada sujeto, se mostrarán 4 arreglos de datos que presenten las estimaciones para
#los ensayos en LB y Magnitud, de acuerdo a la ejecución promedio de los participantes.
layout(matrix(1:2,ncol=2, byrow=TRUE))

A_primaTS <- NULL
B_biprimaTS <- NULL
Beta_TS<- NULL
D_primaTS <- NULL
Sesgo_CTS<- NULL
A_dprimaTS <- NULL
Hit_rTS <- NULL
FA_rTS <- NULL

Sesiones <- c('LB', 'M')

for(x in sort(unique(paty$sujeto))){
  print('===================================================')
  print(c('Sujeto:', x, '==== La Señal es:', Signal_Is[Sujeto==x & Dia=='1' & Condicion=='1v4' & TipoSesion=='LB']))
  print('===================================================')
  for(a in sort(unique(Condicion))){
    print(c('========> Magnitud:', a))
    for(b in sort(unique(TipoSesion))){
      Sesion <- b
      Hits_TS <- sum(Hits[Condicion==a & TipoSesion==b &Sujeto==x])
      FA_TS <- sum(FA[Condicion==a & TipoSesion==b & Sujeto==x]) 
      Signal_TS <- sum(Signal[Condicion==a & TipoSesion==b & Sujeto==x])
      Noise_TS <- sum(Noise[Condicion==a & TipoSesion==b & Sujeto==x])
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
      A_primaTS[b] <- round(A_TS,3)
      B_biprimaTS[b] <- round(B_TS,3)
      Beta_TS[b] <-round(beta_TS,3)
      D_primaTS[b] <- round(d_TS,2)
      Sesgo_CTS[b] <-round(c_TS,3)
      A_dprimaTS[b] <- round(Ad_TS,3)
      Hit_rTS[b] <- round(Hit_rateTS,3)
      FA_rTS[b] <- round(FA_rateTS,3)
    }
    
    valoresTS<- data.frame(cbind(Sesiones, Hit_rTS, FA_rTS, D_primaTS, A_dprimaTS, A_primaTS, Beta_TS, Sesgo_CTS, B_biprimaTS))   #Acomodamos los valores en un arreglo
    colnames(valoresTS) <- c("Sesion",'Hits', 'FA', "D'","A_d'","A'","Beta", "C", "B''")
    print(valoresTS)}}



########################################
# OPCION 4: Promedio de la ejecución registrada por cada magnitud,
# para las sesiones en Linea Base vs Magnitud
# (Promedio entre sujetos)

layout(matrix(1:2,ncol=2, byrow=TRUE))

Par_A_LB <- NULL
Par_A_M <- NULL
Par_B_LB <- NULL
Par_B_M <- NULL

for(a in sort(unique(Condicion))){
  print(c('========> Magnitud:', a))
  for(b in sort(unique(TipoSesion))){
    Sesion <- b
    Hits_ <- sum(Hits[Condicion==a&TipoSesion==b])
    FA_ <- sum(FA[Condicion==a&TipoSesion==b]) 
    Signal_ <- sum(Signal[Condicion==a&TipoSesion==b])
    Noise_ <- sum(Noise[Condicion==a&TipoSesion==b])
    H_rate <- Hits_/Signal_
    FA_rate <- FA_/Noise_
    d_<- qnorm(H_rate,0,1)-qnorm(FA_rate,0,1)
    Ad_<-pnorm(d_/(sqrt(2)))
    if(FA_rate > H_rate){
      A_ <- 0.5- ( ((FA_rate-H_rate)*(1+FA_rate-H_rate)) / ((4*FA_rate)*(1-H_rate)) )
    } else {
      A_ <- 0.5+ ( ((H_rate-FA_rate)*(1+H_rate-FA_rate)) / ((4*H_rate)*(1-FA_rate)) )}
    k_<-qnorm(1-FA_rate,0,1)               
    beta_<-dnorm(k_,d_,1)/dnorm(k_,0,1)             
    c_<-k_-(d_/2)
    if(FA_rate > H_rate){
      B_ <- (((FA_rate*(1-FA_rate))-(H_rate*(1-H_rate)))/((FA_rate*(1-FA_rate))+(H_rate*(1-H_rate))))
    } else {
      B_ <- (((H_rate*(1-H_rate))-(FA_rate*(1-FA_rate)))/((H_rate*(1-H_rate))+(FA_rate*(1-FA_rate))))}
    
    A_ <- round(A_,3)
    B_ <- round(B_,3)
    Beta_<-round(beta_,3)
    D_ <- round(d_,2)
    C_<- round(c_,3)
    A_d_ <- round(Ad_,3)
    H_rate <- round(H_rate,3)
    FA_rate <- round(FA_rate,3)
    
    valores_P<- data.frame(cbind(b, H_rate, FA_rate, A_, B_))   #Acomodamos los valores en un arreglo
    colnames(valores_P) <- c("Sesion",'Hits', 'FA', "A'", "B'") #, "D'","A_d'","A'","Beta", "C", "B''")
    print(valores_P)
  }}
