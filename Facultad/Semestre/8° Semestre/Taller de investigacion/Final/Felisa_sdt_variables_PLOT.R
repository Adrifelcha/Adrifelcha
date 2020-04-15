rm(list=ls())
# Directorio que contiene el archivo 'sdt_variables.csv':
setwd("~/Documents/Luis/Research Projects/CowLogFelisa/Ebbinghaus_Illusion")
sdt_data <- read.csv('sdt_variables.csv')

variables <- c('h_rate','fa_rate','d','B','C','K')
y_limits <- matrix(c(0.5,1,
                     0,0.6,
                     -4,10,
                     0,15,
                     -1,1,
                     -1.5,5),
                   ncol=2,byrow=T)

pdf(file='sdt_variables.pdf',width=11,height=8)
for(variable in variables){
  var_name_training <- paste(variable,'_training',sep='')
  var_name_test <- paste(variable,'_test',sep='')
  training_column <- which(names(sdt_data)==var_name_training)
  test_column <- which(names(sdt_data)==var_name_test)
  ylimits <- y_limits[which(variables==variable),]
  
  layout(matrix(1:4,byrow=T,ncol=2))
  par(omi=c(0,.75,1,0),
      mai=c(0.65,0.2,0.15,0.2))
  plot_counter <- 0
  for(c_bias in c('conservador','liberal')){
    for(c_diff in c('dificil','facil')){
      local_data <- subset(sdt_data,cond_bias==c_bias&cond_difficulty==c_diff)
      plot(0,type='n',ylab='',xlab='',
           axes=F,
           ylim=ylimits,xlim=c(0,3))
      boxplot(local_data[,c(training_column,test_column)],
              border='gray60',lty='solid',staplelty='blank',
              axes=F,add=T,boxwex=.15)
      for(r in 1:nrow(local_data)){
        lines(c(1,2),local_data[r,c(training_column,test_column)],
              type='o',pch=16)
        text(.6,local_data[r,training_column],local_data$participant[r],adj=.5,col='gray70',cex=.6)
        text(2.4,local_data[r,test_column],local_data$participant[r],adj=.5,col='gray70',cex=.6)
      }
      axis(2,pos=0,las=1)
      axis(1,at=c(1,2),labels=c('entrenamiento','prueba'))
      plot_counter <- plot_counter+1
      if(plot_counter==1){
        mtext('conservador',2,line=2.5,cex=2)
        mtext('dificil',3,line=1,cex=2)
      }
      else if(plot_counter==2){
        mtext('facil',3,line=1,cex=2)
      }
      else if(plot_counter==3){
        mtext('liberal',2,line=2.5,cex=2)
      }
    }
  }
  mtext(variable,3,outer=T,line=3,cex=2,font=2)
}
dev.off()
