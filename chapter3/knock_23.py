import re
from knock_20 import pick_UK

UK_text = pick_UK()
UK_text = UK_text.split('\n')

regex1 = r'^==\w*==$'
regex2 = r'===\w*===$'

pattern1 = re.compile(regex1)
pattern2 = re.compile(regex2)

for line in UK_text:
    first =  pattern1.search(line)
    second = pattern2.search(line)
    
    if first:
        print((first.group())[2:-2] + '(1)')
    if second:
        print('  ' + second.group()[3:-3] + '(2)')
