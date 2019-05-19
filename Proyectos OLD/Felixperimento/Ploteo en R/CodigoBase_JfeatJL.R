rm(list=ls())                                               #borrar datos previos
h <- .839                                                   #definir hit rate
f <- .172                                                   #definir false alarm rate
k_hat <- qnorm(1-f,0,1)                                     #crear k
d_hat <- qnorm(h,0,1)-qnorm(f,0,1)                          #crear d'
center_hat <- k_hat-(d_hat/2)                               #calcular c
beta_hat <- dnorm(k_hat,d_hat,1)/dnorm(k_hat,0,1)           #calcular beta
soporte <- seq(-6,5,.01)                        #definir base de la gráfica
d_ruido <- dnorm(soporte,0,1)                               #distribución de ruido
d_senal <- dnorm(soporte,d_hat,1)                           #distribución de señal
plot(soporte,d_ruido,type='l')                              #graficar ruido
lines(soporte,d_senal,type='l',col='blue')                  #graficar señal
abline(v=k_hat,col='red')                                   #graficar k
#Mi agregado
k_hat<-round(k_hat,5)                                       #redondear k
d_hat<-round(d_hat,5)                                       #redondear d'
center_hat<-round(center_hat,5)                             #redondear c
beta_hat<-round(beta_hat,5)                                 #redondear beta
text(-4,0.35,paste("K = ",k_hat))                            #escribir k
text(-4,0.3,paste("d' = ",d_hat))                            #escribir d'
text(-4,0.25,paste("C = ",center_hat))                       #escribir c
text(-4,0.2,paste("Beta = ",beta_hat))                       #escribir beta