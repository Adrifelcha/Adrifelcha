# Validez bajo CTT
#
#######################################
setwd("D:/afchavez/Desktop/Adrifelcha_Lab25/Learning R/Codigo Aplicado")
set.seed(1)

library(hemp)
data("interest")

#### Content Validity Ratio (Validity according to Experts)
cvr(N =20, n_e=17)

#### Criterion-Related Validity
cor(interest[,c("vocab", "reading", "sentcomp")])