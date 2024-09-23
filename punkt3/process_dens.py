from collections import defaultdict
dict1 = defaultdict(list)
op = open("../densities/densitiesGSM40_percent-2109_subtract_from_snp_loop7.txt")
for line in op:
    line = line.strip()
    line = line.split("\t")
    dict1[str(line[0])].append((line[3]))
op.close()
w = open("../compare/compareGSM40_control2_loop7_snp.txt","w")
for key in dict1:
    w.write(str(dict1[key][1])+"\t"+str(dict1[key][0])+"\n")
w.close()
