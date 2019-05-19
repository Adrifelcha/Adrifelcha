#Islas Farias Jaime Osvaldo
rm(list=ls())

#Tarea 2: Obtener promedios de la media (esperanza) y la varianza de las 4 distribuciones vistas 
#en clase, haciendo 100 realizaciones con parámetros inventados.

#distribución binomial--------------------------------------------------------------------------
n<-500                               #n inventada
p<-.7                                #p inventada   
supbinom<-0:n                        #soporte
distbinom<-dbinom(supbinom,n,p)      #distribución binomial

#se obtiene la media mediante su fórmula
medbinom<-n*p
#se obtiene la media mediante 100 ensayos aleatorios
rmedbinom<-mean(rbinom(100,n,p))

#se obtiene la varianza mediante su fórmula
varbinom<-n*p*(1-p)
#se obtiene la varianza mediante 100 ensayos aleatorios
rvarbinom<-var(rbinom(100,n,p))

#resultados
plot(supbinom,distbinom,type="h")                      #gráfica
title(main="Distribución Binomial")
text(150,0.035,paste("media fórmula = ",medbinom))
text(150,0.030,paste("media ensayos = ",rmedbinom))
text(150,0.015,paste("varianza fórmula = ",varbinom))
text(150,0.010,paste("varianza ensayos = ",rvarbinom))



#distribución poisson-------------------------------------------------------------------------
suppois<-0:100                          #soporte
lambda<-23                              #lambda inventada
distpois<-dpois(suppois,lambda)         #distribución poisson

#se obtiene la media mediante su fórmula
medpos<-lambda
#se obtiene la media mediante 100 ensayos aleatorios
rmedpos<-mean(rpois(100,lambda))

#se obtiene la varianza mediante su fórmula
varpos<-lambda
#se obtiene la varianza mediante 100 ensayos aleatorios
rvarpos<-var(rpois(100,lambda))

#resultados
plot(suppois,distpois,type="h")                       #gráfica
title(main="Distribución Poisson")
text(60,0.07,paste("media fórmula = ",medpos))
text(60,0.06,paste("media ensayos = ",rmedpos))
text(60,0.04,paste("varianza fórmula = ",varpos))
text(60,0.03,paste("varianza ensayos = ",rvarpos))



#distribución exponencial-----------------------------------------------------------------------
supexp<-seq(0,20,.1)                              #soporte
lambda2<-.7                                       #lambda inventada
distexp<-dexp(supexp,lambda2)                     #distribución exponencial

#se obtiene la media mediante su fórmula
medexp<-lambda2^(-1)
#se obtiene la media mediante 100 ensayos aleatorios
rmedexp<-mean(rexp(100,lambda2))

#se obtiene la varianza mediante su fórmula
varexp<-lambda2^(-2)
#se obtiene la varianza mediante 100 ensayos aleatorios
rvarexp<-var(rexp(100,lambda2))

#resultados
plot(supexp,distexp,type="l")                                #gráfica
title(main="Distribución Exponencial")
text(10,0.6,paste("media fórmula = ",medexp))
text(10,0.5,paste("media ensayos = ",rmedexp))
text(10,0.3,paste("varianza fórmula = ",varexp))
text(10,0.2,paste("varianza ensayos = ",rvarexp))



#distribución normal----------------------------------------------------------------------------
supnorm<-0:100                        #soporte
mu<-32                                #mu inventada
dist<-6                               #distribución estándar inventada
distnorm<-dnorm(supnorm,mu,dist)      #distribución normal

#se obtiene la media mediante su fórmula
mednorm<-mu
#se obtiene la media mediante 100 ensayos aleatorios
rmednorm<-mean(rnorm(100,mu,dist))

#se obtiene la varianza mediante su fórmula
varnorm<-dist^2
#se obtiene la varianza mediante 100 ensayos aleatorios
rvarnorm<-var(rnorm(100,mu,dist))

#redondeos (para que se vea 'nice')
rmednorm<-round(rmednorm,3)
rvarnorm<-round(rvarnorm,3)

#resultados
plot(supnorm,distnorm,type="l")                                #gráfica
title(main="Distribución Normal")
text(70,0.06,paste("media fórmula = ",mednorm))
text(70,0.05,paste("media ensayos = ",rmednorm))
text(70,0.03,paste("varianza fórmula = ",varnorm))
text(70,0.02,paste("varianza ensayos = ",rvarnorm))
