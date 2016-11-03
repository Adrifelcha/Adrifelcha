rm(list=ls())                                                      #Clear Data
#setwd("/Volumes/NO NAME/APLICACION/Lahav")                        #Mac Directory
setwd("D:/APLICACION/Lahav")                                       #USB Directory
library("grDevices", lib.loc="C:/Program Files/R/R-3.1.1/library") #Colors Library
Treat1 <- read.csv("DataLahav1.csv")                               #Treatment 1 Data
Treat23 <- read.csv("DataLahav23.csv")                             #Treatment 2 Data

Kg <- c(5,15.5,25.5,35.5,45.5,55.5,65.5,75.5,85.5,95.5) #K^: Average of Values of K

Colors1 <- "#7D7D7D4D"                                  #Low Alpha Gray Color

#### T2 S1 ####
Bm21 <- matrix(data=NA, nrow=5, ncol=20)   #Beliefs of All Players in T2S1
C21 <- matrix(data=NA, nrow=5, ncol=20)    #Choices of All Players in T2S1
Fi21 <- matrix(data=NA, nrow=5, ncol=20)   #Differences*2/3 of All Players in T2S1
Di21 <- matrix(data=NA, nrow=5, ncol=20)   #Raw Differences of All Players in T2S1
Fm21 <- matrix(data=NA, nrow=5, ncol=1)    #Average Differences*2/3 in T2S1
Dm21 <- matrix(data=NA, nrow=5, ncol=1)    #Average raw Differences in T2S1
BM21 <- matrix(data=NA, nrow=5, ncol=1)    #Average Beliefs in T2S1
CM21 <- matrix(data=NA, nrow=5, ncol=1)    #Average Choices in T2S1
Periodo21 <- c(0,20,40,60,80)              #Starting Points of each Period in T2S1

for (b in 1:5){ for (a in 1:20){           #a: N of Players  b: Periods
  Ki21 <- Treat23[0+a+Periodo21[b],15:24]  #Player a Distribution of Others Numbers
  Bi21 <- sum(Kg*Ki21)/20                  #Player a Periob b Belief
  Ci21 <- Treat23[0+a+Periodo21[b],28]     #Player a Period b Choice
  Cm21 <- Treat23[0+a+Periodo21[b],29]     #Average Number in Perod b
  Fi21[b,a] <- (((2/3)*Bi21)-Ci21)         #Difference between Belief*2/3 and Choice
  Di21[b,a] <- (Bi21-Ci21)                 #Difference between raw Belief and Choice
  Bm21[b,a] <- Bi21                        #All Players Belief in T2S1
  C21[b,a] <- Ci21                         #All Players Choice in T2S1
  BM21[b] <- (sum(Bm21[b,]))/20            #Average Beliefs in T2S1
  CM21[b] <- (sum(C21[b,]))/20             #Average Choices in T2S1
  BM21 <- round(BM21,2)                    #Round Average Beliefs
  CM21 <- round(CM21,2)                    #Round Average Choices  
  Fm21[b,1] <- (sum(Fi21[b,]))/20          #Average Differences*2/3 in T2S1
  Dm21[b,1] <- (sum(Di21[b,]))/20          #Average raw Differences in T2S1
}}

#### T2 S2 ####
Bm22 <- matrix(data=NA, nrow=5, ncol=17)   #Beliefs of All Players in T2S2
C22 <- matrix(data=NA, nrow=5, ncol=17)    #Choices of All Players in T2S2
Fi22 <- matrix(data=NA, nrow=5, ncol=17)   #Differences*2/3 of All Players in T2S2
Di22 <- matrix(data=NA, nrow=5, ncol=17)   #Raw Differences of All Players in T2S2
Fm22 <- matrix(data=NA, nrow=5, ncol=1)    #Average Differences*2/3 in T2S2
Dm22 <- matrix(data=NA, nrow=5, ncol=1)    #Average raw Differences in T2S2
BM22 <- matrix(data=NA, nrow=5, ncol=1)    #Average Beliefs in T2S2
CM22 <- matrix(data=NA, nrow=5, ncol=1)    #Average Choices in T2S2
Periodo22 <- c(0,17,34,51,68)              #Starting Points of each Period in T2S2

