from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import sys
#пока не добавляем проверку на координаты
for d in range(1,25,1):
    op = open("quadr738_{}_merged.geecee".format(d),"r")
    w = open("non_quadr_gc_nonok4_rep{}.txt".format(d),"a")
    list1 = []
    listx = []
    for line in op:
        flag_line2 = False
        if "#Sequence" not in line:
            break_flag = False
            line = line.strip()
            line = line.split()
            line22 = line[0][:-2]
            line222 = line22.split("-")
            length = int(line222[1]) - int(line222[0])
            gc = float(line[1])
            handle = open("comp{}_gene.fasta".format(d))
            for record in SeqIO.parse(handle,"fasta"):
                flag_line = False
                ids = record.id.split(":")
                ids2 = ids[1].split("-")
                id1 = ids2[0]
                id2 = ids2[1]
                k = 0
                nnumber =0
                for i in range(len(record.seq) - length + 1):
                    each = record.seq[k:i+1]    
                    if "N" not in str(each):
                        m = len(each)
                        if m == 0:
                            k = i
                        if m == length:
                            gc2 = gc_fraction(each,"remove")
                        #    print("each "+str(each) + " gc2 "+str(gc2) + " gc "+str(gc) +" length "+str(length))
                            sys.stdout.flush()
                            if float(gc2)>=float(gc):
                                k1 = int(id1)+i
                                k2 = int(id1)+i+length #bed-формат в обоих случаях
                                if len(set(list(range(k1,k2+1))).intersection(set(list1)))<=8:
                                    list1.extend(list(range(k1,k2+1)))
                                    w.write(str("chr{}".format(d)+"\t"+str(k1)+"\t"+str(k2)+"\t"+str(gc2)+"\t"+str(line222[0])+"\t"+str(line222[1])+"\n"))#здесь координаты верные, вторая не увеличена на 1, обратить внимание
                                    w.flush()
                         #        
                                    break_flag = True
                                    k=i
                                    break
                            else:
                                k=i
                    if "N" in str(each):
                        nnumber+=1
                        if nnumber>5000:
                            break
                    
                    if break_flag == True:
                        flag_line = True
                        break#  переходим на следующий рекорд
                    if flag_line == True:
                        break #переходим на следующий квадруплекс
            if flag_line == False:#не нашли квадруплекса, переходим на следующий
                w.write(str("chr{} ".format(d)+"\t"+str(line222[0])+"\t"+str(line222[1])+"\t"+str(line[1])+"\t"+"ok"+"\n"))
                w.flush()
            
            handle.close()
    w.close()
    op.close()
    
