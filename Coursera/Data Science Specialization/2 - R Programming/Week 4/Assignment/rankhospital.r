setwd("E:/Travail - Ressources/Coursera/Data Science Specialization/2 - R Programming/Week 4/Assignment")

df <- read.csv(file = "hospital-data.csv",na.strings="Not Available",stringsAsFactors=FALSE)
outcome <- read.csv("outcome-of-care-measures.csv",
                    na.strings="Not Available",stringsAsFactors=FALSE)

outcome[,11] <- as.numeric(outcome[,11])
hist(outcome[,11])

rankhospital <- function(state,truc,num = "best") {
  if (truc == "heart attack") {
    case <- "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack"
  }
  else if (truc == "pneumonia") {
    case <- "Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia"
  }
  else {
    case <- "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure"
  }
  
  outcome <- outcome[,c("Hospital.Name","State",case)]
  names(outcome) <- c("Hospital.Name","State","value")
  outcome <- outcome[complete.cases(outcome),]
  outcome <- outcome[outcome$State == state,]
  outcome <- outcome[order(outcome$value,outcome$Hospital.Name),]
  
  if (num == "best"){
    num <- 1
  }
  else if (num == "worst"){
    num <- nrow(outcome)
  }
  
  outcome[num,"Hospital.Name"]
  
}

rankhospital("TX","heart failure",4)
rankhospital("MD","heart attack","worst")
rankhospital("MD","heart attack",5000)

