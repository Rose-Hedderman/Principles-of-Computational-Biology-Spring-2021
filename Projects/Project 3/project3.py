# Rose Hedderman
# EID: rrh2298

# os is imported to be able to access files
import os
import Bio
from Bio import SeqIO
from Bio import Entrez
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

Entrez.email = "roseh12@utexas.edu"
# write assign fasta file to g to write output to
g = open('humanSeq.fasta','w')
d = []
def fromClass(i):
    # from class 
    handle = Bio.Entrez.efetch(db="Nucleotide", id = i, rettype="gb",retmode="text")
    gb_file_contents = handle.read()
    handle.close()
    with open(i+".gb","w") as out_handle:
        out_handle.write(gb_file_contents)
    with open(i+".gb","r") as in_handle:
        record = SeqIO.read(in_handle, format="gb")
    g.write(">"+i+"\n"+str(record.seq)+"\n")
    
# open humanSeq.txt file found in this location given in the assignment
f = open("/work/07475/vagheesh/lonestar/project3/humanSeq.txt", "r")
for lines in f:
    sub = lines.rstrip("\n")
    sub = sub.split("\t",1)
    if sub[0] != "Accession ID":
        fromClass(sub[0])
g.close()

