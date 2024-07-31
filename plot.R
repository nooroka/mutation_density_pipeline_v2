
hg19<-read.csv("hg19_con2.csv", sep="\t")
library("tidyverse")
hg19$chromosome2 <-as.integer(substr(hg19$chromosome, 4, nchar(hg19$chromosome)))
hg19_2<-hg19[order(hg19$chromosome2, decreasing = FALSE), ]
df_2 <- hg19_2 |>
  pivot_longer(cols = quadruplexes:windows,
               names_to = "Type",
               values_to = "Value")
ggplot(df_2, aes(x = chromosome2, y = Value, fill = Type)) +
  geom_bar(stat = "identity", position = position_dodge())+theme(legend.position = c(0.8, 0.85))+scale_x_continuous(name = "chromosome number",limits = c(0,25),breaks = c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24),  labels = c("1", "2", "3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","X","Y"))
