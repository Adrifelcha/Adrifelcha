##########################################################
# Codigo base para el análisis de mario obtenidos en el experimento presentado por Pérez et al (2017)
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
# # # # # # # #  Cargamos los mario
####################################
setwd("C:/Users/Adriana/Desktop/Felisa/Proyectos/Mario_BisecciónTemporal") # Directorio de trabajo
rm(list=ls())  #Reseteamos la consola
dir()          #Imprimimos los archivos contenidos en el directorio en la consola
archive_1 <-'Datos_Dummies_4sujetos_.csv'  #Señalamos el archivo que contiene los mario a analizar
archive_2 <-'Datos_Paty.csv'  
mario <- read.csv(archive_1) #Extraemos los mario del archivo
paty <- read.csv(archive_2)



########################################
# # # # # # # #  Especificamos variables
########################################
Mario_LargoEsSignal <- c(5, 20, 33)  #Especificamos cuáles Sujetos estuvieron en el grupo donde LARGO es Señal
Mario_Intermedias <- c('1v4', '2v8')

Sujeto_M <- mario$Sujeto[mario$Sujeto %in% Mario_LargoEsSignal == FALSE & mario$Grupo %in% Mario_Intermedias == TRUE]         #Del archivo 'datos', identificamos los datos en la columna 'Sujeto' como variable Sujeto
Condicion_M <- mario$Grupo[mario$Sujeto %in% Mario_LargoEsSignal == FALSE & mario$Grupo %in% Mario_Intermedias == TRUE]       #Del archivo 'datos', identificamos los datos en la columna 'Grupo' como variable Condición
TipoSesion_M <- mario$Condicion[mario$Sujeto %in% Mario_LargoEsSignal == FALSE & mario$Grupo %in% Mario_Intermedias == TRUE]  #etc, etc, etc
Dia_M <- mario$Día[mario$Sujeto %in% Mario_LargoEsSignal == FALSE & mario$Grupo %in% Mario_Intermedias == TRUE]
Hits_M <- mario$Corto_enCorto[mario$Sujeto %in% Mario_LargoEsSignal == FALSE & mario$Grupo %in% Mario_Intermedias == TRUE]
FA_M <- mario$Corto_enLargo[mario$Sujeto %in% Mario_LargoEsSignal == FALSE & mario$Grupo %in% Mario_Intermedias == TRUE]
CRej_M <- mario$Largo_enLargo[mario$Sujeto %in% Mario_LargoEsSignal == FALSE & mario$Grupo %in% Mario_Intermedias == TRUE]
Miss_M <- mario$Largo_enCorto[mario$Sujeto %in% Mario_LargoEsSignal == FALSE & mario$Grupo %in% Mario_Intermedias == TRUE]
Noise_M <- mario$EnsayosLargos[mario$Sujeto %in% Mario_LargoEsSignal == FALSE & mario$Grupo %in% Mario_Intermedias == TRUE]
Signal_M <- mario$EnsayosCortos[mario$Sujeto %in% Mario_LargoEsSignal == FALSE & mario$Grupo %in% Mario_Intermedias == TRUE]


Sujeto_P <- paty$sujeto[paty$grupo %in% Mario_Intermedias == TRUE]         #Del archivo 'datos', identificamos los datos en la columna 'Sujeto' como variable Sujeto
Condicion_P <- paty$grupo[paty$grupo %in% Mario_Intermedias == TRUE]       #Del archivo 'datos', identificamos los datos en la columna 'Grupo' como variable Condición
TipoSesion_P <- paty$condición[paty$grupo %in% Mario_Intermedias == TRUE]  #etc, etc, etc
Dia_P <- paty$dia[paty$grupo %in% Mario_Intermedias == TRUE]
Hits_P <- paty$hit[paty$grupo %in% Mario_Intermedias == TRUE]
FA_P <- paty$fa[paty$grupo %in% Mario_Intermedias == TRUE]
CRej_P <- paty$rechazo[paty$grupo %in% Mario_Intermedias == TRUE]
Miss_P <- paty$miss[paty$grupo %in% Mario_Intermedias == TRUE]
Noise_P <- paty$ensayos_largo[paty$grupo %in% Mario_Intermedias == TRUE]
Signal_P <- paty$ensayos_cortos[paty$grupo %in% Mario_Intermedias == TRUE]

TotalSujetos_M <- length(unique(Sujeto_M))
TotalSujetos_P <- length(unique(Sujeto_P))

