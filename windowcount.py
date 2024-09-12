for i in range(1,24,1):
    op = open("quadr738_{}.geecee".format(i))
    for line in op:
        line = line.strip()
        line = line.split()
        if "#Sequence" not in line:
            
