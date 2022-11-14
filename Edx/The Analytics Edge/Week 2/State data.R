data(state)
statedata = cbind(data.frame(state.x77), state.abb, state.area, state.center,  state.division, state.name, state.region)

with(statedata,plot(x,y))

library(dplyr)
statedata %>%
  group_by(state.region) %>%
  summarise(HS.Grad = mean(HS.Grad))

tapply(statedata$HS.Grad,statedata$state.region,FUN = mean)

with(statedata,boxplot(Murder ~ state.region))

statedata %>%
  filter(state.region == "Northeast") %>%
  arrange(desc(Murder))

lm