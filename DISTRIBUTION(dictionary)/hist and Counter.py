from collections import Counter
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 4, 6]
hist = {}
for x in t:
    hist[x] = hist.get(x, 0) + 1
print(hist)
counter = Counter(t)
print(counter)
