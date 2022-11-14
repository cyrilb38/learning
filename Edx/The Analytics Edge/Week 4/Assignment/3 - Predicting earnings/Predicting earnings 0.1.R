
census <- read.csv("census.csv")

library(caTools)

set.seed(2000)
split <- sample.split(census$over50k,SplitRatio = 0.6)
train <- census[split==TRUE,]
test <- census[split==FALSE,]

logModel <- glm(over50k ~ ., data = train, family = "binomial")
summary(logModel)

pred50k <- predict(logModel,test,type = "response")
t <- prop.table(table(test$over50k,pred50k >= 0.5))
t[1,1]+t[2,2]

#Baseline model
table(test$over50k)
9713/(9713+3078)

#calculate the AUC
library(ROCR)
ROCRpredTest = prediction(pred50k, test$over50k)
auc = as.numeric(performance(ROCRpredTest, "auc")@y.values)
auc

#Trees
library(rpart)
library(rpart.plot)

treeModel <- rpart(over50k ~ ., data = train, method = "class")
prp(treeModel)

#classification predictions
pred50k2 <- predict(treeModel,test, type = "class")
t2 <- prop.table(table(test$over50k,pred50k2))
t2[1,1]+t2[2,2]

#probabilities predictions
pred50k2 <- predict(treeModel,test)[,2]
ROCRpredTest = prediction(pred50k2, test$over50k)
auc2 = as.numeric(performance(ROCRpredTest, "auc")@y.values)
auc

#ROC Curve

# Prediction function
ROCRpred = prediction(pred50k, test$over50k)
# Performance function
ROCRperf = performance(ROCRpred, "tpr", "fpr")

ROCRpred2 = prediction(pred50k2, test$over50k)
ROCRperf2 = performance(ROCRpred2, "tpr", "fpr")

plot(ROCRperf)
plot(ROCRperf2)
# Add colors
plot(ROCRperf, colorize=TRUE)

# Add threshold labels 
plot(ROCRperf, colorize=TRUE, print.cutoffs.at=seq(0,1,by=0.1), text.adj=c(-0.2,1.7))

#calculate the AUC
ROCRpredTest = prediction(pred50k2, test$over50k)
auc = as.numeric(performance(ROCRpredTest, "auc")@y.values)
auc


#Random forest
set.seed(1)
trainSmall = train[sample(nrow(train), 2000), ]

set.seed(1)
library(randomForest)
forestModel <- randomForest(over50k ~ ., data = trainSmall, method = "class")
pred50k3 <- predict(forestModel,test)
t3 <- prop.table(table(test$over50k,pred50k3))
t3[1,1]+t3[2,2]

#explore the most significant variables
vu = varUsed(forestModel, count=TRUE)
vusorted = sort(vu, decreasing = FALSE, index.return = TRUE)
dotchart(vusorted$x, names(forestModel$forest$xlevels[vusorted$ix]))

varImpPlot(forestModel)
