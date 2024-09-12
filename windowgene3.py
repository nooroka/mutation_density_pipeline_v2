import sys
import os
from Bio.Seq import Seq
from itertools import islice
from Bio import SeqIO
from Bio.SeqUtils import GC
import re
#sysa = sys.argv[1].split("/")
def mergeIntervals(intervals):
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    # insert first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
        # Check for overlapping interval,
        # if interval overlap
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
 
    #print("The Merged Intervals are :", end=" ")
    for i in range(len(stack)):
        return stack[i]
 
 

w = open("result13_coord_new_all_with_genes2.txt","w")
handle = open(sys.argv[1])#делим на 44 последовательность уже без N
for record in SeqIO.parse(handle, "fasta") :
    #id1 = record.id.split(":")
    #id2 =id1[1].split("-")
    seq = str(record.seq) #it must be one sequence
    k = 0
    #print([(m.start(0), m.end(0)) for m in re.finditer("A|a|T|t|G|g|C|c", seq)])#если пересечем, то так найдем мутации, которые не в N. А они вроде все не в N
    #str11 = re.sub("N|n","",seq)
    t =len(seq)
    for i in range(1,t,1):
        str1 = seq[k: i]
        #print(str(str1)+"\t"+str(len(str1)))
        if len(str1)>0:
            list1 = []
            for d in re.finditer("[ATGCatgc]+",str1):
                list1.append([d.start(0),d.end(0)])
            #print(list1)
            if len(list1)>0:
                int1 = mergeIntervals(list1)
            # print(int1)
            #print(mergeIntervals([[d.start(0), d.end(0)] for d in re.finditer("[ATGCagtc]", str1) if len(d)>0]))
                str11 = re.sub("N|n","",str1)
            #print(str11)
                m =len(str11)
                if m == 0:
                    k = i
                if m == 44:#окошки 44 без N
                    gc = GC(str11)
                    int2 =[]
                    for s in range(len(int1)):
                        al = int(int1[s])+k#еще надо прибавить 1 сейчас или потом, тут координаты по bed!
                        int2.append(al)
                    #print(id1[0])
                    w.write(str(record.id)+"\t"+"gc\t"+str(gc)+'\tseq\t'+str(str11)+"\t"+str(m)+"\t"+str(int2)+"\n")#длина интервала становится меньше
                    k = i
        #if len(seq[i:]) == seq[i:].lower().count("n"):
        if len(str1) > 100000: #костыль, слишком много  N, хромосома никуда не годится
           k = seq[i:].find("[ATGCatgc]+")
           print(k)
         #     break
        

handle.close()
w.close()

