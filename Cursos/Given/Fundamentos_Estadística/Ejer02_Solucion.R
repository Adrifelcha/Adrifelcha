fx <- function(x) 30*x*(1-x)^4
fit <- optimize(fx, c(0, 1), maximum=TRUE)

f1 <- function(x){30*x^2*(1-x)^4}
f2 <- function(x){30*x^3*(1-x)^4}
Ex <- integrate(f1, lower = 0, upper = 1)
Ex2 <- integrate(f2, lower = 0, upper = 1)
Varx <- Ex2$value - Ex$value^2
Pr <- integrate(fx, lower = 0.25, upper = 0.75)
x <- seq(0, 1, 0.001)
f <- fx(x)
plot(x, f, type="l", lwd=2, col="gold3")
cat(sprintf("E(X) = %5.3f, Var(X) = %5.3f, Moda(X) = %5.3f, Pr =
            %5.3f\n", Ex$value, Varx, fit$maximum, Pr$value))



f1 <- function(x){1.5*x^1.5}
f2 <- function(x){1.5*x^0.5}
Ex <- integrate(f1, lower = 0, upper = 1)
Pr <- integrate(f2, lower = 0.5, upper = 1)
cat(sprintf("Tiempo esperado %3.1f minutos, Pr = %5.3f\n",
            60*Ex$value, Pr$value))

plot(f1)