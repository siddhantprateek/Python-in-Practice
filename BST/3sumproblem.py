
def sum3(nums):

    nums.sort()
    seen = set()
    result = []

    for i in range(len(nums) - 1, -1, -1):

        start, end = 0, i - 1
        pointerOnlast = nums[i]

        while start < end:

            s = pointerOnlast + nums[start] + nums[end]


            # s == 0
            if s == 0:
                if (pointerOnlast ,nums[start] , nums[end]) not in seen:
                    result.append([pointerOnlast ,nums[start] , nums[end]])
                    
                seen.add((pointerOnlast ,nums[start] , nums[end]))
                start += 1

            # s < 0 start += 1
            elif s < 0:
                start += 1

            # s > 0 end -= 1
            else:
                end -= 1
    return result

print(sum3([-1,0,1,2,-1,-4]))
