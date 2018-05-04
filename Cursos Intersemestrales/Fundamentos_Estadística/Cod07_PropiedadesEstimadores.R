##### Error Cuadrático Medio

n <- 10
x <- 1:n
J <- 1000
beta <- 2
sigma2_e <- 36
beta_estimada <- rep(0, J)
for(j in 1:J){
  y <- rnorm(n, beta*x, sqrt(sigma2_e))
  beta_estimada[j] <- sum(x*y) / sum(x*x)
}
S2 <- mean((beta_estimada - mean(beta_estimada))^2)
b2 <- (mean(beta_estimada) - beta)^2
MSE <- S2+b2
Se <- sqrt(S2)
cat(sprintf("S2 = %10.8f, Se = %10.8f, sesgo^2 = %10.8f, MSE = %10.8f\n", S2, Se, b2, MSE))




######## Propiedades asintóticas de la MLE

mu <- seq(90, 110, by=0.001)
l1 <- -2*((100 - mu)^2)/8
l2 <- -8*((100 - mu)^2)/8
par(mfrow=c(1,2))
plot(mu, l1, col="darkolivegreen4", lwd=1.5, type="l", ylab="", xlab="", ylim=c(-100,0))
plot(mu, l2, col="darkolivegreen4", lwd=1.5, type="l", ylab="", xlab="", ylim=c(-100,0))


######## Varianza del Estimador en Lenguaje R

x <- c(2, 7, 3)
lk <- function(lambda) -3*log(lambda) - sum(x) / lambda
fit <- optim(1, f=lk, method="Brent", lower=0, upper=10, control=list(fnscale=-1),
             hessian=TRUE)
print(fit)


##

lambda <- fit$par
var_lambda <- -1/fit$hessian
Se <- sqrt(var_lambda)
Z <- abs(qnorm(0.025))
Ls <- lambda + Z *Se
Li <- lambda - Z *Se
cat(sprintf(
  "El estimador es lambda = %5.3f con Se = %5.3f\nIntervalo de confianza: (%5.3f, %5.3f)\n",
  lambda, Se, Li, Ls))



######

y <- c(90, 110, 85, 105, 102, 120)
l <- function(p){
  logLk <- 0
  for(i in 1:length(y)){
    logLk <- logLk + log(dnorm(y[i], p[1], p[2]))
  }
  return(logLk)
}
fit <- optim(c(100,10), f=l, method="L-BFGS-B", lower=0, control=list(fnscale=-1),
             hessian=TRUE)
print(fit)
