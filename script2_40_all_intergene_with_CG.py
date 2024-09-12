#редакт
import os
import subprocess
from collections import defaultdict
import sys
w = open(sys.argv[4],"a")
#for i in range(1,25,1):  
    #os.system("sort -nk2,3   bed_chr_{}.bed > bed_chr_{}_sorted.bed".format(i,i))
os.system("bedtools intersect -a /data/nooroka/grant/punkt3/bed-37/bed_chr_{}_sorted.bed -b {} > /data/nooroka/grant/punkt3/resultgene/resultgenehg19{}_intergene_CG.bed".format(sys.argv[3],sys.argv[1],sys.argv[3]))
op2 = open(sys.argv[1],"r")
d4 = 0
for line2 in op2:
        line2 = line2.strip()
        line2 = line2.split()
        sum22 = int(line2[2])-int(line2[1])
        d4+=sum22
op2.close()
op = open(sys.argv[2],"r")
w3 = open("/data/nooroka/grant/punkt3/gccoords/def/gccoords_{}2defhg19_40_all_loop7_intergene_CG.bed".format(sys.argv[3]),"w")
a  = ""
for line in op:
        line = line.strip()
        line = line.split()
        a = line[6]
        print("line "+str(line))
        line77 = int(line[7][1:-1])
        line88 = line[8][:-1]
        print("line77-88 "+str(line77)+"\t"+str(line88))
        w3.write("chr{}".format(sys.argv[3])+"\t"+str(line77)+"\t"+str(line88)+"\n")
w3.close()
op.close()
d5 = subprocess.check_output("wc -l {}".format(sys.argv[2]),shell = True)
os.system("uniq /data/nooroka/grant/punkt3/gccoords/def/gccoords_{}2defhg19_40_all_loop7_intergene_CG.bed > /data/nooroka/grant/punkt3/gccoords/def/gccoords_{}_undefhg19_40_all_loop7_intergene_CG.bed".format(sys.argv[3],sys.argv[3]))
os.system("uniq /data/nooroka/grant/punkt3/resultgene/resultgenehg19{}_intergene_CG.bed | awk  '!seen[$4]++' > /data/nooroka/grant/punkt3/resultgene/resultgenehg19{}_un_intergene_CG.bed".format(sys.argv[3],sys.argv[3]))
os.system("bedtools intersect  -a /data/nooroka/grant/punkt3/bed-37/bed_chr_{}_sorted.bed -b /data/nooroka/grant/punkt3/gccoords/def/gccoords_{}_undefhg19_40_all_loop7_intergene_CG.bed | awk  '!seen[$4]++' > intmut/intmuthg19{}_intergene_CG.bed".format(sys.argv[3],sys.argv[3],sys.argv[3])) 
d1 = subprocess.check_output('wc -l /data/nooroka/grant/punkt3/intmut/intmuthg19{}_intergene_CG.bed'.format(sys.argv[3]),shell = True) #look at the number of mutations
d2 = subprocess.check_output('wc -l /data/nooroka/grant/punkt3/resultgene/resultgenehg19{}_un_intergene_CG.bed'.format(sys.argv[3]), shell = True)
d6 = subprocess.check_output('wc -l {}'.format(sys.argv[1]),shell = True)
d11 = d1.decode().split()[0]
d22 = d2.decode().split()[0]
d66 = d6.decode().split()[0]
d55 = int(d5.decode().split()[0])*int(a)
print("d11-55-22-4 "+str(d11)+"\t"+str(d55)+"\t"+str(d22)+"\t"+str(d4))

w.write("chr{}".format(sys.argv[3])+"\t"+"non G4 motif"+"\t"+"average density"+"\t"+str(float(int(d11)/int(d55)))+"\taverage G4 motif/interval length"+"\t"+str(a)+"\n")
w.write("chr{}".format(sys.argv[3])+"\t"+"G4 motif all"+"\t"+"average density"+"\t"+str(float(int(d22)/int(d4)))+"\taverage G4 motif/interval length"+"\t"+str(float(int(d4)/int(d66)))+"\n")
w.close()

