rm(list=ls())                                                      #Clear Data
#setwd("/Volumes/NO NAME/APLICACION/Lahav")                        #Mac Directory
setwd("D:/APLICACION/Lahav")                                       #USB Directory
library("grDevices", lib.loc="C:/Program Files/R/R-3.1.1/library") #Colors Library
Treat1 <- read.csv("DataLahav1.csv")                               #Treatment 1 Data
Treat23 <- read.csv("DataLahav23.csv")                             #Treatment 2 Data
Treat23x <- read.csv("DataLahav23x.csv")              #Treatment 2 Data Reordered
Data2 <- read.csv("DataLahavMod.csv")                              #Import Data Exp2
Data2x <- read.csv("DataLahav2.csv")                           #Data Exp2 Original

Kg <- c(5,15.5,25.5,35.5,45.5,55.5,65.5,75.5,85.5,95.5) #K^: Average of Values of K

Colors1 <- "#7D7D7D1A"                                  #Low Alpha Gray Color

#### T1 ####

C1 <- matrix(data=NA, nrow=5, ncol=54)    #Choices of All Players
CM1 <- matrix(data=NA, nrow=5, ncol=1)    #Average Choices
Session1 <- c(0,85)          #Starting Points of each Session
Period1 <- c(0,17,34,51,68)                 #Starting Points of each Period
Period11 <- c(0,20,40,60,80)
Player1 <- c(0,17)              #Starting Points of each Player

for (c in 1:2){ for (b in 1:5){ for (a in 1:17){
  for (d in 1:20){                             #a: Players  b: Periods  c: Sessions
  Cx1 <- Treat1[Session1[c]+Period1[b]+a,7]    #Player a Period b Session c Choice
  Cx11 <- Treat1[170+Period11[b]+d,7]
  Cm1 <- Treat1[Session1[c]+Period1[b]+a,8]    #Average Numbe in Period b Session c
  Cm11 <- Treat1[170+Period11[b]+d,8]
  C1[b,Player1[c]+a] <- Cx1                    #All Players Choices
  C1[b,d+34] <- Cx11
  CM1[b,1] <- (sum(C1[b,]))/54                   #Average Choices
  CM1 <- round(CM1,2)                          #Round Average Choices 
}}}}

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

#### Analysis Exp2 ####

B2 <- matrix(data=NA, nrow=5, ncol=24)    #Beliefs of All Players
C2 <- matrix(data=NA, nrow=5, ncol=24)    #Choices of All Players
Fi2 <- matrix(data=NA, nrow=5, ncol=24)   #Differences*2/3 of All Players
Di2 <- matrix(data=NA, nrow=5, ncol=24)   #Raw Differences of All Players
Fm2 <- matrix(data=NA, nrow=5, ncol=1)    #Average Differences*2/3
Dm2 <- matrix(data=NA, nrow=5, ncol=1)    #Average raw Differences
BM2 <- matrix(data=NA, nrow=5, ncol=1)    #Average Beliefs
CM2 <- matrix(data=NA, nrow=5, ncol=1)    #Average Choices
Session2 <- c(0,20,40,60,80,100)          #Starting Points of each Session
Period2 <- c(0,4,8,12,16)                 #Starting Points of each Period
Player2 <- c(0,4,8,12,16,20)              #Starting Points of each Player

for (c in 1:6){ for (b in 1:5){ for (a in 1:4){  #a: Players  b: Periods  c: Sessions
  K2 <- Data2[Session2[c]+Period2[b]+a,7:16]   #Player Distribution of Others Numbers
  Bx2 <- sum(Kg*K2)/4                          #Player a Period b Session c Belief
  Cx2 <- Data2[Session2[c]+Period2[b]+a,20]    #Pl ayer a Period b Session c Choice
  Cm2 <- Data2[Session2[c]+Period2[b]+a,27]    #Average Numbe in Period b Session c 
  Fi2[b,Player2[c]+a] <- (((2/3)*Bx2)-Cx2)  #Difference between Belief*2/3 and Choice
  Di2[b,Player2[c]+a] <- (Bx2-Cx2)          #Difference between raw Belief and Choice
  B2[b,Player2[c]+a] <- Bx2                    #All Players Beliefs
  C2[b,Player2[c]+a] <- Cx2                    #All Players Choices
  BM2[b] <- (sum(B2[b,]))/24                   #Average Beliefs
  CM2[b] <- (sum(C2[b,]))/24                   #Average Choices
  BM2 <- round(BM2,2)                          #Round Average Beliefs
  CM2 <- round(CM2,2)                          #Round Average Choices   
  Fm2[b,1] <- (sum(Fi2[b,]))/24                #Average Differencies*2/3
  Dm2[b,1] <- (sum(Di2[b,]))/24                #Average raw Differencies
}}}

#### Plot T1 ####

