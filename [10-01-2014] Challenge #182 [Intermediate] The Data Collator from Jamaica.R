library(ggplot2)

data = read.table("challenge182.txt",sep=":",header = TRUE)

ggplot(aes(x=Voltage, y=Current),data=data) + 
  geom_point(size=5) + 
  geom_smooth(method="lm",size=1 ) + 
  xlim(c(0,5)) + 
  ylim(c(0,8))

