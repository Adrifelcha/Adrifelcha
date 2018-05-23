###################################################
# Teoría de las muestras grandes
# por Adriana F. Chávez
# adrifelcha@gmail.com
###################################################

#La teoría de las muestras grandes está compuesta por la Ley de los Grandes Números y el Teorema del Límite Central
#Segun los cuales: 
#a) El valor de la media muestral se aproxima cada vez más al valor de la media poblacional conforme la muestra se acerca al infinito
#b) Los estimadores obtenidos en un número X de muestras, presentan valores que se distribuyen de manera normal cuando X tiende a infinito.



##################################



# Distribución  N O R M A L
####################################
####################################

#Generamos tres muestras con distinto tamaño
n_peque <- rnorm(5,0,1)  
n_media <- rnorm(20,0,1)
n_grande <- rnorm(300,0,1)

ns <- data.frame(round(cbind(mean(n_peque),mean(n_media), mean(n_grande)),3))
colnames(ns) <- c("Pequeña","Media","Grande")
print(ns)

peques<- c(NULL)
medias<- c(NULL)
grandes<- c(NULL)

for(i in 1:10){
peques[i]<- mean(rnorm(5,0,1))
medias[i]<- mean(rnorm(20,0,1))
grandes[i]<- mean(rnorm(300,0,1))
}

cbind(peques,medias,grandes)

cbind(mean(peques),mean(medias),mean(grandes))







# Distribución  P O I S S O N
####################################
####################################
n_peque <- rpois(5,10)
n_media <- rpois(20,10)
n_grande <- rpois(300,10)

ns <- data.frame(round(cbind(mean(n_peque),mean(n_media), mean(n_grande)),3))
colnames(ns) <- c("Pequeña","Media","Grande")
print(ns)

peques<- c(NULL)
medias<- c(NULL)
grandes<- c(NULL)

for(i in 1:10){
  peques[i]<- mean(rpois(5,10))
  medias[i]<- mean(rpois(20,10))
  grandes[i]<- mean(rpois(300,10))
}

cbind(peques,medias,grandes)

cbind(mean(peques),mean(medias),mean(grandes))




# Distribución  Exponencial
####################################
####################################
n_peque <- rexp(5,10)
n_media <- rexp(20,10)
n_grande <- rexp(300,10)

ns <- data.frame(round(cbind(mean(n_peque),mean(n_media), mean(n_grande)),3))
colnames(ns) <- c("Pequeña","Media","Grande")
print(ns)

peques<- c(NULL)
medias<- c(NULL)
grandes<- c(NULL)

for(i in 1:10){
  peques[i]<- mean(rexp(5,10))
  medias[i]<- mean(rexp(20,10))
  grandes[i]<- mean(rexp(300,10))
}

cbind(peques,medias,grandes)

1/10
cbind(mean(peques),mean(medias),mean(grandes))



#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
# Teorema del Lìmite central


####### Variable aleatoria (~Normal)
v_normal <- c(NA)
for(i in 1:5000){
v_normal[i] <- mean(rnorm(500,0,1))  
}
hist(v_normal,breaks=20, xlim=c(-0.2,0.2), main="Variable Normal", col="turquoise")


####### Variable aleatoria (~Binom)
v_binom <- c(NA)
for(i in 1:5000){
v_binom[i] <- mean(rbinom(500,500,0.5))  
}
hist(v_binom, main="Variable Binomial", breaks=20, col="pink")

###### Variable aleatoria (~Poisson)
v_pois <- c(NA)
for(i in 1:5000){
v_pois[i] <- mean(rpois(500,10))
}
hist(v_pois, main="Variable Poisson", breaks=50, col="lightgreen")

###### Variable aleatoria (~Exponencial)
v_exp <- c(NA)
for(i in 1:50000){
v_exp[i] <- mean(rexp(500,10))
}
hist(v_exp, main="Variable Exponencial", breaks=50, col="indianred3")
