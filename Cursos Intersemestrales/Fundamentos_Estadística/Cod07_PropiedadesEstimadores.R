######################################
######################################
## PROPIEDADES DE LOS ESTIMADORES
##
#######################################


##### 1: 
##### Error Cuadrático Medio

n <- 10    #Tamaño de la Muestras
x <- 1:n   #Datos
J <- 1000  #Numero de muestas

beta <- 2  # Valor Real
sigma2_e <- 36   #Varianza (Error)

beta_estimada <- rep(0, J)    #Arreglo vacío a llenar con las estimaciones de Beta

for(j in 1:J){
  y <- rnorm(n, beta*x, sqrt(sigma2_e))     #Por cada muestra, generamos 10 datos de acuerdo a una Normal
  beta_estimada[j] <- sum(x*y) / sum(x*x)  #Segun mi EMC, computo el varlor estimado de Beta
}

S2 <- mean((beta_estimada - mean(beta_estimada))^2)   #Varianza de los estimados
Se <- sqrt(S2)        #Error típico de los estimados

b2 <- (mean(beta_estimada) - beta)^2     #Sesgo al cuadrado del estimado

MSE <- S2+b2      #Error Cuadrático Medio


cat(sprintf("Varianza = %10.4f", S2))
cat(sprintf("Error T. = %10.4f",Se))
cat(sprintf("Sesgo^2 = %10.4f",b2))
cat(sprintf("MSE = %10.4f\n",MSE))




######## Propiedades asintóticas de la MLE

#Datos del Ejemplo:
#Tenemos dos muestras con distinta n (n=2 y n=8, respectivamente) que comparten el mismo promedio(y)
#y ~ Normal (Mu desconocida, D.E. conocida)
#Promedio(y) = 100
#D.E. = 2 
#Mu = A computar mediante el Promedio(y)

mu <- seq(90, 110, by=0.001)   #Definimos la base de las graficas
l1 <- -2*((100 - mu)^2)/8   #l(Mu) cuando n=2 y se omiten los términos que no incluyen Mu
l2 <- -8*((100 - mu)^2)/8   #l(Mu) cuando n=8 y se omiten los términos que no incluyen Mu
par(mfrow=c(1,2))
plot(mu, l1, col="indianred", lwd=3, type="l", ylab="", xlab="", ylim=c(-100,0),main="n = 2")
lines(c(100,100),c(-100,0), lwd=2, lty=3)
plot(mu, l2, col="darkolivegreen4", lwd=3, type="l", ylab="", xlab="", ylim=c(-100,0), main="n = 8")
lines(c(100,100),c(-100,0), lwd=2, lty=3)






######## Varianza del Estimador en Lenguaje R
#Donde Var(x) = Recíproco de la Información Observada
#Información Observada = Segunda derivada del Log-likelihood 

x <- c(2, 7, 3) #Datos
lk <- function(lambda) -3*log(lambda) - sum(x) / lambda
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


H <- fit$hessian
Informacion <- - H
VarCovar <- solve(Informacion)
R <- cov2cor(VarCovar)
print(VarCovar)
