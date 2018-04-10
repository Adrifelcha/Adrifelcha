x <- seq(0, 1, by=0.01)
f <- 6*x*(1-x)
plot(x, f, type="l", lwd=2, ylab="", col="red")



x <- seq(0, 1, by=0.01)
f <- 6*x*(1-x)
g <- 18*x*(1-x)^4
plot(x, f, type="l", lwd=2, ylab="", ylim=c(0,1.6), col="red")
lines(x, g, lwd=2, col="blue")
legend(0.75, 1.6, c("f(x)", "g(x)"), lty=c(1,1), lwd=2, col=c("red", "blue"))


g <- function(x) 18 * x * (1-x)^4
fit <- optimize(g, c(0, 1), maximum=TRUE)
print(fit)



f1 <- function(x) {6*x*(1-x)}
integral <- integrate(f1, lower = 0, upper = 1)
print(integral)



xfx <- function(x) {6*x^2*(1-x)}
Ex <- integrate(xfx, lower = 0, upper = 1)
print(Ex)




x2fx <- function(x) {6*x^3*(1-x)}
Ex2 <- integrate(x2fx, lower = 0, upper = 1)
VarX <- Ex2$value - Ex$value^2
print(VarX)