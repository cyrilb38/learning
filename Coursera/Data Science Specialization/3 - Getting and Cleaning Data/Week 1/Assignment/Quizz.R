download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06hid.csv", destfile = "quizz1.csv")

df1 <- read.csv("quizz1.csv")
str(df1)
names(df1)

df2


#XML files (Q4)
library(XML)
download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Frestaurants.xml", destfile = "xmlfile")

url <- "xmlfile"
doc <- xmlTreeParse(url,useInternalNodes = TRUE)
rootNode <- xmlRoot(doc)

sum(xpathSApply(rootNode,"//zipcode",xmlValue) =="21231")


#Q5
download.file("https://d396qusza40orc.cloudfront.net/getdata%2Fdata%2Fss06pid.csv", destfile = "Q5.csv")
library("data.table")
DT <- fread(input = "Q5.csv")
