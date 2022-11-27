#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        first_space = False
        last_length = 0
        for index in range(len(s)-1, -1, -1):
            if (s[index] == ' ' and not first_space):
                continue
            elif (s[index] != ' '):
                last_length += 1
                first_space = True
            elif (s[index] == ' ' and first_space):
                return last_length
        
        return last_length
        
# @lc code=end

