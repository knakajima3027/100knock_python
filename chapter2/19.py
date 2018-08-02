pref_dict = {}
first_str = []
with open("hightemp.txt", "r") as file:
    Lines = file.readlines()
    for line in Lines:
        word = line.split("\t")
        first_str.append(word[0])
        
    unique_str = set(first_str)
    for prefecture in unique_str:
        pref_dict.setdefault(prefecture, first_str.count(prefecture))
    pref_dict = sorted(pref_dict.items(), key=lambda x: x[1], reverse = True)

    for i in range(len(pref_dict)):
        print(pref_dict[i][0])
    
