#
# @lc app=leetcode id=2103 lang=python3
#
# [2103] Rings and Rods
#

# @lc code=start
class Solution:
    def countPoints(self, rings: str) -> int:
        # Method 1 (hashmap)
        # index = 0
        rings_rods = {}
        for index in range(0, len(rings), 2):
            if rings[index+1] not in rings_rods:
                rings_rods[rings[index+1]] = set()
                rings_rods[rings[index+1]].add(rings[index])
            else:
                rings_rods[rings[index+1]].add(rings[index])
        
        three_rings_rod = 0
        for rods, rings in rings_rods.items():
            print(rings)
            if len(rings) == 3:
                three_rings_rod += 1
        
        return three_rings_rod
        
# @lc code=end

