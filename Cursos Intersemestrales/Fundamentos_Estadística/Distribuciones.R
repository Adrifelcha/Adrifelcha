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
punif(k,a,b)

barplot(dunif(c(a:b),a,b), ylim=c(0,1), col=c("forestgreen", "lightgreen"), main="Encuentre el error!")
axis(2, c(0.2,0.25,0.3), c("0.2","0.25", "0.3"))





############################
# H I P E R G E O M E T r I C A


##### Paso 0 : Entender de què va la Hipergeomètrica

#Parámetros
N <- 10 #Tamaño de la Población
R <- 3 #Numero de "CASOS" en la Población
n <- 5    #Tamaño de la muestra aleatoria

#La distribución Hipergeométrica asume muestreos SIN REEMPLAZO
#Esto implica que la Probabilidad de encontrar un R en n, CAMBIA para cada extracción

p_R <- c(NULL)        #Probabilidad de encontrar un caso R
for(e in 1:n){        #es diferente por definición para cada elemento de mi muestra
  if (e ==1){          
  p_R[e] <- R/N       #Si hablamos de la primera extracción, p_R se computa de manera clàsica (#R/#N)
  }
  else{               #Pero para el resto de los elementos (sin reemplazo)
  p_R[e] <- R/(N-(e-1))}}     #El denominador en mi definición clásica va cambiando

round(p_R,3)   #La probabilidad de observar R cambia para cada elemento


#Además! La probabilidad de R depende de si ya he encontrado una R en mi muestra (asumiendo R es finito en mi poblacion)
muestra_based_on_pR <- c(NULL)
p_R2 <- c(NULL)
for(element in 1:n){
  muestra_based_on_pR[element] <- rbinom(1,1,prob=p_R[element])
  if(muestra_based_on_pR[element]==1){
    p_R2[element] <- (R-(frequency(muestra_based_on_pR==1)))/(N-(element-1)) 
  }else{
    if(element==1){
     p_R2[element] <- p_R[1] 
    }else{
    p_R2[element] <- p_R2[element-1]
  }}}
muestra_based_on_pR
p_R2



muestra_realista <- c(NULL)
for(k in 1:n){
muestra_realista[k] <- rbinom(1,1,prob=p_R2[k])  
}
muestra_realista

#Paso 1 : Bueno pero... ¿Còmo puedo anticiparme al muestreo?
# LA VERDADERA FORMA de la Distribución Hipergeométrica
# (que al igual que la binomial, aprovecha los coeficientes binomiales,
# para computar las posibles combinaciones y permutaciones que yo 
# podrìa esperar encontrar en mi muestra)


#Distribución Hipergeomètrica en R

k <- 5 # Tamaño de mi muestra
x <- c(1:k) #Casos a encontrar en mi muestra
m <- 3 # CASOS en la poblacion
N <- 10  # Tamaño de la poblacion
n <- N-m

plot(c(1:k), dhyper(x,m,n,k), ylab="", ann=FALSE, type='l', 
     lwd=3, col="red")

dhyper(k,m,n,k)