matplot(C1, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T1
        xlab= "Period", ylab= "Chosen Number", main="Choices T1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
lines(CM1[1:5],type="b",lwd=4, col="gray28")
text(4.5,95,"Averages",cex=0.9,font=2)
text(4.5,90,paste("Period 1 = ", CM1[1]),cex=0.9, font=2)
text(4.5,85,paste("Period 2 = ", CM1[2]),cex=0.9, font=2)
text(4.5,80,paste("Period 3 = ", CM1[3]),cex=0.9, font=2)
text(4.5,75,paste("Period 4 = ", CM1[4]),cex=0.9, font=2)
text(4.5,70,paste("Period 5 = ", CM1[5]),cex=0.9, font=2)

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

Fxa <- matrix(data=NA, nrow=1, ncol=580)
Fxa[,1:116]<-Fa[1,]
Fxa[,117:232]<-Fa[2,]
Fxa[,233:348]<-Fa[3,]
Fxa[,349:464]<-Fa[4,]
Fxa[,465:580]<-Fa[5,]

Center <- matrix(data=NA, nrow=6, ncol=3)                   #Percentajes in Ranges
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
summ=0
for (a in 1:580){
if (Fxa[,a] >= -1 && Fxa[,a] <= 1) { summ = summ +1}}
Center[6,1]<-(summ/580)*100
summ=0
for (a in 1:580){
  if (Fxa[,a] > 1) { summ = summ +1}}
  Center[6,2]<-(summ/580)*100
summ=0
for (a in 1:580){
  if (Fxa[,a] < -1) { summ = summ +1}}
  Center[6,3]<-(summ/580)*100
Center <- round(Center,2)                                   #Round Percentajes

pdf_name<-'Hist4.pdf'                                      #Histogram of Differences
pdf(file=pdf_name,width=9,height=6)                       #By Period
layout(matrix(1:6,ncol=3, byrow=T))                       #/By ranges of 1

for (a in 1:5){                                                      #a: Periods
  hist(Fa[a,],breaks=100,xlim=c(-100,50), ylim=c(0,22), col="black", #Ranges of 1
       xlab="Differences (by 1)", ylab="Frecuency", main="")
  text(-27,20,paste("Period ", a),cex=1.2, font=2)                  #Periods
  text(-82,10,paste("% = ", Center[a,3]),cex=0.9, font=2)            #Right Range
  text(38,10,paste("% = ", Center[a,2]),cex=0.9, font=2)             #Left Range
  text(-24,13,paste("% = ", Center[a,1]),cex=0.9, font=2)            #Central Range
  lines(c(-1,-1),c(-1,100),type="l", lty=3, col="red")               #Right Red Line
  lines(c(1,1),c(-1,100),type="l", lty=3, col="red")                 #Left Red Line
}

hist(Fxa[1,],breaks=100,xlim=c(-100,50), ylim=c(0,60), col="black", #Ranges of 1
     xlab="Differences (by 1)", ylab="Frecuency", main="")
text(-27,53,paste("All ", a),cex=1.2, font=2)                  #Periods
text(-82,25,paste("% = ", Center[6,3]),cex=0.9, font=2)            #Right Range
text(34,25,paste("% = ", Center[6,2]),cex=0.9, font=2)             #Left Range
text(-24,32,paste("% = ", Center[6,1]),cex=0.9, font=2)            #Central Range
lines(c(-1,-1),c(-1,100),type="l", lty=3, col="red")               #Right Red Line
lines(c(1,1),c(-1,100),type="l", lty=3, col="red")                 #Left Red Line

dev.off()

#### Plot Lineal ####
Bap <- matrix(data=NA, nrow=5, ncol=116)                       #All Beliefs*2/3
Bap <- Ba*(2/3)                                                #All Beliefs*2/3

pdf_name<-'Lineal.pdf'                                         #Correlation Plot
pdf(file=pdf_name,width=12,height=8)                           #Beliefs x Choices
layout(matrix(1:6,ncol=3, byrow=T))

for (a in 1:5){                                                #a: Period
  plot(Bap[a,],Ca[a,],xlim=c(0,100), ylim=c(0,100),            #x axis: Beliefs
       pch=21, col="#EC0E0E80", bg="#EC0E0E80",
       xlab="Elicited Number", ylab="Chosen Number", main="")  #y axis: Choices
  text(10,90,paste("Period ", a),cex=1.2, font=2)
  lines(c(-10,110), c(-10,110), col="Black")
}
plot(Bap[1:5,],Ca[1:5,],xlim=c(0,100), ylim=c(0,100),            #x axis: Beliefs
     pch=21, col="#EC0E0E80", bg="#EC0E0E80",
     xlab="Elicited Number", ylab="Chosen Number", main="")  #y axis: Choices
text(10,90,paste("All ", a),cex=1.2, font=2)
lines(c(-10,110), c(-10,110), col="Black")

dev.off()

#### Plot Lines2 ####
pdf_name<-'Lines2.pdf'                     #Average of all Sesions
pdf(file=pdf_name,width=18,height=9)
layout(matrix(1:2,ncol=2, byrow=T))

matplot(B2, type="b", lty=1, lwd=4, pch=21, col=Colors1,             #All Beliefs
        cex=1, xlab="Period", ylab="Elicited Number", main="All Beliefs",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
matplot(C2, type="b", lty=1, lwd=4, pch=21, col=Colors1,             #All Choices
        cex=1, xlab="Period", ylab="Chosen Number", main="All Choices",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)

dev.off()

#### Plot Hist2 ####
#Fa is positive= More sofistication in beliefs than choices
#Fa is negative= More sofistication in choices than beliefs

Center2 <- matrix(data=NA, nrow=5, ncol=3)                   #Percentajes in Ranges
for (c in 1:5){                                             #c: Periods
  summ=0                                                    #summ: Counter
  for (d in 1:24){                                         #d: Players
    if (Fi2[c,d] >= -1 &&  Fi2[c,d] <=1) { summ = summ + 1 }} #Central Range: -1 to 1
  Center2[c,1]<-(summ /24)*100                              #Col1: Central Range
}
for (c in 1:5){                                             #c: Periods
  summ=0                                                    #summ: Counter
  for (d in 1:24){                                         #d: Players
    if (Fi2[c,d] > 1) { summ = summ + 1 }}                   #Left Range: 1 to 100
  Center2[c,2]<-(summ /24)*100                              #Col2: Left Range
}
for (c in 1:5){                                             #c: Periods
  summ=0                                                    #summ: Counter
  for (d in 1:24){                                         #d: Players
    if (Fi2[c,d] < -1) { summ = summ + 1 }}                  #Right Range: -100 to -1
  Center2[c,3]<-(summ /24)*100                              #Col3: Right Range
}
Center2 <- round(Center2,2)                                   #Round Percentajes

pdf_name<-'Hist2.pdf'                                      #Histogram of Differences
pdf(file=pdf_name,width=9,height=9)                       #By Period
layout(matrix(1:6,ncol=2, byrow=T))                       #By ranges of 1

for (a in 1:5){                                                      #a: Periods
  hist(Fi2[a,],breaks=100,xlim=c(-50,30), ylim=c(0,7), col="black", #Ranges of 1
       xlab="Differences (by 1)", ylab="Frecuency", main="")
  text(-10,6,paste("Period ", a),cex=1.2, font=2)                  #Periods
  text(-45,4,paste("% = ", Center2[a,3]),cex=0.9, font=2)            #Right Range
  text(25,4,paste("% = ", Center2[a,2]),cex=0.9, font=2)             #Left Range
  text(-5,5,paste("% = ", Center2[a,1]),cex=0.9, font=2)            #Central Range
  lines(c(-1,-1),c(-1,100),type="l",col="red")                       #Right Red Line
  lines(c(1,1),c(-1,100),type="l",col="red")                         #Left Red Line
}
plot(1, type="n", axes=F, xlab="", ylab="")                          #Blank Plot

dev.off()

#### Plot Correlation2 ####
Bp2 <- matrix(data=NA, nrow=5, ncol=24)                       #All Beliefs*2/3
Bp2 <- B2*(2/3)                                              #All Beliefs*2/3

pdf_name<-'Cor2.pdf'                                         #Correlation Plot
pdf(file=pdf_name,width=9,height=12)                         #Beliefs x Choices
layout(matrix(1:6,ncol=2, byrow=T))

for (a in 1:5){                                                #a: Period
  plot(Bp2[a,],C2[a,],xlim=c(0,100), ylim=c(0,100),            #x axis: Beliefs
       xlab="Elicited Number", ylab="Chosen Number", main="")  #y axis: Choices
  text(10,90,paste("Period ", a),cex=1.2, font=2)
  lines(c(-10,110), c(-10,110), col="Red")
}
plot(1, type="n", axes=F, xlab="", ylab="")                    #Blank Plot

dev.off()

#### Plot Bar Comp ####
Desv <- matrix(data=NA, nrow=5, ncol=2)
for (e in 1:5){
Desv[e,1] <- sd(Fa[e,])
Desv[e,2] <- sd(Fi2[e,])
}
Desv[,1] <- (Desv[,1]/(sqrt(116)))
Desv[,2] <- (Desv[,2]/(sqrt(24)))
Comp <- cbind(Fma,Fm2)
Comp <- Comp*-1
Bars <- c(1.5,4.5,7.5,10.5,13.5)

pdf_name<-'BarComp.pdf'                     #Average of all Sesions
pdf(file=pdf_name,width=6,height=4)
layout(matrix(1,ncol=1, byrow=T))

barplot(t(Comp),names.arg=c(1:5), beside=T, col=c("grey39","Grey"),
        xlab="Period", ylab="Difference between choice and belief", ylim=c(-1,14))
for (e in 1:5){
  lines(c(Bars[e],Bars[e]),c(Comp[e,1]-Desv[e,1],Comp[e,1]+Desv[e,1]))
  lines(c(Bars[e]+1,Bars[e]+1),c(Comp[e,2]-Desv[e,2],Comp[e,2]+Desv[e,2]))
  lines(c(Bars[e]-0.3,Bars[e]+0.3),c(Comp[e,1]-Desv[e,1],Comp[e,1]-Desv[e,1]))
  lines(c(Bars[e]-0.3,Bars[e]+0.3),c(Comp[e,1]+Desv[e,1],Comp[e,1]+Desv[e,1]))
  lines(c(Bars[e]+0.7,Bars[e]+1.3),c(Comp[e,2]-Desv[e,2],Comp[e,2]-Desv[e,2]))
  lines(c(Bars[e]+0.7,Bars[e]+1.3),c(Comp[e,2]+Desv[e,2],Comp[e,2]+Desv[e,2]))
}

lines(c(0,15),c(0,0))
points(10,9, pch=15, col="grey39")
points(10,8, pch=15, col="Grey")
text(12,9,"20 Participants")
text(12,8,"4 Participants")

dev.off()

#### Plot CompCor ####
pdf_name<-'CompCor.pdf'                                         #Correlation Plot
pdf(file=pdf_name,width=12,height=8)                           #Beliefs x Choices
layout(matrix(1:6,ncol=3, byrow=T))

for (a in 1:5){                                                #a: Period
  plot(Bap[a,],Ca[a,],xlim=c(0,100), ylim=c(0,100),            #x axis: Beliefs
       pch=21, col="#EC0E0E80", bg="#EC0E0E80",
       xlab="Elicited Number", ylab="Chosen Number", main="")  #y axis: Choices
  points(Bp2[a,],C2[a,],pch=21, col="#0B03FF80", bg="#0B03FF80")
  text(10,90,paste("Period ", a),cex=1.2, font=2)
  lines(c(-10,110), c(-10,110))
}
plot(Bap[1:5,],Ca[1:5,],xlim=c(0,100), ylim=c(0,100),            #x axis: Beliefs
     pch=21, col="#EC0E0E80", bg="#EC0E0E80",
     xlab="Elicited Number", ylab="Chosen Number", main="")  #y axis: Choices
points(Bp2[1:5,],C2[1:5,],pch=21, col="#0B03FF80", bg="#0B03FF80")
text(10,90,paste("All ", a),cex=1.2, font=2)
lines(c(-10,110), c(-10,110))

dev.off()

#### ANOVA ####
Anova <- matrix(data=NA, nrow=170, ncol=2)
Anova[1:54,2] <- 1
Anova[55:111,2] <- 2
Anova[110:170,2] <- 3

Anova[,1] <- rbind(c(C1[1,],Ca[1,]))
Anova1 <- data.frame(Anova)
Anova1$X2 = factor(Anova1$X2, labels = c("T1","T2","T3"))
Anova1x <- aov(X1~X2,data=Anova1)
summary(Anova1x)
TukeyHSD(Anova1x,"X2")

Anova[,1] <- rbind(c(C1[2,],Ca[2,]))
Anova2 <- data.frame(Anova)
Anova2$X2 = factor(Anova2$X2, labels = c("T1","T2","T3"))
Anova2x <- aov(X1~X2,data=Anova2)
summary(Anova2x)
TukeyHSD(Anova2x,"X2")

Anova[,1] <- rbind(c(C1[3,],Ca[3,]))
Anova3 <- data.frame(Anova)
Anova3$X2 = factor(Anova3$X2, labels = c("T1","T2","T3"))
Anova3x <- aov(X1~X2,data=Anova3)
summary(Anova3x)
TukeyHSD(Anova3x,"X2")

Anova[,1] <- rbind(c(C1[4,],Ca[4,]))
Anova4 <- data.frame(Anova)
Anova4$X2 = factor(Anova4$X2, labels = c("T1","T2","T3"))
Anova4x <- aov(X1~X2,data=Anova4)
summary(Anova4x)
TukeyHSD(Anova4x,"X2")

Anova[,1] <- rbind(c(C1[5,],Ca[5,]))
Anova5 <- data.frame(Anova)
Anova5$X2 = factor(Anova5$X2, labels = c("T1","T2","T3"))
Anova5x <- aov(X1~X2,data=Anova5)
summary(Anova5x)
TukeyHSD(Anova5x,"X2")

hist(residuals(Anova1x),freq=F)
curve(dnorm(x,0,1.1),from=-10,to=100,add=T) #1.1 == Residual Standard Error
qqnorm(residuals(Anova1x))
qqline(residuals(Anova1x),distribution=qnorm)
acf(residuals(Anova1x))
boxplot(residuals(Anova1x)~Anovax$fitted.values)

#### Plot Choices between Treatments H1 ####

pdf_name<-'ChoicesAllT2.pdf'                    
pdf(file=pdf_name,width=12,height=8)    
layout(matrix(1:4,ncol=2, byrow=T)) 

matplot(C1, type="b", lty=1, lwd=4, pch=21, cex=1, col=Colors1,  #Choices T1
        xlab= "Period", ylab= "Chosen NumberH", main="Choices T1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 10), las=1)
lines(CM1[1:5],type="b",lwd=4, col="gray28")
text(4.5,96,"Averages",cex=0.9,font=2)
text(4.5,89,paste("Period 1 = ", CM1[1]),cex=1, font=2)
text(4.5,82,paste("Period 2 = ", CM1[2]),cex=1, font=2)
text(4.5,75,paste("Period 3 = ", CM1[3]),cex=1, font=2)
text(4.5,68,paste("Period 4 = ", CM1[4]),cex=1, font=2)
text(4.5,61,paste("Period 5 = ", CM1[5]),cex=1, font=2)

matplot(Ca[,1:56], type="b", lty=1, lwd=4, pch=21, col=Colors1,      #Choices T2
        cex=1, xlab="Period", ylab="Chosen Number", main="Choices T2",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 10), las=1)
lines(TCa[1:5,3],type="b",lwd=4, col="gray28")
text(4.5,96,"Averages",cex=0.9,font=2)
text(4.5,89,paste("Period 1 = ", TCa[1,3]),cex=1, font=2)
text(4.5,82,paste("Period 2 = ", TCa[2,3]),cex=1, font=2)
text(4.5,75,paste("Period 3 = ", TCa[3,3]),cex=1, font=2)
text(4.5,68,paste("Period 4 = ", TCa[4,3]),cex=1, font=2)
text(4.5,61,paste("Period 5 = ", TCa[5,3]),cex=1, font=2)

matplot(Ca[,57:116], type="b", lty=1, lwd=4, pch=21, col=Colors1,    #Choices T3
        cex=1, xlab="Period", ylab="Chosen Number", main="Choices T3",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 10), las=1)
lines(TCa[1:5,4],type="b",lwd=4, col="gray28")
text(4.5,96,"Averages",cex=0.9,font=2)
text(4.5,89,paste("Period 1 = ", TCa[1,4]),cex=1, font=2)
text(4.5,82,paste("Period 2 = ", TCa[2,4]),cex=1, font=2)
text(4.5,75,paste("Period 3 = ", TCa[3,4]),cex=1, font=2)
text(4.5,68,paste("Period 4 = ", TCa[4,4]),cex=1, font=2)
text(4.5,61,paste("Period 5 = ", TCa[5,4]),cex=1, font=2)

plot(TCa[1:5,3], type="b", lty=1, lwd=4, pch=21, col=c("Green"),
     cex=1, xlab="Period", ylab="Average of Chosen Numbers", main="Average Choices",
     ylim=c(0,50), xaxp=c(1,5,4),yaxp=c(0,50,10), las=1)
lines(TCa[1:5,4],type="b",lwd=4,col="Blue")
lines(CM1[1:5],type="b",lwd=4,col="Red")
points(4,45, pch=15, col="Red")
points(4,40, pch=15, col="Green")
points(4,35, pch=15, col="Blue")
text(4.5,45,"Treatment 1",cex=1, font=2)
text(4.5,40,"Treatment 2",cex=1, font=2)
text(4.5,35,"Treatment 3",cex=1, font=2)

dev.off()

#### Plot Differences between Beliefs and Choices H2 ####

Diff <- matrix(data=NA, nrow=5, ncol=4)
for (a in 1:5){                               #a: Periods
TtestX <- t.test(Bap[a,],Ca[a,])                 # T-test
x <- do.call(rbind,TtestX[1:6])                #Convert Beliefs List in Matrix Elements
Diff[a,1] <- x[1,1]                           #T-Statistic for Beliefs in Period a
Diff[a,2] <- x[3,1]                           #p-Value for Beliefs in Period a
Diff[a,3] <- x[5,1]                           #Average of Beliefs in T2 in Period a 
Diff[a,4] <- x[5,2]                           #Average of Beliefs in T3 in Period a
Diff <- round(Diff,2)                          #Round all Beliefs Values
}

Diff2 <- matrix(data=NA, nrow=5, ncol=4)
for (a in 1:5){                               #a: Periods
  TtestX <- t.test(Ba[a,],Ca[a,])                 # T-test
  x <- do.call(rbind,TtestX[1:6])                #Convert Beliefs List in Matrix Elements
  Diff2[a,1] <- x[1,1]                           #T-Statistic for Beliefs in Period a
  Diff2[a,2] <- x[3,1]                           #p-Value for Beliefs in Period a
  Diff2[a,3] <- x[5,1]                           #Average of Beliefs in T2 in Period a 
  Diff2[a,4] <- x[5,2]                           #Average of Beliefs in T3 in Period a
  Diff2 <- round(Diff2,2)                          #Round all Beliefs Values
}

#### Plot Diferences in Levels of Sophistication H3 ? ####

#### Plot Differences in Beliefs and Choices for Big and Small Groups ####

#### Beliefs in Ranges ####

Points <- matrix(data=NA, nrow=580, ncol=11)
for(a in 1:116){
  Points[a,1] <- Treat23x[a,28]
  Points[a+116,1] <- Treat23x[a+116,28]
  Points[a+232,1] <- Treat23x[a+232,28]
  Points[a+348,1] <- Treat23x[a+348,28]
  Points[a+464,1] <- Treat23x[a+464,28]
  for (b in 1:10){
    Points[a,1+b] <- Treat23x[a,14+b]
    Points[a+116,1+b] <- Treat23x[a+116,14+b]
    Points[a+232,1+b] <- Treat23x[a+232,14+b]
    Points[a+348,1+b] <- Treat23x[a+348,14+b]
    Points[a+464,1+b] <- Treat23x[a+464,14+b]
  }}
inter <- c(0,116,232,348,464)

pdf_name<-'Points3.pdf'                                    #Histogram of Differences
pdf(file=pdf_name,width=16,height=8)                     #By Period
layout(matrix(1:10,ncol=5, byrow=T)) 

for (a in 1:10){ for (b in 1:5){                              #a: Ranges  b: Periods
  plot(Points[(1+inter[b]):(116+inter[b]),1+a],Points[(1+inter[b]):(116+inter[b]),1],
       xlim=c(1,20), ylim=c(0,100),            #x axis: Beliefs
       xlab="Players", ylab="Chosen Number", main="")  #y axis: Choices
  text(15,80,paste("Range ", a),cex=1.2, font=2)
  text(15,70,paste("Period ", b),cex=1.2, font=2)
}}
dev.off()

pdf_name<-'Points5.pdf'                                    #Histogram of Differences
pdf(file=pdf_name,width=32,height=16)                     #By Period
layout(matrix(1:50,ncol=10, byrow=F)) 

for (a in 1:10){ for (b in 1:5){                              #a: Ranges  b: Periods
  plot(Points[(1+inter[b]):(116+inter[b]),1+a],Points[(1+inter[b]):(116+inter[b]),1],
       xlim=c(1,20), ylim=c(0,100),            #x axis: Beliefs
       xlab="Players", ylab="Chosen Number", main="")  #y axis: Choices
  lines(c(-5,25),c(a*10,a*10),type="l",col="red")
  lines(c(-5,25),c((a*10)-10,(a*10)-10),type="l",col="red")
  lines(c(-5,25),c((((a*10)-5)*(2/3)),(((a*10)-5)*(2/3))),type="l",col="blue")
  text(15,80,paste("Range ", a),cex=1.2, font=2)
  text(15,70,paste("Period ", b),cex=1.2, font=2)
}}
dev.off()

#### Beliefs All ####
pdf_name<-'BeliefsAllT.pdf'                    
pdf(file=pdf_name,width=12,height=4)    
layout(matrix(1:3,ncol=3, byrow=T)) 

matplot(Ba[,1:56], type="b", lty=1, lwd=4, pch=21, col=Colors1,      #Choices T2
        cex=1, xlab="Period", ylab="Elicited Number", main="Beliefs T2",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 10), las=1)