for (b in 1:5){ for (a in 1:17){           #a: N of Players  b: Periods
  Ki22 <- Treat23[100+a+Periodo22[b],15:24]#Player a Distribution of Others Numbers
  Bi22 <- sum(Kg*Ki22)/17                  #Player a Periob b Belief
  Ci22 <- Treat23[100+a+Periodo22[b],28]   #Player a Period b Choice
  Cm22 <- Treat23[100+a+Periodo22[b],29]   #Average Number in Perod b
  Fi22[b,a] <- (((2/3)*Bi22)-Ci22)         #Difference between Belief*2/3 and Choice
  Di22[b,a] <- (Bi22-Ci22)                 #Difference between raw Belief and Choice
  Bm22[b,a] <- Bi22                        #All Players Belief in T2S2
  C22[b,a] <- Ci22                         #All Players Choice in T2S2
  BM22[b] <- (sum(Bm22[b,]))/20            #Average Beliefs in T2S2
  CM22[b] <- (sum(C22[b,]))/20             #Average Choices in T2S2
  BM22 <- round(BM22,2)                    #Round Average Beliefs
  CM22 <- round(CM22,2)                    #Round Average Choices 
  Fm22[b,1] <- (sum(Fi22[b,]))/17          #Average Differences*2/3 in T2S2
  Dm22[b,1] <- (sum(Di22[b,]))/17          #Average raw Differences in T2S2
}}

#### T2 S3 ####
Bm23 <- matrix(data=NA, nrow=5, ncol=19)   #Beliefs of All Players in T2S3
C23 <- matrix(data=NA, nrow=5, ncol=19)    #Choices of All Players in T2S3
Fi23 <- matrix(data=NA, nrow=5, ncol=19)   #Differences*2/3 of All Players in T2S3
Di23 <- matrix(data=NA, nrow=5, ncol=19)   #Raw Differences of All Players in T2S3
Fm23 <- matrix(data=NA, nrow=5, ncol=1)    #Average Differences*2/3 in T2S3
Dm23 <- matrix(data=NA, nrow=5, ncol=1)    #Average raw Differences in T2S3
BM23 <- matrix(data=NA, nrow=5, ncol=1)    #Average Beliefs in T2S3
CM23 <- matrix(data=NA, nrow=5, ncol=1)    #Average Choices in T2S3
Periodo23 <- c(0,19,38,57,76)              #Starting Points of each Period in T2S3

for (b in 1:5){ for (a in 1:19){           #a: N of Players  b: Periods
  Ki23 <- Treat23[185+a+Periodo23[b],15:24]#Player a Distribution of Others Numbers
  Bi23 <- sum(Kg*Ki23)/19                  #Player a Periob b Belief
  Ci23 <- Treat23[185+a+Periodo23[b],28]   #Player a Period b Choice
  Cm23 <- Treat23[185+a+Periodo23[b],29]   #Average Number in Perod b
  Fi23[b,a] <- (((2/3)*Bi23)-Ci23)         #Difference between Belief*2/3 and Choice
  Di23[b,a] <- (Bi23-Ci23)                 #Difference between raw Belief and Choice
  Bm23[b,a] <- Bi23                        #All Players Belief in T2S3
  C23[b,a] <- Ci23                         #All Players Choice in T2S3
  BM23[b] <- (sum(Bm23[b,]))/20            #Average Beliefs in T2S3
  CM23[b] <- (sum(C23[b,]))/20             #Average Choices in T2S3
  BM23 <- round(BM23,2)                    #Round Average Beliefs
  CM23 <- round(CM23,2)                    #Round Average Choices 
  Fm23[b,1] <- (sum(Fi23[b,]))/19          #Average Differences*2/3 in T2S3
  Dm23[b,1] <- (sum(Di23[b,]))/19          #Average raw Differences in T2S3
}}

