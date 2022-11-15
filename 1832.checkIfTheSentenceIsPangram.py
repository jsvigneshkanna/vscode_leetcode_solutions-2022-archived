#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Method 1 (hashmap)

        # hashmap = [0] * 26
        # for alpha in sentence:
        #     hashmap[ord(alpha)- ord('a')] += 1
        
        # for alpha in hashmap:
        #     if alpha == 0:
        #         return False

        # return True

        # Method 2
        sentence_set = set(sentence)
        return len(sentence_set) == 26
        
# @lc code=end