lines(TBa[1:5,3],type="b",lwd=4, col="gray28")
text(4.5,96,"Averages",cex=0.9,font=2)
text(4.5,89,paste("Period 1 = ", TBa[1,3]),cex=1, font=2)
text(4.5,82,paste("Period 2 = ", TBa[2,3]),cex=1, font=2)
text(4.5,75,paste("Period 3 = ", TBa[3,3]),cex=1, font=2)
text(4.5,68,paste("Period 4 = ", TBa[4,3]),cex=1, font=2)
text(4.5,61,paste("Period 5 = ", TBa[5,3]),cex=1, font=2)

matplot(Ba[,57:116], type="b", lty=1, lwd=4, pch=21, col=Colors1,    #Choices T3
        cex=1, xlab="Period", ylab="Elicited Number", main="Beliefs T3",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 10), las=1)
lines(TBa[1:5,4],type="b",lwd=4, col="gray28")
text(4.5,96,"Averages",cex=0.9,font=2)
text(4.5,89,paste("Period 1 = ", TBa[1,4]),cex=1, font=2)
text(4.5,82,paste("Period 2 = ", TBa[2,4]),cex=1, font=2)
text(4.5,75,paste("Period 3 = ", TBa[3,4]),cex=1, font=2)
text(4.5,68,paste("Period 4 = ", TBa[4,4]),cex=1, font=2)
text(4.5,61,paste("Period 5 = ", TBa[5,4]),cex=1, font=2)

