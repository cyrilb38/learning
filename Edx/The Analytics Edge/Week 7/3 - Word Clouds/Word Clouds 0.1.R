setwd("E:/Travail - Ressources/Edx/The Analytics Edge/Week 7/3 - Word Clouds")

library(tm)
library(SnowballC)

# Read in the data
tweets = read.csv("tweets.csv", stringsAsFactors=FALSE)


# Create corpus
corpus = Corpus(VectorSource(tweets$Tweet))
# Convert to lower-case
corpus = tm_map(corpus, tolower)
corpus = tm_map(corpus, PlainTextDocument)
# Remove punctuation
corpus = tm_map(corpus, removePunctuation)
# Remove stopwords and apple
corpus = tm_map(corpus, removeWords,  stopwords("english"))
# Create matrix
frequencies = DocumentTermMatrix(corpus)

allTweets = as.data.frame(as.matrix(frequencies))

#create visualization
library(wordcloud)
wordcloud(colnames(allTweets),colSums(allTweets))

#removing apple word
corpus = tm_map(corpus, removeWords, c("apple", stopwords("english")))
frequencies = DocumentTermMatrix(corpus)
allTweets = as.data.frame(as.matrix(frequencies))
wordcloud(colnames(allTweets),colSums(allTweets),scale=c(2, 0.25))

#Colorbrewer
library(RColorBrewer)
display.brewer.all()

wordcloud(colnames(allTweets),colSums(allTweets),scale=c(2, 0.25),colors=brewer.pal(9, "Blues")[c(-1, -2, -3, -4)])
