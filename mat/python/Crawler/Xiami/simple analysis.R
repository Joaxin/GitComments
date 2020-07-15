library(ggplot2)
library(dplyr)
Artists <- read.csv(file.choose(), header=FALSE)
colnames(Artists) <- c("image","url","artist","country")
Artists[] <- lapply(Artists, as.character)
Artists$country[Artists$country=="欧美"] <- "Western"
Artists$country<- gsub("[\u4e00-\u9fa5]","",Artists$country)
Artists$country<- gsub("^ | $","",Artists$country)
# Artists$country[Artists$country==""] <- NA
# Artists[is.na(Artists$country),]
Artists$country[Artists$country=="United States of America"] <- "USA"
table(Artists$country)

Artists[Artists$country=="Japan",]$artist

Artists[grep("^S",Artists$artist),]$artist

df <- as.data.frame(table(Artists$country)) %>% arrange(desc(Freq),Var1)
df$Var1 <- factor(df$Var1,levels=rev(as.character(df$Var1)))
ggplot(df) + geom_bar(aes(x=Var1,y=Freq,fill=Var1),stat = "identity")+ 
                  geom_text(aes(label = Freq,x=Var1,y=Freq,vjust = 0.1,hjust = -0.1)) +
                  theme(panel.grid.major=element_blank(),panel.grid.minor=element_blank()) +
                  scale_y_sqrt() + coord_flip() + scale_fill_discrete(guide=FALSE)+
                  xlab("Region") + ylab("sqrt(Count)")
