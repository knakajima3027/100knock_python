from knock_36 import counter
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['font.family'] = 'AppleGothic'
hist = {}
for word in counter:
    if counter[word] in hist:
        hist[counter[word]] += 1
    else:
        hist[counter[word]] = 1

res = sorted(hist.items(), key=lambda x: x[0])

height = []
left = []
label = []
tmp_height = 0

for i in range(len(res)):
    tmp_height += res[i][1]
    if i%5 == 0:
        height.append(tmp_height)
        left.append(i//5)
        tmp_height = 0

plt.bar(left, height)
plt.show()
