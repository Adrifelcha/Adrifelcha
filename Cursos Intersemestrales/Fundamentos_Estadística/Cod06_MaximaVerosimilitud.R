###################################################
# Màxima Verosimilitud
# Mètodo de los momentos y Mìnimos Cuadrados
###################################################

plot(c(1:100), dbinom(c(1:100), 100, .1), type='l', ylim=c(0,.14), main="p(x | n=10, p)", cex.main=2)
lines(c(1:100), dbinom(c(1:100), 100, .2))
lines(c(1:100), dbinom(c(1:100), 100, .3))
lines(c(1:100), dbinom(c(1:100), 100, .4))
lines(c(1:100), dbinom(c(1:100), 100, .5))
lines(c(1:100), dbinom(c(1:100), 100, .6))
lines(c(1:100), dbinom(c(1:100), 100, .7))
lines(c(1:100), dbinom(c(1:100), 100, .8))
lines(c(1:100), dbinom(c(1:100), 100, .9))