#### T3 S1 ####
Bm31 <- matrix(data=NA, nrow=5, ncol=20)   #Beliefs of All Players in T3S1
C31 <- matrix(data=NA, nrow=5, ncol=20)    #Choices of All Players in T3S1
Fi31 <- matrix(data=NA, nrow=5, ncol=20)   #Differences*2/3 of All Players in T3S1
Di31 <- matrix(data=NA, nrow=5, ncol=20)   #Raw Differences of All Players in T3S1
Fm31 <- matrix(data=NA, nrow=5, ncol=1)    #Average Differences*2/3 in T3S1
Dm31 <- matrix(data=NA, nrow=5, ncol=1)    #Average raw Differences in T3S1
BM31 <- matrix(data=NA, nrow=5, ncol=1)    #Average Beliefs in T3S1
CM31 <- matrix(data=NA, nrow=5, ncol=1)    #Average Choices in T3S1
Periodo31 <- c(0,20,40,60,80)              #Starting Points of each Period in T3S1

for (b in 1:5){ for (a in 1:20){           #a: N of Players  b: Periods
  Ki31 <- Treat23[280+a+Periodo31[b],15:24]#Player a Distribution of Others Numbers
  Bi31 <- sum(Kg*Ki31)/20                  #Player a Periob b Belief
  Ci31 <- Treat23[280+a+Periodo31[b],28]   #Player a Period b Choice
  Cm31 <- Treat23[280+a+Periodo31[b],29]   #Average Number in Perod b
  Fi31[b,a] <- (((2/3)*Bi31)-Ci31)         #Difference between Belief*2/3 and Choice
  Di31[b,a] <- (Bi31-Ci31)                 #Difference between raw Belief and Choice
  Bm31[b,a] <- Bi31                        #All Players Belief in T3S1
  C31[b,a] <- Ci31                         #All Players Choice in T3S1
  BM31[b] <- (sum(Bm31[b,]))/20            #Average Beliefs in T3S1
  CM31[b] <- (sum(C31[b,]))/20             #Average Choices in T3S1
  BM31 <- round(BM31,2)                    #Round Average Beliefs
  CM31 <- round(CM31,2)                    #Round Average Choices 
  Fm31[b,1] <- (sum(Fi31[b,]))/20          #Average Differences*2/3 in T3S1
  Dm31[b,1] <- (sum(Di31[b,]))/20          #Average raw Differences in T3S1
}}

#### T3 S2 ####
Bm32 <- matrix(data=NA, nrow=5, ncol=20)   #Beliefs of All Players in T3S2
C32 <- matrix(data=NA, nrow=5, ncol=20)    #Choices of All Players in T3S2
Fi32 <- matrix(data=NA, nrow=5, ncol=20)   #Differences*2/3 of All Players in T3S2
Di32 <- matrix(data=NA, nrow=5, ncol=20)   #Raw Differences of All Players in T3S2
Fm32 <- matrix(data=NA, nrow=5, ncol=1)    #Average Differences*2/3 in T3S2
Dm32 <- matrix(data=NA, nrow=5, ncol=1)    #Average raw Differences in T3S2
BM32 <- matrix(data=NA, nrow=5, ncol=1)    #Average Beliefs in T3S2
CM32 <- matrix(data=NA, nrow=5, ncol=1)    #Average Choices in T3S2
Periodo32 <- c(0,20,40,60,80)              #Starting Points of each Period in T3S2

