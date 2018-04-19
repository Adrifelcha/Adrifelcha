###################################################
# Teoría de los grandes números
# por Adriana F. Chávez
# adrifelcha@gmail.com
###################################################

x <- seq(-6,6,.001)

población <- dnorm(x,0,1)

muestra_1 <- sample(población, 10)

muestra_2 <- sample(población, 100)

muestra_3 <- sample(población, 1000)

muestra_a <- rnorm(10,0,1)

muestra_b <- rnorm(100,0,1)

muestra_v <- rnorm(1000,0,1)