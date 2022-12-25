#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for str_word in strs:
            sorted_str = str(sorted(str_word))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(str_word)
            else:
                hashmap[sorted_str] = [str_word]
        
        result = []
        for value in hashmap.values():
            result.append(value)
        return result
        
        '''
        result = []
        mappings = collections.defaultdict(list)
        for value in strs:
            count = [0]*26
            for chars in value:
                count[ord(chars) - ord('a')] += 1
            mappings[tuple(count)].append(value)

        for value in mappings:
            result.append(mappings[value])
        return result
        '''
# @lc code=end

