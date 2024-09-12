import os
for i in range(1,23,1):
    os.system("revseq comp{}_gene.fasta comp{}_gene_rev.fasta".format(i,i))
