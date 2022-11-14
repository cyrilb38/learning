
setwd("E:/Travail - Ressources/Coursera/Data Science Specialization/3 - Getting and Cleaning Data/Week 4/Assignment")

download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv","UScom.csv")
df <- read.csv("UScom.csv")
strsplit(df,df$wgtp1)

download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FGDP.csv","gdp.csv")
df_gdp <- read.csv("gdp.csv",skip = 3,nrows = 200)
head(df_gdp)
df_gdp$US.dollars. <- as.numeric(gsub(",","",df_gdp$US.dollars.))
mean(df_gdp$US.dollars.,na.rm = TRUE)

grep("^United",df_gdp$Economy)

download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2FEDSTATS_Country.csv","education.csv")
df_edu <- read.csv("education.csv")
library(dplyr)
df_m <- inner_join(df_gdp,df_edu,by = c("X"="CountryCode"))


library(quantmod)
amzn = getSymbols("AMZN",auto.assign=FALSE)
sampleTimes = index(amzn)
library(lubridate)
sum(year(sampleTimes)==2012)
sum(wday(sampleTimes)==2 & year(sampleTimes)==2012)
