setwd("E:/Travail - Ressources/Edx/The Analytics Edge/Week 6/Assignment/3 - Predicting stocks return")

stocks <- read.csv("StocksCluster.csv")

sum(stocks$PositiveDec==1)/nrow(stocks)

max(cor(stocks)[! cor(stocks) == 1])

library(dplyr)

stocks %>%
  summarise_each(funs(mean))

#creating sample tests and training
library(caTools)
set.seed(144)
spl = sample.split(stocks$PositiveDec, SplitRatio = 0.7)
stocksTrain = subset(stocks, spl == TRUE)
stocksTest = subset(stocks, spl == FALSE)

#creating a logistic regression
StocksModel <- glm(PositiveDec ~ ., data = stocksTrain, family = "binomial")
predTrain <- predict(StocksModel,stocksTrain, type = "response")
table(stocksTrain$PositiveDec,predTrain > 0.5)
(990+3640)/(990+2689+787+3640)

predTest <- predict(StocksModel,stocksTest, type = "response")
table(stocksTest$PositiveDec,predTest > 0.5)
(417+1553)/(417+1160+344+1553)

table(stocksTest$PositiveDec)
(1897)/(1897+1577)

#Clustering. First we remove the dependent variable
limitedTrain = stocksTrain
limitedTrain$PositiveDec = NULL
limitedTest = stocksTest
limitedTest$PositiveDec = NULL

#normalizing data
library(caret)
preproc = preProcess(limitedTrain)
normTrain = predict(preproc, limitedTrain)
normTest = predict(preproc, limitedTest)

summary(normTrain$ReturnJan)
summary(normTest$ReturnJan)

set.seed(144)
#???creating k means
km <- kmeans(normTrain,centers = 3)
km

library(flexclust)
km.kcca = as.kcca(km, normTrain)
clusterTrain = predict(km.kcca)
clusterTest = predict(km.kcca, newdata=normTest)

sum(clusterTest==2)

stocksTrain1 = stocksTrain[clusterTrain==1,]
stocksTrain2 = stocksTrain[clusterTrain==2,]
stocksTrain3 = stocksTrain[clusterTrain==3,]

stocksTest1 = stocksTest[clusterTest==1,]
stocksTest2 = stocksTest[clusterTest==2,]
stocksTest3 = stocksTest[clusterTest==3,]

mean(stocksTrain1$PositiveDec)
mean(stocksTrain2$PositiveDec)
mean(stocksTrain3$PositiveDec)

StocksModel1 <- glm(PositiveDec ~ ., data = stocksTrain1, family = "binomial")
StocksModel2 <- glm(PositiveDec ~ ., data = stocksTrain2, family = "binomial")
StocksModel3 <- glm(PositiveDec ~ ., data = stocksTrain3, family = "binomial")
summary(StocksModel1)
summary(StocksModel2)
summary(StocksModel3)

PredictTest1 <- predict(StocksModel1,stocksTest1, type = "response")
PredictTest2 <- predict(StocksModel2,stocksTest2, type = "response")
PredictTest3 <- predict(StocksModel3,stocksTest3, type = "response")

table(stocksTest1$PositiveDec,PredictTest1>0.5)
(30+774)/(30+471+23+774)
table(stocksTest2$PositiveDec,PredictTest2>0.5)
(388+757)/(388+626+309+757)
table(stocksTest3$PositiveDec,PredictTest3>0.5)
(49+13)/(49+13+21+13)

AllPredictions = c(PredictTest1, PredictTest2, PredictTest3)
AllOutcomes = c(stocksTest1$PositiveDec, stocksTest2$PositiveDec, stocksTest3$PositiveDec)
table(AllOutcomes,AllPredictions>0.5)
(467+1544)/(467+1110+353+1544)
