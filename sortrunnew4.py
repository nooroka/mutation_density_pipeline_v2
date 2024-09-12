import sys
import os
for i in range(1,25,1):
    os.system("bedtools intersect -a comp{}_gene.bed -b /data/nooroka/grant/punkt3/sort_sort_sort2/sort_sort_sort_sort2/bed/{}_2_sorted.bed > mutcos{}.bed".format(i,i,i))
