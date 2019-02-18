# Modelo de cr?dito parcial

library(mirt)
library(psych)

# Datos
res2 <- read.csv("res2.csv")

# Descriptivos
describe(res2)


# Modelo
model.pcm <- 'PCM = 1-4' 
results.pcm <- mirt(data=res2, model=model.pcm, itemtype="Rasch", SE=TRUE, verbose=FALSE)
coef.pcm <- coef(results.pcm, IRTpars=TRUE, simplify=TRUE)


# Par?metros de los ?tems
items.pcm <- as.data.frame(coef.pcm$items)
print(items.pcm)

# Plot de items
plot(results.pcm, type = 'trace', which.items = c(2, 3), 
     main = "", par.settings = simpleTheme(lty=1:4,lwd=2),
     auto.key=list(points=FALSE,lines=TRUE, columns=4))

# Funci?n de informaci?n del item
plot(results.pcm, type = 'infotrace', which.items = c(1, 3), 
     main = "", par.settings = simpleTheme(lwd=2))

# Funci?n de informaci?n del test
plot(results.pcm, type = 'info', theta_lim = c(-4,4), lwd=2)     

# Error est?ndar de medici?n
plot(results.pcm, type = 'SE', theta_lim = c(-4,4), lwd=2)    

# Par?metros de las personas
mod <- mirt(res2, 1, itemtype="Rasch")
thetas_PCM <- fscores(mod, method = "WLE")
head(thetas_PCM)
hist(thetas_PCM)
describe(thetas_PCM)
