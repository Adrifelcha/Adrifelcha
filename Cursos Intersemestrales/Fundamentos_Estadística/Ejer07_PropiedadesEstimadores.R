####### Ejercicios 

x <- c(.48,.38,.83,.51,.35,.80,.86,.35,.73,.95)
MediaX <- mean(x)
MediaX


#MLE 
Logs <- log(x)

n <- length(x)
l <- function(theta) n*log(theta) + (((n*theta) - n)*log(x))
lMax <- optimize(l, c(0, 1), maximum=TRUE)
print(lMax)

alpha <- seq(1, 6, by=0.001)
Likelihood <- exp(l(alpha))
logLikelihood <- l(alpha)
par(mfrow=c(1,2))
plot(alpha, Likelihood, col="indianred", lwd=3, type="l", main="Funcion de Verosimilitud")
plot(alpha, logLikelihood, col="cyan", lwd=3, type="l", main="log Funciòn Verosimilitud")



#### Varianza edel Estimador

fit <- optim(1, f=lk, method="Brent", lower=0, upper=10, control=list(fnscale=-1),
             hessian=TRUE)
print(fit)



lambda <- fit$par
var_lambda <- -1/fit$hessian
Se <- sqrt(var_lambda)
Z <- abs(qnorm(0.025))
Ls <- lambda + Z *Se
Li <- lambda - Z *Se
cat(sprintf(
  "El estimador es lambda = %5.3f con Se = %5.3f\nIntervalo de confianza: (%5.3f, %5.3f)\n",
  lambda, Se, Li, Ls))






### Intervalo de confianza
Z <- abs(qnorm(0.025))

Ls <- x_MLE + Z *Se
Li <- x_MLE - Z *Se







# Ejercicio 3: Asumiendo Beta

l <- function(p){
  logLk <- 0
  for(i in 1:length(x)){
    logLk <- logLk + log(dbeta(x[i], p[1], p[2]))
  }
  return(logLk)
}
fit <- optim(c(0,0), f=l, method="L-BFGS-B", lower=0, control=list(fnscale=-1),
             
             hessian=TRUE)

print(fit)






