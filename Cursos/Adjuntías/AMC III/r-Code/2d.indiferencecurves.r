
T=1000

x= 0:T
y= T-x

#restricciones temporales generales
plot(x,y, type="l", col=3)

T=500
x=0:T
y=T-x
lines(x,y, type="l", col="green4")

T=1000
x=0:T
y=T-x

#funciones de utilidad

alpha=.5
beta=.5

plot(x,x^alpha, type="l", col="blue3")
lines(x,x^beta, col="blue2")

#curva de indiferencia
k1=37 #jugar con el parámetro hasta llegar a 34
y2=(k1-x^alpha)^(1/beta)#checar despeje

plot(x,y, type="l", col=3)
lines(x,y2, col="blue")

#metodos numéricos

valor<- function(x){
  -(x^alpha+(T-x)^beta) # revisar parametro T
}

valor(990)

optimize( f=valor, lower=0,upper=T, maximum=F)
optim(par=500, fn=valor)

plot(0:T,valor(0:T),type="l" )
plot(0:T,-valor(0:T),type="l" )

#sustituimos el resultado
v1= 44.72136
y2=(v1-x^alpha)^(1/beta)#checar despeje
plot(x,y, type="l", col=3)
lines(x,y2, col="blue")
points(500,T-500, col=2)

