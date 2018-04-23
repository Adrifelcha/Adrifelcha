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
# Ejercicio 3, "Recuperación de parámetros
###############################################################################

#Genere 200 muestras de tamaño 100 a partir de una Beta (5,2) y recupere el valor de 
#los paràmetros que mejor describan las muestras extraidas


#Empezamos definiendo el àrea de trabajo 
a_True <- 5     #Defino los valores conocidos para alpha y beta poblacional
b_True <- 2
alpha <- function(m,v) m *(m*(1-m)/v - 1)    #Defino las funciones que permiten estimar a y b
beta <- function(m,v) (1-m)*(m*(1-m)/v - 1)  #a partir de la media y la varianza de la muestra


muestras <- 200    #Fijo el nùmero de muestras a realizar m
n <- 100           #cada una con un tamaño n

a_Estimada <- rep(0, muestras)  #Creamos dos arreglos vacíos a rellenar con un ciclo for
b_Estimada <- c(NA)


for(muestra in 1:muestras){          #Por cada muestra en el intervalo 1:muestras
  x <- rbeta(n, a_True, b_True)      #obtendré un conjunto de datos extraidos de una distribucion beta con los parametros definidos para mi poblacion
  media <- mean(x)        #Y de cada una de estas 200 muestras, obtendré una media
  varianza <- var(x)      # y una desviación estándar
  
  a_Estimada[muestra] <- alpha(media, varianza) #La media y la varianza de cada muestra me ayudará a generar un estimado
  b_Estimada[muestra] <- beta(media, varianza)  #sobre los valores de alfa y beta, según las funciones previamente especificadas
}

media_a <- mean(a_Estimada)   #Computamos la media de todas las estimaciones hechas para alfa y beta
media_b <- mean(b_Estimada)
se_a <- sd(a_Estimada)        #Y tambiñen computamos la desviación estándar de estos estimados (qué tano varían)
se_b <- sd(b_Estimada)
correlacion <- cor(a_Estimada,b_Estimada)    #Computamos la correlación entre los estimados realizados para a y b


#Enunciamos nuestros cómputos
cat(sprintf(
  "N = %1.0f, media alpha = %6.4f, Se alpha = %6.4f, media beta = %6.4f, Se beta = %6.4f, r = %5.3f",
  n, media_a, se_a, media_b, se_b, correlacion))


#Graficamos la Recuperación Paramétrica
par(mfrow=c(1,3)) #Pedimos dibujar hasta tres gráficas por pantalla
hist(a_Estimada, main="alpha")     #Empezamos mostrando un histograma con las estimaciones hechas para a por cada muestra
hist(b_Estimada, main="beta")      #...y lo mismo para las estimaciones de b
#(Nota que tienen su pico más alto en los valores reales (poblacionales) de a y b)
plot(a_Estimada, b_Estimada) #Ploteamos la correlacion entre 
