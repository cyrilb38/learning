setwd("E:/Travail - Ressources/Edx/The Analytics Edge/Week 6/Assignment/1 - Document clustering with Daily Kos")

dailyKos <- read.csv("dailykos.csv")

#calculate distances
mdailyKos <- as.matrix(dailyKos)
distances <- dist(mdailyKos, method = "euclidian")

#create and plot hierarical clustering
h <- hclust(distances, method = "ward.D")
plot(h)

#cut in 7 clusters
clusters <- cutree(h, k = 7)

clusterList <- list()

cluster1 <- dailyKos[clusters == 1,]
cluster2 <- dailyKos[clusters == 2,]
cluster3 <- dailyKos[clusters == 3,]
cluster4 <- dailyKos[clusters == 4,]
cluster5 <- dailyKos[clusters == 5,]
cluster6 <- dailyKos[clusters == 6,]
cluster7 <- dailyKos[clusters == 7,]

tail(sort(colMeans(cluster1)))
tail(sort(colMeans(cluster2)))
tail(sort(colMeans(cluster3)))
tail(sort(colMeans(cluster4)))
tail(sort(colMeans(cluster5)))
tail(sort(colMeans(cluster6)))
tail(sort(colMeans(cluster7)))

#Using kmeans clustering
set.seed(1000)
km <- kmeans(mdailyKos, centers = 7)

kcluster1 <- dailyKos[km$cluster == 1,]
kcluster2 <- dailyKos[km$cluster == 2,]
kcluster3 <- dailyKos[km$cluster == 3,]
kcluster4 <- dailyKos[km$cluster == 4,]
kcluster5 <- dailyKos[km$cluster == 5,]
kcluster6 <- dailyKos[km$cluster == 6,]
kcluster7 <- dailyKos[km$cluster == 7,]

tail(sort(colMeans(kcluster1)))
tail(sort(colMeans(kcluster2)))
tail(sort(colMeans(kcluster3)))
tail(sort(colMeans(kcluster4)))
tail(sort(colMeans(kcluster5)))
tail(sort(colMeans(kcluster6)))
tail(sort(colMeans(kcluster7)))

#Comparing 2 methods
table(clusters, km$cluster)
