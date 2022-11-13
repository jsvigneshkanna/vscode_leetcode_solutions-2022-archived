#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Method 1
        length = len(nums)
        if length <=1:
            return num
        for index in range(1, length):
            nums[index] = nums[index] + nums[index-1]
        return nums



# @lc code=end

