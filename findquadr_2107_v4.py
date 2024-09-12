from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import sys
from Bio import SeqIO
import random

listused = []
def find_common_substrings(str1, str2):
    substrings = set()
    len1, len2 = len(str1), len(str2)

    for i in range(len1):
        for j in range(i + 1, len1 + 1):
            substr = str1[i:j]
            if substr in str2:
                substrings.add(substr)

    return substrings
def gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    if len(seq) > 0:
        return gc_count / len(seq)
def find_matching_sequence(fasta_file, target_length, target_gc,w,listused, inter):
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq)
        for i in range(len(seq) - target_length + 1):
            subseq = seq[i:i + target_length]
            if gc_content(subseq) >= target_gc:
                #print(f"Found matching sequence: {subseq} in {record.id} at position {i}")
                sys.stdout.flush()
                for i in range(len(listused)):
                    if len(find_common_substrings(subseq, listused[i]))>0:
                        print("kek")
                        inter = True
            if inter == False and gc_content(subseq)>=target_gc:
                    print("ok2")
                    w.write(str(subseq)+"\t"+str(record.id)+"\t"+str(i)+"\n")
                    w.flush()
                    listused.append(subseq)
                    return
#пока не добавляем проверку на координаты
for d in range(1,25,1):
    op = open("/data/nooroka/grant/punkt1/merged/geecee/quadr7_chain180424_merged2_sorted_{}_40_extracted.geecee".format(d),"r")
    w = open("non_quadr_gc_nonok2_rep{}_v4.txt".format(d),"a")
    for line in op:
        if "#Sequence" not in line:
            line = line.strip()
            line = line.split()
            line22 = line[0]
            line222 = line22.split("-")
          #  print(line222)
            length = int(line222[1]) - int(line222[0])
          #  print(length)
            gc = float(line[1])
            handle = "/data/nooroka/grant/punkt1/control/fasta/control_set_{}_40_my_extracted.fasta".format(d)
            w.write(''.join(str(line))+"\t")
            w.flush()
            inter = False
            result = find_matching_sequence(handle, length, gc, w,listused,inter)
            if inter == True:
               w.write("\n")
               w.flush()
      
    w.close()
    op.close()

