#Luján Zurita Perla Alejandra
#binomial
sbinom=800
Theta=.1
size=0:300
dbinom1<- dbinom(size, sbinom, Theta)
plot(size, dbinom1, type="h")
n<- sbinom
p<- Theta
dbinom1<- dbinom(size, n, p)
#media(esperanza)
mbinom<- n*p
#100 ensayos aleatorios
rmbinom<- mean(rbinom(100, n, p))
#varianza
vbinom<- n*p*(1-p)
#100 ensayos aleatorios
rvbinom<- mean(rbinom(100, n, p*(1-p)))
#plot
plot(size, dbinom1, type="h")
text(150,.04,paste("media = ", mbinom))
text(180, .03, paste("media ensayos aleat. = ", rmbinom))
text(150, .02, paste("varianza = ", vbinom))
text(200, .01, paste("varianza ensayos aleat. = ", rvbinom))

#poisson
lambda=60
spois=0:200
dpois= dpois(spois, lambda)
plot(spois, dpois, type="h")
#media
mpois<- lambda
#media 100 ensayos aleatorios
rmpois<-mean(rpois(100,lambda))
#varianza
vpois<- lambda
#varianza 100 ensayos aleatorios
rvpois<- mean(rpois(100, lambda))
#plot
plot(spois, dpois, type="h")
text(130,.04,paste("media = ", mpois))
text(130, .03, paste("media ensayos aleat. = ", rmpois))
text(130, .02, paste("varianza = ", vpois))
text(145, .01, paste("varianza ensayos aleat. = ", rvpois))

#exponencial
sexp=seq(0,100,.1)
lambdaex=.025
dexpo= dexp(sexp, lambdaex)
plot(sexp, dexpo, type="l")
#media
mexp<- lambdaex^(-1)
#media 100 ensayos aleatorios
rmexp<- mean(rexp(100,lambdaex^2))
rmexp<- round(rmexp,3)
#varianza
vexp<- lambdaex^(-2)
#varianza 100 ensayos aleatorios
vrexp<- mean(rexp(100,lambdaex^2))
vrexp<- round (vrexp, 3)
#plot
plot(sexp, dexpo, type="l")
text(40,.02,paste("media = ", mexp))
text(60, .018, paste("media ensayos aleat. = ", rmexp))
text(53, .015, paste("varianza = ", vexp))
text(65, .013, paste("varianza ensayos aleat. = ", vrexp))

#normal
mu<- 28
snorm= -1500:1500
dnorm1= 85 #sigma?
normd= dnorm(snorm, mu, dnorm1)
plot(snorm, normd, type="l")
#media
mnorm<- mu
#media 100 ensayos aleatorios
rmnorm<- mean(rnorm(100,mu,normd))
#varianza
vnorm<- normd^2
#varianza 100 ensayos aleatorios
rvnorm<- mean(rnorm (100,mu,normd^2))
#plot
plot(snorm, normd, type="l")
text(-700,.004,paste("media = ", mnorm))
text(-700, .003, paste("media ensayos aleat. = ", rmnorm))
text(-700, .002, paste("varianza = ", vnorm))
text(-700, .001, paste("varianza ensayos aleat. = ", rvnorm))
