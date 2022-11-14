#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Method 1
        occurence = {}
        pairs = 0
        for num in nums:
            pairs += occurence.get(num, 0)
            occurence[num] = occurence.get(num, 0) + 1
        return pairs
        
# @lc code=end

