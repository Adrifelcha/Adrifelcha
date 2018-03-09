library(ggplot2)

# Fake data (two normal distributions)
set.seed(20)
dat_a = rnorm(1000, 100, 10)
dat_b = rnorm(2000, 120, 20)
dat1 = data.frame(x=dat_a, group="A")
dat2 = data.frame(x=dat_b, group="B")
dat = rbind(dat1, dat2)

ggplot(dat, aes(x, fill=group, colour=group)) +
  geom_histogram(breaks=seq(0,200,5), alpha=0.8, 
                 position="identity", lwd=0.2) +
  ggtitle("Unormalized")

ggplot(dat, aes(x, fill=group, colour=group)) +
  geom_histogram(aes(y=..density..), breaks=seq(100,100.5,5), alpha=0.6, 
                 position="identity", lwd=0.2) +
  ggtitle("Normalized")