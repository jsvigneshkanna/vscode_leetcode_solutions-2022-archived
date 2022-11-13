#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0]* (2*length)
        for index, num in enumerate(nums):
            result[index], result[index+length] = num, num
        return result

        # Method 2
        # return nums * 2

        # Method 3
        # nums.extend(nums)
        # return nums


        
# @lc code=end

