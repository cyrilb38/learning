setwd("E:/Travail - Ressources/Edx/The Analytics Edge/Assignment")

db <- read.csv("mvtweek1.csv")
max(db$ID)
min(db$Beat)
sum(db$Arrest == T)
