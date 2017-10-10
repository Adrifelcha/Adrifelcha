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
# # # # # # # #  Cargamos los datos
####################################
setwd("C:/Users/Alejandro/Desktop/Felisa/Proyectos/Mario_BisecciónTemporal") # Directorio de trabajo
rm(list=ls())  #Reseteamos la consola
dir()          #Imprimimos los archivos contenidos en el directorio en la consola
archive <-'Datos_Dummies_4sujetos.csv'  #Señalamos el archivo que contiene los datos a analizar
datos <- read.csv(archive)             #Extraemos los datos del archivo
########################################
# # # # # # # #  Especificamos variables
########################################
Sujeto <- datos$Sujeto         #Del archivo 'datos', identificamos los datos en la columna 'Sujeto' como variable Sujeto
Condicion <- datos$Grupo       #Del archivo 'datos', identificamos los datos en la columna 'Grupo' como variable Condición
TipoSesion <- datos$Condicion  #etc, etc, etc
Dia<-datos$Día
Hits <- NULL
FA <- NULL
CRej <- NULL
Miss <- NULL
Noise <- NULL
Signal <- NULL

LargoEsSignal <- c(3, 5, 20, 33)  #Especificamos cuáles Sujetos estuvieron en el grupo donde LARGO es Señal

for(i in 1:length(Dia)){
  if(Sujeto[i] %in% LargoEsSignal == TRUE){
    #if(Sujeto[i] == 3|5|20|33){
    Hits[i] <- datos$Largo_enLargo[i]
    FA[i] <- datos$Largo_enCorto[i]
    CRej[i] <- datos$Corto_enCorto[i]
    Miss[i] <- datos$Corto_enLargo[i]
    Noise[i] <- datos$EnsayosCortos[i] 
    Signal[i] <- datos$EnsayosLargos[i]
  } else {
    Hits[i] <- datos$Corto_enCorto[i]
    FA[i] <- datos$Corto_enLargo[i]
    CRej[i] <- datos$Largo_enLargo[i]
    Signal[i] <- datos$EnsayosCortos[i] 
    Noise[i] <- datos$EnsayosLargos[i]}}


TotalSujetos <- length(unique(Sujeto))
Magnitudes <- c(rep('1v4', 20), rep('2v8', 20), rep('3v12', 20), rep('5v2', 20))
Sesiones <- c(rep('LB',10), rep('M',10))
# Preveemos una solución para los casos donde


########################################
# # # # # # # #  G R A F I C O S
########################################


#########################################           GRAFICO 1
###################################           Grafica de Barras comparando A' y B'' 
###################################           en Linea Base vs Magnitud, en cada condición
###################################           por cada sujeto (Un grafico por condicion)

layout(matrix(1:2,ncol=2, byrow=TRUE))

