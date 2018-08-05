from knock_20 import pick_UK

UK_text = pick_UK()
UK_text = UK_text.split('\n')

for line in UK_text:
    if 'Category' in line:
        print(line)
