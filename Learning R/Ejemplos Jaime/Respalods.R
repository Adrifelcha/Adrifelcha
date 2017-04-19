
#### Gráficas Heu1 ####
matplot(He1_1[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición Heu1 \n Sesión 1", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(He1_1[i,j] > 0){
      points(i,He1_1[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(He1_1[1:4,k+3])
}
text(2,80,col=1,paste("Con Consejo =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Sin Consejo A =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Sin Consejo B =  ", WN[3]),cex=0.9)

matplot(He1_2[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición Heu1 \n Sesión 2", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(He1_2[i,j] > 0){
      points(i,He1_2[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(He1_2[1:4,k+3])
}
text(2,80,col=1,paste("Con Consejo =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Sin Consejo A =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Sin Consejo B =  ", WN[3]),cex=0.9)

matplot(He1_3[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición Heu1 \n Sesión 3", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(He1_3[i,j] > 0){
      points(i,He1_3[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(He1_3[1:4,k+3])
}
text(2,80,col=1,paste("Con Consejo =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Sin Consejo A =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Sin Consejo B =  ", WN[3]),cex=0.9)

#### Gráficas HeuTodos ####
matplot(HeT_1[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición HeuTodos \n Sesión 1", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(HeT_1[i,j] > 0){
      points(i,HeT_1[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(HeT_1[1:4,k+3])
}
text(2,80,col=1,paste("Jugador A =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Jugador B =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Jugador C =  ", WN[3]),cex=0.9)

matplot(HeT_2[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición HeuTodos \n Sesión 2", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(HeT_2[i,j] > 0){
      points(i,HeT_2[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(HeT_2[1:4,k+3])
}
text(2,80,col=1,paste("Jugador A =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Jugador B =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Jugador C =  ", WN[3]),cex=0.9)

matplot(HeT_3[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición HeuTodos \n Sesión 3", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(HeT_3[i,j] > 0){
      points(i,HeT_3[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(HeT_3[1:4,k+3])
}
text(2,80,col=1,paste("Jugador A =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Jugador B =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Jugador C =  ", WN[3]),cex=0.9)

matplot(HeT_4[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición HeuTodos \n Sesión 4", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(HeT_4[i,j] > 0){
      points(i,HeT_4[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(HeT_4[1:4,k+3])
}
text(2,80,col=1,paste("Jugador A =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Jugador B =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Jugador C =  ", WN[3]),cex=0.9)

#### Gráficas Est1 ####
matplot(Es1_1[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición Est1 \n Sesión 1", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(Es1_1[i,j] > 0){
      points(i,Es1_1[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(Es1_1[1:4,k+3])
}
text(2,80,col=1,paste("Con Consejo =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Sin Consejo A =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Sin Consejo B =  ", WN[3]),cex=0.9)

matplot(Es1_2[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición Est1 \n Sesión 2", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(Es1_2[i,j] > 0){
      points(i,Es1_2[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(Es1_2[1:4,k+3])
}
text(2,80,col=1,paste("Con Consejo =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Sin Consejo A =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Sin Consejo B =  ", WN[3]),cex=0.9)

matplot(Es1_3[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición Est1 \n Sesión 3", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(Es1_3[i,j] > 0){
      points(i,Es1_3[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(Es1_3[1:4,k+3])
}
text(2,80,col=1,paste("Con Consejo =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Sin Consejo A =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Sin Consejo B =  ", WN[3]),cex=0.9)

#### Gráficas EstTodos ####
matplot(EsT_1[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición EstTodos \n Sesión 1", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(EsT_1[i,j] > 0){
      points(i,EsT_1[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(EsT_1[1:4,k+3])
}
text(2,80,col=1,paste("Jugador A =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Jugador B =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Jugador C =  ", WN[3]),cex=0.9)

matplot(EsT_2[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición EstTodos \n Sesión 2", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(EsT_2[i,j] > 0){
      points(i,EsT_2[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(EsT_2[1:4,k+3])
}
text(2,80,col=1,paste("Jugador A =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Jugador B =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Jugador C =  ", WN[3]),cex=0.9)

matplot(EsT_3[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición EstTodos \n Sesión 3", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(EsT_3[i,j] > 0){
      points(i,EsT_3[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(EsT_3[1:4,k+3])
}
text(2,80,col=1,paste("Jugador A =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Jugador B =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Jugador C =  ", WN[3]),cex=0.9)

#### Gráficas Exp1 ####
matplot(Ex1_1[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición Exp1 \n Sesión 1", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(Ex1_1[i,j] > 0){
      points(i,Ex1_1[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(Ex1_1[1:4,k+3])
}
text(2,80,col=1,paste("Con Experiencia =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Sin Experiencia A =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Sin Experiencia B =  ", WN[3]),cex=0.9)

matplot(Ex1_2[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición Exp1 \n Sesión 2", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(Ex1_2[i,j] > 0){
      points(i,Ex1_2[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(Ex1_2[1:4,k+3])
}
text(2,80,col=1,paste("Con Experiencia =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Sin Experiencia A =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Sin Experiencia B =  ", WN[3]),cex=0.9)

matplot(Ex1_3[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición Exp1 \n Sesión 3", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(Ex1_3[i,j] > 0){
      points(i,Ex1_3[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(Ex1_3[1:4,k+3])
}
text(2,80,col=1,paste("Con Experiencia =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Sin Experiencia A =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Sin Experiencia B =  ", WN[3]),cex=0.9)

#### Gráficas ExpTodos ####
matplot(ExT_1[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición ExpTodos \n Sesión 1", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(ExT_1[i,j] > 0){
      points(i,ExT_1[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(ExT_1[1:4,k+3])
}
text(2,80,col=1,paste("Con Experiencia =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Sin Experiencia A =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Sin Experiencia B =  ", WN[3]),cex=0.9)

matplot(ExT_2[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición ExpTodos \n Sesión 2", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(ExT_2[i,j] > 0){
      points(i,ExT_2[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(ExT_2[1:4,k+3])
}
text(2,80,col=1,paste("Con Experiencia =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Sin Experiencia A =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Sin Experiencia B =  ", WN[3]),cex=0.9)

matplot(ExT_3[1:3], type="b", pch=21, col=1:3, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Condición ExpTodos \n Sesión 3", cex.main=0.9)
for(i in 1:4){
  for(j in 4:6){
    if(ExT_3[i,j] > 0){
      points(i,ExT_3[i,j-3],col=j-3,pch=21, bg=j-3, cex=1.3)
    }
  }
}
WN <- c(0,0,0)
for(k in 1:3){
  WN[k]<-sum(ExT_3[1:4,k+3])
}
text(2,80,col=1,paste("Con Experiencia =  ", WN[1]),cex=0.9)
text(2,75,col=2,paste("Sin Experiencia A =  ", WN[2]),cex=0.9)
text(2,70,col=3,paste("Sin Experiencia B =  ", WN[3]),cex=0.9)

#### Primera Tirada (Media) ####
PTHeu1<-mean(c(He1_1[1,1],He1_2[1,1],He1_3[1,1]))
PTHeuT<-mean(c(HeT_1[1,1],HeT_2[1,1],HeT_3[1,1],HeT_1[1,2],HeT_2[1,2],HeT_3[1,2],HeT_1[1,3],HeT_2[1,3],HeT_3[1,3]))
PTHeu<-cbind(PTHeu1,PTHeuT)
PTEst1<-mean(c(Es1_1[1,1],Es1_2[1,1],Es1_3[1,1]))
PTEstT<-mean(c(EsT_1[1,1],EsT_2[1,1],EsT_3[1,1],EsT_1[1,2],EsT_2[1,2],EsT_3[1,2],EsT_1[1,3],EsT_2[1,3],EsT_3[1,3]))
PTEst<-cbind(PTEst1,PTEstT)
PTExp1<-mean(c(Ex1_1[1,1],Ex1_2[1,1],Ex1_3[1,1]))
PTExpT<-mean(c(ExT_1[1,1],ExT_2[1,1],ExT_3[1,1],ExT_1[1,2],ExT_2[1,2],ExT_3[1,2],ExT_1[1,3],ExT_2[1,3],ExT_3[1,3]))
PTExp<-cbind(PTExp1,PTExpT)

PTPlot<-matrix(data=NA,nrow=3,ncol=2)
PTPlot<-rbind(PTHeu, PTEst, PTExp)

Tipos<-c("Heu1","HeuT", "Est1","EstT","Exp1","ExpT")
barplot(t(PTPlot),names.arg=Tipos, beside=T, col=Colores,
        main="Primer Número Elegido \n Por Jugadores Con Consejo / Experiencia",
        xlab="Condición", ylab="Número Elegido", ylim=c(0,30))
lines(c(10,0),c(0,0))

#### Gráficas Comparativas (Media) ####
for(x in 1:4){He1_T[x,1]<-mean(c(He1_1[x,1],He1_2[x,1],He1_3[x,1]))}
for(a in 1:4){for(b in 1:3){HeT_Tx[a,b]<-mean(c(HeT_1[a,b],HeT_2[a,b],HeT_3[a,b],HeT_4[a,b]))}}
for(xx in 1:4){HeT_T[xx,1]<-mean(c(HeT_Tx[xx,1],HeT_Tx[xx,1],HeT_Tx[xx,1]))}
for(y in 1:4){Es1_T[y,1]<-mean(c(Es1_1[y,1],Es1_2[y,1],Es1_3[y,1]))}
for(c in 1:4){for(d in 1:3){EsT_Tx[c,d]<-mean(c(EsT_1[c,d],EsT_2[c,d],EsT_3[c,d]))}}
for(yy in 1:4){EsT_T[yy,1]<-mean(c(EsT_Tx[yy,1],EsT_Tx[yy,2],EsT_Tx[yy,3]))}
for(z in 1:4){Ex1_T[z,1]<-mean(c(Ex1_1[z,1],Ex1_2[z,1],Ex1_3[z,1]))}
for(e in 1:4){for(f in 1:3){ExT_Tx[e,f]<-mean(c(ExT_1[e,f],ExT_2[e,f],ExT_3[e,f]))}}
for(zz in 1:4){ExT_T[zz,1]<-mean(c(ExT_Tx[zz,1],ExT_Tx[zz,2],ExT_Tx[zz,3]))}
for(g in 1:4){for(h in 1:3){Sin_Tx[g,h]<-mean(c(Pr1_1[g,h],PrT_1[g,h],PrT_2[g,h],PrT_3[g,h]))}}
for(w in 1:4){Sin_T[w,1]<-mean(c(Sin_Tx[w,1],Sin_Tx[w,2],Sin_Tx[w,3]))}

Todos<-matrix(data=NA,nrow=4,ncol=7) 
Todos<-cbind(He1_T,HeT_T,Es1_T,EsT_T,Ex1_T,ExT_T,Sin_T)

matplot(Todos, type="b", pch=21, col=1:7, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Comparación de condiciones", cex.main=0.9)

text(2,90,labels="Uno Heurístico",col=1,cex=0.9)
text(2,85,labels="Todos Heurístico",col=2,cex=0.9)
text(2,80,labels="Uno Estratégico",col=3,cex=0.9)
text(2,75,labels="Todos Estratégico",col=4,cex=0.9)
text(2,70,labels="Uno Experiencia",col=5,cex=0.9)
text(2,65,labels="Todos Experiencia",col=6,cex=0.9)
text(2,60,labels="Sin Consejo/Experiencia",col=7,cex=0.9)

#### Gráficas Comparativas (Mediana) ####
for(x in 1:4){He1_T[x,1]<-median(c(He1_1[x,1],He1_2[x,1],He1_3[x,1]))}
for(a in 1:4){for(b in 1:3){HeT_Tx[a,b]<-median(c(HeT_1[a,b],HeT_2[a,b],HeT_3[a,b],HeT_4[a,b]))}}
for(xx in 1:4){HeT_T[xx,1]<-median(c(HeT_Tx[xx,1],HeT_Tx[xx,1],HeT_Tx[xx,1]))}
for(y in 1:4){Es1_T[y,1]<-median(c(Es1_1[y,1],Es1_2[y,1],Es1_3[y,1]))}
for(c in 1:4){for(d in 1:3){EsT_Tx[c,d]<-median(c(EsT_1[c,d],EsT_2[c,d],EsT_3[c,d]))}}
for(yy in 1:4){EsT_T[yy,1]<-median(c(EsT_Tx[yy,1],EsT_Tx[yy,2],EsT_Tx[yy,3]))}
for(z in 1:4){Ex1_T[z,1]<-median(c(Ex1_1[z,1],Ex1_2[z,1],Ex1_3[z,1]))}
for(e in 1:4){for(f in 1:3){ExT_Tx[e,f]<-median(c(ExT_1[e,f],ExT_2[e,f],ExT_3[e,f]))}}
for(zz in 1:4){ExT_T[zz,1]<-median(c(ExT_Tx[zz,1],ExT_Tx[zz,2],ExT_Tx[zz,3]))}
for(g in 1:4){for(h in 1:3){Sin_Tx[g,h]<-median(c(Pr1_1[g,h],PrT_1[g,h],PrT_2[g,h],PrT_3[g,h]))}}
for(w in 1:4){Sin_T[w,1]<-median(c(Sin_Tx[w,1],Sin_Tx[w,2],Sin_Tx[w,3]))}

Todos<-matrix(data=NA,nrow=4,ncol=7) 
Todos<-cbind(He1_T,HeT_T,Es1_T,EsT_T,Ex1_T,ExT_T,Sin_T)

matplot(Todos, type="b", pch=21, col=1:7, cex=1, xlab="Periodo",
        ylab="Números Elegidos", ylim=c(0,100), xaxp=c(1, 4, 3),
        yaxp=c(0, 100, 10))
title(main="Comparación de condiciones", cex.main=0.9)

text(2,90,labels="Uno Heurístico",col=1,cex=0.9)
text(2,85,labels="Todos Heurístico",col=2,cex=0.9)
text(2,80,labels="Uno Estratégico",col=3,cex=0.9)
text(2,75,labels="Todos Estratégico",col=4,cex=0.9)
text(2,70,labels="Uno Experiencia",col=5,cex=0.9)
text(2,65,labels="Todos Experiencia",col=6,cex=0.9)
text(2,60,labels="Sin Consejo/Experiencia",col=7,cex=0.9)