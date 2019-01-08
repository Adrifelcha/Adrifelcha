x <- c(0.7, 0.86, 0.87, 0.46, 0.83,0.71,0.33,0.65,0.63)


n <- length(x)
media <- mean(x)

#Metodo de los momentos
teta_MOM <- ((2*media)-1)/(1-media)
teta_MOM

Logs <- log(x)
SumLogs <- sum(Logs)

#Maxima verosimilitud

#Pasamos la función
l <- function(teta) (n*log(1+teta)) + (teta * SumLogs)

#Obtenemos el máximo verosimil
fit_M2 <- optim(c(1), f=l, method="Brent", lower=0, upper=20,
                control=list(fnscale=-1), hessian=TRUE)
Estimador_M2 <- fit_M2$par
Estimador_M2

#Computamos la razón de verosimilitud respecto del modelo restringido (teta = 0.5)
fit_M1 <- l(.5)

razon <- fit_M1/fit_M2$value
razon

G2 = -2*fit_M1 + 2*fit_M2$value

gl <- 1
p_valor <- pchisq(G2, gl, lower.tail=F)
decision <- ifelse(p_valor <= 0.05, "Rechazar H0", "Mantener H0")
cat(sprintf(
  'beta estimada = %5.2f, Se = %5.3f\nG2 = %5.2f, gl = %1.0f p = %5.3f, Decision: %s',
  fit_M2$par, sqrt(-1/fit_M2$hessian), G2, gl, p_valor, decision))


##### Para computar el Intervalo de Confianza
#Interpretamos cada uno de los valores arrojados:
Estimador_M2 <- fit_M2$par            #En "par" fit nos dice el valor estimado
var_M2<- -1/fit_M2$hessian   #La varianza es el inverso de la segunda derivada (hessian)
Se <- sqrt(var_M2)         #El error tipico es la raìz cuadrada de la Varianza


#ntervalo de confianza del 95%
alpha <- .05   #"Error" que estamos dispuestos a dejar pasar (El complemento del Intervalo de Confianza)

Z <- abs(qnorm(alpha/2))   #Computamos el Puntaje Z que corresponde a nuestra alpha

Ls <- Estimador_M2+ Z *Se   #Computamos los Lìmites Superior e Inferior
Li <- Estimador_M2 - Z *Se





#AIC

AIC <- -2*l(fit_M2$par) + 2
AIC


