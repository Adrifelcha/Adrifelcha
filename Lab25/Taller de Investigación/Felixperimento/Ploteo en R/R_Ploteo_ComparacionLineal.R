#D' Entrenamiento 3 grupos

rm(list=ls())
Centro<-matrix(data=c(1.935,1.2803,2.6544,2.5496,2.4323,1.5504,1.7404,2.2425,2.5046,1.5467,2.8677,2.8479,2.4955,1.9219,2.4496,2.058,1.4469,.7415,3.6159,2.45965,3.048324,2.63589,2.0344,.8064,0,0,0,0,1.8925,1.831,0,0,0,0,2.3636,2.3636), nrow=2, ncol=18)
matplot(Centro, type="b", lty=1, lwd=3, pch=21, col=c("Blue","Red","Brown"),
        cex=1, ylim=c(0.5,4.0), xlim=c(0.75,2.25),
        xaxp=c(1,2,1), las=1, labels=F)

axis(1,at=c(1,2),labels=c("Pocos círculos","Muchos círculos"),las=1)
axis(2,at=c(0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0),labels=c("0","0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0"),las=1)

text(2,3.8,paste("Fácil a Difícil"),cex=1.2,col='Blue',f=2)
text(2,3.3,paste("Difícil a Fácil"),cex=1.2,col='Red',f=2)
text(2,3.55,paste("Simultáneo"),cex=1.2,col='Pink',f=2)

#D' Prueba 3 grupos

rm(list=ls())
Centro<-matrix(data=c(1.7873,.8989,3.2256,3.0667,2.0892,1.2754,3.1472,2.2708,2.2889,1.8145,3.1848,3.0236,4.4905,2.7092,3.1405,2.1557,1.6249,.9716,5.22207,3.361525,2.707343,2.412738,1.7422,.544,0,0,0,0,3.3755,1.6831,0,0,0,0,3.361,2.1004), nrow=2, ncol=18)
matplot(Centro, type="b", lty=1, lwd=3, pch=21, col=c("Blue","Red","Purple"),
        cex=1, ylim=c(0.5,5.5), xlim=c(0.75,2.25),
        xaxp=c(1,2,1), las=1, labels=F)

axis(1,at=c(1,2),labels=c("Pocos círculos","Muchos círculos"),las=1)
axis(2,at=c(0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0),labels=c("0","0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5","6.0"),las=1)

text(2,5.1,paste("Fácil a Difícil"),cex=1.2,col='Blue',f=2)
text(2,4.8,paste("Difícil a Fácil"),cex=1.2,col='Red',f=2)
text(2,4.5,paste("Simultáneo"),cex=1.2,col='Purple',f=2)

#D' Cambios en D'

rm(list=ls())
Centro<-matrix(data=c(2.4323,2.0892,1.5504,1.2754,2.8677,3.1848,2.8479,3.0236,1.4469,1.6249,.7415,.9716,2.0344,1.7422,.8064,.544,1.8925,3.3755,1.831,1.6831,2.3636,3.361,2.3636,2.1004), nrow=2, ncol=28)
matplot(Centro, type="b", lty=1, lwd=3, pch=21, col=c("Blue","Red"),
        cex=1, ylim=c(0.5,5.5), xlim=c(0.75,2.25),
        xaxp=c(1,2,1), las=1, labels=F)

axis(1,at=c(1,2),labels=c("Entrenamiento","Prueba"),las=1)
axis(2,at=c(0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5),labels=c("0","0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5"),las=1)

text(1,5,paste("Fácil"),cex=1.2,col='Blue',f=2)
text(1,5.3,paste("Difícil"),cex=1.2,col='Red',f=2)

#D' promedio de Cambios

rm(list=ls())
Centro<-matrix(data=c(2.450934,2.723914,1.913999,2.132941), nrow=2, ncol=2)
matplot(Centro, type="b", lty=1, lwd=3, pch=21, col=c("Blue","Red"),
        cex=1, ylim=c(0.5,5.5), xlim=c(0.75,2.25),
        xaxp=c(1,2,1), las=1, labels=F)

axis(1,at=c(1,2),labels=c("Entrenamiento","Prueba"),las=1)
axis(2,at=c(0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5),labels=c("0","0.5","1.0","1.5","2.0","2.5","3.0","3.5","4.0","4.5","5.0","5.5"),las=1)

text(1,4.9,paste("Fácil"),cex=1.2,col='Blue',f=2)
text(1,5.4,paste("Difícil"),cex=1.2,col='Red',f=2)


#C Entrenamiento 3 grupos

