class Solution:
    def balanced_bracket(self, string):
        count = 0
        for char in string:
            if char == "(":
                count += 1
            if char == ")":
                count -= 1
                if count < 0:
                    return False
        return count == 0

sol = Solution().balanced_bracket("()()")
print(sol)