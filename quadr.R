library("tidyverse")
df<-read.csv("quadr7_all.bed",sep = "\t",header = FALSE)
df
df %>% count(V1,V4,sort = TRUE) -> df2
df2$V3<-as.integer(substr(df2$V1, 4, nchar(df2$V1)))
df2<-df2[order(df2$V3, decreasing = FALSE), ]
df2
title <- "strand"
ggplot(df2, aes(x = V3, y = n, fill = V4))  +
  geom_bar(stat = "identity", position = position_dodge())+theme(legend.position = c(0.8, 0.85))+scale_x_continuous(name = "chromosome number",limits = c(0,25),breaks = c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24))+scale_y_continuous(name = "count")+scale_fill_manual(title, values = c("seagreen3","red"))


df3 <- read.csv("sortedlen21840_new.txt",header = FALSE)
#hist(df3$V1,main = "G-quadruplex length histogram", xlab = "Length", breaks = 50)
hist(df3$V1,main = "G-quadruplex length histogram",cex.main =2, xlab = "Length", ylab = "Number", breaks = "FD", xlim = c(0,150), cex.lab = 1.6)
n <- length(df3$V1)
iqr <- IQR(df3$V1)
bin_width <- 2 * iqr / (n^(1/3))

# Calculate the number of bins
num_bins <- ceiling((max(df3$V1) - min(df3$V1)) / bin_width)

# Print bin width and number of bins
cat("FD Method Bin Width:", bin_width, "\n")
cat("Number of Bins:", num_bins, "\n")