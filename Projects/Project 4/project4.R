# Rose Hedderman
# EID: rrh2298

# Part 1

# read in humanGenome.txt
og_table <- read.table("/work/07475/vagheesh/lonestar/project4/humanGeno.txt", sep = "", header = T)
# head(og_table)
# make the table a data frame
og_df <- as.data.frame(og_table)

# Part 2

# make combination table
# starting with the 5 other populations
comb <- c("Mbuti","Papuan","Dai","Yoruba","British")

# find the 10 unique combinations of them
comb <- as.data.frame(t(combn(comb,2)), stringAsFactors = F)

# double the df and bind them together
comb <- rbind(comb,comb)

# name columns of comb "X" and "Y"
names(comb) <- c("Pop3","Pop4")

# make a "chimp" column
comb$Pop1 <- "Chimp"

# make other rows with nmes Neanderthal and Denisovan
comb$Pop2 <- c(rep("Neanderthal",10), rep("Denisovan",10))

# Reorder the columns
comb <- comb[,c(3,4,1,2)]

# define abba and baba in vectors
abba <- c("0 2 2 0", "2 0 0 2")
baba <- c("2 0 2 0", "0 2 0 2")

# make vectors for stats
d_stats <- vector()
ABBA <- vector()
BABA <- vector()
for (i in 1:nrow(comb)) {
  togetherDF <- og_df[,as.matrix(comb[i,])]
  togetherDF$c <- paste(togetherDF[,1], togetherDF[,2], togetherDF[,3], togetherDF[,4])
  # count abba
  abba_count <- sum(table(togetherDF$c)[abba])
  # count abba
  baba_count <- sum(table(togetherDF$c)[baba])
  # put all abba counts in abba_total
  ABBA <- c(ABBA, abba_count)
  # put all baba counts in baba_total
  BABA <- c(BABA, baba_count)
  # compute d statistic
  Dstat <- (baba_count - abba_count)/(abba_count + baba_count)
  # put all d statistics in 
  d_stats <- c(d_stats, Dstat)
}

# make collection of d statistics a data frame
d_stats <- as.data.frame(d_stats)

# Part 3
#install.packages("dplyr")
#library(dplyr)

# wofirst (0-20000)
wofirst <- og_table[-c(1:20000),]
wofirst <- as.data.frame(wofirst)
d_stats_1 <- vector()

for (i in 1:nrow(comb)) {
  togetherDF <- wofirst[,as.matrix(comb[i,])]
  togetherDF$c <- paste(togetherDF[,1], togetherDF[,2], togetherDF[,3], togetherDF[,4])
  abba_count <- sum(table(togetherDF$c)[abba])
  baba_count <- sum(table(togetherDF$c)[baba])
  Dstat <- (baba_count - abba_count)/(abba_count + baba_count)
  d_stats_1 <- c(d_stats_1, Dstat)
}

# wosecond (20001-40000)

wosecond <- og_table[-c(20001:40000),]
wosecond <- as.data.frame(wosecond)
d_stats_2 <- vector()

for (i in 1:nrow(comb)) {
  togetherDF <- wosecond[,as.matrix(comb[i,])]
  togetherDF$c <- paste(togetherDF[,1], togetherDF[,2], togetherDF[,3], togetherDF[,4])
  abba_count <- sum(table(togetherDF$c)[abba])
  baba_count <- sum(table(togetherDF$c)[baba])
  Dstat <- (baba_count - abba_count)/(abba_count + baba_count)
  d_stats_2 <- c(d_stats_2, Dstat)
}

# wothird (40001-60000)

wothird <- og_table[-c(40001:60000),]
wothird <- as.data.frame(wothird)
d_stats_3 <- vector()

for (i in 1:nrow(comb)) {
  togetherDF <- wothird[,as.matrix(comb[i,])]
  togetherDF$c <- paste(togetherDF[,1], togetherDF[,2], togetherDF[,3], togetherDF[,4])
  abba_count <- sum(table(togetherDF$c)[abba])
  baba_count <- sum(table(togetherDF$c)[baba])
  Dstat <- (baba_count - abba_count)/(abba_count + baba_count)
  d_stats_3 <- c(d_stats_3, Dstat)
}


# wofourth (60001-80000)

wofourth <- og_table[-c(60000:80000),]
wofourth <- as.data.frame(wofourth)
d_stats_4 <- vector()

for (i in 1:nrow(comb)) {
  togetherDF <- wofourth[,as.matrix(comb[i,])]
  togetherDF$c <- paste(togetherDF[,1], togetherDF[,2], togetherDF[,3], togetherDF[,4])
  abba_count <- sum(table(togetherDF$c)[abba])
  baba_count <- sum(table(togetherDF$c)[baba])
  Dstat <- (baba_count - abba_count)/(abba_count + baba_count)
  d_stats_4 <- c(d_stats_4, Dstat)
}

# wofifth (80001-93166)
wofifth <- og_table[-c(80000:93166),]
wofifth <- as.data.frame(wofifth)
d_stats_5 <- vector()

for (i in 1:nrow(comb)) {
  togetherDF <- wofifth[,as.matrix(comb[i,])]
  togetherDF$c <- paste(togetherDF[,1], togetherDF[,2], togetherDF[,3], togetherDF[,4])
  abba_count <- sum(table(togetherDF$c)[abba])
  baba_count <- sum(table(togetherDF$c)[baba])
  Dstat <- (baba_count - abba_count)/(abba_count + baba_count)
  d_stats_5 <- c(d_stats_5, Dstat)
}

# df of d stats
D_list <- list(first = d_stats_1, second = d_stats_2, third = d_stats_3, fourth = d_stats_4, fifth = d_stats_5)


# make list a data frame
D_frame <- as.data.frame(D_list)
# put all mean values into a vector
second <- vector()

for (i in 1:ncol(D_frame)) {
  # create a temporary space without one column
  temp <- D_frame[-c(i)]
  temp_list <- vector()
  # find mean of each row without that column
  temp_list <- rowMeans(temp, na.rm = TRUE)
  second <- c(second,temp_list)
}
# reformat vector 
dim(second) <- c(20,5)
# make vector a data frame
vect <- as.data.frame(second)

# take mean of each row to find jackknife mean
JackMean <- rowMeans(vect)

# jackknife standard error
JackError <- sqrt(rowSums(((vect)-(JackMean))^2)/4)

# find zscore by quotient of jackknife mean and se
z <- JackMean/JackError

# combine all stats to be outputted
humanSeqD <- cbind(comb,ABBA,BABA,JackMean,JackError,z)
# write humanSeqD
humanSeqD
write.table(humanSeqD, file = "humanSeqD.txt", sep = "\t", row.names = F, col.names = T)
