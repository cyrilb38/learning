#Cyril Benhafed - 2016/06/10

setwd("E:/Travail - Ressources/Edx/The Analytics Edge/Competition")
library(dplyr)



#Loading data
train = read.csv("train2016.csv")
test = read.csv("test2016.csv")

#Create a simple model to detect significant variable
SimpleMod = glm(Party ~ . -USER_ID, data=train, family=binomial)
summary(SimpleMod)

#Significant variables are stored in a vector called significantVariable :
significantCoefficients <- row.names(data.frame(summary(SimpleMod)$coef[summary(SimpleMod)$coef[,4] <= .05, 4]))[-1]
#To get names and coeff (from SO) :
#data.frame(summary(score)$coef[summary(score)$coef[,4] <= .05, 4])

#AS the names are not similar with dataframe variable for categorical data, we do a loop to recognize the variable name
for (i in significantCoefficients){
  coefToFound <- substring(i,1,nchar(i)-1)
  bFound <- FALSE
  j <- 1
  while (bFound == FALSE & j <= ncol(train)){
    
    
    coefToFound <- substring(i,1,nchar(i)-(j+1))  
  }
}

#We select only significant variable in the dataframe, and called the new dataframe signTrain
signTrain <- train[,significantVariable[21]]

str(significantVariable)
str(as.vector(significantVariable))
