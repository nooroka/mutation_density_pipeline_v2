from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
#пока не добавляем проверку на координаты
for d in range(1,25,1):
    op = open("quadr738_{}_merged.geecee".format(d),"r")
    w = open("non_quadr_gc_nonok3_rep{}.txt".format(d),"w")
    #w2 = open("test{}.bed".format(d),"w")
    list1 = []
   # m = 0
    for line in op:
        flag_line = False
        if "#Sequence" not in line:
            break_flag = False
            line = line.strip()
            line = line.split()
            line222 = line[0][:-2].split("-")
            length = int(line222[1]) - int(line222[0])
            gc = float(line[1])
            handle = open("comp{}_gene_GCmerged.fasta".format(d))
            for record in SeqIO.parse(handle,"fasta"):
                ids = record.id.split(":")
                ids2 = ids[1].split("-")
                id1 = ids2[0]
                id2 = ids2[1]
                for i in range(len(record.seq) - length + 1):
                    each = record.seq[i: i + length]
                    if "N" not in each or "n" not in each:
                        gc2 = gc_fraction(each,"remove")
                        if float(gc2)>=gc:
                            k1 = int(id1)+i
                            k2 = int(id1)+i+length #bed-формат в обоих случаях
                            if len(set(list(range(k1,k2+1))).intersection(set(list1)))<8:
                            #if k1 not in list1 and k2 not in list1:
                                list1.extend(list(range(k1,k2+1)))
                                w.write("chr{}".format(d)+"\t"+str(k1)+"\t"+str(k2)+"\t"+str(gc2)+"\t"+str(line222[0])+"\t"+str(line222[1])+"\n")#здесь координаты верные, вторая не увеличена на 1, обратить внимание
                        
                                break_flag = True
                                break
                if break_flag == True:
                    flag_line = True
                    break
            if flag_line == False:
                 w.write("str{} ".format(d)+"\t"+str(line222[0])+"\t"+str(line222[1])+"\t"+str(line[1])+"\t"+"ok"+"\n")
            handle.close()
    w.close()
    op.close()
    
