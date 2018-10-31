import MeCab
import collections
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
pprint(counter.most_common())
