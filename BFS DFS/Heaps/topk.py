from heapq import *
def topK(nums, k):

    minHeap = []
    for i in range(k):
        heappush(minHeap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            # removes the smallest element in the minheap
            heappop(minHeap)
            # adds on the next element in the array simultaneously
            heappush(minHeap, nums[i])
    return list(minHeap)


print(topK([1, 3, 8, 9, 4, 6], 3))
