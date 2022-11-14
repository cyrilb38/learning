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


corr <- function (directory , threshold = 0) {
  
  df_completecases = complete(directory,1:332)
  
  df = df_completecases[df_completecases$nobs > threshold,]
  
  if (length(df[,1]) == 0){
    return(c())
  }
  
  df$cor <- 0
  
  for (i in 1:length(df[,1])) {
    
    accespath = paste(getwd(), directory,sep = "/" )
    
    file_number <- toString(df[i,1])  
    while (nchar(file_number) < 3){
      file_number <- paste("0",file_number,sep="")
    }
    
    file = paste(file_number,".csv",sep="")
    filepath = paste(accespath, file,sep = "/" )
    
    echantillon <- read.csv(filepath)
    echantillon <- echantillon[complete.cases(echantillon),]
    
    df[i,3] <- cor(echantillon$sulfate,echantillon$nitrate)

  }

  df$cor
  
}

summary(corr("specdata",150))

cr <- corr("specdata", 400)
head(cr)

cr <- corr("specdata", 5000)
summary(cr)

cr <- corr("specdata")
summary(cr)

cr <- corr("specdata")                
cr <- sort(cr)                
set.seed(868)                
out <- round(cr[sample(length(cr), 5)], 4)
print(out)

cr <- corr("specdata", 129)                
cr <- sort(cr)                
n <- length(cr)                
set.seed(197)                
out <- c(n, round(cr[sample(n, 5)], 4))
print(out)

cr <- corr("specdata", 2000)                
n <- length(cr)                
cr <- corr("specdata", 1000)                
cr <- sort(cr)
print(c(n, round(cr, 4)))