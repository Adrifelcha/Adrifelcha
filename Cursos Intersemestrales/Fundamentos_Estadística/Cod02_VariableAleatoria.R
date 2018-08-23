#Material de apoyo para Introducción a Variables Aleatorias
#Autor: Adriana F. Chávez De la Peña
#adrifelcha@gmail.com
##########################################################

#####################
###### Código 1
###### Representación gráfica de una función
#####################

x <- seq(0, 1, by=0.01)   #Definimos la recta real  
f <- 6*x*(1-x)            #Especificamos la función y=f(x)
plot(x, f, type="l", lwd=2, ylab="", col="red", main="Función cuadratica")   #Ploteamos la relación x-y


#####################
###### Código 2
###### Representación de dos funciones (simultáneamente)
#####################

x <- seq(0, 1, by=0.01)     #Recta real
f <- 6*x*(1-x)              #Función 1
g <- 18*x*(1-x)^4           #Funciión 2
plot(x, f, type="l", lwd=2, ylab="", ylim=c(0,1.6), col="red")      #Ploteamos el valor asignado por la función f a cada valor de la secuencia x
lines(x, g, lwd=2, col="blue")   #Sobreponemos una líea que represente Función 2    (el valor asignado por la función g a cada valor contenido en x)
legend(0.75, 1.6, c("f(x)", "g(x)"), lty=c(1,1), lwd=2, col=c("red", "blue"))     #Añadimos un recuadro/leyenda que señale a qué corresponde cada líea. Separamos los elementos en un arreglo.


#####################
###### Código 3
###### Encontrar el punto máximo de una función (Moda)
#####################
g <- function(x) 18 * x * (1-x)^4  #Especificamos la función
fit <- optimize(g, c(0, 1), maximum=TRUE)   #Usamos la función optimize para obtener el punto máximo (maximum=TRUE) de la función g, en el intervalo 0 y 1
print(fit)  #Imprimimos el elemento fit 

plot(g, type="l", lwd=2, ylab="", col="purple")   #Ploteamos la relación x-y definida por g
points(fit$maximum,fit$objective, col="red", pch=16, cex=2)
points(fit$maximum,0, col="red", pch=16, cex=2)
lines(c(fit$maximum,fit$maximum), c(0,fit$objective), lwd=2, lty=2, col="black")
#En este caso, no hizo falta crear una base para ,la gráfica (un elemento x definido como una secuencia de valores) porque g ya estaba definido como una función de x



#####################
###### Código 4
###### Evaluar una función de densidad
#####################

f1 <- function(x) {6*x*(1-x)}       #Especificamos la funciÃ³n 
integral <- integrate(f1, lower = 0, upper = 1)      #Integramos la funciÃ³n anteriormente definida en el intervalo 0  a 1
print(integral)   #Imprimimos el resultado de la integral


#####################
###### Código 5
###### Valor Esperado y Varianza
#####################

#El valor esperado de una distribución contínua se computa como la integral de la función x * f(x) definida en el intervalo X

xfx <- function(x) {6*x^2*(1-x)}               #Escribimos x * f(x)
Ex <- integrate(xfx, lower = 0, upper = 1)     #Integramos la función previamente descrita en el intervalo 0 y 1
print(Ex)   #Imprimimos el resultado de la integral

#La varianza de una distribución contínua se computa como la diferencia entre el valor esperado de x^2 (el momento de segundo orden centrado en el origen)
# y el valor esperado (la media poblacional; el momento de primer orden centrado en el origen)
x2fx <- function(x) {6*x^3*(1-x)}   #Función que nos ayudará a computar el momento de segundo orden centrado en el origen (x^2 * f(x))
Ex2 <- integrate(x2fx, lower = 0, upper = 1)   #Computamos la esperanza de la función previamente descrita, a partir de una integral definida en el intervlo 0-1
VarX <- Ex2$value - Ex$value^2   #Estimamos la varianza a partir de la diferencia
print(VarX) #Imprimimos el valor de la varianza.


#Con la función integrate podemos conocer la densidad de probabilidad acumulada en un intervalo particular
#a partir de una integral definida entre los dos extremos del intervalo a evaluar.

Pr <- integrate(f1, lower = 0.75, upper=1)
print(Pr)


plot(f1, type="l", lwd=2, ylab="", col="black", xlim=c(0,1), ylim=c(0,1.5))   #Ploteamos la función original
text(0.15,1, "Función")
points(Ex$value,0, pch=17)    # Señalamos el Valor Esperado (Media poblacional)
lines(c(Ex$value, Ex$value), c(0,1.5), lwd=2, lty=3, col="red")    # Ubicamos la densidad de probabilidad asignada al valor esperado
intervalo <- seq(0.75,1,by=0.005)
a <- 0
for(i in 1:length(intervalo)){
  polygon(c(intervalo[i],intervalo[i]),c(0,
  6*intervalo[i]*(1-intervalo[i])),border="forestgreen")
}
lines(c(0.75,1), c(0.01,0.01), lwd=3, lty=2, col="forestgreen") 
lines(c(0.75,0.75), c(0,f1(0.75)), lwd=3, lty=6, col="forestgreen")
text(Ex$value + 0.09, 1, "E(x) ó Valor Esperado", col="red")   #Imprimimos una etiqueta sobre la gráfica
text(0.85, 1.2, paste("F(1) - F(0.75) =",round(Pr$value,3)), col="darkgreen", f=2)   #Imprimimos una etiqueta sobre la gráfica