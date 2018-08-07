import re
from knock_20 import pick_UK

UK_text = pick_UK()

def cut_mark(mark_dict): #強調をカット
    regex = r'\'{2,5}'
    pattern = re.compile(regex)
    for key in mark_dict.keys():
        mark_dict[key] = pattern.sub('', mark_dict[key])
    return mark_dict

regex1 = r'''\{\{基礎情報.*?$
             (.*?)
             ^\}\}$'''
pattern1 = re.compile(regex1, re.MULTILINE + re.VERBOSE + re.DOTALL)
lines1 = pattern1.findall(UK_text)

regex2 = r'\|(.*?)\s*=\s*(.*)'
pattern2 = re.compile(regex2)
lines2 = pattern2.findall(lines1[0])


uk_dict = {}
for line in lines2:
    uk_dict[line[0]] = line[1]
    
print(cut_mark(uk_dict))
