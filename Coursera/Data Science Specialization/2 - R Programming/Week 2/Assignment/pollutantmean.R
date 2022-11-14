setwd("E:/Travail - Ressources/Coursera/Data Science Specialization/2 - R Programming/Week 2/Assignment")

pollutantmean <- function (directory , pollutant , id = 1:332) {
  db = data.frame()
  accespath = paste(getwd(), directory,sep = "/" )
  liste = list.files(path = accespath)
  for (file in liste) {
    if (as.numeric(substr(file,1,3)) %in% id) {
      filepath = paste(accespath, file,sep = "/" )
      db_t <- read.csv(filepath)
      db<- rbind(db,db_t)
    }
  }
  
  if (pollutant == "sulfate") {
    mean(db$sulfate, na.rm = T)
  } else {
    mean(db$nitrate, na.rm = T)
  }
  
}

pollutantmean("specdata", "sulfate", 1:10)

pollutantmean("specdata", "nitrate", 70:72)

pollutantmean("specdata", "nitrate", 23)

pollutantmean("specdata", "sulfate", 1:10)

pollutantmean("specdata", "nitrate", 70:72)

pollutantmean("specdata", "sulfate", 34)

pollutantmean("specdata", "nitrate")
