str = 'Now I need a drink, alocoholc of course, after the heavy lectures involving quantum mechanics.'
words = str.split()
result = []
count = 0
for word in words:
    count = 0
    for char in word:
        if char.isalpha():
            count += 1

    result.append(count)



print(result)
