#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == len(t):
            return s == t
        if len(s) == 0:
            return True
        
        length = len(t)
        s_index, s_len = 0, len(s)
        for index in range(length):
            if s_index < len(s) and s[s_index] == t[index]:
                s_index += 1
            
        return s_index == s_len
        
# @lc code=end

