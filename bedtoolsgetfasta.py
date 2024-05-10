import os
for i in range(1,3,1):
    os.system("bedtools getfasta  -fi hg38_new.fna -bed comp{}_gene.bed > comp{}_gene.fasta".format(i,i))

