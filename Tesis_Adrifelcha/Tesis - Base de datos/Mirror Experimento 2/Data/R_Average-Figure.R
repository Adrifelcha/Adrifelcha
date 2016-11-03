setwd("C:/Users/Adrifelcha/Dropbox/Tesis/Experimentos")
rm(list=ls())
dir()

rm(list=ls())
pdf_name<-'Average_SDT-Mirror_Ex2a & Ex1_v2.pdf'
pdf(file=pdf_name, width=8, height=8)
layout(matrix(1:2,ncol=1))

#  Experimento1_V2

  FAr_an <- .2701
  Hr_as <- .85745
  FAr_bn <- .33665
  Hr_bs <- .68165
  C_AN <- 2.4853125
  C_BN <- 2.7578125
  C_BS <- 4.361875
  C_AS <- 5.20053125
  Confidence <- c(C_AN, C_BN, C_BS, C_AS)

  k <- qnorm(1-FAr_an,0,1)
  d_A <- qnorm(Hr_as,0,1)-qnorm(FAr_an,0,1)
  d_BN <- qnorm(FAr_bn,0,1)-qnorm(FAr_an,0,1)
  d_BS <- (qnorm(Hr_bs,0,1)-qnorm(FAr_bn,0,1))+d_BN
  c <- k-(d_A/2)                    
  #  beta_A <- dnorm(k_A,d_A,1)/dnorm(k_A,0,1)
  #  beta_B <-dnorm(k_B,d_B,1)/dnorm(k_B,0,1)
  print(c(k[length(k)], 
          d_A[length(d_A)], 
          d_BN[length(d_BN)], 
          d_BS[length(d_BS)], 
          c[length(c)]))

  soporte <- seq(-3.5,6,.05)
  dis_AN <- dnorm(soporte,0,1)
  dis_AS <- dnorm(soporte,d_A,1)
  dis_BN <- dnorm(soporte,d_BN,1)
  dis_BS <- dnorm(soporte,d_BS,1)
  
  d_A<-round(d_A,3)
  d_BN<-round(d_BN,3)
  d_BS<-round(d_BS,3)
  k<-round(k,3)
  c<-round(c,3)
  #c_B<-round(c_B,3)
  #beta_A<-round(beta_A,3)
  #beta_B<-round(beta_B,3)
  Hr_as<-round(Hr_as,3)
  FAr_an<-round(FAr_an,3)
  Hr_bs<-round(Hr_bs,3)
  FAr_bn<-round(FAr_bn,3)
  
  plot(soporte,dis_AN,type='l', ylim=c(0,.5), lwd=2, lty=1, col='deepskyblue3', yaxt='n', ann=F)
  lines(soporte,dis_AS,type='l', lwd=2, col='deepskyblue2')
  lines(soporte,dis_BN,type='l', lwd=2, lty=1, col='darkorchid3')
  lines(soporte,dis_BS, type='l', lwd=2, col='darkorchid2')
  abline(v=k,col='black', lwd=2)
  #abline(v=k1,col='red', lty=6, lwd=2)
  text(k+1,0.45,paste("K = ",k))
  text(-2.5,.3,paste("Fa(AN) =",FAr_an),cex=1,col='royalblue4')
  text(-2.5,0.35,paste("FA(BN) =",FAr_bn),cex=1,col='darkorchid2')
  text(-2.5,.4,paste("H(BS) =", Hr_bs),cex=1,col='darkorchid3')
  text(-2.5,0.45,paste("H(AS) =", Hr_as),cex=1,col='royalblue4')
  #text(-2.5,0.35,paste("1"), col='red')
  #text(-3.4,0.15,paste("D' = ",d_B))
  #text(-3.4,0.39,paste("Hits = ",Hr_bs))
  #text(-3.4,0.34,paste("F.A = ",FAr_bn))
  mtext("Yes/No Procedure",3,cex=.8)
  
    plot(Confidence,type='o',pch=16,col='maroon2',ylim=c(1,6),axes=F , ann=F)
    axis(1,at=1:4,labels=c('R(AN)','R(BN)','R(BS)','R(AS)'))
    axis(2,at=c(0, 1, 2, 3, 4, 5, 6),labels=c("0","1", "2","3","4","5","6"),las=1)
    text(1.1,C_AN+.5,paste(C_AN),cex=1,col='violetred',f=2)
    text(1.9,C_BN+.5,paste(C_BN),cex=1,col='violetred',f=2)
    text(3.1,C_BS-.5,paste(C_BS),cex=1,col='violetred',f=2)
    text(3.9,C_BS-.5,paste(C_AS),cex=1,col='violetred',f=2)
    text(1.5,5.5,paste('Confidence Rate'),cex=1,col='violetred4',f=2)
    mtext("Confidence Rating - Means",3,cex=.8)
    title("Adriana F. Chávez, OPAM 2016: The Mirror Effect and Perception", outer = TRUE, line = -2)
    
    
    
