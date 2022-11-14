setwd("E:/Travail - Ressources/Edx/The Analytics Edge/Week 7/2 - Visualizing Network Data")

users <- read.csv("users.csv")
edges <- read.csv("edges.csv")

#Counting friends
library(dplyr)
users$id <- as.factor(users$id)
dfCounts <- left_join(users, as.data.frame(table(edges$V1)), by = c("id"="Var1"))
dfCounts <- left_join(dfCounts, as.data.frame(table(edges$V2)), by = c("id"="Var1"))
dfCounts[is.na(dfCounts)] = 0
dfCounts$Freq = dfCounts$Freq.x + dfCounts$Freq.y
mean(dfCounts$Freq)

table(users[!users$school =="",]$locale)

table(users$school,users$gender)

#create graph plot
library(igraph)
?graph.data.frame

g <- graph.data.frame(edges, directed = FALSE, users)
plot(g, vertex.size=5, vertex.label=NA)
degree(g)
sum(dfCounts$Freq>=10)

V(g)$size = degree(g)/2+2
plot(g, vertex.label=NA)
max(V(g)$size)

V(g)$color = "black"
V(g)$color[V(g)$gender == "A"] = "red"
V(g)$color[V(g)$gender == "B"] = "gray"
plot(g, vertex.label=NA)

V(g)$color = "black"
V(g)$color[V(g)$school == "A"] = "red"
V(g)$color[V(g)$school == "AB"] = "gray"
plot(g, vertex.label=NA)

V(g)$color = "black"
V(g)$color[V(g)$locale == "A"] = "red"
V(g)$color[V(g)$locale == "B"] = "gray"
plot(g, vertex.label=NA)

?igraph.plotting
rglplot.igraph(g)
