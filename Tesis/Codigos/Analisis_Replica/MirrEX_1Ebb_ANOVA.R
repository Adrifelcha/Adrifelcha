setwd("C:/Users/Adriana/Desktop/Felisa/Tesis/CSVs")
rm(list=ls())
dir()

#Archivo que contiene todos los datos
archive <-'Ex_1Ebb_TODOS-.csv'
datos <- read.csv(archive)


############## PRE PRUEBAS
### Binomial para probar la evidencia recolectada contra el azar
Mirror_Rates<- binom.test(17, 20, p = 0.5) 
Mirror_Rates#La probabilidad de obtener #Casos con Mirror Effect, si dependiera del azar.
Mirror_Confidence <- binom.test(18,20,p=0.5)
Mirror_Confidence

### Corroborando que las condiciones SON Diferentes
# Diferencias en D'
#LLamamos los datos
d_Facil <- datos$d_A
d_Dificil <- datos$d_B
#Ordenamos los datos
d_AyB<- data.frame(cbind(d_Facil, d_Dificil))
dprimas <- stack(d_AyB)
#Corremos un ANOVA
Anova_D <- aov(values~ind, data=dprimas)
summary(Anova_D)

##############MIRROR EFFECT
####  Diferencia en Rates (Patron principal)
#LLamamos los datos
FA_Facil <- datos$FaR_A
FA_Dificil <- datos$FaR_B
H_Dificil <- datos$Hr_B
H_Facil <- datos$Hr_A
#ORdenamos los datos
Combined_Rates <- data.frame(cbind(FA_Facil,FA_Dificil,H_Dificil,H_Facil))
FA_Rates <- data.frame(cbind(FA_Facil,FA_Dificil))
Hits_Rates <- data.frame(cbind(H_Dificil,H_Facil))
Rates <-stack(Combined_Rates)
FalsasAlarmas <- stack(FA_Rates)
Hits <- stack(Hits_Rates)
#Corremos los ANOVA
Anova_Rates <- aov(values~ind, data=Rates)
summary(Anova_Rates)
Anova_FA <- aov(values~ind, data=FalsasAlarmas)
summary(Anova_FA)
Anova_Hits <- aov(values~ind, data=Hits)
summary(Anova_Hits)

##### Diferencias en Confidence Rates
#Llamamos los datos
CR_AN <- datos$R_AN
CR_BN <- datos$R_BN
CR_BS <- datos$R_BS
CR_AS <- datos$R_AS
#Ordenamos los datos
Combined_Confidence <- data.frame(cbind(CR_AN,CR_BN,CR_BS,CR_AS))
No_Conf <- data.frame(cbind(CR_AN, CR_BN))
Yes_Conf <- data.frame(cbind(CR_BS,CR_AS))
Confidence <- stack(Combined_Confidence)
EsRuido <- stack(No_Conf)
EsSenal <- stack(Yes_Conf)
#Corremos el ANOVA
Anova_Confidence <- aov(values~ind, data=Confidence)
summary(Anova_Confidence)
Anova_No <- aov(values~ind, data=EsRuido)
summary(Anova_No)
Anova_Yes <- aov(values~ind, data=EsSenal)
summary(Anova_Yes)



#### Diferencias en Misses
#Llamamos los datos
Miss_A <- datos$M_AS
Miss_B <- datos$M_BS
#ORdenamos los datos
Miss_Conf <- data.frame(cbind(Miss_B,Miss_A))
Misses <- stack(Miss_Conf)
#Realizamos el ANOVA
ANOVA_Misses <- aov(values~ind, data=Misses)
summary(ANOVA_Misses)


###### Analisis de Response Time
#####
####

#Llamamos los datos
RT1_A <- datos$RT_A_1
RT2_A <- datos$RT_A_2
RT3_A <- datos$RT_A_3
RT1_B <- datos$RT_B_1
RT2_B <- datos$RT_B_2
RT3_B <- datos$RT_B_3
RT1_AS <- datos$RT_AS_1
RT1_AN <- datos$RT_AN_1
RT1_BS <- datos$RT_BS_1
RT1_BN <- datos$RT_BN_1
RT2_AS <- datos$RT_AS_2
RT2_AN <- datos$RT_AN_2
RT2_BS <- datos$RT_BS_2
RT2_BN <- datos$RT_BN_2
RT3_AS <- datos$RT_AS_3
RT3_AN <- datos$RT_AN_3
RT3_BS <- datos$RT_BS_3
RT3_BN <- datos$RT_BN_3

Comp_AB_1 <- data.frame(cbind(RT1_A,RT1_B))
Comp_AB_2 <- data.frame(cbind(RT2_A,RT2_B))
Comp_AB_3 <- data.frame(cbind(RT3_A,RT3_B))
Comp_A1 <- data.frame(cbind(RT1_AS,RT1_AN))
Comp_A2 <- data.frame(cbind(RT2_AS,RT2_AN))
Comp_A3 <- data.frame(cbind(RT3_AS,RT3_AN))
Comp_B1 <- data.frame(cbind(RT1_BS,RT1_BN))
Comp_B2 <- data.frame(cbind(RT2_BS,RT2_BN))
Comp_B3 <- data.frame(cbind(RT3_BS,RT3_BN)) 
AB_RT1 <- stack(Comp_AB_1)
A_RT1 <- stack(Comp_A1)
B_RT1 <- stack(Comp_B1)
AB_RT2 <- stack(Comp_AB_2)
A_RT2 <- stack(Comp_A2)
B_RT2 <- stack(Comp_B2)
AB_RT3 <- stack(Comp_AB_3)
A_RT3 <- stack(Comp_A3)
B_RT3 <- stack(Comp_B3)


Anova_RT_AB1 <- aov(values~ind, data=AB_RT1)
summary(Anova_RT_AB1)
Anova_RT_A1 <- aov(values~ind, data=A_RT1)
summary(Anova_RT_A1)
Anova_RT_B1 <- aov(values~ind, data=B_RT1)
summary(Anova_RT_B1)

Anova_RT_AB2 <- aov(values~ind, data=AB_RT2)
summary(Anova_RT_AB2)
Anova_RT_A2 <- aov(values~ind, data=A_RT2)
summary(Anova_RT_A2)
Anova_RT_B2 <- aov(values~ind, data=B_RT2)
summary(Anova_RT_B2)

Anova_RT_AB3 <- aov(values~ind, data=AB_RT3)
summary(Anova_RT_AB3)
Anova_RT_A3 <- aov(values~ind, data=A_RT3)
summary(Anova_RT_A3)
Anova_RT_B3 <- aov(values~ind, data=B_RT3)
summary(Anova_RT_B3)