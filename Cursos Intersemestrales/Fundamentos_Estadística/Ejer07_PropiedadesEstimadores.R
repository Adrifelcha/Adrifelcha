############################
############################
# Ejercicios 7:
# Propiedades de los Estimadores
#############################


#EJERCICIO 1
###############
Datos <- c(0.48, 0.38, 0.83, 0.51, 0.35, 0.8, 0.86, 0.35, 0.73, 0.95)

#Computamos sus descriptivos (y derivados)
############################
n <- length(Datos)   #Tamaño de la muestra


media <- mean(Datos)            #Computamos la media (por función y manualmente)
media_manual <- sum(Datos)/n

if(media==media_manual){        #Comprobamos que sean equivalentes
  Media <- media_manual
  print(paste("La media es ", Media))      #Si lo son, se imprimirá su valor
}else{
  print("Error")                           #Sino, se imprimirá un anuncio de ERROR
}



varianza <- var(Datos)      #Computamos la Varianza por función

Diferencias <- c(NA)        #Preparamos un arreglo que nos permita computarla manualmente con un ciclo for
for(i in 1:n){
  Diferencias[i] <- round((Datos[i]-Media)^2,5)       #Llenando el arreglo con cada diferencia cuadrada
}
varianza_manual <- sum(Diferencias)/(n-1)             #Sumamos las diferencias

# Comparamos los valores computados por Función R y manualmente
varianzas <- data.frame(cbind(round(varianza,3), round(varianza_manual,3)))
colnames(varianzas) <- c("var(Datos)", "Varianza manual")
varianzas




Logs <- log(Datos)   #Transformación Logarítmica
SumLogs <- sum(Logs)  #Suma de los logaritmos de cada valor




###########  #  #  #  Metodo de los Momentos

Theta_MOM <- (Media)/(1-Media)
print(paste("Segun el Metodo de los Momentos, Teta vale: ", round(Theta_MOM,5)))



###########  #  #  #  Maxima Verosimilitud
l <- function(p){
  logLk <- 0
  for(i in 1:n){
    logLk <- logLk + log(p[1]) + (p[1]-1)*log(Datos[i])
  }
  return(logLk)
}
fit <- optim(1, f=l, method="Brent", lower=0, upper=10, control=list(fnscale=-1), hessian=TRUE)
fit

print(paste("Segun el Metodo de Màxima Verosimilitud, Teta vale: ", round(fit$par,5)))

Theta_MLE <- fit$par


###########  #  #  #  Varianza del estimador por Máxima Verosimilitud
Informacion <- -(n/(fit$par^2))
Var_Theta <- ((fit$par)^2)/n
Error_Tipico <- sqrt(Var_Theta)

print(paste("La Información Observada (La segunda derivada de logLk) es: ", round(Informacion,5)))
print(paste("La Varianza (El inverso de la Informaciòn) es: ", round(Var_Theta,5)))
print(paste("El error tìpico (Se) es: ", round(Error_Tipico,5)))

info <- fit$hessian 
print(paste("Información segun optim = ", round(info,5)))
print(paste("Información segun formula = ", round(Informacion,5)))

Se <- sqrt(1/-info)
print(paste("Error Tipico segun optim = ", round(Se,5)))
print(paste("Error Tipico segun formula = ", round(Error_Tipico,5)))





###########  #  #  #   Intervalo de Confianza al 95%
Z <- abs(qnorm(0.025))

Lim_S <- Theta_MLE + (Z*Error_Tipico)
Lim_I <- Theta_MLE - (Z*Error_Tipico)

print(paste("El Limite Inferior es ", round(Lim_I,5), " y el límite superior es ", round(Lim_S,5)))










##### EJERCICIO 3 
####################################### 
# Asumiendo que los Datos vienen de una distribución Beta


h <- function(p){
  logLk <- 0
  for(i in 1:n){
    logLk <- logLk + log(dbeta(Datos[i], p[1], p[2]))
  }
  return(logLk)
}


fitBeta <- optim(c(1,1), f=h, method="L-BFGS-B", lower=0, control=list(fnscale=-1),hessian=TRUE)

print(fitBeta$par)

Informacion <- - fitBeta$hessian
VarCovar <- solve(Informacion)
Se <- sqrt(diag(VarCovar))
print(Se)

R <- cov2cor(VarCovar)
print(R)

