x<-0:20
a<-rnorm(21,5,1)
y<-x+a
z<-x+5

plot(x,y)
lines(x,z, type="l", lty=4, lwd=2, col='blue')