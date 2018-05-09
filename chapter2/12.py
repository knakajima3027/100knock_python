
with open('hightemp.txt') as input_file,\
    open('col1.txt', 'a') as col1_file,\
    open('col2.txt', 'a') as col2_file:

    for line in input_file:
        split_file = line.split('\t')
        col1_file.write(split_file[0] + '\n')
        col2_file.write(split_file[1] + '\n')

#答え合わせ cut -f 1,2 hightemp.txt
