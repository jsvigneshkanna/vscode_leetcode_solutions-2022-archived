#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_index, length = 0, len(nums)
        for index in range(length):
            if nums[index] != val:
                nums[last_index] = nums[index]
                last_index += 1
        return last_index
        
# @lc code=end

