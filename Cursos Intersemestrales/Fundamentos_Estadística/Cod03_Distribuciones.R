#Material de apoyo para estudiar distribuciones
#Autor: Adriana F. Chávez De la Peña
#adrifelcha@gmail.com
##########################################################


################################
###### Distribución Binomial
################################
n <- 100      #Observaciones
p <- 0.2      #Probabilidad de observar un exito

ExV <- n*p    #Calculamos el Valor Esperado
print(ExV)

#Creamos una binomial con los parámetros especificados
Ex_Binom <- dbinom(x, size=n, prob=p)

#### Graficamos
layout(matrix(1:2,ncol=2)) #Vamos a acomodar 2 gráficas en 2 columnas por pantalla

x <- c(0:n)   #Definimos el soporte de la gráfica entre 0 y n

#Ploteamos con la función plot() la relación entre cada punto contenido en x y la binomial especificada
#Gráfico 1: Lineal (Incorrecto para variables discretas)
plot(x,Ex_Binom, xlim= c(0,ExV*2), main="Distribución Binomial", type="l",
     cex.main=1.7, lwd=2,col='purple', xlab="Numero de éxitos", 
     ylab="Probabilidad (#Exitos | n, p)",cex.lab=1.2)
    #Argumentos:
        #cex siempre se utiliza para indicar tamaño, cex.main hace referencia al título
        #xlab y ylab asignan un nombre a cada eje
        #lwd modulan el grosor de la línea trasada

#Gráfico 2: Gráfica de barras (Ideal para variables discretas)
barplot(Ex_Binom, main= "Distribución Binomial", xlab="Numero de éxitos", cex.lab=1.2,
        ylab="Probabilidad (#Exitos | n, p)", col=rainbow(length(x)), xlim= c(0,ExV*2))






#####################
###### Distribución  Poisson
#####################
lam <- 4 #El valor del parámetro lambda
x <- c(0:30)  #Definimos una base arbitraria
Ex_Pois <- dpois(x,lambda=lam)   #Creamos una Poisson con la lambda definida


#### Graficamos
layout(matrix(1:1,ncol=1)) #Presentamos un sólo gráfico en una sola columna por página
barplot(Ex_Pois, main="Distribución Poisson", xlab="Conteo de casos", 
        cex.lab=1.3, cex.main=2, col=rainbow(length(x)))








#####################
###### Distribución Normal
#####################
mean <- 0     #Media
sDev <- 1     #Desviación Estándar

#Creamos una Normal con los parámetros especificados
Ex_Norm <- function(x) dnorm(x, mean, sDev)

#Esta vez, especificamos que es una función que depende de x
#por lo que al graficar, no hará falta que especifiquemos el rango x
#porque nuestro objeto Ex_Norm ya contiene todos los pares posibles.

####### Graficamos
plot(Ex_Norm, main = "Distribución Normal", ylab="", cex.main=2, 
     xlim=c(-6,6), col="darkblue", lwd=3, xlab="Valores de X", cex.lab=1.2) 
#Agregamos el parámetro xlim que delimita la gráfica en x (Qué tanto de la función queremos ver)
lines(c(mean, mean),c(0,0.6), lwd=2, lty=1, col="deepskyblue3")   
#Agregamos una línea vertical que señale la media de la distribución 
#(los argumentos x y y se vuelven un arreglo para señalar el inicio y 
#el fin de la línea en cada dimensión; En x la línea permanece en la media, pero en y cambia su altura.)







#####################
###### Distribución Exponencial
#####################
w <- 10  #Velocidad de cambio

#Otra vez definimos nuestra Exponencial como una función para cada valor posible de x
Ex_exp <- function(x) dexp(x, w) 

######### Graficamos la función
plot(Ex_exp, main = "Distribución Exponencial", ylab="", cex.main=2, cex.lab=1.2,
     xlim=c(0,3), ylim=c(0,10), lwd=3, col="forestgreen", xlab="Tiempo transcurrido")







#####################
###### Distribución Gamma
#####################
a <- 4  #Alpha
b <- 2  #Beta

#Creamos una distribución Gamma como una función definida para toda x posible
Ex_gamma <- function(x) dgamma(x, a, b)

#Graficamos la función
plot(Ex_gamma, main = "Distribución Gamma", ylab="", xlab="Tiempo", xlim=c(0,6),
     col="firebrick4", lwd=3, cex.main=2, cex.lab=1.2)



#####################
###### Distribución Beta
#####################
a <- 1   #Alpha
b <- 1   #Beta

#Creamos una distribución Gamma definida como una función apra cada valor de X
Ex_gamma <- function(x) dbeta(x, a, b)

