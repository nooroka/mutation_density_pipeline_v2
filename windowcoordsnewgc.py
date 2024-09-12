import sys
import os
from Bio.Seq import Seq
from itertools import islice
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import re
sysa = sys.argv[1].split("/")
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
 
 

w = open("resultnewgc_coord_new_{}_pattern.txt".format(str(sysa[-1])),"w")
handle = open(sys.argv[1])
for record in SeqIO.parse(handle, "fasta") :
    id1 = record.id.split(":")
    id2 =id1[1].split("-")
    seq = str(record.seq) 
    k = 0
    t =len(seq)
    for i in range(1,t,1):
        str1 = seq[k: i]
        m = len(str1)
        if m == 0:
            k = i
        if m == 44 and "N" not in str1 and "n" not in str1:
                gc = gc_fraction(str1,"remove")
                al = k+int(id2[0])
                al2 = i+int(id2[0])-1
                w.write("gc\t"+str(gc)+'\tseq\t'+str(str1)+"\t"+str(id2[0])+"\t"+str(id2[1])+"\t"+str(m)+"\t"+str(al)+"\t"+str(al2)+"\n")
                k = i
        if len(str1) > 100000:
            break
handle.close()
w.close()

