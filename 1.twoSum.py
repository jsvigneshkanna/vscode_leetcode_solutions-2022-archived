#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
# submission=12/11/22

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            if target-num in hashmap:
                return [index, hashmap.get((target-num))]
            else:
                hashmap[num] = index
        return [-1, -1]
        
        
# @lc code=end

