f = open('hightemp.txt')
count = 0
for line in f.readlines():
    count = count + 1

print(count)
