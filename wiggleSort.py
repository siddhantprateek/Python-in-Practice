class Solution:
    def wiggleSort(self, nums):

        freqOf = [0 for _ in range(5001)]

        for num in nums:
            freqOf[num] += 1

        odd, even = 1, 0
        for num in range(5000, -1, -1):
            if odd > len(nums) and even > len(nums):
                break

            if freqOf[num] == 0:
                continue

            while freqOf[num] and (odd < len(nums) or even < len(nums)):
                freqOf[num] -= 1
                if odd < len(nums):
                    nums[odd] = num
                    odd += 2
                else:
                    nums[even] = num
                    even += 2
