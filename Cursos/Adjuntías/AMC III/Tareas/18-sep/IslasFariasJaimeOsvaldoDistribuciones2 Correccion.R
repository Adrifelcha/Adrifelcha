#Islas Farias Jaime Osvaldo
rm(list=ls())

#Tarea 2: Obtener promedios de la media (esperanza) y la varianza de las 4 distribuciones vistas 
#en clase, haciendo 100 realizaciones con par?metros inventados.

#distribuci?n binomial--------------------------------------------------------------------------
n<-500                               #n inventada
p<-.7                                #p inventada   
supbinom<-0:n                        #soporte
distbinom<-dbinom(supbinom,n,p)      #distribuci?n binomial

#se obtiene la media mediante su f?rmula
medbinom<-n*p
#se obtiene la media mediante 100 ensayos aleatorios
rmedbinom<-mean(rbinom(100,n,p))

#se obtiene la varianza mediante su f?rmula
varbinom<-n*(p*(1-p))
#se obtiene la varianza mediante 100 ensayos aleatorios
rvarbinom<-var(rbinom(100,n,p))

#resultados
plot(supbinom,distbinom,type="h")                      #gr?fica
title(main="Distribuci?n Binomial")
text(150,0.035,paste("media f?rmula = ",medbinom))
text(150,0.030,paste("media ensayos = ",rmedbinom))
text(150,0.015,paste("varianza f?rmula = ",varbinom))
text(150,0.010,paste("varianza ensayos = ",rvarbinom))



#distribuci?n poisson-------------------------------------------------------------------------
suppois<-0:100                          #soporte
lambda<-23                              #lambda inventada
distpois<-dpois(suppois,lambda)         #distribuci?n poisson

#se obtiene la media mediante su f?rmula
medpos<-lambda
#se obtiene la media mediante 100 ensayos aleatorios
rmedpos<-mean(rpois(100,lambda))

#se obtiene la varianza mediante su f?rmula
varpos<-lambda
#se obtiene la varianza mediante 100 ensayos aleatorios
rvarpos<-var(rpois(100,lambda))

#resultados
plot(suppois,distpois,type="h")                       #gr?fica
title(main="Distribuci?n Poisson")
text(60,0.07,paste("media f?rmula = ",medpos))
text(60,0.06,paste("media ensayos = ",rmedpos))
text(60,0.04,paste("varianza f?rmula = ",varpos))
text(60,0.03,paste("varianza ensayos = ",rvarpos))



#distribuci?n exponencial-----------------------------------------------------------------------
supexp<-seq(0,20,.1)                              #soporte
lambda2<-.7                                       #lambda inventada
distexp<-dexp(supexp,lambda2)                     #distribuci?n exponencial

#se obtiene la media mediante su f?rmula
medexp<-lambda2^(-1)
#se obtiene la media mediante 100 ensayos aleatorios
rmedexp<-mean(rexp(100,lambda2))

#se obtiene la varianza mediante su f?rmula
varexp<-lambda2^(-2)
#se obtiene la varianza mediante 100 ensayos aleatorios
rvarexp<-var(rexp(100,lambda2))

#resultados
plot(supexp,distexp,type="l")                                #gr?fica
title(main="Distribuci?n Exponencial")
text(10,0.6,paste("media f?rmula = ",medexp))
text(10,0.5,paste("media ensayos = ",rmedexp))
text(10,0.3,paste("varianza f?rmula = ",varexp))
text(10,0.2,paste("varianza ensayos = ",rvarexp))



#distribuci?n normal----------------------------------------------------------------------------
supnorm<-0:100                        #soporte
mu<-32                                #mu inventada
dist<-6                               #distribuci?n est?ndar inventada
distnorm<-dnorm(supnorm,mu,dist)      #distribuci?n normal

#se obtiene la media mediante su f?rmula
mednorm<-mu
#se obtiene la media mediante 100 ensayos aleatorios
rmednorm<-mean(rnorm(1000,mu,dist))

#se obtiene la varianza mediante su f?rmula
varnorm<-dist^2
#se obtiene la varianza mediante 100 ensayos aleatorios
rvarnorm<-var(rnorm(1000,mu,dist))

#redondeos (para que se vea 'nice')
rmednorm<-round(rmednorm,3)
rvarnorm<-round(rvarnorm,3)

#resultados
plot(supnorm,distnorm,type="l")                                #gr?fica
title(main="Distribuci?n Normal")
text(70,0.06,paste("media f?rmula = ",mednorm))
text(70,0.05,paste("media ensayos = ",rmednorm))
text(70,0.03,paste("varianza f?rmula = ",varnorm))
text(70,0.02,paste("varianza ensayos = ",rvarnorm))
