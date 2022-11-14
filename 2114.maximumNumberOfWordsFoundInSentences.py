#
# @lc app=leetcode id=2114 lang=python3
#
# [2114] Maximum Number of Words Found in Sentences
#

# @lc code=start
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # Method 1 (only single space between words)
        max_words = 0
        for words in sentences:
            spaces = 0
            for word in words:
                if word == ' ':
                    spaces+=1
            max_words = max(max_words, (spaces+1))
        return max_words

        # method 2 (many space beetween words)
        # max_words = 0
        # for words in sentences:
        #     word_count = 0
        #     for index, word in enumerate(words):
        #         if word != ' ' and words[index-1] == ' ':
        #             word_count += 1
        #     max_words = max(max_words, (word_count+ 1))
        # return max_words
        
# @lc code=end

