########################################
# Ejercicios : Teorìa de muestras grandes
########################################


##################################################
# Ejercicio 1: Distribución tipo PARETO
##################################################

# 1.- Grafique la función para valores de a 1,2,3
f <- function(x,a){a/x^{a+1}}

x <- seq(1, 2.5, 0.001)

f1 <- f(x,a=2)
f2 <- f(x,a=3)
f3 <- f(x,a=4)
plot(x, f1, col="cyan", lwd=3, type="l", xlab="X", ylab="f(x)")
lines(x,f2, col="blue", lwd=3)
lines(x,f3, col="navyblue", lwd=3)
legend(2.25, .85, c("a = 1", "a = 2", "a = 3"), lty=c(1,1), lwd=2, col=c("cyan", "blue", "navyblue"))


# 4.- Obtenga la probabilidad de X>2 si a=2

f <- function(x){2/x^3}
Pr <- integrate(f, 2, Inf)
cat(sprintf("P(X > 2) = %4.2f", Pr$value))






#############################################
# Ejercicio 3: Recuperación de parámetros gamma (2, 2)
#############################################

a_True <- 2         #Valores reales de alfa y beta
b_True <- 2
alpha <- function(m,v) m^2/v          #Especificamos las funciones que las definen
beta <- function(m,v) m/v

n <- 100                #Tamaño de cada muestra
muestras <- 200         #Nùmero de muestras
a_Estimada <- rep(0, muestras)        #Creamos dos arreglos vacíos que llenaremos con un For
b_Estimada <- rep(NA)

for(muestra in 1:muestras){         #Para cada una de nuestras muestras
  x <- rgamma(n, a_True, b_True)    #Obtendremos un arreglo x con 100 elementos 
                                    #extraidos de una gamma con los valores reales de alfa y beta
  media <- mean(x)     #Obtenemos la media de esa muestra particular
  varianza <- var(x)   #Obtenemos la varianza
  a_Estimada[muestra] <- alpha(media, varianza)     #Con estas, estimamos un alpha y beta por cada
  b_Estimada[muestra] <- beta(media, varianza)      #muestra extraìda
}

media_a <- mean(a_Estimada)    # Obtenemos el promedio de las alphas computadas por cada muestra
media_b <- mean(b_Estimada)   #... y de las betas
se_a <- sd(a_Estimada)        #Obtenemos sus desviaciones estandar
se_b <- sd(b_Estimada)

par(mfrow=c(1,3))     #Graficamos tres plots por pantalla
hist(a_Estimada, main="alpha")    #El primero, con todas las a estimadas por muestra
hist(b_Estimada, main="beta")     #El segundo, con todas las b
plot(a_Estimada, b_Estimada)      #Finalmente, la correlacion entre a y b estimadas

correlacion <- cor(a_Estimada,b_Estimada) #Valuamos el indice de correlacion
correlacion

#Computamos los Root Mean Square Error
#La raíz cuadrada deEl promedio de las diferencias entre cada estimacion y el valor real al vuadrado)
rmse_a <- sqrt(mean((a_Estimada - a_True)^2))
rmse_b <- sqrt(mean((b_Estimada - b_True)^2))
#el RMSE nos indica qué tanto se aleja un estimado del valor real al que queríamos llegar

#Enunciamos nuestros computos
cat(sprintf(
  "N = %1.0f, media alpha = %6.4f, Se alpha = %6.4f, RMSE(a) = %6.4f,
 media beta = %6.4f, Se beta = %6.4f, RMSE(b) = %6.4f, r = %5.3f",
  n, media_a, se_a, rmse_a, media_b, se_b, rmse_b, correlacion))

