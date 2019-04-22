layout(matrix(1:1,ncol=1))
datos <- tauH

x_axis <- NULL
y_axis <- NULL
numero <- 0
media_post <- NULL
Savage_Dickey <- NULL
color_SD <- NULL
for(i in 1:ncol(datos)){
  numero <- numero+1
  a <- sample(datos[,i],1000)
  espacio_init <- ((numero-1) * length(a)) + 1
  espacio_fin <- numero * length(a)
  y_axis[espacio_init:espacio_fin] <- a
  media_post[i] <- mean(datos[,i])
  Savage_Dickey[i] <- dnorm(0,0,1)/dnorm(0,mean(datos[,i]),sd(datos[,i]))
  
  ifelse(Savage_Dickey[i] == 0, color_SD[i] <- "black",
         ifelse(Savage_Dickey[i] >= 1, color_SD[i] <- "green",
          color_SD[i]<- "indianred1"))
}

numero <- 0
for(i in 1:ncol(datos)){
  numero <- numero+1
  b <- rep(numero, 1000)
  espacio_init <- ((numero-1) * length(b)) + 1
  espacio_fin <- numero * length(b)
  x_axis[espacio_init:espacio_fin] <- b
}



numero <- 0
plot(x_axis, y_axis, ann=F, axes=F,cex=0.9)
for(u in 1:20){
numero <- numero + 1
points(numero,media_post[u], col=color_SD[u], pch=16, cex=2, type="p")}
mtext(side=2, text = "Density", line=2.2, cex=1.5)
mtext(side=1, text = "Participants", line=2.2, cex=1.5)
axis(1,c(1:20),c(1:20))
axis(2,seq(0,5,0.5),seq(0,5,0.5))
