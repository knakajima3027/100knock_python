import math

N = int(input())
count = 0
file_num = 1
text = ''

with open("hightemp.txt", "r") as file:
    Lines = file.readlines()
    file_len = len(Lines)
    split = math.ceil(file_len/N)
    for i in range(file_len):
        text += Lines[i]
        count += 1
        
        if count == split:
            count = 0
            with open("N_split_file{}".format(file_num), "w") as new_file:
                new_file.write(text)
            text = ''
            file_num += 1
        
