###################################################
# Distribuciones
# por Adriana F. Chávez
# adrifelcha@gmail.com
###################################################






############################
# U N I F O R M E

#Parámetros
a <- 1 #Valor mìnimo 
b <- 5 #Valor maximo

#Función de probabilidad (masa)
unif <- c(NA)
for (i in a:b){
unif[i] <- a/b  
}

#Ploteamos los valores asignados por la función 'unif' al intervalo a->b
barplot(unif, col=c("indianred4","indianred1"), ylim=c(0,1), names=as.character(c(a:b)),
        cex.axis = 1.1, main="Distribución Uniforme", cex.main=2, font.main=2)


########### Computando la probabilidad de valores específicos
k <- 3   #Valor a estimar

p_k <- frequency((a:b)==k)/b      
p_k
dunif(k,a,b)

acumulado <- c(NA)
for(j in 1:k){
 acumulado[j] <-  unif[j] 
}
sum(acumulado)