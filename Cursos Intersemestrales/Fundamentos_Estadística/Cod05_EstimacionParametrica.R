###################################################
# Estimaciòn paramètrica
# Mètodo de los momentos y Mìnimos Cuadrados
###################################################


###################################################
# Parte 1:    Método de los momentos
###################################################


########  Estimaciòn de una distribucón Gamma
x = c(5, 3, 7, 9, 1)
media <- mean(x)
varianza <- var(x)
alpha_Momentos <- media^2 / varianza
beta_Momentos <- media / varianza

gamma <- data.frame(cbind(alpha_Momentos,beta_Momentos))
colnames(gamma) <- c("Alpha", "Beta")
gamma


# Estimaciòn Gamma restringida
alpha_Momentos_R <- 16 / varianza
beta_Momentos_R <- 4 / varianza
cat(sprintf("Metodo de los momentos, modelo restringido, a = %5.2f, b = %5.2f",
            alpha_Momentos_R, beta_Momentos_R))
cat(sprintf("Media observada = %5.2f, reproducida = %5.2f",
            mean(x), alpha_Momentos_R/beta_Momentos_R))


gamma <- data.frame(cbind(alpha_Momentos_R,beta_Momentos_R, alpha_Momentos_R/beta_Momentos_R, mean(x)))
colnames(gamma) <- c("Alpha Predicha", "Beta Predicha", "Mu predicha", "Media observada")
gamma




###################################################
# Parte 2: Método de los mínimos cuadrados
###################################################
layout(matrix(1:3,ncol=3))
x <- c(3, 1, 5, 4)
y <- c(5, 1, 7, 9)
plot(x,y, pch=13, cex=1.5, main="Data", cex.main=2)
lines(c(1,10), c(1,19), lty=3, lwd=2)
text(2,7, expression(paste(beta, "x")), cex=2)

d <- function(b) sum(y - x*b)^2
dMin <- optimize(d, c(0, 5))
b <- seq(0, 5, by=0.001)
dist <- sapply(b, d)
plot(b,dist, lwd=1.5, type="l", col="navy", ylab="d(beta)", xlab="beta",
     main=expression(paste("y - x",beta,"^2")))
points(dMin$minimum, dMin$objective, pch=16, col="red")
#lines(c(dMin$minimum,dMin$minimum), c(2,2), lwd=25)
legend(0,1500, sprintf("y' = %3.1fx", dMin$minimum), lty=1, col="navy", lwd=1.5)



plot(x,y, main=expression(paste(beta, "x")), cex.main=2, pch=13, cex=1.5)
Beta <- sum(x*y) / sum(x*x)
xp<-seq(1,5,by=0.001)
yp<-xp*Beta
lines(xp, yp, col="firebrick", lwd=1.5)
text(4,2, paste("Beta =", round(Beta,3)))
legend(1,8, sprintf("y' = %3.1fx", Beta), lty=1, col="firebrick", lwd=1.5)





######## Ejemplo paso a paso
#Empezamos nuestro código especificando el escritorio de trabajo (Working directory: wd)
setwd("C:/Users/sandra/Desktop/Felisa/Cursos Intersemestrales/Fundamentos_Estadística")
#Borramos todas las variables y valores almacenados en consola
rm(list=ls())
#Comprobamos los archivos contenidos en nuestro wd
dir()
layout(matrix(1:2,ncol=2))
#Identificamos el archivo que contiene los datos a trabajar
datos <-'LeastSquare.csv'
datos <- read.csv(datos)

x <- datos$Experiencia
y <- datos$Salario

plot(x,y, pch=16, main="Relaciòn Salario x Años de Experiencia", xlab="Años de experiencia",
     ylab="Salario", col=rainbow(length(y)))


x_Meanx <-  c(NA)
y_Meany <- c(NA)
XMeanx_YMeany <- c(NA)
Sq_x_Meanx <- c(NA)

for (a in 1:length(x)){
x_Meanx[a] <- x[a]-mean(x) 
y_Meany[a] <- y[a]-mean(y)
XMeanx_YMeany[a] <- (x[a]-mean(x))*(y[a]-mean(y))
Sq_x_Meanx[a] <-(x[a]-mean(x))^2
}

computo <- data.frame(round(cbind(x,y,x_Meanx,y_Meany, Sq_x_Meanx, XMeanx_YMeany),3))
colnames(computo) <- c("X","Y","X-mean(X)","y-mean(Y)","X-mean(X)^2", "(X-mean(X))(y-mean(y))")
computo

b <- (sum(XMeanx_YMeany))/(sum(Sq_x_Meanx))
a <- mean(y)-(b*mean(x))

plot(x,y, pch=16, main="Minimos Cuadrados", xlab="Años de experiencia",
     ylab="Salario", col=rainbow(length(y)))
lines(c(0:20), a+(b*c(0:20)), lwd=2, lty=2)
text(4,18, paste("a=", round(a,3)))
text(4,16, paste("b=", round(b,3)))








###################
# Ejemplo 2 : Presentando la función Optim
layout(matrix(1:2,ncol=2))
x <- c(2, 4, 3, 5)
y <- c(5, 8, 7, 10)
plot(x,y, pch=16, cex=1.2, col="black", main="Datos", cex.main=2)


d <- function(v) sum(y - v[1] - x*v[2])^2
dMin <- optim(c(0,0), d)
dMin


plot(x,y, pch=16, cex=1.2, col="black", main="Minimo Cuadrado", cex.main=2)
lines(x, 0.5521 + (1.984*x), col='purple', lwd=1.5)






##########################
# Ejemplo 2 : Stevens
layout(matrix(1:2,ncol=2))
x <- c(5, 8, 3, 4)
y <- c(72, 196, 22, 50)
plot(x,y, pch=16, cex=1.2, col="black", main="Datos", cex.main=2)



d <- function(v) sum(y - v[1]*x^v[2])^2
dMin <- optim(c(0,0), d)
print(dMin)
plot(x,y, pch=16, cex=1.2, col="black", main="Minimo Cuadrado", cex.main=2)
lines(x, (7.747749*x)^1.460461)



