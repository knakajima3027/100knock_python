N = input()
N = int(N)
count1 = 0
count2 = 0
with open('hightemp.txt') as input_file:
    for line in input_file:
        count1 += 1

with open('hightemp.txt') as input_file:
    for line in input_file:
        if  count2 >= count1 - N:
            print(line)
        count2 += 1