#Graficamos la función
plot(Ex_gamma, main = "Distribución Beta", ylab="", cex.lab=1.2, cex.main=2, 
     xlab="Tasa / Proporción / Probabilidad", xlim=c(0,1), lwd=3, col="goldenrod3")





#####################
### CODIGOS DEL CAPITULO 3 (por el Dr. Luis Revuelta)
#####################

#######################
# Código 1

datos <- c(1,3,2)
n <- length(datos) #Tamaño de la muestra
nY <- sum(datos)  #Suma de los datos (n * promedio_de_los_datos)

f <- function(w) w^n * exp(-w * nY) #Computamos la función de densidad conjunta de la muestra
loga <- function(w) n*log(w) - w*nY  #Computamos el logaritmo

fMax <- optimize(f, c(0, 2), maximum=TRUE) #Máximo a partir de la función de densidad
lMax <- optimize(loga, c(0, 2), maximum=TRUE) #Máximo a partir de la función logarítmica
print(fMax)
print(lMax)

#Graficamos ambas funciones
layout(matrix(1:2,ncol=2))
plot(f, type="l", lwd=2, ylab="", ylim=c(0,0.0065), col="darkorchid2", main = "Exponencial")
plot(loga, type="l", lwd=2, ylab="", ylim=c(-15,-5), col="darkmagenta", main = "Log(Exponencial)")
legend(0.75, 1.6, c("f(x)", "g(x)"), lty=c(1,1), lwd=2, col=c("red", "blue"))


#####################
###### Código 2

#Creamos un conjunto de datos inventados con 30 repeticiones de valores entre 0 y 1, en saltos de .1
muestra <- c(rep(0,30), rep(0.1,30), rep(0.2,30), rep(0.3,30), rep(0.4,30), rep(0.5,30), rep(0.6,30), rep(0.7,30), rep(0.8,30), rep(0.9,30), rep(1,30))

alpha <- function(m,v) m *(m*(1-m)/v - 1)       #Especificamos las fórmulas para computar
beta <- function(m,v) (1-m)*(m*(1-m)/v - 1)     #alpha, beta y la asimetría
asimetria <- function(a,b) 2*(b-a)*sqrt(a+b+1)/((a+b+2)*sqrt(a*b))

media <- mean(muestra)    #Computamos la media de nuestra muestra
varianza <- var(muestra)  #Computamos la varianza de la muestra
a <- alpha(media, varianza)     #Calculamos alpha con la función especificada, identificando
                                #los parámetros m y v con la media y la varianza computados para nuestra muestra
b <- beta(media, varianza)      #Calculamos beta con la función especificada y la media y la varianza

#Enunciamos los resultados
cat(sprintf(
  "Los datos de la muestra son: media = %20.4f, varianza = %6.4f y asimetría = %6.4f.
Los parámetros estimados son: alpha = %6.4f y beta = %6.4f.",
  media, varianza, asimetria(a,b), a, b))

#Graficamos la función resultante con los valores paramétricos estimados
layout(matrix(1:1,ncol=1))
plot(function(x) dbeta(x, a, b), main = "Beta", ylab="", xlab="", cex.main=2, 
     lwd=3, col="darkseagreen4")
 





#############################################
############ Trabajando con distribuciones en R
##############################################


#################################################################################
####### Funciones de probabilidad (densidad y masa) (d - dnorm, dbinom, etc...)
#Esta función nos dice cuál es el punto en Y que la función asigna a cada valor X

par(mfrow=c(1,2)) #En una misma fila, presentamos dos figuras

y <- 0:10  #Delimitamos el espacio muestral 
f1 <- dpois(y,4)  #Creamos una Poisson para el espacio Y, con lambda 4
barplot(f1, names=as.character(y), main="Poisson (Lambda = 4)", cex.main=1.5, col="pink")

x <- seq(0, 10, by=0.001) #Delimitamos el espacio muestral entre 0 y 10 en saltos pequeñitos
f2 <- dchisq(x,4) #Creamos una distribución ChiCuadrada para nuestro espacio X, con 4 grados de libertad
plot(x, f2, type="l", lwd=3, col="darkred", main="Chi-cuadrada (gl = 4)",
     xlab="", ylab="", cex.main=1.5)

##### Ejemplo interactivo (con una Normal :D)
valor <- 2  #Valor cuya densidad de probabilidad se quiere estimar
densidad <- dnorm(valor,0,1)
print(densidad)

#Ilustración de lo que las funciones p señalan: Probabilidad acumulada para valores de x
# iguales o menores a un valor específico
layout(matrix(1:1,ncol=1))
plot(function(x) dnorm(x,0,1), xlim=c(-6,6), main="Función dnorm()", cex.main=2)
lines(c(valor,valor),c(0,dnorm(valor,0,1)), lwd=4, lty=1, col="deeppink3")   
text(-4,0.19,paste("Valor = ",valor), font=2, col="deeppink4")   #Especificamos la Tasa de Falsas Alarmas
text(-4,0.14,paste("Densidad = ",round(densidad,3)), font=2, col="deeppink2")

