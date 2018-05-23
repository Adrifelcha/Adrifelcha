######################################
######################################
## COMPARACION DE MODELOS
## Codigos en capítulo
#######################################


##### Ejemplo 1  : Contraste de Hipótesis por Razón de Verosimilitud
##### Ho: La Media vale 100  <- Parámetro fijo
##### Ha: La Media es distinta de 100   <- Parámetro libre

x <- c(116, 85, 90, 125)  # Muestra

lk <- 0 #Creamos un arreglo vacío, que llenaremos con la función de verosimilitud

#La Funcion de Verosimilitud es la multiplicatoria de la funcion de densidad
likelihood <- function(mu, sigma){    #La función de verosimilitud de una norma depende de sus parámetros Mu y Sigma
  lk <- 1   #Valor inicial para la multiplicatoria
  for(i in 1:length(x)){   #Por cada elemento contenido en la muestra
    lk <- lk * dnorm(x[i], mu, sigma)   #Se definirá una verosimilitud que corresponde al  valor computado en la repetición anterior por la función de densidad Normal (que depende de los datos y los parámetros a estimar)
  }
  return(lk)   #En esta función, nos interesa recuperar el valor computado para la verosimilitud
}

#Nota: En este ejemplo trabajamos con la Función de verosimilitud, que se define como la multiplicatoria de la función de densidad. 
#En la mayoría de los ejemplos atendidos anteriormente, se trabajó con la Funciól LOGverisimilitud, por lo que se recurría a una sumatoria

media <- mean(x)  #Estimamos la media de nuestra muestra
desviacion <- sd(x) #Y la desviación estandar

M1 <- likelihood(100, desviacion)   #Calculamos la Verosimilitud para el Modelo 1, que restringe Mu a 100, y estima Sigma a partir de la muestra (desviación estándar)
M2 <- likelihood(media, desviacion) #Calculamos la verosimilitud para el Modelo General, que estima Mu y Sigma a partir de la muestra (su Media y Desviación Estándar)

razon <- M1/M2 #Computamos la Razón de las Verosimilitudes computadas

#Imprimimos los resultados:

print(paste("La media de los datos es ", media, " y su desviación estándar ", round(desviacion,3)))

cat(
  sprintf('La Verosimilitud del Modelo 1 es %14.12f; la del Modelo 2, es %14.12f',M1, M2))

print(paste("La Razón de las Verosimilitudes (lk(M1)/lk(M2)) es ", round(razon,4)))

#Evaluamos el Contraste de la Bondad de Ajustes
alpha <- 0.05  #Probabilidad de caer en la zona crítica

G2 = -2*log(razon)  #Computamos el Estadístico G^2
gl <- 1  #La diferencia entre los parámetros libres en el Modelo General (2 parámetros) y el Modelo Anidado (1 parámetro)

#Computamos el área sobre el estadístico G^2 e una Distribución Chi-cuadrada con (Parámetros_2 - Parámetros_1) Grados de Libertad
p_valor <- pchisq(G2, gl, lower.tail=F)

#Comparamos el área con el nivel de significancia (la probabilidad de caer en la Zona Crítica)
decision <- ifelse(p_valor <= alpha, "Rechazar H0", "Mantener H0")

#Otra forma de expresar el ciclo ifelse sería:
if(p_valor <= alpha){
  print("Cae en Zona Crítica : Se rechaza la HO")
}else{
  print("cae en Zona de Confianza: Se mantiene la HO")
}

#Imprimimos los resultados
cat(sprintf('G2 = %5.2f, gl = %1.0f p = %5.3f. Decision: %s', G2, gl, p_valor, decision))

# Pero ¿Cómo podemos interpretar la Razón de Verosimilitud?
# ¿Qué tanto es tantito?



###### Pesentando la Chi Cuadrada
######
Gl <- 1 #El valor del parámetro lambda
x <- 0:10  #Definimos una base arbitraria
Ex_Chi <- dchisq(x, Gl)   #Creamos una Poisson con la lambda definida


