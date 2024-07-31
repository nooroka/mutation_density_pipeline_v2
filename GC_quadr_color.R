library("tidyverse")
b <- read.table("output_sorted40.geecee")
b %>% count(V1,V3,sort = TRUE) -> df2
df2$V5<-as.integer(substr(df2$V1, 4, nchar(df2$V1)))
df2<-df2[order(df2$V5, decreasing = FALSE), ]
ggplot(df2, aes(x = V5, y = n, fill = V3))  +
  geom_bar(stat = "identity", position = position_dodge())+theme(legend.position = c(0.8, 0.85))+scale_x_continuous(name = "chromosome number",limits = c(0,25),breaks = c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24))+  scale_fill_gradient(low = "green", high = "red")
hist(b$V3, xlab = "GC content of quadruplexes", ylab = "Counts", main = "Histogram of GC-content of quadruplexes",breaks = 100)