for (b in 1:5){ for (a in 1:20){           #a: N of Players  b: Periods
  Ki32 <- Treat23[380+a+Periodo32[b],15:24]#Player a Distribution of Others Numbers
  Bi32 <- sum(Kg*Ki32)/20                  #Player a Periob b Belief
  Ci32 <- Treat23[380+a+Periodo32[b],28]   #Player a Period b Choice
  Cm32 <- Treat23[380+a+Periodo32[b],29]   #Average Number in Perod b
  Fi32[b,a] <- (((2/3)*Bi32)-Ci32)         #Difference between Belief*2/3 and Choice
  Di32[b,a] <- (Bi32-Ci32)                 #Difference between raw Belief and Choice
  Bm32[b,a] <- Bi32                        #All Players Belief in T3S2
  C32[b,a] <- Ci32                         #All Players Choice in T3S2
  BM32[b] <- (sum(Bm32[b,]))/20            #Average Beliefs in T3S2
  CM32[b] <- (sum(C32[b,]))/20             #Average Choices in T3S2
  BM32 <- round(BM32,2)                    #Round Average Beliefs
  CM32 <- round(CM32,2)                    #Round Average Choices 
  Fm32[b,1] <- (sum(Fi32[b,]))/20          #Average Differences*2/3 in T3S2
  Dm32[b,1] <- (sum(Di32[b,]))/20          #Average raw Differences in T3S2
}}

#### T3 S3 ####
Bm33 <- matrix(data=NA, nrow=5, ncol=20)   #Beliefs of All Players in T3S3
C33 <- matrix(data=NA, nrow=5, ncol=20)    #Choices of All Players in T3S3
Fi33 <- matrix(data=NA, nrow=5, ncol=20)   #Differences*2/3 of All Players in T3S3
Di33 <- matrix(data=NA, nrow=5, ncol=20)   #Raw Differences of All Players in T3S3
Fm33 <- matrix(data=NA, nrow=5, ncol=1)    #Average Differences*2/3 in T3S3
Dm33 <- matrix(data=NA, nrow=5, ncol=1)    #Average raw Differences in T3S3
BM33 <- matrix(data=NA, nrow=5, ncol=1)    #Average Beliefs in T3S3
CM33 <- matrix(data=NA, nrow=5, ncol=1)    #Average Choices in T3S3
Periodo33 <- c(0,20,40,60,80)              #Starting Points of each Period in T3S3

for (b in 1:5){ for (a in 1:20){           #a: N of Players  b: Periods
  Ki33 <- Treat23[480+a+Periodo33[b],15:24]#Player a Distribution of Others Numbers
  Bi33 <- sum(Kg*Ki33)/20                  #Player a Periob b Belief
  Ci33 <- Treat23[480+a+Periodo33[b],28]   #Player a Period b Choice
  Cm33 <- Treat23[480+a+Periodo33[b],29]   #Average Number in Perod b
  Fi33[b,a] <- (((2/3)*Bi33)-Ci33)         #Difference between Belief*2/3 and Choice
  Di33[b,a] <- (Bi33-Ci33)                 #Difference between raw Belief and Choice
  Bm33[b,a] <- Bi33                        #All Players Belief in T3S3
  C33[b,a] <- Ci33                         #All Players Choice in T3S3
  BM33[b] <- (sum(Bm33[b,]))/20            #Average Beliefs in T3S3
  CM33[b] <- (sum(C33[b,]))/20             #Average Choices in T3S3
  BM33 <- round(BM33,2)                    #Round Average Beliefs
  CM33 <- round(CM33,2)                    #Round Average Choices 
  Fm33[b,1] <- (sum(Fi33[b,]))/20          #Average Differences*2/3 in T3S3
  Dm33[b,1] <- (sum(Di33[b,]))/20          #Average raw Differences in T3S3
}}

#### T23 S123 ####
Ba <- matrix(data=NA, nrow=5, ncol=116)      #All Players Beliefs in all Sesions
Ca <- matrix(data=NA, nrow=5, ncol=116)      #All Players Choices in all Sesions
Cma <- matrix(data=NA, nrow=5, ncol=116)     #All Average Numbers in all Sesions
Fa <- matrix(data=NA, nrow=5, ncol=116)      #All Differences*2/3 in all Sesions
Da <- matrix(data=NA, nrow=5, ncol=116)      #All raw Differences in all Sesions
Fma <- matrix(data=NA, nrow=5, ncol=1)       #Average or All Differences*2/3
Dma <- matrix(data=NA, nrow=5, ncol=1)       #Average of All eaw Differences

