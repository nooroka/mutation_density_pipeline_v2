for i in range(1,25,1):
    op = open("bed_chr_{}_sorted.bed".format(i),"r")
    w = open("bed_chr_{}_sorted_snp.bed".format(i),"w")
    for line in op:
        line = line.strip()
        if "track" in line:
            w.write(str(line)+"\n")
        if "track" not in line:
            line2 = line.split()
            if int(line2[2])-int(line2[1])==1:
                w.write(str(line)+"\n")
    w.close()


