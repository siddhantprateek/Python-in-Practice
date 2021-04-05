def ArrSum(nums, index = 0,first = [], second = [], result = [],fsum = 0, ssum = 0):

    if index == len(nums):
        if fsum == ssum:
           print(first, second)
           if first not in result or second not in result:
               result.append(first)
               result.append(second)
        return 
    
    first.append(nums[index])
    ArrSum(nums, index + 1, first, second, result, fsum + nums[index], ssum)
    first.pop()

    second.append(nums[index])
    ArrSum(nums, index + 1, first, second, result, fsum, ssum + nums[index])
    second.pop()
ans = ArrSum([1, 2, 4, 2, 4, 1])
print(ans)
