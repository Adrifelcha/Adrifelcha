###################################################
# Màxima Verosimilitud
# Mètodo de los momentos y Mìnimos Cuadrados
###################################################

plot(c(1:100), dbinom(c(1:100), 100, .1), type='l', ylim=c(0,.14), main="p(x | n=10, p)", cex.main=2)
lines(c(1:100), dbinom(c(1:100), 100, .2))
lines(c(1:100), dbinom(c(1:100), 100, .3))
lines(c(1:100), dbinom(c(1:100), 100, .4))
lines(c(1:100), dbinom(c(1:100), 100, .5))
lines(c(1:100), dbinom(c(1:100), 100, .6))
lines(c(1:100), dbinom(c(1:100), 100, .7))
lines(c(1:100), dbinom(c(1:100), 100, .8))
lines(c(1:100), dbinom(c(1:100), 100, .9))

###################################
# Ejemplos del capìtulo
###################################

#### Ejemplo 1: Funciòn Weibull (Un parámetro)
x <- c(2,7,3)
n <- length(x)
Mean <- mean(x)

m <- seq(0,10,.01)
densidad_Muestral <- function(lambda_1) (1/lambda_1)*(exp(-((m)/(lambda_1))))
plot(y, densidad_Muestral)

l <- function(lambda) (-n*log(lambda)) - ((n*Mean)/(lambda))
lMax <- optimize(l, c(0, 10), maximum=TRUE)
print(lMax)




#### Ejemplo 2:  Distribucion Normal (Màs de un paràmetro)
n <- 30
media <- 85
varianza <- 16

l <- function(x){ - n*0.5*log(x[2]) - 0.5*(n*varianza + n*(media - x[1])^2)/x[2] }
fit <- optim(par=c(100, 20), fn=l, lower=c(-Inf, 0), method="L-BFGS-B", control=list(fnscale=-1))
print(fit)



#### Ejemplo 3:  Distribucion Gamma y funciones de distribucion en R
tiempo = c(5, 3, 7, 9, 1)
n <- length(tiempo)
l <- function(p){
  logLk <- 0
  for(i in 1:n){
    logLk <- logLk + log(dgamma(tiempo[i], p[1], p[2]))
  }
  return(logLk)
}
media <- mean(tiempo)
varianza <- var(tiempo)
alpha_Momentos <- media^2 / varianza
beta_Momentos <- media / varianza
fit <- optim(par=c(alpha_Momentos, beta_Momentos), fn=l, control=list(fnscale=-1))
print(fit)



##### Ejemplo 4:  Regresion Lineal
x <- c(5, 2, 3, 7, 9, 8)
y <- c(5, 4, 5, 22, 15, 18)
n <- length(x)
l <- function(p){
  logLk <- 0
  for(i in 1:n){
    logLk <- logLk + log(dpois(y[i], exp(p[1] + p[2]*x[i])))
  }
  return(logLk)
}
fit <- optim(par=c(0, 0), fn=l, control=list(fnscale=-1))
print(fit)

