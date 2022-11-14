setwd("E:/Travail - Ressources/Coursera/Data Science Specialization/3 - Getting and Cleaning Data/Week 3/Assignment")

doc <- read.csv("getdata_data_ss06hid.csv")
which(doc$ACR == 3 & doc$AGS == 6)

library(jpeg)
pic <- readJPEG(source = "getdata_jeff.jpg", native = TRUE)
quantile(pic,probs = c(0.3,0.8))


db <- read.csv("getdata_data_GDP.csv",skip = 3)
db2 <- read.csv("getdata_data_EDSTATS_Country.csv")

library(dplyr)

db_m <- inner_join(db,db2,by = c("X" = "CountryCode"))
head(arrange(db_m,desc(Ranking)),13)
mutate(db_m, rank = as.numeric(Ranking))
db_m %>%
  mutate(rank = as.numeric(Ranking)) %>%
  group_by(Income.Group) %>%
  summarize(mean(rank,na.rm = TRUE))