rm(list=ls())
h <- .952
f <- .011

k_hat <- qnorm(1-f,0,1)
d_hat <- qnorm(h,0,1)-qnorm(f,0,1)
center_hat <- k_hat-(d_hat/2)
beta_hat <- dnorm(k_hat,d_hat,1)/dnorm(k_hat,0,1)


soporte <- seq(-10,10,.05)
d_ruido <- dnorm(soporte,0,1)
d_senal <- dnorm(soporte,d_hat,1)
plot(soporte,d_ruido,type='l')
lines(soporte,d_senal,type='l',col='blue')
abline(v=k_hat,col='red')