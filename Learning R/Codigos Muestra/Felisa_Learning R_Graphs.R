#######################################################
#Gráficas en R
#por Adriana F. Chávez
#######################################################


# GRAFICAS LINEALES 
######################################################

#Especificamos los datos
rango_x<-0:20   #Rango de valores contenidos en X 

#Valores Y serán aleatorios
variable_aleatoria<-rnorm(21,5,1)   #Pedimos que se extraigan aleatoriamente (r), 20 valores de una distribución normal (norm), con media en 5 y desviacion estandar de 1
y<-rango_x+variable_aleatoria  #Asumamos que Y incrementa proporcionalmente a X, más un 

#Función describiendo los valores
z<-rango_x+5

plot(rango_x,y)
lines(rango_x,z, type="l", lty=4, lwd=2, col='blue')



#Scatter plot
#######################################################
a <- rnorm(100,5,1)
b <- rnorm(100,2,1)

a
b

plot(a,b)



#Gráficas de Barras
#######################################################

calificaciones <- c(5,7,9,6,8,1,2,7,6,8,10,3,9,5,10,7,4,6,9,10,1,4,6,7,1,10,6,8,3,6,4,10)

tabla <- table(calificaciones)
Tabla <- as.data.frame(tabla)

barplot(Tabla[,2], labels = Tabla[,1])





########################################################
#Gráficas Pastel
########################################################
#Especificamos los datos
grupos <-c('A','B','C','D','E') #Etiqueta de los grupos a comparar (el nombre de las rebanadas)
valores <- c(100, 122, 314, 216, 338) #Valores correspondientes a cada grupo (el valor representado por cada rebanada)

#Computamos los porcentajes
porcentaje <- round(valores/sum(valores)*100) 
#La función de arriba se lee: Por cada elemento en el arreglo 'valores', 
#éste se va a dividir entre el 'valor total' (la suma de los otros valores)
#Luego, multiplicamos el valor resultante por 100 para poder interpretarlo como porcentaje
#El 'round' es para redondear el resultado de lo contenido en el paréntesis

#Reordenamos los datos
grupos <- paste(grupos, porcentaje) # En el arreglo de 'grupos', agregamos los valores porcentuales de cada elemento
grupos <- paste(grupos,"%",sep="") # Y sobre este nuevo arreglo, agregamos al final de cada pareja grupo-porcentaje, el simbolo "%"

#Hacemos la gráfica
pie(valores,labels = grupos, col=c('red','pink', 'yellow','green','blue'), main="Gráfica de Pastel")
#Pedimos una gráfica de pastel (pie), que muestre/represente los valores netos  (valores)
#usando el arreglo 'grupos' construido (labels = grupos)
#en los colores especificados (col=C(...))
#con el título principal "Grafica de Pastel" (main= "blabla")

#También podemos hacer una gráfica con volúmen 
pie3D(valores,labels=grupos,explode=0.1, main="Gráfica de Pastel 3D")
#Usamos la función 'pie3D' (después de instalar y activar el paquete 'plotrix')
#Otra vez pedimos que muestre los valores, con las etiquetas creaas
#con 