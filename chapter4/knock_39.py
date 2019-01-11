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

res = sorted(hist.items(), key=lambda x: x[1], reverse=True)

height = []
left = []
label = []
tmp_height = 0

for i in range(len(res)):
    height.append(res[i][1])
    left.append(i)

plt.plot(left, height)
ax = plt.gca()
ax.set_yscale('log')
plt.xlabel('単語出現頻度順')
plt.ylabel('頻度')
plt.grid(which="both")
plt.show()
