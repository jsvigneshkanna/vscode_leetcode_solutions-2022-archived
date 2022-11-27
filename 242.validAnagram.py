#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_set = {}
        if len(s) != len(t):
            return False
        for index in range(len(s)):
            alpha_set[s[index]] = alpha_set.get(s[index], 0)+ 1
            alpha_set[t[index]] = alpha_set.get(t[index], 0)- 1
        
        for alpha, alpha_value in alpha_set.items():
            if alpha_value != 0:
                return False
        
        return True

        
# @lc code=end

