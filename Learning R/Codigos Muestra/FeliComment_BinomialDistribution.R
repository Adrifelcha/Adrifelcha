#Binomial distributions
#dbinom(x, size, prob, log = FALSE)
#pbinom(q, size, prob, lower.tail = TRUE, log.p = FALSE)
#qbinom(p, size, prob, lower.tail = TRUE, log.p = FALSE)
#rbinom(n, size, prob)

rm(list=ls())  
#Borrar datos previos

#Probabilidad de y=7 (caras) al tirar una moneda n=10 veces, con p=.7

dbinom(x=7, size=10, prob=0.7)

#Probabilidad de obtener tantos eventos como casos y=n
dbinom(x=0:10, size=10, prob=0.7)

#Probabilidad acumulada (Obtener 7 éxitos o menos)
sum(dbinom(x=0:7, size=10, prob=0.7))

#Survival function: Probabilidad de obtener más de 7 exitos
sum(dbinom(x=8:10, size=10, prob=0.7))

#Evaluando complementariedad
sum(.6172172, .3827828)
