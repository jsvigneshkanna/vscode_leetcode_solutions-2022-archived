#
# @lc app=leetcode id=1941 lang=python3
#
# [1941] Check if All Characters Have Equal Number of Occurrences
#

# @lc code=start
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        alphabet_map = {}
        for alpha in s:
            alphabet_map[alpha] = alphabet_map.get(alpha, 0)+ 1
        count = alphabet_map[s[0]]
        for alpha in alphabet_map:
            if count != alphabet_map[alpha]:
                return False

        return True
        
# @lc code=end

