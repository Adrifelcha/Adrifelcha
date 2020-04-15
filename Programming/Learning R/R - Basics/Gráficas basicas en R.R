###################################################
# Gráficas Básicas en R
# por Adriana F. Chávez
# adrifelcha@gmail.com
###################################################



########################################################
# PARTE 1:
# Diferencias entre grupos (V. categóricas)
########################################################
########################################################
########################################################

rm(list=ls())  # Este comando 'reinicia al default' todas las configuraciones que hayas hecho
#Por regla general, se recomienda ponerse al inicio de cada código, para no 'jalar' las características
#especificadas en otra sección

#Especificamos los datos
grupos <-c('A','B','C','D','E') #Etiqueta de los grupos a comparar (variable independiente)
valores <- c(100, 122, 314, 216, 338) #Valores correspondientes a cada grupo  (variable dependiente)





#######################################################
#Gráficas Pastel
########################################################

#Traducimos los valores a porcentajes
porcentaje <- round(valores/sum(valores)*100) 
#La función de arriba se lee: Por cada elemento en el arreglo 'valores', 
#éste se va a dividir entre el 'valor total' (la suma de los otros valores)
#Luego, el valor resultante se multiplica por 100 para poder interpretarlo como porcentaje
#El 'round' es para redondear el resultado de lo contenido en el paréntesis

#Reordenamos los datos
grupos_1 <- paste(grupos, porcentaje) # En el arreglo de 'grupos', agregamos los valores porcentuales de cada elemento
grupos_2 <- paste(grupos_1,"%",sep="") # Y sobre este nuevo arreglo, agregamos al final de cada pareja grupo-porcentaje, el simbolo "%"

#Hacemos la gráfica de pastel
pie(valores,labels = grupos_2, col=c('red','pink', 'yellow','green','blue'), main="Gráfica de Pastel")
#Pedimos una gráfica de pastel (pie), que muestre/represente los valores netos  (valores)
#usando el arreglo 'grupos'para señalar los valores (labels = grupos)
#en los colores especificados en el arreglo (col=C(...))
#con el título principal "Grafica de Pastel" (main= "blabla")

#También podemos hacer una gráfica con volúmen 
pie3D(valores,labels=grupos_2,explode=0.05, main="Gráfica de Pastel 3D")
#Usamos la función 'pie3D' (después de instalar y activar el paquete 'plotrix')
#Otra vez pedimos que muestre los valores, con las etiquetas creaas
#El argumento 'explode' indica qué tan separados están las rebanadas.


###########33
#Gráficas de Barras
####################################################
barplot(valores,main="Gráfica de barras", horiz=FALSE, axes=F,
        ylim=c(0,500), xlab="Grupos", ylab="Casos",
        col=c('red','blue','yellow','green','pink'))
axis(2,at=c(0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500),labels=c("0", "50", "100", "150", "200", "250", "300", "350", "400", "450", "500"),las=1)
axis(1,at=c(0.7,1.9,3.1,4.3,5.5),labels=grupos)
text(0.7,valores[1]+15,paste(valores[1]),cex=1,col='black',f=1)
text(1.9,valores[2]+15,paste(valores[2]),cex=1,col='black',f=2)
text(3.1,valores[3]+15,paste(valores[3]),cex=1,col='black',f=3)
text(4.3,valores[4]+15,paste(valores[4]),cex=1,col='black',f=1)
text(5.5,valores[5]+15,paste(valores[5]),cex=1,col='black',f=1)






#Scatter plot
layout(matrix(1:3,ncol=1))

plot(valores, main="Scatter Plot", axes=F, ylim=c(0,500), xlab="Grupos",
     ylab="Casos",col=c('red','blue','purple', 'pink', 'orange'), pch=16)
axis(2,at=c(0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500),labels=c("0", "50", "100", "150", "200", "250", "300", "350", "400", "450", "500"),las=1)
axis(1,at=c(1,2,3,4,5),labels=grupos)
mtext("Coordenadas",3,cex=0.6, line=-0.7, f=2)

plot(valores, type='o', main="", axes=F, ylim=c(0,500), xlab="Grupos",
     ylab="Casos",col=c('red','blue','purple', 'pink', 'orange'), pch=16)
axis(2,at=c(0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500),labels=c("0", "50", "100", "150", "200", "250", "300", "350", "400", "450", "500"),las=1)
axis(1,at=c(1,2,3,4,5),labels=grupos)
mtext("Coordenadas unidas por línea",3,cex=0.6, line=-0.7, f=2)

plot(valores, type = 'l', main="", axes=F, ylim=c(0,500), xlab="Grupos",
     ylab="Casos",col=c('red','blue','purple', 'pink', 'orange'), pch=16)
axis(2,at=c(0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500),labels=c("0", "50", "100", "150", "200", "250", "300", "350", "400", "450", "500"),las=1)
axis(1,at=c(1,2,3,4,5),labels=grupos)
mtext("Sólo lineas",3,cex=0.6, line=-0.7, f=2)




########################################################
# Diferencias en Y como función de X (V. Numéricas)
########################################################
########################################################
########################################################
rm(list=ls())

##########
#Especificamos un conjunto de datos

###
#Variable independiente: El eje de las abscisas
###
absc_años<-2010:2017   #Rango de valores contenidos en X 
#0:10 indica un rango de 0 a 10
print(absc_años)

absc_x <-seq(0,100,5) #Una secuencia del 0 al 100 en saltos de 5
print(absc_x)

absc_y <-seq(-3,3,0.05) #Una secuencia del -3 al 3 en saltos de .05
print(absc_y)

#Variable Dependiente: Eje de las ordenadas

#para años
ord_años <- rnorm(8,200,30)
ord_años <- round(ord_años,2)
print(ord_años)

#para X
ord_x <- 250:270
print(ord_x)

#para y
ord_y <- seq(0,12,0.1)
print(ord_y)


# GRAFICAS LINEALES
#######################################################
plot(absc_años,ord_años, type='o', pch=16, col=c('blue','red'), axes=F, ylab="Aleatorio", xlab="Años", main ="Holiwi")
axis(1)
axis(2,at=seq(0,600,30), labels = seq(0,600,30))

plot(absc_x,ord_x, type='l',col='blue', main="Pedro")


#Especificamos los datos
