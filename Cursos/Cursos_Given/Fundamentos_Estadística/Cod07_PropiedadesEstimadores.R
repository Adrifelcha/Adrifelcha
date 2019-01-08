######################################
######################################
## PROPIEDADES DE LOS ESTIMADORES
## Codigo en el capitulo
#######################################






##### Codigo Ejemplar 1: 
##### Error Cuadrático Medio  (MSE)


#MSE = Varianza + Sesgo^2

n <- 10    #Tamaño de las Muestras
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

#Imprimimos los resulados
print(paste("La varianza es ", round(S2,4)))
print(paste("El Error Típico es ", round(Se,4)))
print(paste("El Sesgo al cuadrado es ", round(b2,4)))
print(paste("MSE = ", round(MSE,4)))






##### Codigo Ejemplar 2: 
##### Propiedades asintóticas de la MLE

#Datos del Ejemplo:
#Tenemos dos muestras con distinta n (n=2 y n=8) que comparten el mismo promedio(y)
#Y ~ Normal (Mu desconocida, D.E. conocida)
#Promedio(y) = 100
#D.E. = 2 
#Mu = A computar mediante el Promedio(y)

mu <- seq(90, 110, by=0.001)   #Definimos la base de las graficas
l1 <- -2*((100 - mu)^2)/8   #l(Mu) cuando n=2 y se omiten los términos que no incluyen Mu
l2 <- -8*((100 - mu)^2)/8   #l(Mu) cuando n=8 y se omiten los términos que no incluyen Mu

par(mfrow=c(1,2)) # Dividimos la pantalla para imprimir dos plots
#Plot 1 (n = 2)
plot(mu, l1, col="indianred", lwd=3, type="l", ylab="", xlab="", ylim=c(-100,0),main="n = 2")
lines(c(100,100),c(-100,0), lwd=2, lty=3)
#Plot 2 (n = 8)
plot(mu, l2, col="darkolivegreen4", lwd=3, type="l", ylab="", xlab="", ylim=c(-100,0), main="n = 8")
lines(c(100,100),c(-100,0), lwd=2, lty=3)








##### Codigo Ejemplar 3: 
##### Varianza del Estimador en Lenguaje R

#Donde Var(x) = Recíproco de la Información Observada
#Información Observada = -Segunda derivada del Log-likelihood 

x <- c(2, 7, 3)  #Datos

#Logaritmo de la función de verosimilitud (la multiplicatoria de la función original)
lk <- function(lambda) -3*log(lambda) - sum(x) / lambda

#Computamos la segunda derivada añadiendo hessian=TRUE como argumento a la función optim
fit <- optim(1, f=lk, method="Brent", lower=0, upper=10, control=list(fnscale=-1),
             hessian=TRUE)
print(fit)  #Imprimimos los resultados de Optim

#Interpretamos cada uno de los valores arrojados:
lambda <- fit$par              #En "par" fit nos dice el valor estimado
var_lambda <- -1/fit$hessian   #La varianza es el inverso de la segunda derivada (hessian)
Se <- sqrt(var_lambda)         #El error tipico es la raìz cuadrada de la Varianza


#Con estos datos, podemos computar un Intervalo de confianza del 95%
alpha <- .05   #"Error" que estamos dispuestos a dejar pasar (El complemento del Intervalo de Confianza)


Z <- abs(qnorm(alpha/2))   #Computamos el Puntaje Z que corresponde a nuestra alpha

Ls <- lambda + Z *Se   #Computamos los Lìmites Superior e Inferior
Li <- lambda - Z *Se


#Imprimimos los resultados:

print(paste("El Lambda estimado por MLE es ", round(lambda,4)))
print(paste(" con un Error Tipico de ", round(Se,4)))
print(paste("Intervalo de Confianza: (", round(Ls,4), ", ", round(Li,4), ")" ))









##### Codigo Ejemplar 4: 
##### Máxima Verosimilitud con más de un parámetro

#Datos
y <- c(90, 110, 85, 105, 102, 120)



l <- function(p){
  logLk <- 0   #Valor inicial de la función, que se va a ir actualizando segun un for
  for(i in 1:length(y)){   #Por cada dato contenido en y (6 veces)
    logLk <- logLk + log(dnorm(y[i], p[1], p[2])) 
    #LogLk se va a actualizar sumando el logaritmo de la función normal al LogLk
    #que se había acumulado en la repetición inmediatamente anterior
  }
  return(logLk)   #Recuperamos el valor logLk obtenido tras las repeticiones del ciclo
}

#Computamos los estimadores con Optim, indicando dos valores iniciales a estimar
fit <- optim(c(100,10), f=l, method="L-BFGS-B", lower=0, control=list(fnscale=-1),
             hessian=TRUE)
print(fit)

#Interpretamos los resultados de optim
H <- fit$hessian       # Matriz de segundas derivadas
Informacion <- - H     # La informaciòn es el negativo de las segundas derivadas
VarCovar <- solve(Informacion)    #  La matriz de Varianza-Covarianza es el inverso de la matriz de informacion
R <- cov2cor(VarCovar)            # 
print(VarCovar)                   #










##### Codigo Ejemplar 5: 
##### Evaluaciòn de un modelo de Regresion

f <- c(10, 9, 6, 5, 4)  #Numero de ensayos con descarga por día 
x <- 1:5                #Día
y <- c(60, 40, 70, 30, 50)    #Señal en decibeles
l <- function(p){
  logLk <- 0
  for(i in 1:length(y)){
    lambda <- exp(p[1] + p[2]*x[i] + p[3]*y[i])
    logLk <- logLk + log(dpois(f[i], lambda))
  }
  return(logLk)
}
fit <- optim(c(0,0,0), f=l, control=list(fnscale=-1), hessian=TRUE)
print(fit)


H <- fit$hessian
Informacion <- - H
VarCovar <- solve(Informacion)
R <- cov2cor(VarCovar)
print(VarCovar)