####cambia la variable "Valor" para ver cómo cambia.




##################################################################################
####### Funciones de distribuciòn (p - pnorm, pbinom, etc ...)
#Estas funciones nos permiten conocer la probabilidad ACUMULADA de un valor X particular

valor <- 2  #Valor cuya probabilidad acumulada se quiere estimar
acumulada <- pnorm(valor,0,1)
print(acumulada)

#Ilustración de lo que las funciones p señalan: Probabilidad acumulada para valores de x
# iguales o menores a un valor específico
layout(matrix(1:1,ncol=1))
plot(function(x) dnorm(x,0,1), xlim=c(-6,6), main="Función pnorm()", cex.main=2)
lines(seq(-6,valor,0.01),dnorm(seq(-6,valor,0.01),0,1), lwd=2, lty=1, col="deepskyblue2")
lines(c(valor,valor),c(0,dnorm(valor,0,1)), lwd=4, lty=1, col="deepskyblue4")   
text(-4,0.19,paste("Valor = ",valor), font=2, col="deepskyblue4")   #Especificamos la Tasa de Falsas Alarmas
text(-4,0.14,paste("P. acumulada = ",round(acumulada,3)), font=2, col="deepskyblue2")

####cambia la variable "Valor" para ver cómo cambia.



##################################################################################
####### Phi inversa (q - qnorm, qbinom, etc....)
#Estas funciones nos permiten saber cuál es el valor en X, en el que se ha acumulado una
#cierta probabilidad (es una pregunta inversa a la planteada por las funciones p)
qnorm(0.05, lower.tail=FALSE) #A la derecha de la distribución
qnorm(0.05, lower.tail=TRUE) #A la izquierda de la distribución


#Ejemplo interactivo (Cambia la variable Valor)
acum <- 0.6  #Probabilidad acumulada cuyo valor en X queremos conocer
valor_izq <- qnorm(acum,0,1, lower.tail = TRUE)
valor_der <- qnorm(acum,0,1, lower.tail = FALSE)
print(acumulada)

#Ilustración de lo que las funciones p señalan: Probabilidad acumulada para valores de x
# iguales o menores a un valor específico
layout(matrix(1:1,ncol=1))
plot(function(x) dnorm(x,0,1), xlim=c(-6,6), main="Función qnorm()", cex.main=2)
lines(seq(-6,valor_izq,0.01),dnorm(seq(-6,valor_izq,0.01),0,1), lwd=3, lty=2, col="deepskyblue2")
lines(seq(valor_der,6,0.01),dnorm(seq(valor_der,6,0.01),0,1), lwd=3, lty=2, col="brown1")
lines(c(valor_izq,valor_izq),c(0,dnorm(valor_izq,0,1)), lwd=2, lty=6, col="blue")
lines(c(valor_der,valor_der),c(0,dnorm(valor_der,0,1)), lwd=2, lty=6, col="brown3")   
text(-4,0.19,paste(acum*100, "% acumulado a la izquierda"), font=2, col="deepskyblue4")   #Especificamos la Tasa de Falsas Alarmas
text(-4,0.16,paste("valor x = ",round(valor_izq,3)), font=2, col="deepskyblue2")
text(4,0.19,paste(acum*100, "% acumulado a la derecha"), font=2, col="brown4")   #Especificamos la Tasa de Falsas Alarmas
text(4,0.16,paste("valor x = ",round(valor_der,3)), font=2, col="brown2")




####### Muestreo aleatorio (r - rnorm, rbinom, etc....
#Con estas funciones extraemos un N número de muestras de una distribución particular, 
#definida por parámetros específicos   rnorm(#extracciones, parámetros)


#####Ejemplo 1:
muestra <- rpois(100, 15)   #Creamos una muestra
#Enunciamos las características de nuestra muestra
cat(sprintf("La media es %5.2f y la varianza %5.2f", mean(muestra), sd(muestra)))


######Ejemplo 2:
n <- 50            #Número de muestras extraídas
muestras <- 1000   #Tamaño de cada muestra

dat <- rbeta(muestras*n, 0.5, 0.5)     #Extraemos tantos datos aleatorios de una beta por cada muestra extraída
muestra <- matrix(dat, ncol=n)         #Acomodamos nuestra muestra en 50 columnas (una por cada muestra)
medias <- colMeans(muestra)            #Computamos la media de cada columna
hist(medias, ylab="Frecuencia", main=   
       sprintf("Media = %10.2f, Sd = %4.2f", mean(medias), sd(medias)))
#Computamos un histograma para las medias estimadas con las cincuenta muestras