plot(TBa[1:5,3], type="b", lty=1, lwd=4, pch=21, col=c("Green"),
     cex=1, xlab="Period", ylab="Average of Elicited Numbers",
     main="Average Beliefs", ylim=c(0,50), xaxp=c(1,5,4),yaxp=c(0,50,10), las=1)
lines(TBa[1:5,4],type="b",lwd=4,col="Blue")
points(4,40, pch=15, col="Green")
points(4,35, pch=15, col="Blue")
text(4.5,40,"Treatment 2",cex=1, font=2)
text(4.5,35,"Treatment 3",cex=1, font=2)

dev.off()

#### Direct Comp ####
CaA <- matrix(data=NA, nrow=5, ncol=1)
BaA <- matrix(data=NA, nrow=5, ncol=1)
for (e in 1:5){
CaA[e,1] <- mean(Ca[e,])
BaA[e,1] <- mean(Ba[e,])
}
CaA <- round(CaA,2)
BaA <- round(BaA,2)

pdf_name<-'DComp.pdf'                    
pdf(file=pdf_name,width=12,height=8)    
layout(matrix(1:6,ncol=3, byrow=T)) 

matplot(Ca[,1:116], type="b", lty=1, lwd=4, pch=21, col=Colors1,      #Choices T2
        cex=1, xlab="Period", ylab="Chosen Number", main="Choices T2 & T3",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 10), las=1)
