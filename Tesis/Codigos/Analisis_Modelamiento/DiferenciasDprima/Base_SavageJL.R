library('R2jags')

reA <- rnorm(100,mean=10,sd=1)
reB <- rnorm(100,mean=12,sd=1)
n_obs <- 100

data_jags <- list('n_obs','reA','reB')

write('
model{

mA_prior ~ dnorm(0,.001)
mB_prior ~ dnorm(0,.001)
delta_prior <- mB_prior-mA_prior

mA ~ dnorm(0,.001)
mB ~ dnorm(0,.001)
delta <- mB-mA

for(i in 1:n_obs){
reA[i]~dnorm(mA,1)
reB[i]~dnorm(mB,1)
}

}
      ','delta.bug')

param <- c('delta','mA','mB',
           'delta_prior','mA_prior','mB_prior')
js <- jags(data=data_jags,
     model.file = 'delta.bug',
     parameters.to.save = param,
     n.iter = 1000)

nds <- js$BUGSoutput$sims.list
layout(matrix(1:6,ncol=2))
hist(nds$mA)
hist(nds$mB)
hist(nds$delta)
hist(nds$mA_prior)
hist(nds$mB_prior)
hist(nds$delta_prior)

layout(1)
hist(nds$delta,breaks=100,col='#0000ee44',xlim = c(-4,4),freq=F)
hist(nds$delta_prior,breaks=100,add=T,col='#ee000044',freq=F)

