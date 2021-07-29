def CountSort(nums):

    freqOf = [0]*100

    for num in nums:
        freqOf[num] += 1
    print(freqOf)
    result = []
    # O(n) time
    for num in range(len(freqOf)):
        for freq in range(freqOf[num]):
            result.append(num)

    return result
nums = [4, 6, 1, 7, 2, 8, 12, 1, 1, 1, 10, 4, 4]
print("Sorted: ",CountSort(nums))
