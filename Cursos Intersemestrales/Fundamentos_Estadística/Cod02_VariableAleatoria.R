#####################
###### Código 1
###### Representación gráfica de una función
#####################

x <- seq(0, 1, by=0.01)   #Definimos la recta real
f <- 6*x*(1-x)            #Especificamos la funcion y=f(x)
plot(x, f, type="l", lwd=2, ylab="", col="red")   #Ploteamos la relación x-y


#####################
###### Código 2
###### Representación de dos funciones (simultáneamente)
#####################

x <- seq(0, 1, by=0.01)     #Recta real
f <- 6*x*(1-x)              #Función 1
g <- 18*x*(1-x)^4           #Función 2
plot(x, f, type="l", lwd=2, ylab="", ylim=c(0,1.6), col="red")
lines(x, g, lwd=2, col="blue")   #Sobreponemos una línea que represente Función 2
legend(0.75, 1.6, c("f(x)", "g(x)"), lty=c(1,1), lwd=2, col=c("red", "blue"))


#####################
###### Código 3
###### Encontrar el punto máximo de una función (Moda)
#####################
g <- function(x) 18 * x * (1-x)^4
fit <- optimize(g, c(0, 1), maximum=TRUE)
print(fit)

plot(g, type="l", lwd=2, ylab="", col="purple")   #Ploteamos la relación x-y



#####################
###### Código 1
#####################

f1 <- function(x) {6*x*(1-x)}
integral <- integrate(f1, lower = 0, upper = 1)
print(integral)


#####################
###### Código 1
#####################
xfx <- function(x) {6*x^2*(1-x)}
Ex <- integrate(xfx, lower = 0, upper = 1)
print(Ex)




x2fx <- function(x) {6*x^3*(1-x)}
Ex2 <- integrate(x2fx, lower = 0, upper = 1)
VarX <- Ex2$value - Ex$value^2
print(VarX)