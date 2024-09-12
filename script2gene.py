import os
import subprocess
from collections import defaultdict
def solve(intervals, point):
       count = 0
       for i, j in intervals:
            if point >= i and point <= j:
                count += 1
       return count
w = open("densitiesall9.txt","a")
for i in range(1,25,1):  
    op = open("gccoords_chr_new44_all_with_genes_pattern.txt","r")
    w2 = open("anna{}.bed".format(i),"w")
    for line in op:
        line = line.strip()
        line = line.split()
        if str(line[0][:3])== "chr" and ((str(line[0][-1]) == str(i) and str(line[0][-2]).isnumeric() is False) or str(line[0][-2:]) == str(i)):
            print(line,i)
            line88 = line[8][1:-1]
            line99 = line[9][:-1]
            w2.write(str(line[0])+"\t"+str(line88)+"\t"+str(line99)+"\n")
    w2.close()
    op.close()
    d5 = subprocess.check_output("wc -l anna{}.bed".format(i),shell = True)
    os.system("uniq anna{}.bed > gccoords_{}_all_un.bed".format(i,i))
    os.system("bedtools intersect  -a bed_chr_{}_sorted.bed -b gccoords_{}_all_un.bed > intmut_all{}.bed".format(i,i,i)) 
    os.system("uniq intmut_all{}.bed > intmut_all_un{}.bed".format(i,i))
    d1 = subprocess.check_output('wc -l intmut_all_un{}.bed'.format(i),shell = True) 
    d11 = d1.decode().split()[0]
    d55 = int(d5.decode().split()[0])*44
    print("d11-55 "+str(d11)+"\t"+str(d55)+"\n")
    w.write("chr{}".format(i)+"\t"+"average density"+"\t"+str(float(int(d11)/int(d55)))+"\tinterval length"+"\t"+"44"+"\n")
w.close()

