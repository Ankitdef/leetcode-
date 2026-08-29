class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_profit = float('inf')
        for i in prices:
            min_profit = min(min_profit, i)
            differ = i - min_profit
            max_profit = max(max_profit, differ)

        return max_profit

        

        