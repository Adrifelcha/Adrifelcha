#########################################
# Básicos en R: Primera aproximación
# por Adriana F. Chávez
#########################################


rm(list=ls())   # Vaciamos el controlador de Variables 


#Declarar variables
a <- 1
b <- 2
c <- c(1:10)
d <- c(101:110)
e <- a * b
f <- d * e
g <- d/2

x <- seq(0, 100, 10)
y <- seq(69,70,0.1)

n <- c(1,2,3,4,5,6)
n_mat <- matrix(n, nrow=2, byrow=FALSE)

o <- c(rep(10,6))
o_mat <- matrix(o, nrow=2, byrow=FALSE)

name <- "Adriana"
name_2 <- name

nchar(name)
print(name)



calificaciones <- c(5,7,9,6,8,1,2,7,6,8,10,3,9,5,10,7,4,6,9,10,1,4,6,7,1,10,6,8,3,6,4,10)

tabla <- table(calificaciones)
Tabla <- as.data.frame(tabla)




#Scatter plot
#######################################################
a <- rnorm(100,5,1)
b <- rnorm(100,2,1)

a
b

plot(a,b)







