import re
from knock_20 import pick_UK

UK_text = pick_UK()

regex1 = r'(?:File|ファイル):(.+?)\|'
pattern1 = re.compile(regex1)
lines = pattern1.findall(UK_text)

for line in lines:
    print(line)
       