#### Graficamos
layout(matrix(1:1,ncol=1)) #Presentamos un sólo gráfico en una sola columna por página
plot(Ex_Chi, type='l',xlim=c(0,8), main="Distribución Chi-cuadrada", xlab="Conteo de casos", 
        cex.lab=1.3, cex.main=2, col="indianred", lwd=3, lty=3)








##### Ejemplo 2  : Comparando el Valor P de dos muestras binomiales
##### Ho:  p1 y p2 son iguales
##### Ha:  p1 y p2 son distintas

x1 = c(1, 1, 1, 0, 0, 1, 1, 1, 0, 0)  #Muestra 1
x2 = c(0, 0, 0, 1, 1, 1, 0, 0)        #Muestra 2 

s1 = sum(x1)      #La suma de cada muestra (A utilizar en la funcion de log-verosimilitud)
s2 = sum(x2)        

n1 = length(x1)   #Tamaño de cada muestra
n2 = length(x2)

# Definimos la función LOGverosimilitud del Modelo 1 como la sumatoria del logaritmo de dos funciones de densidad binomiales, con un mismo parámetro p
M1 <- function(p) { log(dbinom(s1, n1, p)) + log(dbinom(s2, n2, p)) }

# Definimos la función LOGverosimilitud del Modelo 2 como la sumatoria del logaritmo de dos funciones de densidad binomiales, con DISTINTAS p (expresado como un vector de parámetros q)
M2 <- function(q) { log(dbinom(s1, n1, q[1])) + log(dbinom(s2, n2, q[2])) }

#Hacemos la Estimación Máximo Verosimil para el Modelo 1
fit1 <- optim(c(0.5), f=M1, method="Brent", lower=0, upper=1, control=list(fnscale=-1))
#El modelo 1 sólo tiene una p, así que especificamos un sólo parámetro inicial

fit2 <- optim(c(0.5, 0.5), f=M2, control=list(fnscale=-1))
#El modelo 2 tiene dos p distintas, así que especificamos un vector de valores iniciales.

G2 = -2*fit1$value + 2*fit2$value     # Computamos el estadístico G cuadrada
       #Como trabajamos con la función Logverosimilitud, no es necesario sacar el logaritmo de nada
       #Se trabaja directamente con las densidades de las funciones Logverosimilitud en el punto Máximo Verosimil estimado (la casilla 'value' del objeto fit)

gl <- 1    #Diferencias en parámetros libres entre el Modelo 1 y 2 (O bien, "Número de modelos restrigngidos por el Modelo 1")

p_valor <- pchisq(G2, gl, lower.tail=F) #Calculamos el área a la derecha de la G cuadrada en una distribución Chi cuadrada con 1 grado de libertad


cat(sprintf('pi = %5.3f, pi2(1) = %5.3f, pi2(2) = %5.3f, G2 = %6.3f'))
#Imprimimos los resultados


##### Ejemplo 3  : Contraste de Hipótesis por Razón de Verosimilitud
##### Una muestra con datos que se distribuyen segun una Gamma
##### Ho: La Media vale 4  <- Parámetro fijo
##### Ha: La Media es distinta de 4   <- Parámetro libre

x = c(5, 3, 7, 9, 1) #Datos

#Comenzamos con la Estimación Máxima Verosimil del Modelo General

#Trabajamos con la función LOGverosimilitud (requiere SUMATORIA)
logLikelihood <- function(p){
  lk <- 0    #Planteamos un valor inicial de 0
  for(i in 1:length(x)){      #Por cada elemento contenido en nuestra muestra de datos
    lk <- lk + log(dgamma(x[i], p[1], p[2]))     #Vamos a actualizar el valor de Logverosimilitud, sumando a lo que ya se tenía el logaritmo de la función beta que corresponde con el dato registrado
  }
  return(lk)     #Vamos a trabajar con lk
}

#Computamos el Estimador Máximo Verosimil con la función optim
#Fijamos dos valores iniciales (el arreglo c(1,1) porque dejamos variar alfa y beta (parámetros típicos de la Gamma)
fit_M2 <- optim(c(1,1), f=logLikelihood, method="L-BFGS-B", control=list(fnscale=-1),
                lower=0, hessian=TRUE)
# Agregamos el hessian=TRUE, para evaluar si el valor estimado corresponde con un máximo o mínimo

