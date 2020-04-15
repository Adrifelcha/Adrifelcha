#############################################################
# A plot whitin a plot
#############################################################
rm(list=ls())    


################################################################
# Ejemplo Original ( de https://stackoverflow.com/questions/14288194/plot-inside-a-plot)
curve(exp(x), from=1, to=5, lwd=5)
curve(150-exp(x), from=1, to=5, lwd=5, col="darkblue",add=T)
par(new=TRUE)
par(oma=c(1,4,5,1))
par(mfcol=c(2,2), mfg=c(1,1))
par(mar=c(7,7,1,1))
curve(exp(x), from=1, to=5, lwd=7, xlab="chi", ylab="exp(x)", cex.lab=2,axes=F)
axis(1, labels=NA,at=c(0,5))
axis(2, labels=NA,at=c(0,150))
text(1,120,"Alpha",adj=c(0,0),cex=1.5)
text(4,10,"Beta",adj=c(0,0),cex=1.5)

################################################
# EJEMPLO FELI
################################################
rm(list=ls())   
x <- rnorm(1000, 10,2)
y  <- rnorm(50,2,0.1)
hist(x)

par(new=TRUE)
par(oma=c(1,1,2,1))
par(mfcol=c(2,2), mfg=c(1,1))
par(mar=c(2,7,1,1))

hist(y)