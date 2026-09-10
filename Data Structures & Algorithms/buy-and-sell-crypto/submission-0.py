class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while l < r and r < len(prices):
            price = prices[r] - prices[l]
            if price < 0:
                l = r
                r += 1
            else:
                res = max(res, price)
                r += 1
        return res