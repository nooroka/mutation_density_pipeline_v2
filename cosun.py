import subprocess
import os
for i in range(1,25,1):
    op = open("gccoords_chr_new52_all_with_genes.txt","r")
    w3 = open("gccoords_all_genes{}.bed".format(i),"w")
    for line in op:
        line = line.strip()
        line = line.split()
        if str(line[0][:3]) == "chr" and ((str(line[0][-1]) == str(i) and str(line[0][-2]).isnumeric() is False) or str(line[0][-2:]) == str(i)):
            #print("line "+str(i)+"\t"+str(line))
            line88 = line[6][1:-1]
            line99 = line[7][:-1]
            #print("line88-99 "+str(line88)+"\t"+str(line99))
            w3.write(str(line[0])+"\t"+str(line88)+"\t"+str(line99)+"\n")
    w3.close()
    op.close()
    os.system("uniq gccoords_all_genes{}.bed > gccoords_all_genes{}_un.bed".format(i,i))