lines(CaA[1:5,1],type="b",lwd=4, col="gray28")
text(4.5,96,"Averages",cex=0.9,font=2)
text(4.5,89,paste("Period 1 = ", CaA[1,1]),cex=1, font=2)
text(4.5,82,paste("Period 2 = ", CaA[2,1]),cex=1, font=2)
text(4.5,75,paste("Period 3 = ", CaA[3,1]),cex=1, font=2)
text(4.5,68,paste("Period 4 = ", CaA[4,1]),cex=1, font=2)
text(4.5,61,paste("Period 5 = ", CaA[5,1]),cex=1, font=2)

matplot(C2[,1:24], type="b", lty=1, lwd=4, pch=21, col=Colors1,      #Choices T2
        cex=1, xlab="Period", ylab="Chosen Number", main="Choices Exp2",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 10), las=1)
lines(CM2[1:5,1],type="b",lwd=4, col="gray28")
text(4.5,96,"Averages",cex=0.9,font=2)
text(4.5,89,paste("Period 1 = ", CM2[1,1]),cex=1, font=2)
text(4.5,82,paste("Period 2 = ", CM2[2,1]),cex=1, font=2)
text(4.5,75,paste("Period 3 = ", CM2[3,1]),cex=1, font=2)
text(4.5,68,paste("Period 4 = ", CM2[4,1]),cex=1, font=2)
text(4.5,61,paste("Period 5 = ", CM2[5,1]),cex=1, font=2)

