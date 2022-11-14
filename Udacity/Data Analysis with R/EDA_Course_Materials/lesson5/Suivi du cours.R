setwd("~/Travail - Ressources/Udacity/Data Analysis with R/EDA_Course_Materials/lesson3")

pf = read.delim("pseudo_facebook.tsv")

library(ggplot2)
library(dplyr)
age_gender = group_by(pf,age,gender)
pf.fc_by_age_gender = summarise(age_gender,mean_friend_count = mean(friend_count),median_friend_count=median(friend_count),n = n())

#code récupéré sur le site
pf.fc_by_age_gender<-NA
pf.fc_by_age_gender<- subset(pf,!is.na(gender)) %.%
  group_by(age, gender) %.%
  summarise (mean_friend_count = mean(friend_count),
             median_friend_count = median(friend_count),
             n = n()) %.%
  ungroup() %.%
  arrange(age, gender)

library(reshape2)
pf.fc_by_age_gender.wide = dcast(pf.fc_by_age_gender,
                                 age ~ gender,
                                 value.var = "median_friend_count")

ggplot(data=pf.fc_by_age_gender.wide,aes(x=age,y=female/male))+geom_line(color = "blue")+geom_hline(yintercept = 1,linetype=2)

pf$year_joined = floor(2014 - pf$tenure/365) 


pf$year_joined.bucket <- cut(pf$year_joined,breaks = c(2004,2009,2011,2012,2014))

ggplot(data = subset(pf,!is.na(pf$year_joined.bucket)),aes(x=age,y=friend_count))+geom_line(aes(color=year_joined.bucket),stat = "summary",fun.y = median)

ggplot(data = subset(pf,!is.na(pf$year_joined.bucket)),aes(x=age,y=friend_count))+geom_line(aes(color=year_joined.bucket),stat = "summary",fun.y = median)+
  geom_line(stat="summary",fun.y = mean,linetype = 2)

friend_rate <- with(pf[pf$tenure>0 & !is.na(pf$friend_count),],friend_count / tenure)
summary(friend_rate)

ggplot(data = pf[pf$tenure >0,], aes(x =tenure,y=friendships_initiated/tenure))+geom_line(aes(color = year_joined.bucket),stat = "summary",fun.y = mean)

ggplot(data = pf[pf$tenure >0,], aes(x =tenure,y=friendships_initiated/tenure))+geom_smooth(aes(color = year_joined.bucket),stat = "summary",fun.y = mean)
