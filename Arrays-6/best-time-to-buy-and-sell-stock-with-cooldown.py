# TC: O(n) | SC: O(n)
# Note: both buy[i] and sell[i] are considered as profits and we're trying to maximize them.
# buy[i] - the maximum profit that can be gained if a buy operation is carried out on day i. If you decide to buy on day i, you can't sell on day i - 1, so the maximum profit would be sell[i - 2] - prices[i] (profit from day i - 2 and the cost to buy on day i). However, if buying today leads to less profit than the maximum profit gained so far, you won't buy, so buy[i] is the maximum of these two.
# sell[i] - the maximum profit that can be gained if a sell operation is carried out on day i. If you decide to sell on day i, the profit would be buy[i - 1] + prices[i] (profit from buying on day i - 1 and the gain from selling on day i). But if selling today results in less profit than the maximum profit so far, you won't sell, so sell[i] is the maximum of these two.
class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) <= 1:
            return 0

        buy = [0]*len(prices)
        sell = [0]*len(prices)

        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(sell[0], buy[0] + prices[1])

        for i in range(2, len(prices)):
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

        return sell[-1]

# TC: O(n) | SC: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(maxsize=None)
        def f(i, isHoldingStock):
            if i >= len(prices): return 0
            mp = 0
            # do nothing
            mp = max(mp, f(i+1, isHoldingStock))
            # buy
            if not isHoldingStock:
                mp = max(mp, -prices[i] + f(i+1, 1))
            # sell
            if isHoldingStock:
                mp = max(mp, prices[i] + f(i+2, 0))

            return mp

        return f(0, 0)