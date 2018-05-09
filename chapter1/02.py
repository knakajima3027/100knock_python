str1 = 'パトカー'
str2 = 'タクシー'
str = ''

for a,b in zip(str1, str2):
    str += a + b

print(str)
