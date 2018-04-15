#####################
###### Código 1
###### Representación gráfica de una función
#####################

f <- function(w) w^3 * exp(-w * 6)
loga <- function(w) 3*log(w) - w*6
fMax <- optimize(f, c(0, 2), maximum=TRUE)
lMax <- optimize(l, c(0, 2), maximum=TRUE)
plot(f, type="l", lwd=2, ylab="", ylim=c(0,1.6), col="red")
lines(seq(0,1,.01),loga, lwd=2, col="blue")   #Sobreponemos una línea que represente Función 2
legend(0.75, 1.6, c("f(x)", "g(x)"), lty=c(1,1), lwd=2, col=c("red", "blue"))

print(fMax)
print(lMax)