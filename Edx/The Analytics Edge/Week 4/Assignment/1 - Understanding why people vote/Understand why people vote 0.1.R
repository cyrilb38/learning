library(dplyr)

setwd("C:/Users/cbenhafed/Desktop/Documents/- Personnel/Formation/R/Edx/The Analytics Edge/Week 4/Assignment/1 - Understanding why people vote")

gerber <- read.csv("gerber.csv")

sum(gerber$voting==1)/nrow(gerber)

#proportion of voter
with(gerber[gerber$civicduty==1,],mean(voting==1))
with(gerber[gerber$hawthorne==1,],mean(voting==1))
with(gerber[gerber$self==1,],mean(voting==1))
with(gerber[gerber$neighbors==1,],mean(voting==1))
with(gerber[gerber$control==1,],mean(voting==1))

#logistic regression
model <- glm(voting ~ ., data = select(gerber, -c(sex,yob,control)), family = "binomial")
summary(model)

#predictions based on the model
predVotes <- predict(model,type="response")
t <- table(gerber$voting,predVotes >=0.3)
prop.table(t)[1,1]+prop.table(t)[2,2]

t <- table(gerber$voting,predVotes >=0.5)
prop.table(t)[1,1]

prop.table(table(gerber$voting))

#calculate the AUC
library(ROCR)
ROCRpredTest = prediction(predVotes, gerber$voting)
auc = as.numeric(performance(ROCRpredTest, "auc")@y.values)
auc

#create a tree model (CART)
library(rpart)
library(rpart.plot)
CARTmodel = rpart(voting ~ civicduty + hawthorne + self + neighbors, data=gerber)
prp(CARTmodel)

CARTmodel2 = rpart(voting ~ civicduty + hawthorne + self + neighbors, data=gerber, cp=0.0)
prp(CARTmodel2)

CARTmodel3 = rpart(voting ~ civicduty + hawthorne + self + neighbors + sex, data=gerber, cp=0.0)
prp(CARTmodel3)

CARTmodel4 <- rpart(voting ~ control, data = gerber, cp = 0.0)
prp(CARTmodel4, digits = 6)
0.34-0.296638

CARTmodel5 <- rpart(voting ~ control + sex, data = gerber, cp = 0.0)
prp(CARTmodel5, digits = 6)
0.345818-0.302795
0.334176-0.290456

model2 <- glm(voting ~ sex + control, data = gerber, family = "binomial")
summary(model2)

Possibilities = data.frame(sex=c(0,0,1,1),control=c(0,1,0,1))
predict(model2, newdata=Possibilities, type="response")
abs(0.2908065-0.290456)

LogModel2 = glm(voting ~ sex + control + sex:control, data=gerber, family="binomial")
summary(LogModel2)

predict(LogModel2, newdata=Possibilities, type="response")
abs(0.2904558-0.290456)
