import MeCab
import collections
import matplotlib.pyplot as plt
from pprint import pprint 


word_list = []
tagger = MeCab.Tagger("-Owakati")

with open('neko.txt') as neko_text:
    text = neko_text.readline()
    while text:
        str_output = tagger.parse(text)
        str_output = str_output[:-2]
        if str_output != '':
            word_list += str_output.split(' ')
        text = neko_text.readline()

counter = collections.Counter(word_list)

height = []
left = []
label = []

for i in range(10):
    left.append(i+1)
    height.append(counter.most_common()[i][1])
    label.append(counter.most_common()[i][0])
    
plt.bar(left, height, tick_label=label)
plt.show()
