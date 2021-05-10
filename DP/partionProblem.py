def SubSetSum(nums, index, sum):

    if sum == 0:
        return True

    if index < 0 or sum < 0:
        return False


    include = SubSetSum(nums, index - 1, sum - nums[index])
    if include:
        return True

    exclude = SubSetSum(nums, index - 1, sum)

    return exclude


def partition(nums):
    total = sum(nums)
    # the no. is even or odd is determined by its LSB
    # if no. is positive or negative is determined be MSB
    # (total & 1) == 0 checks whether the number is even or not
    return (total & 1) == 0 and SubSetSum(nums, len(nums) - 1, total//2)

nums = [7, 3, 1, 5, 4, 8]
print(partition(nums))
