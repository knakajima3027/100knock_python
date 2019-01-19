import re

file = open('nlp.txt', 'r') 
string = file.read()      
 
result = re.split('(\.|\;|\:)\s', string)

file.close()

text = [result[0]]
for i in range(1, len(result)):
    if result[i][0].isupper():
        text.append(result[i])
    else:
        text[-1] += result[i]
        
for sentence in text:
    print(sentence)
