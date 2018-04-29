###################################################
# Estimaciòn paramètrica
# EJERCICIOS
###################################################
###################################################



#  EJERCICIO 1:
#  Medidas de Tiempo : Gamma(1600,5)
###################################################
###################################################

alpha <- 1600 
beta <- 5


#Valor Esperado
ExpVal<- alpha/beta
ExpVal

#Varianza
Var <- alpha/(beta^2)
Var

#P(x>320s)
P_320 <- pgamma(320, 1600, 5, lower.tail=F)
P_320

#¿Entre qué límites se encuentra la media muestral con una probabilidad de 0,95% si n = 25?
qnorm(.95, ExpVal, sqrt(Var))
qnorm(.95, ExpVal, sqrt(Var), lower.tail = FALSE)

#Tomamos una muestra de diez personas. Obtenga la probabilidad de que cinco
#personas tarden más de 320 segundos en terminar la tarea si sus respuestas son
#esadísticamente independientes.
CincoPersonas <-  dbinom(x=5, size=10, prob=P_320)
round(CincoPersonas,4)








#  EJERCICIO 2:
#  Mètodo de los Momentos para Muestra (n=10)
###################################################
###################################################
x <- c(0.66, 0.75, 0.22, 0.79, 0.35, 0.47, 0.07, 0.04, 0.51, 0.15)

#Momentos muestrales
Media <- mean(x)
Var <- var(x)

# Asumiendo Distribucion Exponencial
w <- 1/Media

# Asumiendo Distribucion Gamma
alpha_g <- (Media^2)/(Var)
beta_g <- Media/Var

#Asumiendo Distribuciòn Beta
alpha_b <- Media*(Media*(1-Media)/Var - 1)
beta_b <- (1-Media)*(Media*(1-Media)/Var - 1)

Results <- data.frame(round(cbind(w, alpha_g , beta_g, alpha_b, beta_b),3))
colnames(Results) <- c("W", "Gamma (a)", "Gamma(B)", "Beta(a)", "Beta(B)")
Results









#  EJERCICIO 3:
#  Mìnimos Cuadrados : Regresiòn Lineal
###################################################
###################################################

#Datos
x <- c(1:10)
y <- c(0.30, 0.29, 0.37, 0.59, 0.74, 0.69, 0.84, 0.99, 0.92, 0.95)
plot(x,y, xlim = c(0,10), ylim=c(0,1), pch=15, main="Datos")

#Minimizamos el error entre los datos y la prediccion de nuestra funcion
funcion <- function(v) sum((y - exp(v[1] + v[2]*x)/(1+exp(v[1] + v[2]*x)))^2)
dMin <- optim(c(0,0), funcion)

MinimosCuadrados <- data.frame(round(cbind(dMin$par[1],dMin$par[2]),3))
colnames(MinimosCuadrados) <- c("alpha", "beta")
MinimosCuadrados

#Sustituimos los valores estimados en nuestra funcion para todas las X Posibles
x_inf <- seq(0,10,.001)
sustitucion<- exp(dMin$par[1] + dMin$par[2]*x_inf)/(1+exp(dMin$par[1] + dMin$par[2]*x_inf))

#Ploteamos nuestra estimacion por el metodo de Minimos Cuadrados
plot(x,y, xlim = c(0,10), ylim=c(0,1), pch=15, main="Estimación") 
lines(x_inf, sustitucion, col="firebrick", lwd=3)

#Proporción de Varianza Explicada
Razon <- var(sustitucion)/var(y)
round(Razon,5)
