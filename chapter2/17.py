first_str = []
with open("hightemp.txt", "r") as file:
    Lines = file.readlines()
    for line in Lines:
        word = line.split("\t")
        first_str.append(word[0])
        
print(set(first_str))
