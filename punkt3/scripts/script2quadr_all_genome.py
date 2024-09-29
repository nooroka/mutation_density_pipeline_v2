import os
import subprocess
from collections import defaultdict

w = open("../densities/densitiesall_genequadr_merged.txt","a")
for i in range(1,25,1):  
    os.system("bedtools intersect  -a /data/nooroka/grant/punkt3/bed-37/bed_chr_{}_sorted.bed -b /data/nooroka/grant/punkt3/stage2/hg19_quadr/merged/hg19_new_quadr_loop7_merged_{}.bed | awk  '!seen[$4]++' > /data/nooroka/grant/punkt3/stage2/allgenequadr/merged/mutall_quadr_merged{}.bed".format(i,i,i))
    op = open("/data/nooroka/grant/punkt3/stage2/hg19_quadr/merged/hg19_new_quadr_loop7_merged_{}.bed".format(i),"r")
    sum1 = 0
    for line in op:
        line = line.strip()
        line = line.split()
       # if str(line[0][:3])== "chr" and ((str(line[0][-1]) == str(i) and str(line[0][-2]).isnumeric() is False) or str(line[0][-2:]) == str(i)):
        sum1 += int(line[2])-int(line[1])
    d1 = subprocess.check_output('wc -l /data/nooroka/grant/punkt3/stage2/allgenequadr/merged/mutall_quadr_merged{}.bed'.format(i),shell = True)
    d11 = d1.decode().split()[0]
    w.write("chr{}".format(i)+"\t"+"average density"+"\t"+str(float(int(d11)/int(sum1)))+"\n")
w.close()

