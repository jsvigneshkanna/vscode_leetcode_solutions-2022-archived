#
# @lc app=leetcode id=1313 lang=python3
#
# [1313] Decompress Run-Length Encoded List
#

# @lc code=start
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for index in range(0, len(nums), 2):
            freq = nums[index]
            val = nums[index+ 1]
            result.extend([val]* freq)

        return result
        
# @lc code=end

