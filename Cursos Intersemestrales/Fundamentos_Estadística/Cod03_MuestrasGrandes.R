###################################################
# Teoría de los grandes números
# por Adriana F. Chávez
# adrifelcha@gmail.com
###################################################



# Distribución  N O R M A L
####################################
####################################
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




# Distribución  P O I S S O N
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

cbind(mean(peques),mean(medias),mean(grandes))

1/10



#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
# Teorema del Lìmite central

v_normal <- rnorm(5000,0,1)
hist(v_normal,breaks=50, main="Variable Normal")

v_binom <- rbinom(5000,500,0.5)
hist(v_binom, main="Variable Binomial", breaks=50)

v_pois <- rpois(5000,10)
hist(v_pois, main="Variable Poisson", breaks=50)


