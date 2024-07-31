library("plotly")
df<-read.csv("all_len39.txt", header = F,sep = " ")
df2<-aggregate(df$V2, list(df$V1), FUN=sum)
df2$Group.2<-as.integer(substr(df2$Group.1, 4, nchar(df2$Group.1)))
df3<-df2[order(df2$Group.2, decreasing = FALSE), ]
barplot(x~ Group.2,data = df3, xlab = "chromosomes", ylab = "counts")
df4<-read.csv("chromosomes.csv",sep = "\t", header = F)
df4$Group.2<-as.integer(substr(df4$V1, 4, nchar(df4$V1)))
df5<-df4[order(df4$Group.2, decreasing = FALSE),]
df3$length <- df5$V2
df3$GSM3003539 <-df3$x/df3$length
barplot(GSM3003539~ Group.2,data = df3, xlab = "chromosomes", ylab = "normalized counts")
df1<-read.csv("all_len40.txt", header = F,sep = " ")
df21<-aggregate(df1$V2, list(df1$V1), FUN=sum)
df21$Group.2<-as.integer(substr(df21$Group.1, 4, nchar(df21$Group.1)))
df31<-df21[order(df21$Group.2, decreasing = FALSE), ]
barplot(x~ Group.2,data = df31, xlab = "chromosomes", ylab = "counts")
df41<-read.csv("chromosomes.csv",sep = "\t", header = F)
df41$Group.2<-as.integer(substr(df41$V1, 4, nchar(df41$V1)))
df51<-df41[order(df41$Group.2, decreasing = FALSE),]
df31$length <- df51$V2
df31$GSM3003540 <-df31$x/df31$length
barplot(GSM3003540~ Group.2,data = df31, xlab = "chromosomes", ylab = "normalized counts")
merged_df <- merge(df3, df31, by = c("Group.1","Group.2"))
merged_df_selected<-merged_df[,c("Group.2","GSM3003539","GSM3003540")]
library(tidyverse)
df_2 <- merged_df_selected |>
  pivot_longer(cols = GSM3003539:GSM3003540,
               names_to = "Sample",
               values_to = "Value")
ggplot(df_2, aes(x = Group.2, y = Value, fill = Sample)) +
  geom_bar(stat = "identity", position = position_dodge())+theme(legend.position = c(0.82, 0.9))+scale_x_continuous(name = "chromosome number",limits = c(0,25),breaks = c(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24))
