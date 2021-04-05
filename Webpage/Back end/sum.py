class Solution:
    def twoSum(self, target, nums=[]):
        index = []
        self.nums = nums
        self.target = target
        self.index = index
        input(self.nums)
        input(self.target)

        for x, j in self.nums:
            if self.target == self.nums[x] + self.nums[j]:
                return self.index == x, j
            j+1
        print(self.index)


output = Solution()
nums = [2, 7, 4, 5]
print(nums)
target = input("target:")
output.twoSum(target, nums)
print(output.index)