Ba <- cbind(Bm21,Bm22,Bm23,Bm31,Bm32,Bm33)  #Binding Players Beliefs of all Sesions
Ca <- cbind(C21,C22,C23,C31,C32,C33)        #Binding Players Choices of all Sesions
Cma <- cbind(Cm21,Cm22,Cm23,Cm31,Cm32,Cm33) #Binding Average Numbers of all Sesions

for (c in 1:5){                       #c: Periodos
Fa <- (((2/3)*Ba)-Ca)                 #All Differences between Belief*2/3 and Choice
Da <- (Ba-Ca)                         #All raw Differences between Belief and Choice
Fma[c] <- (sum(Fa[c,]))/116           #Average of All Differences*2/3
Dma[c] <- (sum(Da[c,]))/116           #Average of All raw Differences
}

TBa <- matrix(data=NA, nrow=5, ncol=4) #T-Test between Beliefs in Treatments 2 - 3
TCa <- matrix(data=NA, nrow=5, ncol=4) #T-Test between Choices in Treatments 2 - 3

for (a in 1:5){                              #a: Periodos
TtBa <- t.test(Ba[a,1:56],Ba[a,57:116])      #T-Test Values for Beliefs in Period a
TtCa <- t.test(Ca[a,1:56],Ca[a,57:116])      #T-Test Values for Choices in Period a
x <- do.call(rbind,TtBa[1:6])                #Convert Beliefs List in Matrix Elements
TBa[a,1] <- x[1,1]                           #T-Statistic for Beliefs in Period a
TBa[a,2] <- x[3,1]                           #p-Value for Beliefs in Period a
TBa[a,3] <- x[5,1]                           #Average of Beliefs in T2 in Period a 
TBa[a,4] <- x[5,2]                           #Average of Beliefs in T3 in Period a
TBa <- round(TBa,2)                          #Round all Beliefs Values
x <- do.call(rbind,TtCa[1:6])                #Convert Choices List in Matrix Elements
TCa[a,1] <- x[1,1]                           #T-Statistic for Choices in Period a
TCa[a,2] <- x[3,1]                           #p-Value for Choices in Period a
TCa[a,3] <- x[5,1]                           #Average of Choices in T2 in Period a
TCa[a,4] <- x[5,2]                           #Average of Choices in T3 in Period a
TCa <- round(TCa,2)                          #Round all Choices Values
}

#### Plot Ind ####
pdf_name<-'Ind.pdf'                     #All Individual Sesions
pdf(file=pdf_name,width=9,height=9)     #Page 1: Choices T2-T3 #Page 2: Beliefs T2-T3
layout(matrix(1:6,ncol=2, byrow=T))     #Page 3: T2 Cho-Bel #Page 4: T3 Cho-Bel 

