def arraySum(nums, first=[], second=[], index = 0,fsum = 0, ssum=0):
    if len(nums) == index:
        if fsum == ssum:
            print(first, second)
        return
    first.append(nums[index])
    arraySum(nums, first, second, index + 1, fsum+nums[index], ssum)
    first.pop()
    second.append(nums[index])
    arraySum(nums, first, second, index + 1, fsum,ssum+nums[index])
    second.pop()

arraySum([1, 2, 3, 3, 1, 2])