rm(list=ls())
Centro<-matrix(data=c(-.024,.091450,-.018400,.2833,.24855,.1008,.356500,-.154050,.130200,.501350,-.12505,-.04145,.135950,-.106850,.658900,.772600,-.29295,.16025,-.076319,-.079475,-.456591,-.484798,-.6513,-.1623,5,5,5,5,-.85665,-1.0654,5,5,5,5,-.0602,.0597), nrow=2, ncol=18)
matplot(Centro, type="b", lty=1, lwd=3, pch=21, col=c("Blue","Red","Purple"),
        cex=1, ylim=c(-1.0,1.0), xlim=c(0.75,2.25),
        xaxp=c(1,2,1), las=1, labels=F)

axis(1,at=c(1,2),labels=c("Pocos círculos","Muchos círculos"),las=1)
axis(2,at=c(-1.0,-0.5,0,0.5,1.0),labels=c("-1.0","-0.5","0","0.5","1.0"),las=1)

text(1,1,paste("Fácil a Difícil"),cex=1.2,col='Blue',f=2)
text(1.5,1,paste("Difícil a Fácil"),cex=1.2,col='Red',f=2)
text(2,1,paste("Simultáneo"),cex=1.2,col='Purple',f=2)

#C Prueba 3 grupos

rm(list=ls())
Centro<-matrix(data=c(.773850,.494050,-.190100,.565750,.077,-.0367,.228000,.422700,.200550,.650850,.2092,-.0471,1.473750,-.204300,.502450,.805850,-.02095,.1513,.630135,.121981,.906517,.138798,-.1967,.0308,3,3,3,3,-2.02225,-.96135,3,3,3,3,-.1224,.1292), nrow=2, ncol=18)
matplot(Centro, type="b", lty=1, lwd=3, pch=21, col=c("Blue","Red","Purple"),
        cex=1, ylim=c(-2.0,2.0), xlim=c(0.75,2.25),
        xaxp=c(1,2,1), las=1, labels=F)

axis(1,at=c(1,2),labels=c("Pocos círculos","Muchos círculos"),las=1)
axis(2,at=c(-2.0,-1.5,-1.0,-0.5,0,0.5,1.0,1.5,2.0),labels=c("-2.0","-1.5","-1.0","-0.5","0","0.5","1.0","1.5","2.0"),las=1)

text(1,1.8,paste("Fácil a Difícil"),cex=1.2,col='Blue',f=2)
text(1.5,1.8,paste("Difícil a Fácil"),cex=1.2,col='Red',f=2)
text(2,1.8,paste("Simultáneo"),cex=1.2,col='Purple',f=2)

#C Cambios en C

rm(list=ls())
Centro<-matrix(data=c(.24855,.077,.1008,-.0367,-.12505,.2092,-.04145,-.0471,-.29295,-.02095,.16025,.1513,-.6513,-.1967,-.1623,.0308,-.85665,-2.02225,-1.0654,-.96135,-.0602,-.1224,.0597,.1292), nrow=2, ncol=28)
matplot(Centro, type="b", lty=1, lwd=3, pch=21, col=c("Blue","Red"),
        cex=1, ylim=c(-2,2), xlim=c(0.75,2.25),
        xaxp=c(1,2,1), las=1, labels=F)

axis(1,at=c(1,2),labels=c("Entrenamiento","Prueba"),las=1)
axis(2,at=c(-2.0,-1.5,-1.0,-0.5,0,0.5,1.0,1.5,2.0),labels=c("-2.0","-1.5","-1.0","-0.5","0","0.5","1.0","1.5","2.0"),las=1)

text(1,2,paste("Fácil"),cex=1.2,col='Blue',f=2)
text(1,1.7,paste("Difícil"),cex=1.2,col='Red',f=2)

# C Cambios Promedio


rm(list=ls())
Centro<-matrix(data=c(1.349789,1.820059,1.080854,1.449058), nrow=2, ncol=2)
matplot(Centro, type="b", lty=1, lwd=3, pch=21, col=c("Blue","Red"),
        cex=1, ylim=c(-2,2), xlim=c(0.75,2.25),
        xaxp=c(1,2,1), las=1, labels=F)

axis(1,at=c(1,2),labels=c("Entrenamiento","Prueba"),las=1)
axis(2,at=c(-2.0,-1.5,-1.0,-0.5,0,0.5,1.0,1.5,2.0),labels=c("-2.0","-1.5","-1.0","-0.5","0","0.5","1.0","1.5","2.0"),las=1)

text(2,-.5,paste("Fácil"),cex=1.2,col='Blue',f=2)
text(2,-.8,paste("Difícil"),cex=1.2,col='Red',f=2)