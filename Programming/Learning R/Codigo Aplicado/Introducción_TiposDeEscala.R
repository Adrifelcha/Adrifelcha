# Introducción a Escalas de Medición
#
#######################################
setwd("D:/afchavez/Desktop/Adrifelcha_Lab25/Learning R/Codigo Aplicado")

# Usamos un conjunto de datos de prueba
library(hemp)                # Cargamos la librería Hemmp
data <- data("interest")     # Activamos la base de datos
interest                     # Visualizamos los datos

write.csv(interest, file = "interest.csv", row.names = FALSE)   # Pasamos los datos a un CSV
datos <- read.csv("interest.csv", header = TRUE,stringsAsFactors = FALSE) # Leemos el CSV creado

##################################
########## Manipulación de Variables Categóricas (Nominales y Ordinales)

# Creamos una variable Categórica que responda al género
gender_cat <- ifelse(datos$gender == 1, "mujer", "hombre")
table(gender_cat)                # Tabla de Frecuencias
prop.table(table(gender_cat))    # Tabla de Proporciones

# Creamos una variable ordinal a partir de una variable numérica
age_nom <- cut(datos$age, breaks = seq(10,70, by =10))  
age_ord <- sort(age_nom)      # Ordenamos los datos
table(age_nom)                # Tabla de Frecuencias

ftable(age_nom,gender_cat)     #Creamos una Matriz de Contingencias

############################################
############  Ploteamos nuestras Variables CATEGÓRICAS
library(lattice)
barchart(age_ord, col=c("green", "forestgreen")) 

dotplot(table(age_ord), col=c("blue", "skyblue"))

#Trellis or Facet plot
age_gender_table <- table(gender_cat, age_ord)     #Creamos una Tabla de Frecuencias compuesta por dos variables
age_gender_data <- data.frame(age_gender_table)   #Convertimos la Tabla en un arreglo de datos

dotplot(age_ord ~ Freq | gender_cat, age_gender_data, xlab="Freq", ylab="Age")
#Creamos un dotplot que plotee la frecuencia de la variable Edad condicionada por cada Género


################################################
############# Explorando variables continuas

summary(datos$vocab)

# Se puede evaluar la Normalidad del dato cargado con Q-Q plot

qqnorm(datos$vocab, ylab="Vocab")
qqline(datos$vocab)