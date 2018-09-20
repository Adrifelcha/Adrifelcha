###################################################
# Repaso genral de Estadística
# Adriana F. ChÃ¡vez
# adrifelcha@gmail.com
###################################################

###################################################
# UNO: Variables aleatorias
###################################################
x <- seq(0, 1, by=0.01)     #Recta real
f <- 6*x*(1-x)              #Función 1
g <- 18*x*(1-x)^4           #Funciión 2
plot(x, f, type="l", lwd=2, ylab="", ylim=c(0,1.6), col="red")      #Ploteamos el valor asignado por la función f a cada valor de la secuencia x
lines(x, g, lwd=2, col="blue")   #Sobreponemos una líea que represente Función 2    (el valor asignado por la función g a cada valor contenido en x)
legend(0.75, 1.6, c("f(x)", "g(x)"), lty=c(1,1), lwd=2, col=c("red", "blue"))     #Añadimos un recuadro/leyenda que señale a qué corresponde cada líea. Separamos los elementos en un arreglo.


g <- function(x) 18 * x * (1-x)^4  #Especificamos la función
fit <- optimize(g, c(0, 1), maximum=TRUE)   #Usamos la función optimize para obtener el punto máximo (maximum=TRUE) de la función g, en el intervalo 0 y 1
print(fit)  #Imprimimos el elemento fit 
plot(g, type="l", lwd=2, ylab="", col="purple")   #Ploteamos la relación x-y definida por g
points(fit$maximum,fit$objective, col="red", pch=16, cex=2)
points(fit$maximum,0, col="red", pch=16, cex=2)
lines(c(fit$maximum,fit$maximum), c(0,fit$objective), lwd=2, lty=2, col="black")

f1 <- function(x) {6*x*(1-x)}       #Especificamos la funciÃ³n 
integral <- integrate(f1, lower = 0, upper = 1)      #Integramos la funciÃ³n anteriormente definida en el intervalo 0  a 1
print(integral)   #Imprimimos el resultado de la integral


#################
# Distribuciones de probabilidad
#################

####### PARAMETROS
mean <- 0     #Media
sDev <- 1     #Desviación Estándar

#Creamos una Normal con los parámetros especificados
Ex_Norm <- function(x) dnorm(x, mean, sDev)

####### Graficamos
plot(Ex_Norm, main = "Distribución Normal", ylab="", cex.main=2, 
     xlim=c(-6,6), col="darkblue", lwd=3, xlab="Valores de X", cex.lab=1.2) 
lines(c(mean, mean),c(0,0.6), lwd=2, lty=1, col="deepskyblue3")   

################
# Teoría de las muestras grandes
################
#Según la Ley de los Grandes Números:
#El valor de la media muestral se aproxima al valor de la media poblacional conforme n se acerca al infinito
#por tanto decimos que la media muestral es un estimador INSESGADO de la media poblacional.

#Generamos tres muestras aleatorias [ rnorm() ] con distinto tamaÃ±o de muestra (primer argumento), pero con la misma media (0) y desviaciÃ³n (1)
n_peque <- rnorm(5,0,1)  
n_media <- rnorm(20,0,1)
n_grande <- rnorm(300,0,1)

#Revisemos cuÃ¡l es la media computada para cada una de estas muestras y prestemos atenciÃ³n en cuÃ¡l se acerca mÃ¡s al valor real de la poblaciÃ³n de donde se extrajeron (0)
ns <- data.frame(round(cbind(mean(n_peque),mean(n_media), mean(n_grande)),3))
colnames(ns) <- c("Pequeña","Media","Grande")
print(ns)


#Según el Teorema del Límite Central:
# Los estimadores obtenidos en N muestras, presentan valores que se distribuyen normalmente cuando N tiende a infinito.

v_normal <- c(NA)   #Creamos un arreglo vacío
for(i in 1:5000){   #Que vamos a llenar con 5000 valores (que representan el nÃºmero de muestras extraÃ?das) 
  v_normal[i] <- mean(rnorm(500,0,1))      #Por cada una de esas 5000 muestras, voy a computar la media de 500 valores extraÃ?dos aleatoriamente de una distribuciÃ³n normal con media en 0 y desviaciÃ³n 1
}
#Si graficamos un histograma con todas las medias muestrales computadas, encontramos una distribuciÃ³n normal cuya media se encuentra en el valor real del parÃ¡metro a estimar (en este caso, la media poblacional previamente establecida como 0)
hist(v_normal,breaks=20, xlim=c(-0.2,0.2), main="Variable Normal", col="turquoise") 


###########################
# Métodos de Estimación Paramétrica
###########################
#Nos preparamos para imprimir 3 figuras, en 3 columnas diferentes, en una sola pantalla.
layout(matrix(1:3,ncol=3))

#Empezamos con un conjunto de datos/observaciones
x <- c(3, 1, 5, 4)   #Valores en X
y <- c(5, 1, 7, 9)   #Valores registrados de Y
plot(x,y, pch=13, cex=1.5, main="Data", cex.main=2) #Ploteamos la relaciÃ³n observada (segun los datos) entre X y Y
lines(c(1,10), c(1,19), lty=3, lwd=2) #Trazamos una línea
text(2,7, expression(paste(beta, "x")), cex=2)

d <- function(b) sum(y - x*b)^2
dMin <- optimize(d, c(0, 5))
b <- seq(0, 5, by=0.001)
dist <- sapply(b, d)
plot(b,dist, lwd=1.5, type="l", col="navy", ylab="d(beta)", xlab="beta",
     main=expression(paste("y - x",beta,"^2")))
points(dMin$minimum, dMin$objective, pch=16, col="red")
legend(0,1500, sprintf("y' = %3.1fx", dMin$minimum), lty=1, col="navy", lwd=1.5)

plot(x,y, main=expression(paste(beta, "x")), cex.main=2, pch=13, cex=1.5)
Beta <- sum(x*y) / sum(x*x)
xp<-seq(1,5,by=0.001)
yp<-xp*Beta
lines(xp, yp, col="firebrick", lwd=1.5)
text(4,2, paste("Beta =", round(Beta,3)))
legend(1,8, sprintf("y' = %3.1fx", Beta), lty=1, col="firebrick", lwd=1.5)