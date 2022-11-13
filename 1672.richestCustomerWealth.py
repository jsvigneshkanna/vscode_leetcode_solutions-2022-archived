#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth, rows, cols = 0, len(accounts), len(accounts[0])
        for row in range(rows):
            wealth = 0
            for col in range(cols):
                wealth += accounts[row][col]

            max_wealth = max(max_wealth, wealth)
        return max_wealth

        
# @lc code=end

