class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = inf
        maxProfit = -inf

        for price in prices:
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(minPrice, price)

        return maxProfit if maxProfit > 0 else 0
