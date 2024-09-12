import subprocess
w = open("mutdensgeneall.txt","a")
for i in range(1,25,1):
    d5 = subprocess.check_output("wc -l gccoords_all_genes{}_un.bed".format(i),shell = True)   
    d1 = subprocess.check_output('wc -l mutcosall{}.bed'.format(i),shell = True)#штуки мутаций
    d55 = d5.decode().split()[0]
    d11 = d1.decode().split()[0]
    sum1 = int(d55)*52
    w.write("chr{}".format(i)+"\t"+str(float(int(d11)/int(sum1)))+"\n")
w.close()
