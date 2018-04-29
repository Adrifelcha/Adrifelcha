###################################################
# Ejercicio
# Estimaciòn por Màxima Verosimilitud
###################################################


#M.A.S (~Pareto(?))
x <- c(6.13, 1.80, 1.34, 1.39, 1.25, 1.24, 1.15, 1.17, 1.17, 1.18)
Logs <- log(x)

suma <- sum(Logs)
n <- length(x)
l <- function(alpha) n*log(alpha) - (alpha+1)*suma
lMax <- optimize(l, c(1, 10), maximum=TRUE)
print(lMax)

alpha <- seq(1, 6, by=0.001)
Likelihood <- exp(l(alpha))
logLikelihood <- l(alpha)
par(mfrow=c(1,2))
plot(alpha, Likelihood, col="indianred", lwd=3, type="l", main="Funcion de Verosimilitud")
plot(alpha, logLikelihood, col="cyan", lwd=3, type="l", main="log Funciòn Verosimilitud")