#Interpretamos los resultados
H <- fit_M2$hessian    #La matriz de segundas derivadas se va a iedntificar con H
Informacion <- - H     #El negativo de la matriz hessiana nos indica la informaciñon observada
VarCovar <- solve(Informacion)      #Si obtenemos el inverso de la matriz de información, obtenemos la matriz de varianzas-covarianzas

#Hasta aquí, podemos presentar un resumen de las estimaciones obtenidas por máxima verosimilitud para el Modelo General (2)
cat(sprintf("Metodo de maxima-verosimilitud, a = %5.2f(%4.2f), b = %5.2f(%4.2f)",
            fit_M2$par[1], sqrt(VarCovar[1,1]), fit_M2$par[2], sqrt(VarCovar[2,2])))

#Definimos la Función LOGverosimilitud (requiere sumatria) de nuestro modelo restringido (Media = 4)
logLikelihood_R <- function(beta){
  #Dado que hablamos de una distribución gamma, sabemos que la Media = alpha/beta, por lo que despejamos alpha = mu*beta
  alpha <- 4*beta    #Alfa NO es un parámetro libre, sino que lo estimamos a partir de las estimaciones hechas para beta (EL parametro libre) y el valor fijo para mu
  lk <- 0   #Valor inicial (en el dato 0) de la función de verosimilitud...
  for(i in 1:length(x)){    #...que se actualziará por cada elemento contenido en la muestra
    lk <- lk + log(dgamma(x[i], alpha, beta))   #Sumando al valor computado en el ensayo inmediatamente anterior, el logaritmo de la función de densidad gamma que resulte de los datos y la definición de solo un parámetro libre
  }
  return(lk)
}

#Computamos el estimador Máximo Verosimil con la función optim y un sólo valor inicial
fit_M1 <- optim(c(1), f=logLikelihood_R, method="Brent", lower=0, upper=1,
                control=list(fnscale=-1), hessian=TRUE)
#Interpretamos los resultados de la función optim 
Informacion <- - fit_M1$hessian    #La información es el negativo de la segunda derivada computada
Se <- sqrt(1/Informacion)    #El error típico es la raíz cuadrada de la Varianza, que a su vez se define como el inverso de la Información contenida

#Imprimimos los resultados acerca de la estimación máximo verosímil del Modelo 2.
cat(sprintf("Metodo de maxima-verosimilitud, modelo restringido, a = %5.2f(%4.2f), b = %5.2f(%4.2f)",
            4*fit_M1$par, 4*Se, fit_M1$par, Se))

#Computamos el estadístico G2 a partir de las densidades de las funciones LOGverosimilitud computadas por cada Modelo
G2 = -2*fit_M1$value + 2*fit_M2$value
gl <- 1  #Definimos la diferencia entre el número de parámetros libres contenidos en el Modelo General y el Modelo Anidado.

p_valor <- pchisq(G2, gl, lower.tail=F)  #Calculamos el área de una distribución chi cuadrada con 1 grado de libertad que cae por encima de nuestro estadístico G2

#Realizamos una operación para decidir si conservar o mantener la Hipótesis Nula a partir de una función ifelse
decision <- ifelse(p_valor <= 0.05, "Rechazar H0", "Mantener H0")

#Imprimimos los resultados
cat(sprintf('G2 = %5.2f, gl = %1.0f p = %5.3f. Decision: %s', G2, gl, p_valor, decision))






##### Ejemplo 4  : Contraste de Hipótesis por Razón de Verosimilitud
##### La distribuciòn que se asume no es una Distribución Predefinida (No viene ya explicitada en R)
##### Ho: El parámetro Beta = 1
##### Ha: El paràmetro Beta es distinto de 1

x <- c(5, 2, 4, 3, 1)
n <- length(x)
media <- mean(x)
l <- function(beta) -5*n*log(beta) - n*media/beta
fit_M2 <- optim(c(1), f=l, method="Brent", lower=0, upper=20,
                control=list(fnscale=-1), hessian=TRUE)
