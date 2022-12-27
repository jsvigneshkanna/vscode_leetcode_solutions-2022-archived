#
# @lc app=leetcode id=1389 lang=python3
#
# [1389] Create Target Array in the Given Order
#

# @lc code=start
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        current = 0
        for ind in index:
            result.insert(ind, nums[current])
            current += 1
        return result
        
# @lc code=end

