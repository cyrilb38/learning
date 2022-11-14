
letters <- read.csv("letters_ABPR.csv")

letters$isB = as.factor(letters$letter == "B")
set.seed(1000)
library(caTools)
split <- sample.split(letters$isB, SplitRatio = 0.5)
train <- letters[split == TRUE,]
test <- letters[split == FALSE,]

table(test$isB)
1175/(1175+383)

#Decision tree
library(rpart)
CARTb = rpart(isB ~ . - letter, data=train, method="class")
#make predictions based on model
pred <- predict(CARTb,test,type = "class")
t <- prop.table(table(test$isB,pred))
t[1,1] + t[2,2]

#random forest
library(randomForest)
fModel <- randomForest(isB ~ . - letter, data = train)
pred <- predict(fModel,test,type = "class")
t <- prop.table(table(test$isB,pred))
t[1,1] + t[2,2]

#multiclass classification
letters$letter = as.factor( letters$letter ) 
set.seed(2000)
split <- sample.split(letters$letter,SplitRatio = 0.5)
train <- letters[split == TRUE,]
test <- letters[split == FALSE,]
table(test$letter)
401/(nrow(test))

Cartl <- rpart(letter ~ . - isB, data = train, method = "class") # method class car c'est un pb de classification
pred <- predict(Cartl,test,type = "class")
t <- prop.table(table(test$letter,pred))
t[1,1] + t[2,2] + t[3,3] + t[4,4]

lModel <- randomForest(letter ~ . - isB, data = train)
pred <- predict(lModel,test,type = "class")
t <- prop.table(table(test$letter,pred))
t[1,1] + t[2,2] + t[3,3] + t[4,4]
t
