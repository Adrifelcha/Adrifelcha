#Luján Zurita Perla Alejandra
#binomial + normal
n=1000
p= 0.4
sbinom=0:1000
binomd=dbinom(sbinom, n, p)
plot(sbinom, binomd, type= "h")
mean(rbinom(2, 1000, .4))

#normal
mu= n*p
sigma= sqrt(n*p*(1-p))
snorm= seq(0, n, .1)
normd= dnorm(snorm, mu, sigma)
lines(snorm, normd, type="l", col="red")
#objetivo p(500)
dbinom(500, n, p)
#área bajo la curva (aproximación)
pnorm(499.5, mu, sigma)
pnorm(500.5, mu, sigma)
pnorm(499.5, mu, sigma)-pnorm(500.5, mu, sigma)