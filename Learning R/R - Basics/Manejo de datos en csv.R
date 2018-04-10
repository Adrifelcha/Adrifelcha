###################################################
# Manejo de datos (CSV) con R
# por Adriana F. Chávez
# adrifelcha@gmail.com
###################################################

#Empezamos nuestro código especificando el escritorio de trabajo (Working directory: wd)
setwd("C:/Users/Alejandro/Desktop/Felisa/Learning R/R - Basics")
#Borramos todas las variables y valores almacenados en consola
rm(list=ls())
#Comprobamos los archivos contenidos en nuestro wd
dir()

#Identificamos el archivo que contiene los datos a trabajar
datos <-'Datos_Example2.csv'
#Recogemos los datos del archivo
granja <- read.csv(datos)



##################
##################
#  Leemos CSV    #
##################
##################


#############¿Qué queremos saber?

#Promedios
mean(granja$Accidentes)
#Valor Máximo
max(granja$Accidentes)
#Valor Minimo
min(granja$Accidentes)
#Desviacion Estandar
sd(granja$Accidentes)


############# Declaramos variables con nuestros datos
accidentes <- granja$Accidentes
Visitas <- granja$Visitas
Calificación <- granja$Calificación
Conejos <- granja$Conejos
Cerdos <- granja$Cerdos
Caballos <- granja$Caballos
Año <- granja$Tiempo..Año.


#Creamos arreglos
Visitas_Anuales <- cbind(Año,Visitas)
print(Visitas_Anuales)

visitas_anuales <- rbind(Año,Visitas)
print(visitas_anuales)

promedios <- data.frame(round(cbind(mean(accidentes), mean(Visitas), mean(Calificación), mean(Conejos), mean(Cerdos), mean(Caballos)),3))
colnames(promedios) <- c("Accidentes","Visitas","Calif", "Conejos", "Cerdos", "Caballos")
print(promedios)





##################
##################
#  Leemos CSV    #
##################
##################
plot(Año,Visitas, main="Visitas anuales")

plot(Visitas_Anuales, main="Visitas anuales")

barplot(Visitas, xlab="Años", ylab="Visitas", col=rainbow(length(Año)), main="Visitas anuales")
axis(1,at=c(0.6,1.9,3.1,4.3,5.5,6.7,7.9,9.1,10.3,11.5,12.7,13.9), labels= Año)