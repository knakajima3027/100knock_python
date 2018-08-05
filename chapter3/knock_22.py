import re
from knock_20 import pick_UK

UK_text = pick_UK()
UK_text = UK_text.split('\n')

regex1 = r'(\[\[Category:)'
regex2 = r'(\]\])|\|'

pattern1 = re.compile(regex1)
pattern2 = re.compile(regex2)

for line in UK_text:
    start =  pattern1.search(line)
    end = pattern2.search(line)
    
    if start:
        s = (start.span())[1]
        t = (end.span())[0]
        print(line[s:t])
