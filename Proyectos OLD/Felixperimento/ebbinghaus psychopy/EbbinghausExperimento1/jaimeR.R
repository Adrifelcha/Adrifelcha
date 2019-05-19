rm(list=ls())    #esto borra los datos

setwd("C:/Users/Adriana/Dropbox/Octavo Semestre/Taller de investigacion/Ebbinghaus PsychoPy/EbbinghausExperimento1/")
CMB1<-read.csv("Muchos-BL-FA_Suj2_A_Sa.csv")
CMT1<-read.csv("Muchos-TL-FA_Suj2_A_Sa.csv")
CMB2<-read.csv("Muchos-BL-FA_Suj3_A_Br.csv")
CMT2<-read.csv("Muchos-TL-FA_Suj3_A_Br.csv")
CMB3<-read.csv("Muchos-BL-FA_Suj4_A_An.csv")
CMT3<-read.csv("Muchos-TL-FA_Suj4AAn.csv")
CPB1<-read.csv("Pocos-BL-FA_Suj1_AAl.csv")
CPT1<-read.csv("Pocos-TL-FA_Suj1_AAl.csv")
CPB2<-read.csv("Pocos-BL-FA_Suj4AAn.csv")
CPT2<-read.csv("Pocos-TL-FA_Suj4AAn.csv")

#Comparacion baseline VS testline
Comp1<-c(CMB1[336,"ContadorH"],CMT1[336,"ContadorH"],
        CMB2[336,"ContadorH"],CMT2[336,"ContadorH"],
        CMB3[336,"ContadorH"],CMT3[336,"ContadorH"],
        CPB1[336,"ContadorH"],CPT1[336,"ContadorH"],
        CPB2[336,"ContadorH"],CPT2[336,"ContadorH"])
Comp1=Comp1/168
barplot(t(Comp1[1:6]),beside=T,ylim=c(0.8,1))
rect(0,0.5,15,-5,col="white",border=NA)
barplot(t(Comp1[7:10]),beside=T)
X<-c(CMB1[336,"ContadorH"],CMB2[336,"ContadorH"],
              CMB3[336,"ContadorH"],CPB1[336,"ContadorH"],
              CPB2[336,"ContadorH"],CMT1[336,"ContadorH"],
              CMT2[336,"ContadorH"],CMT3[336,"ContadorH"],
              CPT1[336,"ContadorH"],CPT2[336,"ContadorH"])
plot2<-matrix(X,nrow=2,ncol=5)
matplot(plot2,type="b",xlim=c(1:2),pch=1,col=1:5)
axis(1, at = seq(1,2, by=1))
