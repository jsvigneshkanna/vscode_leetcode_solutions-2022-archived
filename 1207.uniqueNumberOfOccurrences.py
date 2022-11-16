#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Method 1 (hashmap)
        occurence = {}
        for num in arr:
            occurence[num] = occurence.get(num, 0)+ 1
        count = set()
        for occu in occurence:
            if occurence[occu] in count:
                return False
            count.add(occurence[occu])
        return True
        
# @lc code=end

