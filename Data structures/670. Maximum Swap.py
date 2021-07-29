# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
# Return the maximum valued number you could get.

class Solution:
    def maximumSwap(self, num: int):
        self.num = num
        m = str(self.num)


ret = Solution().maximumSwap(452)
