class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        boughtAt = prices[0]
        for price in prices[1:]:
            if price > boughtAt:
                profit += price - boughtAt
            boughtAt = price

        return profit
