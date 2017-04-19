library("grDevices", lib.loc="C:/Program Files/R/R-3.1.1/library") #Librería de rgb
rm(list=ls()) #Borra datos previos

#### DATA LOAD ####

setwd("D:/APLICACION/DATOS") #Indica el directorio de trabajo

He1_1 <- read.csv("He1_1.csv")
He1_2 <- read.csv("He1_2.csv")
He1_3 <- read.csv("He1_3.csv")
HeT_1 <- read.csv("HeT_1.csv")
HeT_2 <- read.csv("HeT_2.csv")
HeT_3 <- read.csv("HeT_3.csv")
HeT_4 <- read.csv("HeT_4.csv")
Es1_1 <- read.csv("Es1_1.csv")
Es1_2 <- read.csv("Es1_2.csv")
Es1_3 <- read.csv("Es1_3.csv")
EsT_1 <- read.csv("EsT_1.csv")
EsT_2 <- read.csv("EsT_2.csv")
EsT_3 <- read.csv("EsT_3.csv")
Ex1_1 <- read.csv("Ex1_1.csv")
Ex1_2 <- read.csv("Ex1_2.csv")
Ex1_3 <- read.csv("Ex1_3.csv")
ExT_1 <- read.csv("ExT_1.csv")
ExT_2 <- read.csv("ExT_2.csv")
ExT_3 <- read.csv("ExT_3.csv")
Pr1_1 <- read.csv("Pr1_1.csv")
PrT_1 <- read.csv("PrT_1.csv")
PrT_2 <- read.csv("PrT_2.csv")
PrT_3 <- read.csv("PrT_3.csv")

#### DATA ANALYSIS ####

CH1 <- matrix(data=NA, nrow=4, ncol=9)    #Choices of All Players in Heu-1
CHT <- matrix(data=NA, nrow=4, ncol=9)    #Choices of All Players in Heu-T
CS1 <- matrix(data=NA, nrow=4, ncol=9)    #Choices of All Players in Est-1
CST <- matrix(data=NA, nrow=4, ncol=9)    #Choices of All Players in Est-T
CX1 <- matrix(data=NA, nrow=4, ncol=9)    #Choices of All Players in Exp-1
CXT <- matrix(data=NA, nrow=4, ncol=9)    #Choices of All Players in Exp-T
CPT <- matrix(data=NA, nrow=4, ncol=12)   #Choices of All Players in Prep

CMH1 <- matrix(data=NA, nrow=4, ncol=1)    #Average Choices of All Players in Heu-1
CMHT <- matrix(data=NA, nrow=4, ncol=1)    #Average Choices of All Players in Heu-T
CMS1 <- matrix(data=NA, nrow=4, ncol=1)    #Average Choices of All Players in Est-1
CMST <- matrix(data=NA, nrow=4, ncol=1)    #Average Choices of All Players in Est-T
CMX1 <- matrix(data=NA, nrow=4, ncol=1)    #Average Choices of All Players in Exp-1
CMXT <- matrix(data=NA, nrow=4, ncol=1)    #Average Choices of All Players in Exp-T
CMPT <- matrix(data=NA, nrow=4, ncol=1)    #Average Choices of All Players in Prep

for (a in 1:4){ for (b in 1:3){
  CH1[a,b] <- He1_1[a,b]
  CH1[a,b+3] <- He1_2[a,b]
  CH1[a,b+6] <- He1_3[a,b]

  CHT[a,b] <- HeT_1[a,b]
  CHT[a,b+3] <- HeT_2[a,b]
  CHT[a,b+6] <- HeT_3[a,b]

  CS1[a,b] <- Es1_1[a,b]
  CS1[a,b+3] <- Es1_2[a,b]
  CS1[a,b+6] <- Es1_3[a,b]

  CST[a,b] <- EsT_1[a,b]
  CST[a,b+3] <- EsT_2[a,b]
  CST[a,b+6] <- EsT_3[a,b]

  CX1[a,b] <- Ex1_1[a,b]
  CX1[a,b+3] <- Ex1_2[a,b]
  CX1[a,b+6] <- Ex1_3[a,b]

  CXT[a,b] <- ExT_1[a,b]
  CXT[a,b+3] <- ExT_2[a,b]
  CXT[a,b+6] <- ExT_3[a,b]

  CPT[a,b] <- Pr1_1[a,b]
  CPT[a,b+3] <- PrT_1[a,b]
  CPT[a,b+6] <- PrT_2[a,b]
  CPT[a,b+9] <- PrT_3[a,b]  
}}

for (a in 1:4){
CMH1[a] <- mean(CH1[a,])
CMHT[a] <- mean(CHT[a,])
CMS1[a] <- mean(CS1[a,])
CMST[a] <- mean(CST[a,])
CMX1[a] <- mean(CX1[a,])
CMXT[a] <- mean(CXT[a,])
CMPT[a] <- mean(CPT[a,])
}

#### PLOTS ####

pdf_name<-'NEW.pdf'          
pdf(file=pdf_name,width=8,height=16)     
layout(matrix(1:8,ncol=2, byrow=T)) 

