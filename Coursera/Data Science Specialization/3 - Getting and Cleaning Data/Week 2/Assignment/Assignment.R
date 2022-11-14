setwd("E:/Travail - Ressources/Coursera/Data Science Specialization/3 - Getting and Cleaning Data/Week 2/Assignment")

acs <- read.csv("getdata_data_ss06pid.csv")

con = url("http://biostat.jhsph.edu/~jleek/contact.html")
htmlCode = readLines(con)
close(con)
nchar(htmlCode[10])
nchar(htmlCode[20])
nchar(htmlCode[30])
nchar(htmlCode[100])

read.fortran("getdata_wksst8110.for",format = )
