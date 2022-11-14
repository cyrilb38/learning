setwd("C:/Users/Cyril/Documents/Travail - Ressources/Fun/Introduction à la statistique avec R/Données")
smp <- read.csv2("smp2.csv")

sum(smp$age >=20 & smp$age <= 30, na.rm = T)

smp$age_breaks <- cut(smp$age, breaks=c(0,quantile(smp$age,0.25,na.rm=T),
                                                quantile(smp$age,0.5,na.rm=T),
                                                quantile(smp$age,0.75,na.rm=T),
                                                max(smp$age,na.rm=T)))

cor.test(smp$age,smp$dur.interv)

t.test(smp$dur.interv~smp$dep.cons,var.equal = T)

wilcox.test(smp$dur.interv~smp$suicide.past)
