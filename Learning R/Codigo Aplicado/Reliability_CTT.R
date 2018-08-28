# Confiabilidad bajo CTT
#
#######################################
setwd("D:/afchavez/Desktop/Adrifelcha_Lab25/Learning R/Codigo Aplicado")
set.seed(1)

library(hemp)
data(SAPA)

write.csv(SAPA, file = "reliability.csv", row.names = FALSE)   # Pasamos los datos a un CSV
datos <- read.csv("reliability.csv", header = TRUE,stringsAsFactors = FALSE) # Leemos el CSV creado

num_miss(datos)   #Exploramos el número de datos faltantes.


#Split-half reliability (Comparing first and second halves of data)

split_half(SAPA, type = "alternate") #Halves are generated alternating items
split_half(SAPA, type = "random")    #Halves are generated at random

split_half(SAPA, type = "alternate", sb = TRUE)  #We can add the 


##### Ideal test lenght in order to take Reliability to a desired standard value
test_length(SAPA, r=.95, r_type="split")
#arguments: Data set, Reliability desired, Current reliability (can be a method or a directly computed value)





# Alfa coefficient

coef_alpha(SAPA)



###########################################
# Introduction to Bootstrapping (Empirical Sampling Distributions)
library("boot")

#At minimun we need: A data set, a function to bootstrap and the number of samples to draw.

#Create an arbitrary function to bootstrap
Funcion <- function(data, row){
  coef_alpha(data[row, ])
}

alpha_boot <- boot(datos, Funcion, R = 1e4)
alpha_boot

plot(alpha_boot)

boot.ci(alpha_boot, type = c("norm", "basic", "perc", "bca"))

