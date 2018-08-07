import re
from knock_20 import pick_UK

'''メモ
re.MULTILINE 行毎にマッチさせる
re.VERBOSE　正規表現の途中にコメントを入れられる
re.DOTALL　. を改行にもマッチさせる
'''
UK_text = pick_UK()

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
    
print(uk_dict)
