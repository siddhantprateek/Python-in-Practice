

a = [2, 1, 5, 1, 3, 2]
k = 3
maximum = 0
for i in range(len(a) - k):
    maximum = max(maximum, a[i:i+k])

print(maximum)
