# Best Time to Buy and Sell Stock (LC 121)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minprice = prices[0]
        profit = 0
        for i, price in enumerate(prices):
            if price < minprice:
                minprice = price
            elif price - minprice > profit:
                profit = price - minprice 
        return profit


prices = [7,1,5,3,6,4]
sol = Solution()
sol.maxProfit(prices)