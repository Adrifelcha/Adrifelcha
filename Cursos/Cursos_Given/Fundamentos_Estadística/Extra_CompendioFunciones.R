#########################
##### Funciòn RETURN
#########################


check <- function(x) {
  if (x > 0) {
    result <- "Positive"
  }
  else if (x < 0) {
    result <- "Negative"
  }
  else {
    result <- "Zero"
  }
  return(result)
}


check(2)
check(-2)





check <- function(x) {
  if (x > 0) {
    result <- "Positive"
  }
  else if (x < 0) {
    result <- "Negative"
  }
  else {
    result <- "Zero"
  }
  result
}

check(2)
check(-2)
check(0)






x <- c(10,20,30,40,50)


l <- function(p){
  a <- 0   #Valor inicial de la función, que se va a ir actualizando segun un for
  for(i in 1:length(y)){   #Por cada dato contenido en y (6 veces)
    a <- a + x[i] * p
    #LogLk se va a actualizar sumando el logaritmo de la función normal al LogLk
    #que se había acumulado en la repetición inmediatamente anterior
  }
  return(a)
}

