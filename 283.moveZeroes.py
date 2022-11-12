#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pointer, nonzero_pointer = 0,0
        while nonzero_pointer < len(nums):
            if nums[nonzero_pointer] != 0:
                nums[nonzero_pointer], nums[zero_pointer]= nums[zero_pointer], nums[nonzero_pointer]
                zero_pointer +=1

            nonzero_pointer += 1
        

        
# @lc code=end

 