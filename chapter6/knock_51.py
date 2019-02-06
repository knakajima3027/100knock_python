import re

file = open('nlp.txt', 'r')  #読み込みモードでオープン
string = file.read()      #readですべて読み込む
 
result = re.split('(\.|\;|\:)\s', string)

file.close()

text = [result[0]]
for i in range(1, len(result)):
    if result[i][0].isupper():
        text.append(result[i])
    else:
        text[-1] += result[i]


words = []
for sentence in text:
    sentence = sentence.replace(",", "")
    sentence = sentence.replace(".", "")
    words += sentence.split(" ")
        
for word in words:
    print(word)
