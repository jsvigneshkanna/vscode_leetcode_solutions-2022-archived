 #
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = 0
        for candy in candies:
            max_candy = max(max_candy, candy)
        
        length = len(candies)
        for index in range(length):
            candies[index] = True if (candies[index]+extraCandies>= max_candy) else False

        return candies
        
# @lc code=end

