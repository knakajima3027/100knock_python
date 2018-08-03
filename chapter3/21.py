import json
import re
"""正規表現"""
pattern = re.compile(r'''
    ^   # 行の初め
    (   # グループ開始
    .*  # 任意の文字0文字以上
    \[\[Category:
    .*  # 任意の文字0文字以上
    \]\]
    .*  # 任意の文字0文字以上
    )   # グループ終了
    $   # 行の終わり
    ''', re.MULTILINE + re.VERBOSE)

with open("jawiki-country.json", "r") as file:
    line = file.readline() 
    while line:
        json_dict = json.loads(line)
        if json_dict['title'] == 'イギリス':
            print(pattern.findall(json_dict['text']))
        line = file.readline()
        
