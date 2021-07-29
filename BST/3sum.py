class Solution:
    def threeSum(self, nums):
        return print(self.usingSortingAndTwoPointer(nums))

    def usingSortingAndTwoPointer(self, nums):
        nums.sort()
        added = set()
        out = []

        for i in range(len(nums) - 1, -1, -1):
            last = nums[i]
            start, end = 0, i - 1

            while start < end:
                s = last + nums[start] + nums[end]

                if s == 0:
                    if (last, nums[start], nums[end]) not in added:
                        out.append([last, nums[start], nums[end]])

                    # for having unique set of numbers and not repeatation of same set
                    added.add((last, nums[start], nums[end]))
                    start += 1

                elif s > 0:
                    end -= 1
                else:
                    start += 1

        return out

sol = Solution().threeSum([-1,0,1,2,-1,-4])
