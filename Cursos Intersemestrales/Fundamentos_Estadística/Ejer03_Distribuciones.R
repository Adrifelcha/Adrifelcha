#################
#### Ejercicios 3: 
####       Distribuciones de probablidad
#################
#################




###############################################################################
# Ejercicio 1, a resolver analíticamente (Extra)
###############################################################################
########   Tome la siguiente funcion de densidad definida en el intervalo (0,1)
g <- function(x) (3/8)*((4*x)-((2*(x^2)))) 

#Represente gráficamente la función
plot(g, type="l", lwd=4, col="forestgreen", main="Función de densidad g(x)",
     lty=3, ylab="Densidad", xlab="x", xlim=c(0,2))   #Ploteamos la relaciÃ³n x-y

#Obtenga el Valor Esperado
Test_Distr <- integrate(g, lower = 0, upper = 2)  #But is it actually a distribution?
print(Test_Distr)

xfx <- function(x){3*(4*x^2 - 2*x^3)/8}
Ex_1 <- integrate(xfx, lower = 0, upper = 2)
print(Ex_1)

Pr <- integrate(g, lower = 1, upper = 2)
print(Pr)

##### IMPRIMIMOS LOS RESULTADOS 
Estimaciones <- data.frame(round(cbind(Ex_1$value, Pr$value),3))
colnames(Estimaciones) <- c("V. Esperado","P(X > 1)")
print(Estimaciones)







###############################################################################
# Ejercicio 2, "Resuelva en R"
###############################################################################
########   Tome la siguiente funcion de densidad definida en el intervalo (0,1)
x <- 0:12
f <- dpois(x, 12)

#Represente gráficamente la función
plot(f, type="l", lwd=4, col="turquoise", main="Función de densidad f(x) Poisson",
     lty=3, ylab="Densidad", xlab="x")   #Ploteamos la relaciÃ³n x-y

#Obtenga los centiles 5 y 95
val_1 <- qpois(0.05, 12)
val_2 <- qpois(0.95, 12)
print(c(val_1,val_2))


#La probabilidad de que x>15
Pr15 <- ppois(15,12,lower.tail=F)

Pr15_2 <- ppois(15,10,lower.tail=F)

##### IMPRIMIMOS LOS RESULTADOS 
Estimaciones <- data.frame(cbind(val_1, val_2, Pr15, Pr15_2))
colnames(Estimaciones) <- c("5%", "95%", "P(15)", "P(15,lambda)")
print(Estimaciones)











###############################################################################
# Ejercicio 3, "Ejercicio de simulaciòn"
###############################################################################
########   Tome la siguiente funcion de densidad definida en el intervalo (0,1)
m <- function(x) dbeta(x, 5, 2)

muestras <- 200
tamano_m <-  100

dat <- rbeta(muestras*tamano_m, 5, 2)
muestra <- matrix(dat, ncol=n)
medias <- colMeans(muestra)
hist(medias, ylab="Frecuencia", main=
       sprintf("Media = %10.2f, Sd = %4.2f", mean(medias), sd(medias)))


#Represente gráficamente la función
plot(m, type="l", lwd=4, col="purple", main="Función de densidad f(x)",
     lty=3, ylab="Densidad", xlab="x")   #Ploteamos la relaciÃ³n x-y

#Obtenga el Valor Esperado
Test_Distrib <- integrate(m, lower = 0, upper = 1)  #But is it actually a distribution?
print(Test_Distrib)


