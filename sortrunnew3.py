import sys
import os
for i in range(1,25,1):
    op = open("comp{}_gene.bed".format(i),"r")
    for line in op:
        line = line.strip()
        line = line.split()
        os.system("python sortnew3.py /data/nooroka/grant/punkt3/sort_sort_sort/{}_sorted_sorted_sorted.txt {} {} result2_cosm_{}.txt".format(i,line[1],line[2],i))
    op.close()
