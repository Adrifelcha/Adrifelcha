rm(list=ls())                                                      #Clear Data
#setwd("/Volumes/NO NAME/APLICACION/Lahav")                        #Mac Directory
setwd("D:/APLICACION/Lahav")                                       #USB Directory
library("grDevices", lib.loc="C:/Program Files/R/R-3.1.1/library") #Colors Library
Data2 <- read.csv("DataLahavMod.csv")                               #Import Data

Colors1 <- "#7D7D7D4D"                                         #Low Alpha Gray Color

#### Analysis ####

Kg <- c(5,15.5,25.5,35.5,45.5,55.5,65.5,75.5,85.5,95.5)   #K^: Average of Values of K

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