Sesiones <- c(rep('LB',10), rep('M',10))







###################################           GRAFICO 3
###################################           Grafica de Barras comparando A' y B'' 
###################################           en Linea Base vs Magnitud, en cada condición
###################################           PROMEDIANDO TODOS LOS SUJETOS

layout(matrix(1:2,ncol=2, byrow=TRUE))

Par_A_LBM <- NULL
Par_A_M <- NULL
Par_B_LBM <- NULL
Par_B_M <- NULL

Par_A_LBP <- NULL
Par_A_Pre <- NULL
Par_B_LBP <- NULL
Par_B_Pre <- NULL


#Ciclo para Mario
for(a in sort(unique(Condicion_M))){
  print(c('========> Magnitud:', a))
  for(b in sort(unique(TipoSesion_M))){
    M_Sesion <- b
    M_Hits <- sum(Hits_M[Condicion_M==a&TipoSesion_M==b])
    M_FA <- sum(FA_M[Condicion_M==a&TipoSesion_M==b]) 
    M_Signal <- sum(Signal_M[Condicion_M==a&TipoSesion_M==b])
    M_Noise <- sum(Noise_M[Condicion_M==a&TipoSesion_M==b])
    M_Hrate <- M_Hits/M_Signal
    M_FArate <- M_FA/M_Noise
    if(M_FArate > M_Hrate){
      M_A <- 0.5- ( ((M_FArate-M_Hrate)*(1+M_FArate-M_Hrate)) / ((4*M_FArate)*(1-M_Hrate)) )
    } else {
      M_A <- 0.5+ ( ((M_Hrate-M_FArate)*(1+M_Hrate-M_FArate)) / ((4*M_Hrate)*(1-M_FArate)) )}
    if(M_FArate > M_Hrate){
      M_B <- (((M_FArate*(1-M_FArate))-(M_Hrate*(1-M_Hrate)))/((M_FArate*(1-M_FArate))+(M_Hrate*(1-M_Hrate))))
    } else {
      M_B <- (((M_Hrate*(1-M_Hrate))-(M_FArate*(1-M_FArate)))/((M_Hrate*(1-M_Hrate))+(M_FArate*(1-M_FArate))))}
    
    M_A <- round(M_A,3)
    M_B <- round(M_A,3)
    M_Hrate <- round(M_Hrate,3)
    M_FArate <- round(M_FArate,3)
    
    valores_P<- data.frame(cbind(b, M_Hrate, M_FArate, M_A, M_B))   #Acomodamos los valores en un arreglo
    colnames(valores_P) <- c("Sesion",'Hits', 'FA', "A'", "B'") #, "D'","A_d'","A'","Beta", "C", "B''")
    print(valores_P)
    
    if(b=='LB'){
      Par_A_LBM[a] <- M_A
      Par_B_LBM[a] <- M_B
    } else {
      Par_A_M[a] <- M_A
      Par_B_M[a] <- M_B
    }}}

#Ciclo para PAty
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
    if(FA_rate > H_rate){
      A_ <- 0.5- ( ((FA_rate-H_rate)*(1+FA_rate-H_rate)) / ((4*FA_rate)*(1-H_rate)) )
    } else {
      A_ <- 0.5+ ( ((H_rate-FA_rate)*(1+H_rate-FA_rate)) / ((4*H_rate)*(1-FA_rate)) )}
    if(FA_rate > H_rate){
      B_ <- (((FA_rate*(1-FA_rate))-(H_rate*(1-H_rate)))/((FA_rate*(1-FA_rate))+(H_rate*(1-H_rate))))
    } else {
      B_ <- (((H_rate*(1-H_rate))-(FA_rate*(1-FA_rate)))/((H_rate*(1-H_rate))+(FA_rate*(1-FA_rate))))}
    
    A_ <- round(A_,3)
    B_ <- round(B_,3)
    H_rate <- round(H_rate,3)
    FA_rate <- round(FA_rate,3)
    
    valores_P<- data.frame(cbind(b, H_rate, FA_rate, A_, B_))   #Acomodamos los valores en un arreglo
    colnames(valores_P) <- c("Sesion",'Hits', 'FA', "A'", "B'") #, "D'","A_d'","A'","Beta", "C", "B''")
    print(valores_P)
    
    if(b=='LB'){
      Par_A_LBP[a] <- A_
      Par_B_LBP[a] <- B_
    } else {
      Par_A_Pre[a] <- A_
      Par_B_Pre[a] <- B_
    }}}


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
text(7.5, 1, labels="Pre-Fed", offset=0, cex = 0.9, pos=4)
mtext("A'",3,cex=3.5, line=1, f=2)

