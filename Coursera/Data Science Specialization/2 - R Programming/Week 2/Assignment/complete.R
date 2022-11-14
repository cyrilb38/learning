setwd("E:/Travail - Ressources/Coursera/Data Science Specialization/2 - R Programming/Week 2/Assignment")

complete <- function (directory , id = 1:332) {
  accespath = paste(getwd(), directory,sep = "/" )
  
  ids = integer(length(id))
  nobs = integer(length(id))
  i = 1
  
  liste = list.files(path = accespath)
  for (file in liste) {
    if (as.numeric(substr(file,1,3)) %in% id) {
      filepath = paste(accespath, file,sep = "/" )
      db_t <- read.csv(filepath)
      
      ids[i] <- as.numeric(substr(file,1,3))
      nobs[i] <- sum(complete.cases(db_t))
      i = i + 1
      
    }
  }
  data.frame(ids,nobs )
}

complete("specdata", 1)

complete("specdata", c(2, 4, 8, 10, 12))

complete("specdata", 30:25)

complete("specdata", 3)

cc <- complete("specdata", c(6, 10, 20, 34, 100, 200, 310))
print(cc$nobs)

cc <- complete("specdata", 54)
print(cc$nobs)

set.seed(42)
cc <- complete("specdata", 332:1)
use <- sample(332, 10)
print(cc[use, "nobs"])