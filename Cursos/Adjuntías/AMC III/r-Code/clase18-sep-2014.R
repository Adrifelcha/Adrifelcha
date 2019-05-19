lamda=.5
spois=0:100
pois= dpois(spois, lamda)
plot(spois, pois, type="h")
abline(v=lamda, col="red")
poisac<- ppois(spois, lamda)
plot(spois, poisac, type="s")

#binomial
n=1000
p= .4
sbinom=0:n
binomd=dbinom(sbinom, n, p)
plot(sbinom, binomd, type="h")
mean(rbinom(2, 100, .4))
#objetivo p(30)
dbinom(30, n, p)

#normal
mu= n*p
sigma= sqrt(n*p*(1-p))
snorm=seq(0,n, .1)
normd= dnorm(snorm, mu, sigma)
lines(snorm, normd, col="red")
#aproximación
pnorm(30.5, mu, sigma)
pnorm(29.5, mu, sigma)
pnorm(30.5, mu, sigma)-pnorm(29.5, mu, sigma)
#exponencial
sexp= seq(0,100,.1)
lambda= 1/20
expo= dexp(sexp, lambda)
plot(sexp, expo, type="l")

expac<- pexp(sexp, lambda)
plot(sexp, expac, type="s")

#uniforme
sunif
