str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
words = str.split()
list = [0, 4, 5, 6, 7, 8, 14, 15, 18]
key = []
count = 0
for word in words:
    if count in list:
        key.append(word[0])
    else:
        key.append(word[0] + word[1])

    count += 1

print(key)
