import os
#for file1 in os.listdir("/data/nooroka/grant/punkt3/fasta/"):
def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num
for i in range(1,25,1):
   op = open("meanquadr.txt","r")
   for line in op:
        line = line.strip()
        line = line.split()
        line11 = int_r(float(line[1]))
        if int(line[0])==i:
             os.system("python windowcoords15.py /data/nooroka/grant/punkt3/comp{}_gene_GCmerged.fasta {}".format(i,line11))
   op.close()
