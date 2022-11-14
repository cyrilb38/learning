library(maps)
library(ggplot2)
library(ggmap)
library(dplyr)

setwd("E:/Travail - Ressources/Edx/The Analytics Edge/Week 7/1 - Election forecast revisited")

statesMap = map_data("state")

table(statesMap$group)

ggplot(statesMap, aes(x = long, y = lat, group = group)) + geom_polygon(fill = "white", color = "black") 

polling <-read.csv("PollingImputed.csv")

Train <- filter(polling, Year <= 2008)
Test <- filter(polling, Year >= 2012)

#Creating a logistic regression
mod2 = glm(Republican~SurveyUSA+DiffCount, data=Train, family="binomial")
TestPrediction = predict(mod2, newdata=Test, type="response")
TestPredictionBinary = as.numeric(TestPrediction > 0.5)

predictionDataFrame = data.frame(TestPrediction, TestPredictionBinary, Test$State)

sum(predictionDataFrame$TestPredictionBinary==1)
mean(predictionDataFrame$TestPrediction)

#plotting it on the 
predictionDataFrame$region = tolower(predictionDataFrame$Test.State)
predictionMap = merge(statesMap, predictionDataFrame, by = "region")
predictionMap = predictionMap[order(predictionMap$order),]

ggplot(predictionMap, aes(x = long, y = lat, group = group, fill = TestPredictionBinary)) + geom_polygon(color = "black")

predictionMap[predictionMap$region == "florida",]

?geom_polygon
