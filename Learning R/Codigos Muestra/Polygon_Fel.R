rm(list=ls())
##################
#### EXAMPLE 1 
#AS SIMPLE AS....

a <- c(1:100)
b <- c(301:400)

plot(a,b, pch=8, cex=0.8, col="indianred")
for(i in 1:length(a)){
 polygon(c(a[i],a[i]), c(0,b[i]), border="forestgreen")
}



####################
##### EXAMPLE 2
# Area Under Curve

x <- seq(-3,3,0.01)
y1 <- dnorm(x,0,1)
y2 <- 0.5*dnorm(x,0,1)
x.shade <- seq(-2,1,0.01)
plot(x,y1,type="l",bty="L",xlab="X",ylab="dnorm(X)")
points(x,y2,type="l",col="gray")
l <- length(x.shade)
color <- heat.colors(l)
for (i in 1:l)
{
  polygon(c(x.shade[i],rev(x.shade[i])),c(dnorm(x.shade[i],0,1),
  0.5*dnorm(rev(x.shade[i]),0,1)),border=color[i],col=NA)
}