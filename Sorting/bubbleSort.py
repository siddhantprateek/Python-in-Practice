

def BubbleSort(nums):

    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums

nums = [4, 6, 1, 7, 2, 8, 12, 1, 1, 1, 10, 4, 4]
# print("Sorted: ", BubbleSort(nums))

# O(n)
def BubbleSortModified(nums):

    for i in range(len(nums)):
        swapped = False

        for j in range(0, len(nums) - i - 1):

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if swapped == False:
            break

    return nums

print(BubbleSortModified(nums))
