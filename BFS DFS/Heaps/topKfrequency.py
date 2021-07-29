from heapq import *

def topKfreq(nums, k):

    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    minHeap = []
    print("(frequnecy, num)")
    for num, frequnecy in freq.items():

        """
        # we passing a tuple into the min heap
        # basically minHeap is storing the max elements in it
        """
        heappush(minHeap, (frequnecy, num))
        print("itr: ",minHeap)

        if len(minHeap) > k:
            heappop(minHeap)

    print(minHeap)
    ans = []
    while minHeap:
        """
        # heappop(minHeap)[1] is the num
        # the index 1 from each is popped
        """
        ans.append(heappop(minHeap)[1])
    return ans

print(topKfreq([1, 2, 2, 5, 6, 8, 8, 8, 10], 2))
