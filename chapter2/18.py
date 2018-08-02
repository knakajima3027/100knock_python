cul_temp = {}
with open("hightemp.txt", "r") as file:
    Lines = file.readlines()
    for line in Lines:
        cul = line.split("\t")
        cul_temp.setdefault(line, float(cul[2]))
    sorted_line = sorted(cul_temp.items(), key=lambda x: x[1], reverse = True)

with open("sorted_temp.txt", "w") as result:
    for i in range(len(sorted_line)):
        result.write(sorted_line[i][0])