plot(CaA[1:5,1], type="b", lty=1, lwd=4, pch=21, col=c("Green"),
     cex=1, xlab="Period", ylab="Average of Chosen Numbers",
     main="Average Choices", ylim=c(0,50), xaxp=c(1,5,4),yaxp=c(0,50,10), las=1)
lines(CM2[1:5,1],type="b",lwd=4,col="Blue")
points(4,40, pch=15, col="Green")
points(4,35, pch=15, col="Blue")
text(4.5,40,"Exp 1",cex=1, font=2)
text(4.5,35,"Exp 2",cex=1, font=2)

matplot(Ba[,1:116], type="b", lty=1, lwd=4, pch=21, col=Colors1,      #Choices T2
        cex=1, xlab="Period", ylab="Elicited Number", main="Beliefs T2 & T3",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 10), las=1)
lines(BaA[1:5,1],type="b",lwd=4, col="gray28")
text(4.5,96,"Averages",cex=0.9,font=2)
text(4.5,89,paste("Period 1 = ", BaA[1,1]),cex=1, font=2)
text(4.5,82,paste("Period 2 = ", BaA[2,1]),cex=1, font=2)
text(4.5,75,paste("Period 3 = ", BaA[3,1]),cex=1, font=2)
text(4.5,68,paste("Period 4 = ", BaA[4,1]),cex=1, font=2)
text(4.5,61,paste("Period 5 = ", BaA[5,1]),cex=1, font=2)

