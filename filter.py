import sys
#for i in range(1,25,1)
op = open(sys.argv[1],"r")
w = open(sys.argv[2],"w")
for line in op:
        line22 = line.strip()
        line22 = line22.split()
        print(line22)
        if str(line22[0][3:])== str(sys.argv[3]):
            w.write(str(line))
w.close()
op.close()

