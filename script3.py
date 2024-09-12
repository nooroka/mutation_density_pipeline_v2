import os
import subprocess
for i in range(1,25,1):
    
    #os.system('''awk '{{print $2,$3}}'  /data/nooroka/qgrs/comp{}_out_gene_quadr_rev.txt >comp{}_out_gene_quadr_rev1.bed'''.format(i,i))
    #os.system('''awk '{{print $2,$3}}' /data/nooroka/qgrs/comp{}_out_gene_quadr.txt > comp_out_gene_quadr{}.bed'''.format(i,i))#already changed "-" to " " in comp{}_out_quadr.txt
    #os.system("sed -i 's/-/ /g' comp{}_out_gene_quadr_rev1.bed".format(i))
    #os.system("sed -i 's/-/ /g' comp_out_gene_quadr{}.bed".format(i))
    #os.system('''awk '{{print $1"\t"$2-1"\t"$3}}' comp{}_out_gene_quadr_rev1.bed > comp{}_out_gene_quadr_rev11.bed'''.format(i,i))
    #os.system('''awk '{{print $1"\t"$3-1"\t"$2}}' comp{}_out_gene_quadr_rev1.bed > comp{}_out_gene_quadr_rev111.bed'''.format(i,i))
    #os.system("sort -nk 2,3  comp{}_out_gene_quadr_rev111.bed >  comp{}_out_gene_quadr_rev111_sorted.bed".format(i,i))
    #os.system('''awk '{{print $1"\t"$2"\t"$3}}' comp_out_gene_quadr{}.bed > comp_out_gene_quadr{}{}.bed'''.format(i,i,i))
    #os.system("cat  comp{}_out_gene_quadr_rev111_sorted.bed  comp_out_gene_quadr{}{}.bed > comp{}_out_gene_quadr_all.bed".format(i,i,i,i))
    #os.system("sort -nk2,3 comp{}_out_gene_quadr_all.bed > comp{}_out_gene_quadr_all_sorted.bed".format(i,i))
    
    os.system("samtools faidx comp{}hg19_gene.fasta".format(i))