#################### Experimento 2a
    
    FAr_an_2a <- .08031
    Hr_as_2a <- .919135
    FAr_bn_2a <- .14375
    Hr_bs_2a <- .8609825
    C_AN_2a <- 1.5657025
    C_BN_2a <- 1.8823575
    C_BS_2a <- 5.2124025
    C_AS_2a <- 5.4465225
    Confidence_2a <- c(C_AN_2a, C_BN_2a, C_BS_2a, C_AS_2a)
    
    k_2a <- qnorm(1-FAr_an_2a,0,1)
    d_A_2a <- qnorm(Hr_as_2a,0,1)-qnorm(FAr_an_2a,0,1)
    d_BN_2a <- qnorm(FAr_bn_2a,0,1)-qnorm(FAr_an_2a,0,1)
    d_BS_2a <- (qnorm(Hr_bs_2a,0,1)-qnorm(FAr_bn_2a,0,1))+d_BN_2a
    c_2a <- k_2a-(d_A_2a/2)                    
    #  beta_A <- dnorm(k_A,d_A,1)/dnorm(k_A,0,1)
    #  beta_B <-dnorm(k_B,d_B,1)/dnorm(k_B,0,1)
    print(c(k_2a[length(k_2a)], 
            d_A_2a[length(d_A_2a)], 
            d_BN_2a[length(d_BN_2a)], 
            d_BS_2a[length(d_BS_2a)], 
            c_2a[length(c_2a)]))
    
    soporte_2a <- seq(-3.5,6,.05)
    dis_AN <- dnorm(soporte,0,1)
    dis_AS_2a <- dnorm(soporte,d_A_2a,1)
    dis_BN_2a <- dnorm(soporte,d_BN_2a,1)
    dis_BS_2a <- dnorm(soporte,d_BS_2a,1)
    
    d_A_2a<-round(d_A_2a,3)
    d_BN_2a<-round(d_BN_2a,3)
    d_BS<-round(d_BS_2a,3)
    k_2a<-round(k_2a,3)
    c_2a<-round(c_2a,3)
    #c_B<-round(c_B,3)
    #beta_A<-round(beta_A,3)
    #beta_B<-round(beta_B,3)
    Hr_as_2a<-round(Hr_as_2a,3)
    FAr_an_2a<-round(FAr_an_2a,3)
    Hr_bs_2a<-round(Hr_bs_2a,3)
    FAr_bn_2a<-round(FAr_bn_2a,3)
    
    plot(soporte_2a,dis_AN,type='l', ylim=c(0,.5), lwd=2, lty=1, col='deepskyblue3', yaxt='n', ann=F)
    lines(soporte_2a,dis_AS_2a,type='l', lwd=2, col='deepskyblue2')
    lines(soporte_2a,dis_BN_2a,type='l', lwd=2, lty=1, col='darkorchid3')
    lines(soporte_2a,dis_BS_2a, type='l', lwd=2, col='darkorchid2')
    abline(v=k_2a,col='black', lwd=2)
    #abline(v=k1,col='red', lty=6, lwd=2)
    text(k_2a+1,0.45,paste("K = ",k_2a))
    text(-2.5,.3,paste("Fa(AN) =",FAr_an_2a),cex=1,col='royalblue4')
    text(-2.5,0.35,paste("FA(BN) =",FAr_bn_2a),cex=1,col='darkorchid2')
    text(-2.5,.4,paste("H(BS) =", Hr_bs_2a),cex=1,col='darkorchid3')
    text(-2.5,0.45,paste("H(AS) =", Hr_as_2a),cex=1,col='royalblue4')
    #text(-2.5,0.35,paste("1"), col='red')
    #text(-3.4,0.15,paste("D' = ",d_B))
    #text(-3.4,0.39,paste("Hits = ",Hr_bs))
    #text(-3.4,0.34,paste("F.A = ",FAr_bn))
    mtext("Yes/No Procedure",3,cex=1)
  
    
    plot(Confidence_2a,type='o',pch=16,col='maroon2',ylim=c(1,6),axes=F , ann=F)
    axis(1,at=1:4,labels=c('R(AN)','R(BN)','R(BS)','R(AS)'))
    axis(2,at=c(0, 1, 2, 3, 4, 5, 6),labels=c("0","1", "2","3","4","5","6"),las=1)
    text(1.1,C_AN_2a+.5,paste(C_AN_2a),cex=1,col='violetred',f=2)
    text(1.9,C_BN_2a+.5,paste(C_BN_2a),cex=1,col='violetred',f=2)
    text(3.1,C_BS_2a-.5,paste(C_BS_2a),cex=1,col='violetred',f=2)
    text(3.9,C_BS_2a-.5,paste(C_AS_2a),cex=1,col='violetred',f=2)
    text(1.5,5.5,paste('Confidence Rate'),cex=1,col='violetred4',f=2)
    mtext("Confidence Rating - Means",3,cex=.8)
    title("Adriana F. Chávez, OPAM 2016: The Mirror Effect and Perception", outer = TRUE, line = -2)

  dev.off()
  
  
