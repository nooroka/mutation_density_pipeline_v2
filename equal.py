for i in range(24,25,1):
    w = open("gccoords_percents_{}_my_39_subtract_from_all_filtered_loop5.txt".format(i),"w")
    with open("gccoordsmax/max_all_39_{}_gc_loop5_matched.txt".format(i)) as f:
        my_file = f.readlines()
        #print(my_file)
    with open("gccoords_percents_{}_my_39_subtract_from_all_loop5.txt".format(i)) as f2:
        my_file2 = f2.readlines()
        #print(my_file2)
    set_my_file = set(my_file)
    set_my_file2 = set(my_file2)
    set3 = set_my_file2.difference(my_file)
    for line in set3:
        w.write(line)
    w.close()



