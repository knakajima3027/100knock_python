str = 'I am an NLPer'

def n_gram(arg, n): #入力された文書の文字nグラムを生成
    result = []
    for i in range(len(arg)-n+1):
        result.append(arg[i:i+n])
    return result

x = n_gram(str, 2)
print(x)

word = str.split(' ')
y = n_gram(word, 2)
print(y)
