#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # Method 1 additional space

        # length = len(nums)
        # permutation_arr  = [0]* length
        # for index in range(length):
        #     permutation_arr[index] = nums[nums[index]]
        # return permutation_arr

        # Method 2 (optimal space)
        max_weight = 1001
        length = len(nums)
        for index in range(length):
            nums[index] = nums[index] + (max_weight* (nums[nums[index]] % max_weight))
            print(nums[index])
            
        for index in range(length):
            nums[index] = nums[index] // max_weight
        
        return nums
        
# @lc code=end

