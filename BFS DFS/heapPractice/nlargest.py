from heapq import *

def nlarge(nums, n):
    return nlargest(n, nums)

print(nlarge([4,2,1,6,5,9,8, 11,10, 17,12,13,21], 3))
