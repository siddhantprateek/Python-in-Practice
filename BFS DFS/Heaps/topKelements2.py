def firstK(nums, k):
    minHeap = []
    for i in range(k):
        minHeap.append(nums[i])

    for i in range(k, len(nums)):
        minHeap.sort()

        # if minHeap[0] > nums[i]:
        #     continue
        # else:
        #     minHeap.pop(0)
        #     minHeap.append(nums[i])


        if nums[i] > minHeap[0]:
            minHeap.pop(0)
            minHeap.append(nums[i])
    return minHeap

print(firstK([4, 2, 1, 11, 10, 17, 12, 21], 3))
