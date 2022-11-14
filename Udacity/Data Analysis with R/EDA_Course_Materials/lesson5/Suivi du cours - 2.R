setwd("~/Travail - Ressources/Udacity/Data Analysis with R/EDA_Course_Materials/lesson5")
yo <- read.csv("yogurt.csv")
library(ggplot2)

yo$id <- factor(yo$id)
ggplot(data=yo,aes(x = price))+geom_histogram()

yo<- transform(yo,all.purchases = strawberry+blueberry+pina.colada+plain+mixed.berry)

ggplot(data=yo,aes(x=time,y=price))+geom_point(alpha=1/10,color = "blue")+geom_smooth()

set.seed(50)
sample.id <- sample(yo$id,16,replace = F)

ggplot(data=yo[yo$id%in%sample.id,],aes(x=time,y=price))+geom_point(aes(size=all.purchases),pch=1)+
  facet_wrap(~id)+geom_smooth()
