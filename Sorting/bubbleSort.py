

def BubbleSort(nums):

    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

nums = [4, 6, 1, 7, 2, 8, 12, 1, 1, 1, 10, 4, 4]
print("Sorted: ", BubbleSort(nums))
