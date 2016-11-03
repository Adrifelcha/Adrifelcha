rm(list=ls())
#Teorema de bayes

#PROBLEMA
#Preparaste 50 tartas de vainilla y 50 tartas de fresa envenenadas para matar al rey.
#En el castillo ya habían 170 tartas de vainilla y 30 tartas de fresa hechas.

#Te cuelas en la cocina y revuelves las tartas Envenenadas con las No envenenadas.

#Un vasallo desconfiado saca una tarta aleatoria del montón revuelto y te pide que la comas. 
#La tarta es de vainilla. 
#¿Cuál es la probabilidad de que mueras al comerla?

#Definimos las conclusiones posibles entre las que se asigna la probabilidad
x <- 'La galleta está envenenada'
NOx <- 'La galleta NO está envenenada'

#Definimos las priors
prior_x <- 0.5 
prior_NOx <- 1-prior_x  #Debido a que las conclusiones son mutuamente excluyentes, la probabilidad de que ocurra una u otra debe sumar a 1
#Graficamos las priors
Priors <- c(prior_x,prior_NOx)

plot(Priors,type='o',pch=16,col='black',ylim=c(0,1),axes=F , ann=F)
axis(1,at=1:2,labels=c('Veneno','No veneno'))
axis(2,at=c(0, .1, .2, .3, .4, .5, .6,.7,.8,.9,1),labels=c("0",".1", ".2",".3",".4",".5",".6",".7",".8",".9","1"),las=1)
text(1,prior_x+.05,paste(prior_x),cex=.8,col='red',f=2)
text(2,prior_NOx+.05,paste(prior_NOx),cex=.8,col='red',f=2)
text(1.5,1,paste('Priors'),cex=1,col='red4',f=2)


#Definimos las verosimilitudes
verosimilitud_x <- 0.5
proporcion_vainilla_en_x <-
proporcion_vainilla_en_x
tartas_x

verosimilitud_NOx <- 0.85
proporcion_vainilla_en_NOx

plot(Priors,type='o',pch=16,col='black',ylim=c(0,1),axes=F , ann=F)
axis(1,at=1:2,labels=c('Vainilla','Fresa'))
axis(2,at=c(0, .1, .2, .3, .4, .5, .6,.7,.8,.9,1),labels=c("0",".1", ".2",".3",".4",".5",".6",".7",".8",".9","1"),las=1)
text(1,prior_x+.05,paste(prior_x),cex=.8,col='red',f=2)
text(2,prior_NOx+.05,paste(prior_NOx),cex=.8,col='red',f=2)
text(1.5,1,paste('Verosimilitud de X'),cex=1,col='red4',f=2)
text(1.5,0.95,paste('P(Tarta de vainilla|La tarta es de las envenenadas)'),cex=0.9,col='red4',f=2)


#Calculamos la verosimilitud marginal  
verosimilitud_marginal <- ((prior_x)*(verosimilitud_x))+((prior_NOx)*(verosimilitud_NOx))

#Definimos las posteriores  
Posterior_x <- (((prior_x)*(verosimilitud_x))/verosimilitud_marginal)
Posterior_NOx <- (((prior_NOx)*(verosimilitud_NOx))/verosimilitud_marginal)

#Posterior_x_<-paste("Probabilidad de", x, "=", Posterior_x)

print(paste("Probabilidad de que", x, "=", Posterior_x))
print(paste("Probabilidad de que", NOx, "=", Posterior_NOx))