matplot(B2[,1:24], type="b", lty=1, lwd=4, pch=21, col=Colors1,      #Choices T2
        cex=1, xlab="Period", ylab="Elicited Number", main="Beliefs Exp2",
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 10), las=1)
lines(BM2[1:5,1],type="b",lwd=4, col="gray28")
text(4.5,96,"Averages",cex=0.9,font=2)
text(4.5,89,paste("Period 1 = ", BM2[1,1]),cex=1, font=2)
text(4.5,82,paste("Period 2 = ", BM2[2,1]),cex=1, font=2)
text(4.5,75,paste("Period 3 = ", BM2[3,1]),cex=1, font=2)
text(4.5,68,paste("Period 4 = ", BM2[4,1]),cex=1, font=2)
text(4.5,61,paste("Period 5 = ", BM2[5,1]),cex=1, font=2)

plot(BaA[1:5,1], type="b", lty=1, lwd=4, pch=21, col=c("Green"),
     cex=1, xlab="Period", ylab="Average of Elicited Numbers",
     main="Average Beliefs", ylim=c(0,50), xaxp=c(1,5,4),yaxp=c(0,50,10), las=1)
lines(BM2[1:5,1],type="b",lwd=4,col="Blue")
points(4,40, pch=15, col="Green")
points(4,35, pch=15, col="Blue")
text(4.5,40,"Exp 1",cex=1, font=2)
text(4.5,35,"Exp 2",cex=1, font=2)