for(x in sort(unique(datos$Sujeto))){
  print('===================================================')
  print(c('Sujeto:', x))
  print('===================================================')
  for(a in sort(unique(Condicion))){
    print(c('========> Magnitud:', a))
      Sesion <- c('LB','M')
      Hits_TS <- Hits[Condicion==a&Sujeto==x]
      FA_TS <- FA[Condicion==a&Sujeto==x] 
      Hits_LB <- sum(Hits_TS[1:10])
      FA_LB <- sum(FA_TS[1:10])
      Hits_M <- sum(Hits_TS[11:20])
      FA_M <- sum(FA_TS[11:20])
      Signal_TS <- Signal[Condicion==a&Sujeto==x]
      Noise_TS <- Noise[Condicion==a&Sujeto==x]
      N_LB <- sum(Noise_TS[1:10])
      S_LB <- sum(Signal_TS[1:10])
      N_M <- sum(Noise_TS[11:20])
      S_M <- sum(Signal_TS[11:20])
      H_rateLB <- Hits_LB/S_LB
      FA_rateLB <- FA_LB/N_LB
      H_rateM <- Hits_M/S_M
      FA_rateM <- FA_M/N_M
      d_LB<- qnorm(H_rateLB,0,1)-qnorm(FA_rateLB,0,1)
      d_M<- qnorm(H_rateM,0,1)-qnorm(FA_rateM,0,1)
      Ad_LB<-pnorm(d_LB/(sqrt(2)))
      Ad_M<-pnorm(d_M/(sqrt(2)))
      if(FA_rateLB > H_rateLB){
        A_LB <- 0.5- ( ((FA_rateLB-H_rateLB)*(1+FA_rateLB-H_rateLB)) / ((4*FA_rateLB)*(1-H_rateLB)) )
      } else {
        A_LB <- 0.5+ ( ((H_rateLB-FA_rateLB)*(1+H_rateLB-FA_rateLB)) / ((4*H_rateLB)*(1-FA_rateLB)) )}
      if(FA_rateM > H_rateM){
        A_M <- 0.5- ( ((FA_rateM-H_rateM)*(1+FA_rateM-H_rateM)) / ((4*FA_rateM)*(1-H_rateM)) )
      } else {
        A_M <- 0.5+ ( ((H_rateM-FA_rateM)*(1+H_rateM-FA_rateM)) / ((4*H_rateM)*(1-FA_rateM)) )}
      k_LB<-qnorm(1-FA_rateLB,0,1)               
      k_M<-qnorm(1-FA_rateM,0,1)               
      beta_LB<-dnorm(k_LB,d_LB,1)/dnorm(k_LB,0,1)             
      beta_M<-dnorm(k_M,d_M,1)/dnorm(k_M,0,1)             
      c_LB<-k_LB-(d_LB/2)
      c_M<-k_M-(d_M/2)                                
      if(FA_rateLB > H_rateLB){
        B_LB <- (((FA_rateLB*(1-FA_rateLB))-(H_rateLB*(1-H_rateLB)))/((FA_rateLB*(1-FA_rateLB))+(H_rateLB*(1-H_rateLB))))
      } else {
        B_LB <- (((H_rateLB*(1-H_rateLB))-(FA_rateLB*(1-FA_rateLB)))/((H_rateLB*(1-H_rateLB))+(FA_rateLB*(1-FA_rateLB))))}
      if(FA_rateM > H_rateM){
        B_M <- (((FA_rateM*(1-FA_rateM))-(H_rateM*(1-H_rateM)))/((FA_rateM*(1-FA_rateM))+(H_rateM*(1-H_rateM))))
      } else {
        B_M <- (((H_rateM*(1-H_rateM))-(FA_rateM*(1-FA_rateM)))/((H_rateM*(1-H_rateM))+(FA_rateM*(1-FA_rateM))))}
      
      A_TS <- c(round(A_LB,3), round(A_M,3))
      B_TS <- c(round(B_LB,3), round(B_M,3))
      Beta_TS<-c(round(beta_LB,3), round(beta_M,3))
      D_TS <- c(round(d_LB,2), round(d_M,3))
      C_TS<- c(round(c_LB,3), round(c_M,3))
      A_d_TS <- c(round(Ad_LB,3), round(Ad_M,3))
      H_rateTS <- c(round(H_rateLB,3), round(H_rateM,3))
      FA_rateTS <- c(round(FA_rateLB,3), round(FA_rateM,3))
      
      valoresTS<- data.frame(cbind(Sesion[unique(TipoSesion)], H_rateTS, FA_rateTS, A_TS, B_TS))   #Acomodamos los valores en un arreglo
      colnames(valoresTS) <- c("Sesion",'Hits', 'FA', "A'", "B'") #, "D'","A_d'","A'","Beta", "C", "B''")
      print(valoresTS)
      
      barplot(A_TS, main = "", xlab = "", ylab = "", font.lab=2, ylim = c(0,1), axes = FALSE, col =c("cadetblue2", "deepskyblue4"))
      axis(1,at=c(0.72,1.9),labels=c("Línea Base", "Matriz de Pagos"), font=2)
      axis(2,at=c(0, 0.25, 0.5, 0.75, 1),labels=c("0", "0.25", "0.5", "0.75", "1"),las=1)
      text(0.72,(A_TS[1]/2),paste(A_TS[1]),cex=.9,col='black',f=2)
      text(1.9,(A_TS[2]/2),paste(A_TS[2]),cex=.9,col='white',f=2)
      mtext("A'",3,cex=3.5, line=1, f=2)

      barplot(B_TS, main = "", xlab = "", ylab = "", font.lab=2, ylim = c(-1,1), axes = FALSE, col =c("darkseagreen3", "darkseagreen4"))
      axis(1,at=c(0.72,1.9),labels=c("Línea Base", "Matriz de Pagos"), font=2)
      axis(2,at=c(0, -0.5, 0.5, -1, 1),labels=c("0", "-0.5", "0.5", "-1","1"),las=1)
      text(0.72,(B_TS[1]/2),paste(B_TS[1]),cex=.9,col='black',f=2)
      text(1.9,(B_TS[2]/2),paste(B_TS[2]),cex=.9,col='white',f=2)
      mtext("B'",3,cex=3.5, line=1, f=2)
      mtext(a,4,cex=2.5, line=1, f=2)
  }}

