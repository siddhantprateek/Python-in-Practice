from heapq import *

def HeapSort(nums):

    minHeap = []

    for item in nums:
        heappush(minHeap, item)

    result = []
    while minHeap:
        popped = heappop(minHeap)
        result.append(popped)

    return result

# Overall Time complexity is : O(NlogN)
def HeapSort2(nums):

    heapify(nums) # time complexity to heapify is O(logN)
    result = []

    while nums:
        # for N element to pop in heap it takes O(NlogN)
        popped = heappop(nums)
        result.append(popped)
    return result

nums = [4, 6, 1, 7, 2, 8, 12]
print(HeapSort2(nums))
