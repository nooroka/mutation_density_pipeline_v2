from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import sys
from Bio import SeqIO
import random

listused = []
def gc_content(seq):
    gc_count = seq.count('G') + seq.count('C')
    if len(seq) > 0:
        return gc_count / len(seq)
def find_intersections(seq1, seq2, min_length=8):
    # Найти все подстроки длиной min_length и более в первой последовательности
    substrings_seq1 = set()
    for length in range(min_length, len(seq1) + 1):
        for i in range(len(seq1) - length + 1):
            substrings_seq1.add(seq1[i:i + length])
    
    # Найти все подстроки длиной min_length и более во второй последовательности
    substrings_seq2 = set()
    for length in range(min_length, len(seq2) + 1):
        for i in range(len(seq2) - length + 1):
            substrings_seq2.add(seq2[i:i + length])
    
    # Найти пересечения
    intersections = substrings_seq1 & substrings_seq2
    
    return intersections
def find_matching_sequence(fasta_file, target_length, target_gc,w,listused):
    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq)
        for i in range(len(seq) - target_length + 1):
            inter = False
            subseq = seq[i:i + target_length]
            if gc_content(subseq) >= target_gc:
                print(f"Found matching sequence: {subseq} in {record.id} at position {i}")
                sys.stdout.flush()
                for i in range(len(listused)):
                    if len(find_intersections(subseq, listused[i]))>0:
                        inter = True
                if inter == False:
                    w.write(str(subseq)+"\t"+str(record.id)+"\t"+str(i)+"\n")
                    w.flush()
                    listused.append(subseq)
                else:
                    w.write("\n")
                    w.flush()
                return
#пока не добавляем проверку на координаты
for d in range(1,25,1):
    op = open("/data/nooroka/grant/punkt1/merged/geecee/quadr7_chain180424_merged2_sorted_{}_40_extracted.geecee".format(d),"r")
    w = open("non_quadr_gc_nonok2_rep{}_v3.txt".format(d),"a")
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
            result = find_matching_sequence(handle, length, gc, w,listused)
    w.close()
    op.close()