matplot(CH1, type="b", lty=1, lwd=4, pch=21, cex=1, col=c("red","blue","blue"),
        xlab= "Period", ylab= "Chosen Number", main="Heu-1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
lines(CMH1[1:4],type="b",lwd=4, col="black")
text(4.5,95,"Averages",cex=0.9,font=2)
text(3.5,90,paste("Period 1 = ", CMH1[1]),cex=0.9, font=2)
text(3.5,85,paste("Period 2 = ", CMH1[2]),cex=0.9, font=2)
text(3.5,80,paste("Period 3 = ", CMH1[3]),cex=0.9, font=2)
text(3.5,75,paste("Period 4 = ", CMH1[4]),cex=0.9, font=2)

matplot(CHT, type="b", lty=1, lwd=4, pch=21, cex=1, col=c("red","blue","blue"),
        xlab= "Period", ylab= "Chosen Number", main="Heu-T", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
lines(CMHT[1:4],type="b",lwd=4, col="black")
text(4.5,95,"Averages",cex=0.9,font=2)
text(3.5,90,paste("Period 1 = ", CMHT[1]),cex=0.9, font=2)
text(3.5,85,paste("Period 2 = ", CMHT[2]),cex=0.9, font=2)
text(3.5,80,paste("Period 3 = ", CMHT[3]),cex=0.9, font=2)
text(3.5,75,paste("Period 4 = ", CMHT[4]),cex=0.9, font=2)

matplot(CS1, type="b", lty=1, lwd=4, pch=21, cex=1, col=c("red","blue","blue"),
        xlab= "Period", ylab= "Chosen Number", main="Est-1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
lines(CMS1[1:4],type="b",lwd=4, col="black")
text(4.5,95,"Averages",cex=0.9,font=2)
text(3.5,90,paste("Period 1 = ", CMS1[1]),cex=0.9, font=2)
text(3.5,85,paste("Period 2 = ", CMS1[2]),cex=0.9, font=2)
text(3.5,80,paste("Period 3 = ", CMS1[3]),cex=0.9, font=2)
text(3.5,75,paste("Period 4 = ", CMS1[4]),cex=0.9, font=2)

matplot(CST, type="b", lty=1, lwd=4, pch=21, cex=1, col=c("red","blue","blue"),
        xlab= "Period", ylab= "Chosen Number", main="Est-T", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
lines(CMST[1:4],type="b",lwd=4, col="black")
text(4.5,95,"Averages",cex=0.9,font=2)
text(3.5,90,paste("Period 1 = ", CMST[1]),cex=0.9, font=2)
text(3.5,85,paste("Period 2 = ", CMST[2]),cex=0.9, font=2)
text(3.5,80,paste("Period 3 = ", CMST[3]),cex=0.9, font=2)
text(3.5,75,paste("Period 4 = ", CMST[4]),cex=0.9, font=2)

matplot(CX1, type="b", lty=1, lwd=4, pch=21, cex=1, col=c("red","blue","blue"),
        xlab= "Period", ylab= "Chosen Number", main="Exp-1", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
lines(CMX1[1:4],type="b",lwd=4, col="black")
text(4.5,95,"Averages",cex=0.9,font=2)
text(3.5,90,paste("Period 1 = ", CMX1[1]),cex=0.9, font=2)
text(3.5,85,paste("Period 2 = ", CMX1[2]),cex=0.9, font=2)
text(3.5,80,paste("Period 3 = ", CMX1[3]),cex=0.9, font=2)
text(3.5,75,paste("Period 4 = ", CMX1[4]),cex=0.9, font=2)

matplot(CXT, type="b", lty=1, lwd=4, pch=21, cex=1, col=c("red","blue","blue"),
        xlab= "Period", ylab= "Chosen Number", main="Exp-T", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
lines(CMXT[1:4],type="b",lwd=4, col="black")
text(4.5,95,"Averages",cex=0.9,font=2)
text(3.5,90,paste("Period 1 = ", CMXT[1]),cex=0.9, font=2)
text(3.5,85,paste("Period 2 = ", CMXT[2]),cex=0.9, font=2)
text(3.5,80,paste("Period 3 = ", CMXT[3]),cex=0.9, font=2)
text(3.5,75,paste("Period 4 = ", CMXT[4]),cex=0.9, font=2)

matplot(CPT, type="b", lty=1, lwd=4, pch=21, cex=1, col=c("red","blue","blue"),
        xlab= "Period", ylab= "Chosen Number", main="Prep", 
        ylim=c(0,100), xaxp=c(1, 5, 4), yaxp=c(0, 100, 5), las=1)
lines(CMPT[1:4],type="b",lwd=4, col="black")
text(4.5,95,"Averages",cex=0.9,font=2)
text(3.5,90,paste("Period 1 = ", CMPT[1]),cex=0.9, font=2)
text(3.5,85,paste("Period 2 = ", CMPT[2]),cex=0.9, font=2)
text(3.5,80,paste("Period 3 = ", CMPT[3]),cex=0.9, font=2)
text(3.5,75,paste("Period 4 = ", CMPT[4]),cex=0.9, font=2)

dev.off()