import re
from knock_20 import pick_UK

"""メモ
(?: キャプチャ対象外にする
"""

UK_text = pick_UK()

def cut_mark(mark_dict): #強調をカット
    regex = r'\'{2,5}'
    pattern = re.compile(regex)
    for key in mark_dict.keys():
        mark_dict[key] = pattern.sub('', mark_dict[key])
    return mark_dict

def cut_url_mark(mark_dict): #urlをカット
    regex = r'''
            \[\[
            (?:
                [^|]*?
                \|
            )?
            ([^|]*?)
            \]\]
            '''
    pattern = re.compile(regex, re.VERBOSE)
    for key in mark_dict.keys():
        mark_dict[key] = pattern.sub(r'\1', mark_dict[key])
    return mark_dict

def cut_media(mark_dict):
    regex = r'''(\<(.*)\>)
                |
                ({{.*\|(?:.*)?}})
                |
                (\[\[ファイル:(?:.*)?.*)
            '''
    pattern = re.compile(regex, re.VERBOSE)
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

result1 = cut_mark(uk_dict)
result2 = cut_url_mark(result1)
result3 = cut_media(result2)

print(result3)


