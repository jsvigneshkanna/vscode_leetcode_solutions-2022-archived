#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = arr[-1]
        for index in range(len(arr)-1, -1, -1):
            if index == len(arr)-1:
                right_max = max(right_max, arr[index])
                arr[index] = -1
            else:
                temp = arr[index]
                arr[index] = right_max
                right_max = max(right_max, temp)
            
        return arr
        
# @lc code=end

