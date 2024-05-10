import sys
op = open(sys.argv[1],"r")
w1 = open(sys.argv[2],"w")
w2 = open(sys.argv[3],"w")
for line in op:
    line = line.strip()
    if "+" in line:
        w1.write(str(line)+"\n")
    if "-" in line:
        w2.write(str(line)+"\n")
w2.close()
w1.close()
op.close()
