from Bio import SeqIO
from itertools import chain
from Bio.SeqUtils import gc_fraction
#пока не добавляем проверку на координаты
for d in range(1,25,1):
    op = open("quadr738_{}_merged.geecee".format(d),"r")
    w = open("non_quadr_gc_nonda_rep{}.txt".format(d),"a")
    #w2 = open("test{}.bed".format(d),"w")
    list1 = []
    dict2 = {}
    for line in op:
        flag_line = False
        if "#Sequence" not in line:
            break_flag = False
            line = line.strip()
            line = line.split()
            line22 = line[0][:-2]
            line222 = line22.split("-")
            length = int(line222[1]) - int(line222[0])
            gc = float(line[1])
            if (length,gc) not in dict2.keys():
                dict2[(length,gc)] = []
            dict2[(length,gc)].append((int(line222[0]),int(line222[1])))
   # m = 0
   # print(dict2)
    handle = open("comp{}_gene.fasta".format(d))
    listd = []
    for record in SeqIO.parse(handle,"fasta"):
        length2 = 35
        ids = record.id.split(":")
        ids2 = ids[1].split("-")
        id1 = ids2[0]
        id2 = ids2[1]
        while length2!=551:
            #break1 = False
            #break2 = False
            k = 0
            m = 0
            for i in range(len(record.seq)):
                #each = record.seq[i: i + length2]# сделаем не скользящее окно
                print("length2 "+str(length2))
                print("k "+str(k)+" i+length2 "+str(i)+" "+str(length2))
                each = record.seq[k: i+1]
                if "N" not in str(each):
                    print("each "+str(each))
                    m = len(each)
                    if m == 0:
                        k = i
                    if m == length2:
                        gc2 = gc_fraction(each,"remove")
                        print("gc2 "+str(gc2) + " gc"+str(gc))
                        k1 = int(id1)+i
                        k2 = int(id2)+i+length2
                        list1 = [list(dict2.values())[i] for i in range(len(list(dict2.keys()))) if list(dict2.keys())[i][0]==length2 and list(dict2.keys())[i][1] >= round(gc2)]#список списков 
                        print("list1 "+str(list1))
                        for h in range(len(list1)):
                            for m1 in range(len(list1[h])):
                                if len(set(list(range(k1,k2+1))).intersection(set(listd)))<=8:
                                    listd.extend(list(range(k1,k2+1)))
                                    w.write("chr{}".format(d)+"\t"+str(k1)+"\t"+str(k2)+"\t"+str(gc2)+"\t"+str(list1[h][m1][0])+"\t"+str(list1[h][m1][1])+"\n")
            
                           
                        
                        #print(list1)
                        list2 = [list(dict2.values())[i] for i in range(len(list(dict2.keys()))) if list(dict2.keys())[i][0] == length2 and list(dict2.keys())[i][1]>=round(gc2)-0.12 and list(dict2.keys())[i][1]<round(gc2)]
                        print("list2 "+str(list2))
                        for h2 in range(len(list2)):
                            for m2 in range(len(list2[h2])):
                                if len(set(list(range(k1,k2+1))).intersection(set(listd)))<=8:
                                    listd.extend(list(range(k1,k2+1)))
                                    w.write("chr{}".format(d)+"\t"+str(list2[h2][m2][0])+"\t"+str(list2[h2][m2][1])+"\t"+"ok"+"\n")
                                    break
                        k = i       
            length2+=1
   
    w.close()
    op.close()
    
