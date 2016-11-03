setwd("~/Desktop/Felisa/Mirror Experiment/Exp-1_DobleEbbinghaus/Data and Plots/Data")
rm(list=ls())


dir()

#archive <-'MirrorEx1a_Elias_2016-05-05_Y_N+R.csv'

for(archive in dir()){
  felisa <- read.csv(archive)
  felisa <- felisa[1:800,]
  # Codificacion Estimulos
  # Estimulo 1-200 senalfacil/AS
  # Estimulo 201-400 ruidofacil/AN
  # Estimulo 401-600 senaldificil/BS
  # Estimulo 601-800 ruidodificil/BN
  
  
  facilidad <- NULL
  senal <- NULL
  tamano_centrales <- NULL
  num_circulos_externos <- NULL
  pos_externos_grandes <- NULL
  
  facilidad[felisa$Estimulo<=400] <- 'pocos'
  facilidad[felisa$Estimulo>400] <- 'muchos'
  
  senal[(felisa$Estimulo>=1&felisa$Estimulo<=200)|(felisa$Estimulo>=401&felisa$Estimulo<=600)] <- 'senal'
  senal[(felisa$Estimulo>=201&felisa$Estimulo<=400)|(felisa$Estimulo>=601&felisa$Estimulo<=800)] <- 'ruido'
  
  tamano_centrales[(felisa$Estimulo>=1&felisa$Estimulo<=40)|(felisa$Estimulo>=401&felisa$Estimulo<=440)] <- '3, 3'
  tamano_centrales[(felisa$Estimulo>=41&felisa$Estimulo<=80)|(felisa$Estimulo>=441&felisa$Estimulo<=480)] <- '2.5, 2.5'
  tamano_centrales[(felisa$Estimulo>=81&felisa$Estimulo<=120)|(felisa$Estimulo>=481&felisa$Estimulo<=520)] <- '2, 2'
  tamano_centrales[(felisa$Estimulo>=121&felisa$Estimulo<=160)|(felisa$Estimulo>=521&felisa$Estimulo<=560)] <- '1.5, 1.5'
  tamano_centrales[(felisa$Estimulo>=161&felisa$Estimulo<=200)|(felisa$Estimulo>=561&felisa$Estimulo<=600)] <- '1, 1'
  
  tamano_centrales[(felisa$Estimulo>=201&felisa$Estimulo<=240)|(felisa$Estimulo>=601&felisa$Estimulo<=640)] <- '2.5, 3'
  tamano_centrales[(felisa$Estimulo>=241&felisa$Estimulo<=280)|(felisa$Estimulo>=641&felisa$Estimulo<=680)] <- '2, 2.5'
  tamano_centrales[(felisa$Estimulo>=281&felisa$Estimulo<=320)|(felisa$Estimulo>=681&felisa$Estimulo<=720)] <- '1.5, 2'
  tamano_centrales[(felisa$Estimulo>=321&felisa$Estimulo<=360)|(felisa$Estimulo>=721&felisa$Estimulo<=760)] <- '1, 1.5'
  tamano_centrales[(felisa$Estimulo>=361&felisa$Estimulo<=400)|(felisa$Estimulo>=761&felisa$Estimulo<=800)] <- '2.5, 1.5'
  
  
  
  pos_externos_grandes[felisa$Estimulo%%2==1] <- 'derecha' #nones
  pos_externos_grandes[felisa$Estimulo%%2==0] <- 'izquierda'
  
  
  orden_externos <- function(tamanos_centrals){
    return(
      data.frame(
        estim=felisa$Estimulo[tamano_centrales==tamanos_centrals],
        label=rep(c(rep('2-2',10),rep('3-3',10),rep('2-3',10),rep('3-2',10)),2)[order(order(felisa$Estimulo[tamano_centrales==tamanos_centrals]))],
        posicion_global=which(tamano_centrales==tamanos_centrals)
      )  
    )
  }
  
  for(tam in unique(tamano_centrales)){
    extra <- orden_externos(tam)
    num_circulos_externos[extra$posicion_global] <- as.character(extra$label)
  }
  
  
  felisa$facilidad <- facilidad
  felisa$num_circulos_externos <- num_circulos_externos
  felisa$pos_externos_grandes <- pos_externos_grandes
  felisa$tamano_centrales <- tamano_centrales
  felisa$senal <- senal
  head(felisa,50)
  
  
  write.csv(felisa,file=archive)
  
}
#is.recursive(felisa)


