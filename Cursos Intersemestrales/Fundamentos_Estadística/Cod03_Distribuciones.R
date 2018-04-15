#####################
###### Distribuciòn 2
###### Binomial
#####################
n <- 100
x <- c(0:n)
p <- 0.2

ExV <- n*p

layout(matrix(1:2,ncol=2))
Ex_Binom <- dbinom(x, size=n, prob=p)
plot(x,Ex_Binom, xlim= c(0,ExV*2), main="Distribuciòn Binomial",cex.main=1.7, type='l',lwd=2,col='purple', xlab="Numero de exitos", ylab="Probabilidad (#Exitos | n=10, Wi)",cex.lab=1.2)

barplot(Ex_Binom, main= "Distribución binomial", col=rainbow(length(x)))


layout(matrix(1:1,ncol=1))
#####################
###### Distribuciòn 3
###### Poisson
#####################
f1 <- dpois(y,4)
barplot(f1, main="Distribución Poisson")

#####################
###### Distribuciòn 4
###### Normal
#####################
mean <- 0
sDev <- 1
Ex_Norm <- function(x) dnorm(x, mean, sDev)

plot(Ex_Norm, main = "Distribuciòn Normal", ylab="", xlab="", xlim=c(-6,6))

#####################
###### Distribuciòn 5
###### Exponencial
#####################
w <- 4
Ex_exp <- function(x) dexp(x, w)

plot(Ex_exp, main = "Distribuciòn Exponencial", ylab="", xlab="", xlim=c(0,5), ylim=c(0,10))


#####################
###### Distribuciòn 6
###### Gamma
#####################
a <- 4
b <- 2
Ex_gamma <- function(x) dgamma(x, a, b)

plot(Ex_gamma, main = "Distribuciòn Gamma", ylab="", xlab="", xlim=c(0,6))



#####################
###### Distribuciòn 7
###### Beta
#####################
a <- 1
b <- 1
Ex_gamma <- function(x) dbeta(x, a, b)

plot(Ex_gamma, main = "Distribuciòn Beta", ylab="", xlab="", xlim=c(0,1))





#####################
###### Código 1
###### Distribución Exponencial
#####################

f <- function(w) w^3 * exp(-w * 6)
loga <- function(w) 3*log(w) - w*6
fMax <- optimize(f, c(0, 2), maximum=TRUE)
lMax <- optimize(loga, c(0, 2), maximum=TRUE)
plot(f, type="l", lwd=2, ylab="", ylim=c(0,0.0065), col="red", main = "Exponencial")
plot(loga, type="l", lwd=2, ylab="", ylim=c(-15,-5), col="purple", main = "Log(Exponencial)")
legend(0.75, 1.6, c("f(x)", "g(x)"), lty=c(1,1), lwd=2, col=c("red", "blue"))

print(fMax)
print(lMax)

#####################
###### Código 2
###### Distribuciòn Beta
#####################
muestra <- c(rep(0.1,30), rep(0.2,30), rep(0.3,30), rep(0.4,30), rep(0.5,30), rep(0.6,30), rep(0.7,30), rep(0.8,30), rep(0.9,30), rep(1,30))

alpha <- function(m,v) m *(m*(1-m)/v - 1)
beta <- function(m,v) (1-m)*(m*(1-m)/v - 1)
asimetria <- function(a,b) 2*(b-a)*sqrt(a+b+1)/((a+b+2)*sqrt(a*b))
media <- mean(muestra)
varianza <- var(muestra)
a <- alpha(media, varianza)
b <- beta(media, varianza)
cat(sprintf(
  "Los datos de la muestra son: media = %20.4f, varianza = %6.4f y asimetría = %6.4f.
Los parámetros estimados son: alpha = %6.4f y beta = %6.4f.",
  media, varianza, asimetria(a,b), a, b))

plot(function(x) dbeta(x, a, b), main = "Beta", ylab="", xlab="")
 
## Valor esperado
xfx <- function(x) x * dbeta(x, 2, 3)
Ex <- integrate(xfx, lower = 0, upper = 1)
print(Ex)



############ Trabajando con funciones en R

####### Funciones de probabilidad (d)
par(mfrow=c(1,2))
y <- 0:10
f1 <- dpois(y,4)
barplot(f1, names=as.character(y), main="Poisson(4)")
x <- seq(0, 10, by=0.001)
f2 <- dchisq(x,4)
plot(x, f2, type="l", lwd=1.5, col="darkblue", main="chi-cuadrado(4)", xlab="", ylab="")

####### Funciones de distribuciòn (p)
pbinom(5, 10, 0.5, lower.tail=FALSE)

####### Phi inversa (q)
qnorm(0.05, lower.tail=FALSE)


####### Muestreo aleatorio (r)
muestra <- rpois(100, 15)
cat(sprintf("La media es %5.2f y la varianza %5.2f", mean(muestra), sd(muestra)))


n <- 50
muestras <- 1000
dat <- rbeta(muestras*n, 0.5, 0.5)
muestra <- matrix(dat, ncol=n)
medias <- colMeans(muestra)
hist(medias, ylab="Frecuencia", main=
       sprintf("Media = %10.2f, Sd = %4.2f", mean(medias), sd(medias)))




muestras <- 1000
vectorMedias <- rep(0, 1000)
for(muestra in 1:muestras){
  vectorMedias[muestra] <- mean(rchisq(50, 10))
}
cat(sprintf("La media es %5.2f y la varianza %5.2f", mean(vectorMedias), var(vectorMedias)))





muestras <- 1000
vectorMedias <- replicate(muestras, mean(rchisq(50, 10)))
cat(sprintf("La media es %5.2f y la varianza %5.2f", mean(vectorMedias), var(vectorMedias)))








