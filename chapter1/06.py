target1 = "paraparaparadise"
target2 = "paragraph"

def n_gram(arg, n): #入力された文書の文字nグラムを生成
    result = []
    for i in range(len(arg)-n+1):
        result.append(arg[i:i+n])
    return result

X = n_gram(target1, 2)
Y = n_gram(target2, 2)

print(X)
print(Y)

wa = set(X) | set(Y)
seki = set(X).intersection(set(Y))
sa =  set(X) - set(Y)

print(sa, wa, seki)

print('se' in X)
print('se' in Y)
