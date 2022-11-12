#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        actual_sum = (length * (length+1))// 2
        array_sum = 0
        for num in nums:
            array_sum += num
        return actual_sum- array_sum
        
# @lc code=end