barplot(Parejas_B, main = "", xlab = "", ylab = "", font.lab=2, ylim = c(-1,1.05), axes = FALSE, col =c("darkseagreen3", "darkseagreen4"))
axis(1,at=c(1.3,3.7,6.1,8.5),labels=c("1vs4", "2vs8", "3vs12", "5vs2"), font=2)
axis(2,at=c(0, -0.5, 0.5, -1, 1),labels=c("0", "-0.5", "0.5", "-1","1"),las=1)
text(0.72,0.5,paste(Parejas_B[1]),cex=.9,col='black',f=2, srt=90)
text(1.9,0.5,paste(Parejas_B[2]),cex=.9,col='black',f=2, srt=90)
text(3.08,0.5,paste(Parejas_B[3]),cex=.9,col='black',f=2, srt=90)
text(4.26,0.5,paste(Parejas_B[4]),cex=.9,col='black',f=2, srt=90)
text(5.5,0.5,paste(Parejas_B[5]),cex=.9,col='black',f=2, srt=90)
text(6.67,0.5,paste(Parejas_B[6]),cex=.9,col='black',f=2, srt=90)
text(7.9,0.5,paste(Parejas_B[7]),cex=.9,col='black',f=2, srt=90)
text(9.1,0.5,paste(Parejas_B[8]),cex=.9,col='black',f=2, srt=90)
lines(c(5.7, 7.3),c(1,1), lwd=3, lty=1, col="darkseagreen4")
lines(c(0.7, 2.3),c(1,1), lwd=3, lty=1, col="darkseagreen3")
text(2.5, 1, labels="Baseline", offset=0, cex = 0.9, pos=4)
text(7.5, 1, labels="Pre-Fed", offset=0, cex = 0.9, pos=4)
mtext("B'",3,cex=3.5, line=1, f=2)
mtext("ALL subjects",4,cex=2, line=1, f=2)


##############           GRAFICO 5
###################################           Grafica de Barras comparando A' y B'' 
###################################           en Linea Base vs Magnitud, en cada condición
###################################           PROMEDIANDO TODOS LOS SUJETOS
###################################           Una Gráfica por Condición

layout(matrix(1:4,ncol=2, byrow=TRUE))

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
      Par_A_LB <- A_
      Par_B_LB <- B_
    } else {
      Par_A_M <- A_
      Par_B_M <- B_
    }}
  
  Parejas_A <- c(rbind(Par_A_LB, Par_A_M))
  Parejas_B <- c(rbind(Par_B_LB, Par_B_M))
  
  barplot(Parejas_A, main = "", xlab = "", ylab = "", font.lab=2, ylim = c(0,1), axes = FALSE, col =c("cadetblue2", "deepskyblue4"))
  axis(1,at=c(0.72,1.9),labels=c("Baseline", "Magnitud"), font=2)
  axis(2,at=c(0, 0.25, 0.5, 0.75, 1),labels=c("0", "0.25", "0.5", "0.75", "1"),las=1)
  text(0.72,(Parejas_A[1]/2),paste(Parejas_A[1]),cex=.9,col='black',f=2)
  text(1.9,(Parejas_A[2]/2),paste(Parejas_A[2]),cex=.9,col='white',f=2)
  mtext("A'",1,cex=1.3, line=3, f=2)
  
  barplot(Parejas_B, main = "", xlab = "", ylab = "", font.lab=2, ylim = c(-1,1), axes = FALSE, col =c("darkseagreen3", "darkseagreen4"))
  axis(1,at=c(0.72,1.9),labels=c("Baseline", "Magnitud"), font=2)
  axis(2,at=c(0, -0.5, 0.5, -1, 1),labels=c("0", "-0.5", "0.5", "-1","1"),las=1)
  text(0.72,(Parejas_B[1]/2),paste(Parejas_B[1]),cex=.9,col='black',f=2)
  text(1.9,(Parejas_B[2]/2),paste(Parejas_B[2]),cex=.9,col='white',f=2)
  mtext("B''",1,cex=1.5, line=3, f=2)
  mtext(a,4,cex=1.3, line=1, f=2)
  title(paste("All Subjects"), outer = TRUE, line = -2)}






