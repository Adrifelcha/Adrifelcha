#Islas Farias Jaime Osvaldo
rm(list=ls())

#Tarea 1: Encontrar la probabilidad p(x=500) en una distribución binomial con n=1000 y p=0.4
#usando una distribución normal

#distribucion binomial
n=1000
p=.4

supbinom<-0:n                            #soporte
distbinom<-dbinom(supbinom,n,p)          #distribución binomial
plot(supbinom,distbinom,type="h")        #gráfica

#distribución normal
mu<-n*p                                  #media
sigma<-sqrt(n*p*(1-p))                   #desviación estándar
supnorm<-seq(0,1000,0.1)                 #soporte
distnorm<-dnorm(supnorm,mu,sigma)        #distribución normal
plot(supnorm,distnorm,type="l")          #gráfica


plot(supbinom,distbinom,type="h")        #gráficas sobrepuestas
lines(supnorm,distnorm,col="red")

#objetivo con distribución binomial
a<-dbinom(500,n,p)

#aproximación por distribución normal
b<-pnorm(500.5,mu,sigma)-pnorm(499.5,mu,sigma)

#resultados
text(550,0.020,paste("Binomial = ",a))
text(550,0.015,paste("Normal = ",b),col="red")