class Solution:
    #     def canJump(self, nums: List[int]) -> bool:
        
#         jump_length = 0
#         while jump_length < len(nums) -1:
#             if nums[jump_length] == nums[len(nums) - 1]:
#                 return True
#             jump_length += nums[jump_length] 
        
#         return False
    
    def canJump(self, nums: List[int]) -> bool:
        
        # jump_length = 0
        maximum = 0
        last_index = len(nums) - 1
        for jump in range(len(nums)):
            
            value = nums[jump]
            maximum = max(maximum, jump + value)
            
            if maximum == jump:
                break
        return maximum >= last_index
    
    
    