#########################################           GRAFICO 2
###################################           Grafica de Barras comparando A' y B'' 
###################################           en Linea Base vs Magnitud, en cada condición
###################################           por cada sujeto  (Todas las condiciones en un solo grafico)

layout(matrix(1:2,ncol=2, byrow=TRUE))

Par_A_LB <- NULL
Par_A_M <- NULL
Par_B_LB <- NULL
Par_B_M <- NULL

for(x in sort(unique(datos$Sujeto))){
  print('===================================================')
  print(c('Sujeto:', x))
  print('===================================================')
  for(a in sort(unique(Condicion))){
    print(c('========> Magnitud:', a))
    Sesion <- c('LB','M')
    Hits_TS <- Hits[Condicion==a&Sujeto==x]
    FA_TS <- FA[Condicion==a&Sujeto==x] 
    Hits_LB <- sum(Hits_TS[1:10])
    FA_LB <- sum(FA_TS[1:10])
    Hits_M <- sum(Hits_TS[11:20])
    FA_M <- sum(FA_TS[11:20])
    Signal_TS <- Signal[Condicion==a&Sujeto==x]
    Noise_TS <- Noise[Condicion==a&Sujeto==x]
    N_LB <- sum(Noise_TS[1:10])
    S_LB <- sum(Signal_TS[1:10])
    N_M <- sum(Noise_TS[11:20])
    S_M <- sum(Signal_TS[11:20])
    H_rateLB <- Hits_LB/S_LB
    FA_rateLB <- FA_LB/N_LB
    H_rateM <- Hits_M/S_M
    FA_rateM <- FA_M/N_M
    d_LB<- qnorm(H_rateLB,0,1)-qnorm(FA_rateLB,0,1)
    d_M<- qnorm(H_rateM,0,1)-qnorm(FA_rateM,0,1)
    Ad_LB<-pnorm(d_LB/(sqrt(2)))
    Ad_M<-pnorm(d_M/(sqrt(2)))
    if(FA_rateLB > H_rateLB){
      A_LB <- 0.5- ( ((FA_rateLB-H_rateLB)*(1+FA_rateLB-H_rateLB)) / ((4*FA_rateLB)*(1-H_rateLB)) )
    } else {
      A_LB <- 0.5+ ( ((H_rateLB-FA_rateLB)*(1+H_rateLB-FA_rateLB)) / ((4*H_rateLB)*(1-FA_rateLB)) )}
    if(FA_rateM > H_rateM){
      A_M <- 0.5- ( ((FA_rateM-H_rateM)*(1+FA_rateM-H_rateM)) / ((4*FA_rateM)*(1-H_rateM)) )
    } else {
      A_M <- 0.5+ ( ((H_rateM-FA_rateM)*(1+H_rateM-FA_rateM)) / ((4*H_rateM)*(1-FA_rateM)) )}
    k_LB<-qnorm(1-FA_rateLB,0,1)               
    k_M<-qnorm(1-FA_rateM,0,1)               
    beta_LB<-dnorm(k_LB,d_LB,1)/dnorm(k_LB,0,1)             
    beta_M<-dnorm(k_M,d_M,1)/dnorm(k_M,0,1)             
    c_LB<-k_LB-(d_LB/2)
    c_M<-k_M-(d_M/2)                                
    if(FA_rateLB > H_rateLB){
      B_LB <- (((FA_rateLB*(1-FA_rateLB))-(H_rateLB*(1-H_rateLB)))/((FA_rateLB*(1-FA_rateLB))+(H_rateLB*(1-H_rateLB))))
    } else {
      B_LB <- (((H_rateLB*(1-H_rateLB))-(FA_rateLB*(1-FA_rateLB)))/((H_rateLB*(1-H_rateLB))+(FA_rateLB*(1-FA_rateLB))))}
    if(FA_rateM > H_rateM){
      B_M <- (((FA_rateM*(1-FA_rateM))-(H_rateM*(1-H_rateM)))/((FA_rateM*(1-FA_rateM))+(H_rateM*(1-H_rateM))))
    } else {
      B_M <- (((H_rateM*(1-H_rateM))-(FA_rateM*(1-FA_rateM)))/((H_rateM*(1-H_rateM))+(FA_rateM*(1-FA_rateM))))}
    
    A_TS <- c(round(A_LB,3), round(A_M,3))
    B_TS <- c(round(B_LB,3), round(B_M,3))
    Beta_TS<-c(round(beta_LB,3), round(beta_M,3))
    D_TS <- c(round(d_LB,2), round(d_M,3))
    C_TS<- c(round(c_LB,3), round(c_M,3))
    A_d_TS <- c(round(Ad_LB,3), round(Ad_M,3))
    H_rateTS <- c(round(H_rateLB,3), round(H_rateM,3))
    FA_rateTS <- c(round(FA_rateLB,3), round(FA_rateM,3))
    
    valoresTS<- data.frame(cbind(Sesion[unique(TipoSesion)], H_rateTS, FA_rateTS, A_TS, B_TS))   #Acomodamos los valores en un arreglo
    colnames(valoresTS) <- c("Sesion",'Hits', 'FA', "A'", "B'") #, "D'","A_d'","A'","Beta", "C", "B''")
    print(valoresTS)
    
    Par_A_LB[a] <- A_TS[1]
    Par_A_M[a] <- A_TS[2]
    Par_B_LB[a] <- B_TS[1]
    Par_B_M[a] <- B_TS[2]
  }
  
  Parejas_A <- c(rbind(Par_A_LB, Par_A_M))
  Parejas_B <- c(rbind(Par_B_LB, Par_B_M))
  
  barplot(Parejas_A, main = "", xlab = "", ylab = "", font.lab=2, ylim = c(0,1.05), axes = FALSE, col =c("cadetblue2", "deepskyblue4"))
  axis(1,at=c(1.3,3.7,6.1,8.5),labels=c("1vs4", "2vs8", "3vs12", "5vs2"), font=2)
  axis(2,at=c(0, 0.25, 0.5, 0.75, 1),labels=c("0", "0.25", "0.5", "0.75", "1"),las=1)
  text(0.72,(Parejas_A[1]-.07),paste(Parejas_A[1]),cex=.9,col='black',f=2, srt=90)
  text(1.9,(Parejas_A[2]-.07),paste(Parejas_A[2]),cex=.9,col='white',f=2, srt=90)
  text(3.08,(Parejas_A[3]-.07),paste(Parejas_A[3]),cex=.9,col='black',f=2, srt=90)
  text(4.26,(Parejas_A[4]-.07),paste(Parejas_A[4]),cex=.9,col='white',f=2, srt=90)
  text(5.5,(Parejas_A[5]-.07),paste(Parejas_A[5]),cex=.9,col='black',f=2, srt=90)
  text(6.67,(Parejas_A[6]-.07),paste(Parejas_A[6]),cex=.9,col='white',f=2, srt=90)
  text(7.9,(Parejas_A[7]-.07),paste(Parejas_A[7]),cex=.9,col='black',f=2, srt=90)
  text(9.1,(Parejas_A[8]-.07),paste(Parejas_A[8]),cex=.9,col='white',f=2, srt=90)
  lines(c(5.7, 7.3),c(1,1), lwd=3, lty=1, col="deepskyblue4")
  lines(c(0.7, 2.3),c(1,1), lwd=3, lty=1, col="cadetblue2")
  text(2.5, 1, labels="Baseline", offset=0, cex = 0.9, pos=4)
  text(7.5, 1, labels="Magnitud", offset=0, cex = 0.9, pos=4)
  mtext("A'",3,cex=3.5, line=1, f=2)
  
  barplot(Parejas_B, main = "", xlab = "", ylab = "", font.lab=2, ylim = c(-1,1.05), axes = FALSE, col =c("darkseagreen3", "darkseagreen4"))
  axis(1,at=c(1.3,3.7,6.1,8.5),labels=c("1vs4", "2vs8", "3vs12", "5vs2"), font=2)
  axis(2,at=c(0, -0.5, 0.5, -1, 1),labels=c("0", "-0.5", "0.5", "-1","1"),las=1)
  text(0.72,(Parejas_B[1]+.07),paste(Parejas_B[1]),cex=.9,col='black',f=2, srt=90)
  text(1.9,(Parejas_B[2]+.07),paste(Parejas_B[2]),cex=.9,col='black',f=2, srt=90)
  text(3.08,(Parejas_B[3]+.07),paste(Parejas_B[3]),cex=.9,col='black',f=2, srt=90)
  text(4.26,(Parejas_B[4]+.07),paste(Parejas_B[4]),cex=.9,col='black',f=2, srt=90)
  text(5.5,(Parejas_B[5]+.07),paste(Parejas_B[5]),cex=.9,col='black',f=2, srt=90)
  text(6.67,(Parejas_B[6]+(Parejas_B[6]/3)),paste(Parejas_B[6]),cex=.9,col='black',f=2)
  text(7.9,(Parejas_B[7]+(Parejas_B[7]/3)),paste(Parejas_B[7]),cex=.9,col='black',f=2)
  text(9.1,(Parejas_B[8]+(Parejas_B[8]/3)),paste(Parejas_B[8]),cex=.9,col='black',f=2)
  lines(c(5.7, 7.3),c(1,1), lwd=3, lty=1, col="darkseagreen4")
  lines(c(0.7, 2.3),c(1,1), lwd=3, lty=1, col="darkseagreen3")
  text(2.5, 1, labels="Baseline", offset=0, cex = 0.9, pos=4)
  text(7.5, 1, labels="Magnitud", offset=0, cex = 0.9, pos=4)
  mtext("B'",3,cex=3.5, line=1, f=2)
  mtext(paste("Subject No.",x),4,cex=2, line=1, f=2)}



