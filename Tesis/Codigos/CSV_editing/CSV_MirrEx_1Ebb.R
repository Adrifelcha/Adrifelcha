setwd("C:/Users/Adriana/Desktop/Felisa/Tesis/Datos_CSVs/Datos_MirrExp_1Ebb")

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
  color <- NULL
  tipo <- NULL
  choice <- NULL
  Exito <- NULL
  outcome <- NULL
  
  
  outcome[felisa$Rechazos=='True'] <- 3
  outcome[felisa$Hits=='True'] <- 4
  outcome[felisa$Falsas.alarmas=='True'] <- 1
  outcome[felisa$Omisiones=='True'] <-2
  
  facilidad[felisa$Estimulo<=320] <- 'pocos'
  facilidad[felisa$Estimulo>320] <- 'muchos'
  
  choice[felisa$Respuesta=='n'] <- '0'
  choice[felisa$Respuesta=='s'] <- '1'
  
  Exito[felisa$Correcto=='True'] <- '1'
  Exito[felisa$Correcto=='False'] <- '0'

  
  signal[(felisa$Estimulo>=1&felisa$Estimulo<=160)|(felisa$Estimulo>=321&felisa$Estimulo<=480)] <- 'senal'
  signal[(felisa$Estimulo>=161&felisa$Estimulo<=320)|(felisa$Estimulo>=481&felisa$Estimulo<=640)] <- 'ruido'
  
  tamano_central[(felisa$Estimulo>=161&felisa$Estimulo<=200)|(felisa$Estimulo>=481&felisa$Estimulo<=520)] <- '3'
  tamano_central[(felisa$Estimulo>=201&felisa$Estimulo<=240)|(felisa$Estimulo>=521&felisa$Estimulo<=560)] <- '2.5'
  tamano_central[(felisa$Estimulo>=1&felisa$Estimulo<=40)|(felisa$Estimulo>=321&felisa$Estimulo<=360)] <- '2_o2'
  tamano_central[(felisa$Estimulo>=41&felisa$Estimulo<=80)|(felisa$Estimulo>=361&felisa$Estimulo<=400)] <- '2_o3'
  tamano_central[(felisa$Estimulo>=81&felisa$Estimulo<=120)|(felisa$Estimulo>=401&felisa$Estimulo<=440)] <- '2_u2'
  tamano_central[(felisa$Estimulo>=121&felisa$Estimulo<=160)|(felisa$Estimulo>=441&felisa$Estimulo<=480)] <- '2_u3'
  tamano_central[(felisa$Estimulo>=241&felisa$Estimulo<=280)|(felisa$Estimulo>=561&felisa$Estimulo<=600)] <- '1.5'
  tamano_central[(felisa$Estimulo>=281&felisa$Estimulo<=320)|(felisa$Estimulo>=601&felisa$Estimulo<=640)] <- '1'
  
  
  
  
  #pos_externos_grandes[felisa$Estimulo%%2==1] <- 'derecha' #nones
  #pos_externos_grandes[felisa$Estimulo%%2==0] <- 'izquierda'
  num_ext[(felisa$Estimulo>=1&felisa$Estimulo<=40)|(felisa$Estimulo>=81&felisa$Estimulo<=120)|(felisa$Estimulo>=161&felisa$Estimulo<=170)|(felisa$Estimulo>=181&felisa$Estimulo<=190)|(felisa$Estimulo>=201&felisa$Estimulo<=210)|(felisa$Estimulo>=221&felisa$Estimulo<=230)|(felisa$Estimulo>=241&felisa$Estimulo<=250)|(felisa$Estimulo>=261&felisa$Estimulo<=270)|(felisa$Estimulo>=281&felisa$Estimulo<=290)|(felisa$Estimulo>=301&felisa$Estimulo<=310)] <- '2'
  num_ext[(felisa$Estimulo>=41&felisa$Estimulo<=80)|(felisa$Estimulo>=121&felisa$Estimulo<=160)|(felisa$Estimulo>=171&felisa$Estimulo<=180)|(felisa$Estimulo>=191&felisa$Estimulo<=200)|(felisa$Estimulo>=211&felisa$Estimulo<=220)|(felisa$Estimulo>=231&felisa$Estimulo<=240)|(felisa$Estimulo>=251&felisa$Estimulo<=260)|(felisa$Estimulo>=271&felisa$Estimulo<=280)|(felisa$Estimulo>=291&felisa$Estimulo<=300)|(felisa$Estimulo>=311&felisa$Estimulo<=320)] <- '3'
  num_ext[(felisa$Estimulo>=321&felisa$Estimulo<=360)|(felisa$Estimulo>=401&felisa$Estimulo<=440)|(felisa$Estimulo>=481&felisa$Estimulo<=490)|(felisa$Estimulo>=501&felisa$Estimulo<=510)|(felisa$Estimulo>=521&felisa$Estimulo<=530)|(felisa$Estimulo>=541&felisa$Estimulo<=550)|(felisa$Estimulo>=561&felisa$Estimulo<=570)|(felisa$Estimulo>=581&felisa$Estimulo<=590)|(felisa$Estimulo>=601&felisa$Estimulo<=610)|(felisa$Estimulo>=621&felisa$Estimulo<=630)] <- '7'
  num_ext[(felisa$Estimulo>=361&felisa$Estimulo<=400)|(felisa$Estimulo>=441&felisa$Estimulo<=480)|(felisa$Estimulo>=491&felisa$Estimulo<=500)|(felisa$Estimulo>=511&felisa$Estimulo<=520)|(felisa$Estimulo>=531&felisa$Estimulo<=540)|(felisa$Estimulo>=551&felisa$Estimulo<=560)|(felisa$Estimulo>=571&felisa$Estimulo<=580)|(felisa$Estimulo>=591&felisa$Estimulo<=600)|(felisa$Estimulo>=611&felisa$Estimulo<=620)|(felisa$Estimulo>=631&felisa$Estimulo<=640)] <- '8'

  tam_ext[(felisa$Estimulo>=1&felisa$Estimulo<=80)|(felisa$Estimulo>=161&felisa$Estimulo<=180)|(felisa$Estimulo>=201&felisa$Estimulo<=220)|(felisa$Estimulo>=241&felisa$Estimulo<=260)|(felisa$Estimulo>281&felisa$Estimulo<=300)|(felisa$Estimulo>=321&felisa$Estimulo<=400)|(felisa$Estimulo>=481&felisa$Estimulo<=500)|(felisa$Estimulo>=521&felisa$Estimulo<=540)|(felisa$Estimulo>=561&felisa$Estimulo<=580)|(felisa$Estimulo>=601&felisa$Estimulo<=620)] <- 'over'
  tam_ext[(felisa$Estimulo>=81&felisa$Estimulo<=160)|(felisa$Estimulo>=181&felisa$Estimulo<=200)|(felisa$Estimulo>=221&felisa$Estimulo<=240)|(felisa$Estimulo>=261&felisa$Estimulo<=280)|(felisa$Estimulo>301&felisa$Estimulo<=320)|(felisa$Estimulo>=401&felisa$Estimulo<=480)|(felisa$Estimulo>=501&felisa$Estimulo<=520)|(felisa$Estimulo>=541&felisa$Estimulo<=560)|(felisa$Estimulo>=581&felisa$Estimulo<=600)|(felisa$Estimulo>=621&felisa$Estimulo<=640)] <- 'under'

  ###
  orden_color <- function(tamanos_centrals){
    return(
      data.frame(
        estim=felisa$Estimulo[tamano_central==tamanos_centrals],
        label=rep(c(rep('naranja',2),rep('azul',2),rep('verde',2),rep('purpura',2),rep('guinda',2)),8)[order(order(felisa$Estimulo[tamano_central==tamanos_centrals]))],
        posicion_glob=which(tamano_central==tamanos_centrals)
      )  
    )
  }
  
  for(tam in unique(tamano_central)){
    extra <- orden_color(tam)
    color[extra$posicion_glob] <- as.character(extra$label)
  }
  #####
  
  tipo[(felisa$Estimulo>=1&felisa$Estimulo<=160)] <- '4 AS'
  tipo[(felisa$Estimulo>=321&felisa$Estimulo<=480)] <- '3 BS'
  tipo[(felisa$Estimulo>=161&felisa$Estimulo<=320)] <- '1 AN'
  tipo[(felisa$Estimulo>=481&felisa$Estimulo<=640)] <- '2 BN'
  

    
  felisa$facilidad <- facilidad
  felisa$num_circulos_externos <- num_ext
  felisa$tam_circulos_externos <- tam_ext
  felisa$tamano_central <- tamano_central
  felisa$senal <- signal
  felisa$color <- color
  felisa$tipo <- tipo
  felisa$choice <- choice
  felisa$Exito <- Exito
  felisa$outcome <- outcome
  head(felisa,50)
  
  
  write.csv(felisa,file=archive)
}


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


