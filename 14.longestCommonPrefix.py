#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]
        for index in range(1, len(strs)):
            while len(longest_prefix)>0:
                if not strs[index].startswith(longest_prefix):
                    longest_prefix = longest_prefix[:-1]
                else:
                    break
        return longest_prefix
        
# @lc code=end

