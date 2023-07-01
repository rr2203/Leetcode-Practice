# Reinvestment Tricks
# TC: O(n*k) | SC: O(k)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buys = [float('inf')] * k
        sells = [0] * k

        for price in prices:
            for j in range(k):
                curBuy = price if j == 0 else price - sells[j-1]
                buys[j] = min(buys[j], curBuy)
                sells[j] = max(sells[j], price - buys[j])

        return sells[-1]

# DP Solution
# TC: O(n*k) | SC: O(n*k)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @lru_cache(maxsize = None)
        def f(i, k, isHoldingStock):
            if i == len(prices) or k == 0: return 0
            # ignore
            mp = f(i+1, k, isHoldingStock)
            # buy
            if not isHoldingStock:
                mp = max(mp, -prices[i] + f(i+1, k, 1))
            # sell
            if isHoldingStock:
                mp = max(mp, prices[i] + f(i+1, k-1, 0))
            return mp


        return f(0, k, 0)