# from heapq import *
#
# def ksmallestElements(nums, k):
#
#     maxHeap = []
#     for i in range(k):
#         heappush(maxHeap, nums[i])
#
#     for i in range(k, len(nums)):
#         if nums[i] < maxHeap[0]:
#             heappop(maxHeap)
#             heappush(nums[i])
#
#     return list(maxHeap)
#
# print(ksmallestElements([4,2,1,6,5,9,8, 3,10, 17,12,13,21], 3))
