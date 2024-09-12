
import os
for i in range(1,25,1):
 #   os.system("bedtools subtract -a comp{}_gene.bed -b comp{}_out_gene_quadr_all_sorted.bed  > comp{}_gene_GC.bed".format(i,i,i))
  #  os.system("bedtools subtract -a comp{}_gene.bed -b /data/nooroka/grant/punkt1/quadr738_flanks{}.bed  > comp{}_gene_GCnew.bed".format(i,i,i))
    os.system("bedtools subtract -a GSM_hg196_un_{}.bed -b  quadr7_chain180424_merged2_sorted_{}.bed > comphg19{}_gene_GCmerged.bed".format(i,i,i))
    os.system("bedtools getfasta -fi hg19_new.fna -bed comphg19{}_gene_GCmerged.bed> comphg19{}_gene_GCmerged.fasta".format(i,i))
