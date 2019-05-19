
####restricciones temporales####

T=1000
t=0:T
C=matrix(,nrow=T+1, ncol=T+1)

for(i in 1:T+1){
  C[1,1:1]=t[1:1]#por alguna razon no corre el primer valor
  C[i,1:i]=t[i:1]
}
#C= t(C)
rotate <- function(x) t(apply(x, 2, rev))
C=(rotate(C))#solo para ue quede el origen donde debe

I=0:T
N=0:T

library(rgl)
persp3d(I, N, C, col=3)

####agregamos otra restriccion temporal general####
T= 600
t=0:T
C2 =matrix(,nrow=T+1, ncol=T+1)

for(i in 1:T+1){
  C2[1,1:1]=t[1:1]
  C2[i,1:i]=t[i:1]
}
C2= t(C2)
C2


I=0:T
N=0:T

triangles3d(c(500,0,0), c(0,500,0) , c(0,0,500), col="green4")

#agregamos una restriccion (contingencia) entre I y C de razon
T=1000 #restricción general
#RF1
quads3d(c(0,0,T,T),c(0,T,T,0),c(0,0,T/2,T/2), col="red")
#RF3
quads3d(c(0,0,T,T),c(0,T,T,0),c(0,0,T/3,T/3), col="red4")
