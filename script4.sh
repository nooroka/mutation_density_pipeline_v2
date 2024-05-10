
#!/bin/bash
for i in {1..24}
do
    bedtools subtract -a $1 -b  $2 > comp${i}_gene_GCmerged.bed
    bedtools getfasta -fi hg38_new.fna -bed comp${i}_gene_GCmerged.bed -fo $3
done
