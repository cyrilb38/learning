setwd("E:/Travail - Ressources/Coursera/Data Science Specialization/2 - R Programming/Week 4/Assignment")

df <- read.csv(file = "hospital-data.csv",na.strings="Not Available",stringsAsFactors=FALSE)
outcome <- read.csv("outcome-of-care-measures.csv",
                    na.strings="Not Available",stringsAsFactors=FALSE)

outcome[,11] <- as.numeric(outcome[,11])
hist(outcome[,11])

best <- function(state,truc) {
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
  outcome <- outcome[outcome$value == min(outcome$value),]
  outcome[1,1]  
}

best("TX", "heart attack")
best("TX", "heart failure")
best("MD", "heart attack")
best("MD", "pneumonia")