#########################################           GRAFICO 3
###################################           Grafica de Barras comparando A' y B'' 
###################################           en Linea Base vs Magnitud, en cada condición
###################################           PROMEDIANDO TODOS LOS SUJETOS

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
    
    
    if(b=='LB'){
      Par_A_LB[a] <- A_
      Par_B_LB[a] <- B_
    } else {
      Par_A_M[a] <- A_
      Par_B_M[a] <- B_
      }}}
  
  Parejas_A <- c(rbind(Par_A_LB, Par_A_M))
  Parejas_B <- c(rbind(Par_B_LB, Par_B_M))
  
  barplot(Parejas_A, main = "", xlab = "", ylab = "", font.lab=2, ylim = c(0,1.05), axes = FALSE, col =c("cadetblue2", "deepskyblue4"))
  axis(1,at=c(1.3,3.7,6.1,8.5),labels=c("1vs4", "2vs8", "3vs12", "5vs2"), font=2)
  axis(2,at=c(0, 0.25, 0.5, 0.75, 1),labels=c("0", "0.25", "0.5", "0.75", "1"),las=1)
  text(0.72,(Parejas_A[1]-.07),paste(Parejas_A[1]),cex=.9,col='black',f=2, srt=90)
  text(1.9,(Parejas_A[2]-.07),paste(Parejas_A[2]),cex=.9,col='white',f=2, srt=90)
  text(3.08,(Parejas_A[3]-.07),paste(Parejas_A[3]),cex=.9,col='black',f=2, srt=90)
  text(4.26,(Parejas_A[4]-.07),paste(Parejas_A[4]),cex=.9,col='white',f=2, srt=90)
  text(5.5,(Parejas_A[5]-.07),paste(Parejas_A[5]),cex=.9,col='black',f=2, srt=90)
  text(6.67,(Parejas_A[6]-.07),paste(Parejas_A[6]),cex=.9,col='white',f=2, srt=90)
  text(7.9,(Parejas_A[7]-.07),paste(Parejas_A[7]),cex=.9,col='black',f=2, srt=90)
  text(9.1,(Parejas_A[8]-.07),paste(Parejas_A[8]),cex=.9,col='white',f=2, srt=90)
  lines(c(5.7, 7.3),c(1,1), lwd=3, lty=1, col="deepskyblue4")
  lines(c(0.7, 2.3),c(1,1), lwd=3, lty=1, col="cadetblue2")
  text(2.5, 1, labels="Baseline", offset=0, cex = 0.9, pos=4)
  text(7.5, 1, labels="Magnitud", offset=0, cex = 0.9, pos=4)
  mtext("A'",3,cex=3.5, line=1, f=2)
  
  barplot(Parejas_B, main = "", xlab = "", ylab = "", font.lab=2, ylim = c(-1,1.05), axes = FALSE, col =c("darkseagreen3", "darkseagreen4"))
  axis(1,at=c(1.3,3.7,6.1,8.5),labels=c("1vs4", "2vs8", "3vs12", "5vs2"), font=2)
  axis(2,at=c(0, -0.5, 0.5, -1, 1),labels=c("0", "-0.5", "0.5", "-1","1"),las=1)
  text(0.72,(Parejas_B[1]+.07),paste(Parejas_B[1]),cex=.9,col='black',f=2, srt=90)
  text(1.9,(Parejas_B[2]+.07),paste(Parejas_B[2]),cex=.9,col='black',f=2, srt=90)
  text(3.08,(Parejas_B[3]+.07),paste(Parejas_B[3]),cex=.9,col='black',f=2, srt=90)
  text(4.26,(Parejas_B[4]+.07),paste(Parejas_B[4]),cex=.9,col='black',f=2, srt=90)
  text(5.5,(Parejas_B[5]+.07),paste(Parejas_B[5]),cex=.9,col='black',f=2, srt=90)
  text(6.67,(Parejas_B[6]+(Parejas_B[6]/3)),paste(Parejas_B[6]),cex=.9,col='black',f=2)
  text(7.9,(Parejas_B[7]+(Parejas_B[7]/3)),paste(Parejas_B[7]),cex=.9,col='black',f=2)
  text(9.1,(Parejas_B[8]+(Parejas_B[8]/3)),paste(Parejas_B[8]),cex=.9,col='black',f=2)
  lines(c(5.7, 7.3),c(1,1), lwd=3, lty=1, col="darkseagreen4")
  lines(c(0.7, 2.3),c(1,1), lwd=3, lty=1, col="darkseagreen3")
  text(2.5, 1, labels="Baseline", offset=0, cex = 0.9, pos=4)
  text(7.5, 1, labels="Magnitud", offset=0, cex = 0.9, pos=4)
  mtext("B'",3,cex=3.5, line=1, f=2)
  mtext("All subjects",4,cex=2, line=1, f=2)
