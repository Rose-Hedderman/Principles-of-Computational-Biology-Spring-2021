library(seqinr)
library(ape)
cleanAlignment <- function(alignment, minpcnongap, minpcid)
{
 # make a copy of the alignment to store the new alignment in:
 newalignment <- alignment
 # find the number of sequences in the alignment
 numseqs <- alignment$nb
 # empty the alignment in "newalignment")
 for (j in 1:numseqs) { newalignment$seq[[j]] <- "" }
 # find the length of the alignment
 alignmentlen <- nchar(alignment$seq[[1]])
 # look at each column of the alignment in turn:
 for (i in 1:alignmentlen)
 {
	# see what percent of the letters in this column are non-gaps:
	nongap <- 0
	for (j in 1:numseqs)
	{
	   seqj <- alignment$seq[[j]]
	   letterij <- substr(seqj,i,i)
	   if (letterij != "-") { nongap <- nongap + 1}
	}
	pcnongap <- (nongap*100)/numseqs
	# Only consider this column if at least minpcnongap % of the letters are not gaps:
	if (pcnongap >= minpcnongap)
	{
	   # see what percent of the pairs of letters in this column are identical:
	   numpairs <- 0; numid <- 0
	   # find the letters in all of the sequences in this column:
	   for (j in 1:(numseqs-1))
	   {
		  seqj <- alignment$seq[[j]]
		  letterij <- substr(seqj,i,i)
		  for (k in (j+1):numseqs)
		  {
			 seqk <- alignment$seq[[k]]
			 letterkj <- substr(seqk,i,i)
			 if (letterij != "-" && letterkj != "-")
			 {
				numpairs <- numpairs + 1
				if (letterij == letterkj) { numid <- numid + 1}
			 }
		  }
	   }
	   pcid <- (numid*100)/(numpairs)
	   # Only consider this column if at least %minpcid of the pairs of letters are identical:
	   if (pcid >= minpcid)
	   {
		   for (j in 1:numseqs)
		   {
			  seqj <- alignment$seq[[j]]
			  letterij <- substr(seqj,i,i)
			  newalignmentj <- newalignment$seq[[j]]
			  newalignmentj <- paste(newalignmentj,letterij,sep="")
			  newalignment$seq[[j]] <- newalignmentj
		   }
	   }
	}
 }
 return(newalignment)
}

#You will now add additional lines to take in your aligned DNA sequences and build a PCA and phylogenetic trees here
one <- read.alignment("humanSeqAligned.fasta", "fasta")
two <- cleanAlignment(one,30,30)
three <- as.DNAbin(two)
four <- dist.dna(three)
fiveTree <- nj(four)
sixRoot <- root(fiveTree, "NC_001643.1",r=TRUE)
plot(sixRoot, type ="p")
# stage 8
?plot()
eight <- prcomp(four, scale=T)
plot(eight$x[,1], eight$x[,2], xlab = "PC1", ylab = "PC2")
text(eight$x[,1], eight$x[,2], labels=rownames(eight$x))