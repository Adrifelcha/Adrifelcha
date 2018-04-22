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







#########################################
# Ejercicio 3 -

a_True <- 5
b_True <- 2
alpha <- function(m,v) m *(m*(1-m)/v - 1)
beta <- function(m,v) (1-m)*(m*(1-m)/v - 1)
n <- 100
muestras <- 200
a_Estimada <- rep(0, muestras)
b_Estimada <- rep(0, muestras)

for(muestra in 1:muestras){
  x <- rbeta(n, a_True, b_True)
  media <- mean(x)
  varianza <- var(x)
  a_Estimada[muestra] <- alpha(media, varianza)
  b_Estimada[muestra] <- beta(media, varianza)
}
media_a <- mean(a_Estimada)
media_b <- mean(b_Estimada)
se_a <- sd(a_Estimada)
se_b <- sd(b_Estimada)
correlacion <- cor(a_Estimada,b_Estimada)
cat(sprintf(
  "N = %1.0f, media alpha = %6.4f, Se alpha = %6.4f, media beta = %6.4f, Se beta = %6.4f, r = %5.3f",
  n, media_a, se_a, media_b, se_b, correlacion))
## N = 100, media alpha = 5.2041, Se alpha = 0.8397, media beta = 2.0669, Se beta = 0.3120, r = 0.863
par(mfrow=c(1,2))
hist(a_Estimada, main="alpha")
hist(b_Estimada, main="beta")

