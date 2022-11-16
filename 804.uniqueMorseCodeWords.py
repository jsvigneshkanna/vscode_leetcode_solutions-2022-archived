#
# @lc app=leetcode id=804 lang=python3
#
# [804] Unique Morse Code Words
#

# @lc code=start
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Method 1 (hashmap and sets)
        morse_code_map = {
            'a': ".-",
            'b':"-...",
            'c':"-.-.",
            'd':"-..",
            'e':".",
            'f':"..-.",
            'g':"--.",
            'h':"....",
            'i':"..",
            'j':".---",
            'k':"-.-",
            'l':".-..",
            'm':"--",
            'n':"-.",
            'o':"---",
            'p':".--.",
            'q':"--.-",
            'r':".-.",
            's':"...",
            't':"-",
            'u':"..-",
            'v':"...-",
            'w':".--",
            'x':"-..-",
            'y':"-.--",
            'z':"--..",
        }
        result = set()
        for word in words:
            morse_word = ''
            for alpha in word:
                morse_word += morse_code_map[alpha]
            result.add(morse_word)
        return len(result)
        
# @lc code=end