dev.off()

#### Direct Comp T-Test ####
t.test(Ca[1,1:116],C2[1,1:24])
t.test(Ba[1,1:116],B2[1,1:24])
t.test(Fa[1,1:116],Fi2[1,1:24])

#### Beliefs in Ranges 2 ####
Points2 <- matrix(data=NA, nrow=120, ncol=11)
for(a in 1:24){
  Points2[a,1] <- Data2x[a,20]
  Points2[a+24,1] <- Data2x[a+24,20]
  Points2[a+48,1] <- Data2x[a+48,20]
  Points2[a+72,1] <- Data2x[a+72,20]
  Points2[a+96,1] <- Data2x[a+96,20]
  for (b in 1:10){
    Points2[a,1+b] <- Data2x[a,6+b]
    Points2[a+24,1+b] <- Data2x[a+24,6+b]
    Points2[a+48,1+b] <- Data2x[a+48,6+b]
    Points2[a+72,1+b] <- Data2x[a+72,6+b]
    Points2[a+96,1+b] <- Data2x[a+96,6+b]
  }}
inter2 <- c(0,24,48,72,96)

pdf_name<-'Pointsx.pdf'                                    #Histogram of Differences
pdf(file=pdf_name,width=32,height=16)                     #By Period
layout(matrix(1:50,ncol=10, byrow=F)) 

for (a in 1:10){ for (b in 1:5){                              #a: Ranges  b: Periods
  plot(Points2[(1+inter2[b]):(24+inter2[b]),1+a],Points2[(1+inter2[b]):(24+inter2[b]),1],
       xlim=c(1,20), ylim=c(0,100),            #x axis: Beliefs
       xlab="Players", ylab="Chosen Number", main="")  #y axis: Choices
  lines(c(-5,25),c(a*10,a*10),type="l",col="red")
  lines(c(-5,25),c((a*10)-10,(a*10)-10),type="l",col="red")
  lines(c(-5,25),c((((a*10)-5)*(2/3)),(((a*10)-5)*(2/3))),type="l",col="blue")
  text(15,80,paste("Range ", a),cex=1.2, font=2)
  text(15,70,paste("Period ", b),cex=1.2, font=2)
}}
dev.off()

pdf_name<-'PointsAll.pdf'                                    #Histogram of Differences
pdf(file=pdf_name,width=32,height=16)                     #By Period
layout(matrix(1:50,ncol=10, byrow=F)) 

for (a in 1:10){ for (b in 1:5){                              #a: Ranges  b: Periods
  plot(Points2[(1+inter2[b]):(24+inter2[b]),1+a],Points2[(1+inter2[b]):(24+inter2[b]),1],
       xlim=c(1,20), ylim=c(0,100),            #x axis: Beliefs
       xlab="Players", ylab="Chosen Number", main="")  #y axis: Choices
  points(Points[(1+inter[b]):(116+inter[b]),1+a],Points[(1+inter[b]):(116+inter[b]),1])
  lines(c(-5,25),c(a*10,a*10),type="l",col="red")
  lines(c(-5,25),c((a*10)-10,(a*10)-10),type="l",col="red")
  lines(c(-5,25),c((((a*10)-5)*(2/3)),(((a*10)-5)*(2/3))),type="l",col="blue")
  text(15,80,paste("Range ", a),cex=1.2, font=2)
  text(15,70,paste("Period ", b),cex=1.2, font=2)
}}
dev.off()