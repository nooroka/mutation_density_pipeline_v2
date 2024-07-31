from collections import defaultdict
dict1 = defaultdict(list)
op = open("../densities/densitiesGSM40_percent-3107_subtract_from_all_loop5_filtered_without_all_CG.txt","r")
for line in op:
    line = line.strip()
    line = line.split("\t")
    dict1[str(line[0])].append((line[3]))
op.close()
w = open("../compare/compareGSM40_percent-3107_subtract_from_all_loop5_filtered_without_all_CG.txt","w")
for key in dict1:
    w.write(str(dict1[key][1])+"\t"+str(dict1[key][0])+"\n")
w.close()
