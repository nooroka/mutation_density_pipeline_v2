import sys
op = open(sys.argv[1],"r")
anna2 = sys.argv[1].split("/")
anna = anna2[-1].split("_")
list1 = []
w = open(sys.argv[4],"a")
for line in op:
    numbers = ''.join(c if c.isdigit() else ' ' for c in line).split()
    if ">" in line:
       # numbers = ''.join(c if c.isdigit() else ' ' for c in line).split()
        if int(numbers[0])>=int(sys.argv[2])+1 and int(numbers[0])<=int(sys.argv[3]):#1, т.к.bed-файлы
         #print(numbers)
       # if sum(map(lambda x:x.isdigit(),line)) == int(sys.argv[4]):
        #    if int(line[:(int(sys.argv[4]))])>=int(sys.argv[2]) and int(line[:(int(sys.argv[4]))])<=int(sys.argv[3]):
                list1.append("{}".format(anna[0])+":g."+str(line))
    if "_" in line:
        if "ins" in line or "del" in line:
           #print(line,numbers)
            if int(numbers[1])>=int(sys.argv[2])+1 and int(numbers[0])<=int(sys.argv[3]):
                list1.append("{}".format(anna[0])+":g."+str(line)) #???запись
    if "_" not in line and ">" not in line:
        if "del" in line:
        #    numbers = ''.join(c if c.isdigit() else ' ' for c in line).split()
            if int(numbers[0])>=int(sys.argv[2])+1 and int(numbers[0])<=int(sys.argv[3]):
                list1.append("{}".format(anna[0])+":g."+str(line)) #???запись
            
            #print(numbers)
set1 = set(list1)
w.write(str(sys.argv[2])+"\t"+str(sys.argv[3])+"\t"+str(len(list1))+"\n")
#for symb in sorted(list(set1)):
#    w.write(str(symb))
#w.write(str(len(set1))+"\n")
w.close()
