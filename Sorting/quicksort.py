

def Quicksort(nums: list[int], start, end):


    div = partition(nums, start, end)

    Quicksort(nums, start, div - 1)
    Quicksort(nums, div + 1, end)

    return nums

def partition(nums, start, end):


    pivot = nums[end]
    i = start - 1
    for j in range(start, end - 1):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[end] = nums[end], nums[i + 1]
    return i + 1


nums = [4, 6, 1, 7, 2, 8, 12]
low, high = 0, len(nums) - 1
print(Quicksort(nums, low, high))
