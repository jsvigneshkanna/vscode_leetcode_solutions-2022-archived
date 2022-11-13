#
# @lc app=leetcode id=2011 lang=python3
#
# [2011] Final Value of Variable After Performing Operations
#

# @lc code=start
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operation_map = {
            '++X': 1, 'X++': 1, '--X': -1, 'X--': -1,
        }
        result = 0
        for operation in operations:
            result += operation_map.get(operation)
        return result
        
# @lc code=end

