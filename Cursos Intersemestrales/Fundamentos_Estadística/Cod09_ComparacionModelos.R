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



###### Pesentando la Chi Cuadrada
######
Gl <- 1 #El valor del parámetro lambda
x <- 0:10  #Definimos una base arbitraria
Ex_Chi <- dchisq(x, Gl)   #Creamos una Poisson con la lambda definida


#### Graficamos
layout(matrix(1:1,ncol=1)) #Presentamos un sólo gráfico en una sola columna por página
plot(Ex_Chi, type='l',xlim=c(0,8), main="Distribución Chi-cuadrada", xlab="Conteo de casos", 
        cex.lab=1.3, cex.main=2, col="indianred", lwd=3, lty=3)