matplot(C21, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T2S1
        xlab= "Period", ylab= "Chosen Number", main="Choices T2S1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM21[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM21[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM21[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM21[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM21[5]),cex=0.9, font=2)
matplot(C31, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T3S1
        xlab= "Period", ylab= "Chosen Number", main="Choices T3S1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM31[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM31[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM31[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM31[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM31[5]),cex=0.9, font=2)

matplot(C22, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T2S2
        xlab= "Period", ylab= "Chosen Number", main="Choices T2S2", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM22[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM22[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM22[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM22[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM22[5]),cex=0.9, font=2)
matplot(C32, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T3S2
        xlab= "Period", ylab= "Chosen Number", main="Choices T3S2", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM32[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM32[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM32[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM32[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM32[5]),cex=0.9, font=2)

matplot(C23, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T2S3
        xlab= "Period", ylab= "Chosen Number", main="Choices T2S3", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM23[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM23[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM23[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM23[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM23[5]),cex=0.9, font=2)
matplot(C33, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T3S3
        xlab= "Period", ylab= "Chosen Number", main="Choices T3S3", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM33[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM33[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM33[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM33[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM33[5]),cex=0.9, font=2)

matplot(Bm21, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1, #Beliefs T2S1
        xlab= "Period", ylab= "Elicited Number", main="Beliefs T2S1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", BM21[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", BM21[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", BM21[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", BM21[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", BM21[5]),cex=0.9, font=2)
matplot(Bm31, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1, #Beliefs T3S1
        xlab= "Period", ylab= "Elicited Number", main="Beliefs T3S1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", BM31[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", BM31[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", BM31[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", BM31[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", BM31[5]),cex=0.9, font=2)

matplot(Bm22, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1, #Beliefs T2S2
        xlab= "Period", ylab= "Elicited Number", main="Beliefs T2S2", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", BM22[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", BM22[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", BM22[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", BM22[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", BM22[5]),cex=0.9, font=2)
matplot(Bm32, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1, #Beliefs T3S2
        xlab= "Period", ylab= "Elicited Number", main="Beliefs T3S2", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", BM32[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", BM32[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", BM32[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", BM32[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", BM32[5]),cex=0.9, font=2)

matplot(Bm23, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1, #Beliefs T2S3
        xlab= "Period", ylab= "Elicited Number", main="Beliefs T2S3", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", BM23[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", BM23[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", BM23[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", BM23[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", BM23[5]),cex=0.9, font=2)
matplot(Bm33, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1, #Beliefs T3S3
        xlab= "Period", ylab= "Elicited Number", main="Beliefs T3S3", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", BM33[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", BM33[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", BM33[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", BM33[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", BM33[5]),cex=0.9, font=2)

matplot(Bm21, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1, #Beliefs T2S1
        xlab= "Period", ylab= "Elicited Number", main="Beliefs T2S1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", BM21[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", BM21[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", BM21[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", BM21[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", BM21[5]),cex=0.9, font=2)
matplot(C21, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T2S1
        xlab= "Period", ylab= "Chosen Number", main="Choices T2S1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM21[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM21[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM21[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM21[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM21[5]),cex=0.9, font=2)

matplot(Bm22, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1, #Beliefs T2S2
        xlab= "Period", ylab= "Elicited Number", main="Beliefs T2S2", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", BM22[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", BM22[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", BM22[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", BM22[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", BM22[5]),cex=0.9, font=2)
matplot(C22, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T2S2
        xlab= "Period", ylab= "Chosen Number", main="Choices T2S2", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM22[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM22[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM22[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM22[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM22[5]),cex=0.9, font=2)

matplot(Bm23, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1, #Beliefs T2S3
        xlab= "Period", ylab= "Elicited Number", main="Beliefs T2S3", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", BM23[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", BM23[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", BM23[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", BM23[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", BM23[5]),cex=0.9, font=2)
matplot(C23, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T2S3
        xlab= "Period", ylab= "Chosen Number", main="Choices T2S3", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM23[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM23[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM23[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM23[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM23[5]),cex=0.9, font=2)

matplot(Bm31, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1, #Beliefs T3S1
        xlab= "Period", ylab= "Elicited Number", main="Beliefs T3S1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", BM31[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", BM31[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", BM31[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", BM31[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", BM31[5]),cex=0.9, font=2)
matplot(C31, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T3S1
        xlab= "Period", ylab= "Chosen Number", main="Choices T3S1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM31[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM31[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM31[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM31[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM31[5]),cex=0.9, font=2)

matplot(Bm32, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1, #Beliefs T3S2
        xlab= "Period", ylab= "Elicited Number", main="Beliefs T3S2", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", BM32[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", BM32[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", BM32[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", BM32[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", BM32[5]),cex=0.9, font=2)
matplot(C32, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T3S2
        xlab= "Period", ylab= "Chosen Number", main="Choices T3S2", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM32[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM32[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM32[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM32[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM32[5]),cex=0.9, font=2)

matplot(Bm33, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1, #Beliefs T3S3
        xlab= "Period", ylab= "Elicited Number", main="Beliefs T3S3", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", BM33[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", BM33[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", BM33[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", BM33[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", BM33[5]),cex=0.9, font=2)
matplot(C33, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T3S3
        xlab= "Period", ylab= "Chosen Number", main="Choices T3S3", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM33[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM33[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM33[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM33[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM33[5]),cex=0.9, font=2)

dev.off()

#### Plot All ####
pdf_name<-'All.pdf'                     #Average of all Sesions
pdf(file=pdf_name,width=18,height=9)    #Col1: Average Beliefs and Choices in T2 
layout(matrix(1:6,ncol=3, byrow=F))     #Col2: Average Beliefs and Choices in T3
                                        #Col3: All Belief and Choices, T-Test
matplot(Ba[,1:56], type="b", lty=1, lwd=4, pch=21, col=Colors1,      #Beliefs T2
        cex=1, xlab="Period", ylab="Elicited Number", main="Beliefs T2", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", TBa[1,3]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", TBa[2,3]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", TBa[3,3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", TBa[4,3]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", TBa[5,3]),cex=0.9, font=2)
matplot(Ca[,1:56], type="b", lty=1, lwd=4, pch=21, col=Colors1,      #Choices T2
        cex=1, xlab="Period", ylab="Chosen Number", main="Choices T2",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", TCa[1,3]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", TCa[2,3]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", TCa[3,3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", TCa[4,3]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", TCa[5,3]),cex=0.9, font=2)

matplot(Ba[,57:116], type="b", lty=1, lwd=4, pch=21, col=Colors1,    #Beliefs T3
        cex=1, xlab="Period", ylab="Elicited Number", main="Beliefs T3",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", TBa[1,4]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", TBa[2,4]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", TBa[3,4]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", TBa[4,4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", TBa[5,4]),cex=0.9, font=2)
matplot(Ca[,57:116], type="b", lty=1, lwd=4, pch=21, col=Colors1,    #Choices T3
        cex=1, xlab="Period", ylab="Chosen Number", main="Choices T3",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", TCa[1,4]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", TCa[2,4]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", TCa[3,4]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", TCa[4,4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", TCa[5,4]),cex=0.9, font=2)

matplot(Ba, type="b", lty=1, lwd=4, pch=21, col=Colors1,             #All Beliefs
        cex=1, xlab="Period", ylab="Elicited Number", main="All Beliefs",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(3.5,95,"T-Statistic",cex=0.9,font=2)                            #T-Statistics
text(3.5,90,paste("Period 1 = ", TBa[1,1]),cex=0.9, font=2)
text(3.5,85,paste("Period 2 = ", TBa[2,1]),cex=0.9, font=2)
text(3.5,80,paste("Period 3 = ", TBa[3,1]),cex=0.9, font=2)
text(3.5,75,paste("Period 4 = ", TBa[4,1]),cex=0.9, font=2)
text(3.5,70,paste("Period 5 = ", TBa[5,1]),cex=0.9, font=2)
text(4.5,95,"p-Value",cex=0.9,font=2)                                #p-Values
text(4.5,90,paste("Period 1 = ", TBa[1,2]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", TBa[2,2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", TBa[3,2]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", TBa[4,2]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", TBa[5,2]),cex=0.9, font=2)
matplot(Ca, type="b", lty=1, lwd=4, pch=21, col=Colors1,             #All Choices
        cex=1, xlab="Period", ylab="Chosen Number", main="All Choices",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
text(3.5,95,"T-Statistic",cex=0.9,font=2)                            #T-Statistics
text(3.5,90,paste("Period 1 = ", TCa[1,1]),cex=0.9, font=2)
text(3.5,85,paste("Period 2 = ", TCa[2,1]),cex=0.9, font=2)
text(3.5,80,paste("Period 3 = ", TCa[3,1]),cex=0.9, font=2)
text(3.5,75,paste("Period 4 = ", TCa[4,1]),cex=0.9, font=2)
text(3.5,70,paste("Period 5 = ", TCa[5,1]),cex=0.9, font=2)
text(4.5,95,"p-Value",cex=0.9,font=2)                                #p-Values
text(4.5,90,paste("Period 1 = ", TCa[1,2]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", TCa[2,2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", TCa[3,2]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", TCa[4,2]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", TCa[5,2]),cex=0.9, font=2)

dev.off()

#### Plot Hist ####
#Fa is positive= More sofistication in beliefs than choices
#Fa is negative= More sofistication in choices than beliefs

Center <- matrix(data=NA, nrow=5, ncol=3)                   #Percentajes in Ranges
for (c in 1:5){                                             #c: Periods
  summ=0                                                    #summ: Counter
  for (d in 1:116){                                         #d: Players
    if (Fa[c,d] >= -1 &&  Fa[c,d] <=1) { summ = summ + 1 }} #Central Range: -1 to 1
  Center[c,1]<-(summ /116)*100                              #Col1: Central Range
}
for (c in 1:5){                                             #c: Periods
  summ=0                                                    #summ: Counter
  for (d in 1:116){                                         #d: Players
    if (Fa[c,d] > 1) { summ = summ + 1 }}                   #Left Range: 1 to 100
  Center[c,2]<-(summ /116)*100                              #Col2: Left Range
}
for (c in 1:5){                                             #c: Periods
  summ=0                                                    #summ: Counter
  for (d in 1:116){                                         #d: Players
    if (Fa[c,d] < -1) { summ = summ + 1 }}                  #Right Range: -100 to -1
  Center[c,3]<-(summ /116)*100                              #Col3: Right Range
}
Center <- round(Center,2)                                   #Round Percentajes

pdf_name<-'Hist.pdf'                                      #Histogram of Differences
pdf(file=pdf_name,width=9,height=9)                       #By Period
layout(matrix(1:6,ncol=2, byrow=T))                       #By ranges of 1

for (a in 1:5){                                                      #a: Periods
  hist(Fa[a,],breaks=100,xlim=c(-100,50), ylim=c(0,22), col="black", #Ranges of 1
       xlab="Differences (by 1)", ylab="Frecuency", main="")
  text(-25,20,paste("Period ", a),cex=1.2, font=2)                  #Periods
  text(-80,10,paste("% = ", Center[a,3]),cex=0.9, font=2)            #Right Range
  text(40,10,paste("% = ", Center[a,2]),cex=0.9, font=2)             #Left Range
  text(-20,13,paste("% = ", Center[a,1]),cex=0.9, font=2)            #Central Range
  lines(c(-1,-1),c(-1,100),type="l",col="red")                       #Right Red Line
  lines(c(1,1),c(-1,100),type="l",col="red")                         #Left Red Line
}
plot(1, type="n", axes=F, xlab="", ylab="")                          #Blank Plot

dev.off()

#### Plot Lineal ####
Bap <- matrix(data=NA, nrow=5, ncol=116)                       #All Beliefs*2/3
Bap <- Ba*(2/3)                                                #All Beliefs*2/3

pdf_name<-'Lineal.pdf'                                         #Correlation Plot
pdf(file=pdf_name,width=9,height=12)                           #Beliefs x Choices
layout(matrix(1:6,ncol=2, byrow=T))

for (a in 1:5){                                                #a: Period
  plot(Bap[a,],Ca[a,],xlim=c(0,100), ylim=c(0,100),            #x axis: Beliefs
       xlab="Elicited Number", ylab="Chosen Number", main="")  #y axis: Choices
  text(10,90,paste("Period ", a),cex=1.2, font=2)
  lines(c(-10,110), c(-10,110), col="Red")
}
plot(1, type="n", axes=F, xlab="", ylab="")                    #Blank Plot

dev.off()