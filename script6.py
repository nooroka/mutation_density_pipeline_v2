
import os
for i in range(1,25,1):
      os.system("bedtools getfasta -fi hg19_new.fna -bed comp{}hg19_gene.bed > comp{}hg19_gene.fasta".format(i,i))
