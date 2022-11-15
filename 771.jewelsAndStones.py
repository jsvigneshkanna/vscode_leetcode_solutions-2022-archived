#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #  Method 1 (hashmap)
        jewel_stone_count = {}
        for jewel in jewels:
            jewel_stone_count[jewel] = jewel_stone_count.get(jewel, 0)+ 1
        
        proper_stone_count = 0
        for stone in stones:
            if stone in jewel_stone_count:
                proper_stone_count += jewel_stone_count[stone]
        return proper_stone_count

        
# @lc code=end

