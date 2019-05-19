
alpha=.1
beta=.112
gamma=.189
valor=12
T=1000

x <- seq(0,T,length=100)
y <- x
f <- function(x,y) { (valor-(x^alpha+y^beta))^(1/gamma) }
z <- outer(x, y, f)
z[is.na(z)] <- 1

library(rgl)

open3d()
bg3d("white")
material3d(col="black")

persp3d(x, y, z, aspect=c(1, 1, 0.5), col = "blue",
        xlab = "I", ylab = "N", zlab = "C", zlim=c(0,T))

# otra curva de indiferencia
valor=9.5#probar este valor para las restricciones
prec=100
x <- seq(100,T,length=prec)
y=rep(x,each=prec)
x=rep(x,prec)
points3d(x,y,f(x,y), col="blue4")

#metodos numéricos

valor3<- function(x){
  I<- x[2]
  C<- x[1]
  if ((C+I)> T) return ("Fuera de los limites")
  -(C^alpha+(I)^beta+(T-C-I)^gamma) # revisar parametro T
}
x=c(500,400)
valor3(x)

optim(par=x, fn=valor3, method="L-BFGS-B", lower=c(0,0), upper=c(T,T))
resul= optim(par=x, fn=valor3, method="L-BFGS-B", lower=c(0,0), upper=c(T,T))

# sustitucion del resultado
valor= -resul$value #probar este valor para las restricciones

x <- seq(100,T,length=100) #ajustar limites para poder visualizar
y <- x
z <- outer(x, y, f)
z[is.na(z)] <- 1
surface3d(x,y,z, col="blue4")

points3d(resul$par[1], resul$par[2],(T-resul$par[1]-resul$par[2]),col="red")

