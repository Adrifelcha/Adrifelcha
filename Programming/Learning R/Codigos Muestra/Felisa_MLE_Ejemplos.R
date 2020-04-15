#Paquetes de interes: likelihood + maxLik

maxLik(logLik, start)
#(logLik) -> Function tat calculates the log-likelihood as a function of the parameter (usually a vector)
#(start) -> A vector of starting values

##########################

rm(list=ls())

#Ejemplo 1: Likelihood de distribucion binomial a partir de un conjunto de datos X

library(maxLik)

#First: We generate a vector of data (x)

#random values unique to a specific seed. It ensures reproducibility)
set.seed(123)
x<-rbinom(100,n=100,prob=.3)

logLikFun <- function(param) {
 #casos <-param[2]
 w <-param
 sum(dbinom(x,100, prob=w, log= TRUE))
}

mle<- maxLik(logLik=logLikFun, start=c(w=0.1))
summary(mle)

#########################

rm(list=ls())

#Ejemplo 2: Power vs Exponential functions on Forgetting data 

#Power -> X se eleva a una potencia fija
#Exponential -> x es el exponente

library(maxLik)

#Escribimos nuestros datos
t<-c(1,3,6,9,12,18)
m<-6
y<-c(.94, .77, .40, .26, .24, .16)
n<-100
x<-y*n

plot(t,y,xlab='Proporcion de respuestas correctas',ylab='Tiempo (segundos)')
#So far: Datos
#So far: Predicci??n de nuestros modelos segun MLE


