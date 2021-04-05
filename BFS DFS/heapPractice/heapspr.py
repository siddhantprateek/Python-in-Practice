
from heapq import *


def topK(nums, k):


    minHeap = []
    print(nums)
    for i in range(k):
        heappush(minHeap, nums[i])
    print(minHeap)

    for i in range(k, len(nums)):
        curr = nums[i]
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])

    return list(minHeap)

print(topK([4,2,1,6,5,9,8, 11,10, 17,12,13,21], 3))
