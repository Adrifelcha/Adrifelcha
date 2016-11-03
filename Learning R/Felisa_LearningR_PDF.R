#Probability functions
rm(list=ls())

library(stats4)
#n<-10
#x<-7
data<-rbinom(10,1,.7)

LL<-function(prob){
  R=dbinom(data,n,prob)
  -sum(log(R))
}

mle(minuslogl = LL, start = list(prob = 0.5), method = "L-BFGS-B", lower = 0, upper = 1)



dbinom_w0<-dbinom(x, n, prob=0)
dbinom_w1<-dbinom(x, n, prob=0.1)
dbinom_w2<-dbinom(x, n, prob=0.2)
dbinom_w3<-dbinom(x, n, prob=0.3)
dbinom_w4<-dbinom(x, n, prob=0.4)
dbinom_w5<-dbinom(x, n, prob=0.5)
dbinom_w6<-dbinom(x, n, prob=0.6)
dbinom_w7<-dbinom(x, n, prob=0.7)
dbinom_w8<-dbinom(x, n, prob=0.8)
dbinom_w9<-dbinom(x, n, prob=0.9)
dbinom_w10<-dbinom(x, n, prob=1)

#plot(soporte,d_ruido,type='l',lwd=2)
#lines(soporte,d_senal,type='l',col='purple',lwd=2)
soporte<-seq(0,10,.1)

plot(soporte, main="PDF por cada posible valor de W",cex.main=1.7, dbinom_w1,type='l',lwd=2,col='purple', xlab="Numero de exitos", ylab="Probabilidad (#Exitos | n=10, Wi)",cex.lab=1.2)
axis(1,at=c(1:10),labels=c("1","2","3","4","5","6","7","8","9","10"),las=1)
axis(2,labels=FALSE,las=1)
lines(soporte, dbinom_w2,type='l',lwd=2, col='green')
lines(soporte, dbinom_w3,type='l',lwd=2, col='blue')
lines(soporte, dbinom_w4,type='l',lwd=2, col='pink')
lines(soporte, dbinom_w5,type='l',lwd=2, col='red',lty=1)
lines(soporte, dbinom_w6,type='l',lwd=2, col='darkgoldenrod2')
lines(soporte, dbinom_w7,type='l',lwd=2, col='brown')
lines(soporte, dbinom_w8,type='l',lwd=2,col='gray')
lines(soporte, dbinom_w9,type='l',lwd=2)
text(3,.12,paste("W=0.1"),cex=1,col='purple',f=2)
text(3.5,.10,paste("W=0.2"),cex=1,col='green',f=2)
text(4,.12,paste("W=0.3"),cex=1,col='Blue',f=2)
text(4.5,.10,paste("W=0.4"),cex=1,col='pink',f=2)
text(5,.12,paste("W=0.5"),cex=1,col='red',f=2)
text(5.5,.10,paste("W=0.6"),cex=1,col='darkgoldenrod2',f=2)
text(6,.12,paste("W=0.7"),cex=1,col='brown',f=2)
text(6.5,.10,paste("W=0.8"),cex=1,col='gray',f=2)
text(7,.12,paste("W=0.9"),cex=1,f=2)

likel<-(dbinom_w2*dbinom_w3*dbinom_w4*dbinom_w5*dbinom_w6*dbinom_w7*dbinom_w8*dbinom_w9)