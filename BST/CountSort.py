def CountSort(nums):

    freq_arr = [0]*100

    for num in nums:
        freq_arr[num] += 1

    result = []
    for index in range(len(freq_arr)):
        for freq in range(freq_arr[index]):
            result.append(index)

    return result
print(CountSort([4, 5,1,2, 7, 9, 8]))