fit_M1 <- l(1)
G2 = -2*fit_M1 + 2*fit_M2$value
gl <- 1
p_valor <- pchisq(G2, gl, lower.tail=F)
decision <- ifelse(p_valor <= 0.05, "Rechazar H0", "Mantener H0")
cat(sprintf(
  'beta estimada = %5.2f, Se = %5.3f\nG2 = %5.2f, gl = %1.0f p = %5.3f, Decision: %s',
  fit_M2$par, sqrt(-1/fit_M2$hessian), G2, gl, p_valor, decision))








##### Ejemplo 5  : Contraste de Hipótesis por Razón de Verosimilitud
##### Regresión Beta
##### Ho: El parámetro Beta = 1
##### Ha: El paràmetro Beta es distinto de 1

p <- c(0.5, 0.2, 0.1, 0.6, 0.3, 0.7, 0.6, 0.6, 0.9, 0.4)    #Proporciones
x <- c(10, 4, 2, 15, 8, 20, 16, 18, 19, 12)   #Numero de casos
logLikelihood_1 <- function(parametros){
  lk <- 0
  for(i in 1:length(x)){
    phi <- exp(-parametros[1])
    mu <- exp(parametros[2]) / (1+exp(parametros[2]))
    alpha <- mu * phi
    beta <- (1-mu) * phi
    lk <- lk + log(dbeta(p[i], alpha, beta))
  }
  return(lk)
}
logLikelihood_2 <- function(parametros){
  lk <- 0
  for(i in 1:length(x)){
    phi <- exp(-parametros[1])
    mu <- exp(parametros[2] + parametros[3]*x[i]) / (1+exp(parametros[2] + parametros[3]*x[i]))
    alpha <- mu * phi
    beta <- (1-mu) * phi
    lk <- lk + log(dbeta(p[i], alpha, beta))
  }
  return(lk)
}

fit_M1 <- optim(c(0,0), f=logLikelihood_1, control=list(fnscale=-1), hessian=TRUE)
fit_M2 <- optim(c(0,0,0), f=logLikelihood_2, control=list(fnscale=-1), hessian=TRUE)
G2 = -2*fit_M1$value + 2*fit_M2$value
gl <- 1
p_valor <- pchisq(G2, gl, lower.tail=F)
decision <- ifelse(p_valor <= 0.05, "Rechazar H0", "Mantener H0")
Se <- sqrt(diag(solve(-fit_M2$hessian)))
cat(sprintf("G2 = %5.2f, gl = %1.0f p = %5.3f, Decision: %s
            Parametros estimados. v = %5.2f(%4.2f), a = %5.2f(%4.2f) b = %5.2f(%4.2f)",
            G2, gl, p_valor, decision, fit_M2$par[1], Se[1], fit_M2$par[2], Se[2], fit_M2$par[3], Se[3]))
## G2 = 19.56, gl = 1 p = 0.000, Decision: Rechazar H0
## Parametros estimados. v = -3.31(0.44), a = -2.13(0.33) b = 0.17(0.02)
xaxis <- seq(2, 20, by=0.01)
mu <- exp(fit_M2$par[2] + fit_M2$par[3]*xaxis) / (1+exp(fit_M2$par[2] + fit_M2$par[3]*xaxis))
plot(x,p)
lines(xaxis,mu, lwd=2, col="navyblue")






##### Ejemplo 6  : Comparaciòn de Modelos (AIC)
##### Queremos saber si los datos observados provienen de una Normal o Exponencial

x = c(7, 3, 3, 1, 20, 4, 12, 2, 0, 2)   #Datos
n <- length(x)     #Tamaño de la Muestra
media <- mean(x)   #Media
desviacion <- sqrt((n-1)*var(x)/n)     # Desviación Estándar

omega <- 1/media      #Valor Omega por el Metodo de los Momentos

l_normal <- sum(log(dnorm(x, media, desviacion)))
l_exponencial <- sum(log(dexp(x, omega)))

AIC_normal <- -2*l_normal + 4
AIC_exponencial <- -2*l_exponencial + 2

cat(sprintf("AIC normal = %6.2f. AIC exponencial = %6.2f\nmedia %5.2f Sd = %5.2f omega = %5.2f",
            AIC_normal, AIC_exponencial, media, desviacion, omega))
