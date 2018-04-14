#################
#### Ejercicios 2: 
####       Variables Aleatorias
#################
#################




###############################################################################
# Ejercicio 1, a resolver analíticamente (Extra)
###############################################################################
########   Tome la siguiente funcion de densidad definida en el intervalo (0,1)
g <- function(x) 6*x*(1-x) 

#Represente gráficamente la función
plot(g, type="l", lwd=4, col="forestgreen", main="Función de densidad g(x)",
     lty=3, ylab="Densidad", xlab="x")   #Ploteamos la relaciÃ³n x-y

#Obtenga la moda de g(x)
fit <- optimize(g, c(0, 1), maximum=TRUE)
print(fit)


#Obtenga el Valor Esperado
Test_Distr <- integrate(g, lower = 0, upper = 1)  #But is it actually a distribution?
print(Test_Distr)

xfx <- function(x) {6*x^2*(1-x)}
Ex <- integrate(xfx, lower = 0, upper = 1)
print(Ex)

##### IMPRIMIMOS LOS RESULTADOS 
Estimaciones <- data.frame(round(cbind(Ex$value, fit$maximum),3))
colnames(Estimaciones) <- c("V. Esperado","Moda")
print(Estimaciones)







###############################################################################
# Ejercicio 2, "Resuelva en R"
###############################################################################
########   Tome la siguiente funcion de densidad definida en el intervalo (0,1)
f <- function(x) 30*x*(1-x)^4 

#Represente gráficamente la función
plot(f, type="l", lwd=4, col="turquoise", main="Función de densidad f(x)",
     lty=3, ylab="Densidad", xlab="x")   #Ploteamos la relaciÃ³n x-y

#Obtenga el Valor Esperado
Test_Distr <- integrate(f, lower = 0, upper = 1)  #But is it actually a distribution?
print(Test_Distr)

xfx <- function(x) {30*x^2*(1-x)^4}
Ex <- integrate(xfx, lower = 0, upper = 1)
print(Ex)

#Obtenga la Varianza
x2fx <- function(x) {30*x^3*(1-x)^4}
Ex2 <- integrate(x2fx, lower = 0, upper = 1)
VarX <- Ex2$value - Ex$value^2
print(VarX)

#Obtenga la moda de X
fit <- optimize(f, c(0, 1), maximum=TRUE)
print(fit)

#Proabilidad acumulada entre .25 y .75
integral <- integrate(f, lower = 0.25, upper = 0.75)
print(integral)

##### IMPRIMIMOS LOS RESULTADOS 
Estimaciones <- data.frame(round(cbind(Ex$value, VarX, fit$maximum, integral$value),3))
colnames(Estimaciones) <- c("V. Esperado","Varianza","Moda", "P. Acumulada")
print(Estimaciones)











###############################################################################
# Ejercicio 3, "Resuelva analíticamente y en R"
###############################################################################
########   Tome la siguiente funcion de densidad definida en el intervalo (0,1)
x <- seq(0, 1, 1)
m <- function(x) (3*x^(1/2))/2

#Represente gráficamente la función
plot(m, type="l", lwd=4, col="purple", main="Función de densidad f(x)",
     lty=3, ylab="Densidad", xlab="x")   #Ploteamos la relaciÃ³n x-y

#Obtenga el Valor Esperado
Test_Distrib <- integrate(m, lower = 0, upper = 1)  #But is it actually a distribution?
print(Test_Distrib)


xfx <- function(x) {(3*x^(3/2))/2}
Ex <- integrate(xfx, lower = 0, upper = 1)
print(Ex)
Ex_mins <- Ex$value*60
print(Ex_mins)

#Proabilidad acumulada para x>.5
integral <- integrate(m, lower = 0.5, upper = 1)
print(integral)

##### IMPRIMIMOS LOS RESULTADOS 
Estimaciones <- data.frame(round(cbind(Ex$value, integral$value),3))
colnames(Estimaciones) <- c("V. Esperado","P. Acumulada")
print(Estimaciones)

