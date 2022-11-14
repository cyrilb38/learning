setwd("E:/Travail - Ressources/Udacity/Intro to Datascience/Week 1/Titanic")
db <- read.csv("titanic_data.csv")

require("ggplot2")

str(db)

ggplot(data =db,aes(x=Survived))+geom_bar(aes(y = (..count..)/tapply(..count..,..PANEL..,sum)[..PANEL..]))+
  facet_grid(Sex~Pclass)

ggplot(data =db,aes(x=Survived))+geom_bar(aes(y = (..count..)/tapply(..count..,..PANEL..,sum)[..PANEL..]))+
  facet_grid(Sex ~ SibSp)

db$Age.Cat <- cut(db$Age,seq(0,max(db$Age,na.rm=T),5))


ggplot(data =db,aes(x=Survived))+geom_bar(aes(y = (..count..)/tapply(..count..,..PANEL..,sum)[..PANEL..]))+
  facet_grid(Sex ~ Age.Cat)