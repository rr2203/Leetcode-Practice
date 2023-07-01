# TC: O(n) | SC: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy1 = buy2 = float('inf')
        sell1 = sell2 = 0

        for price in prices:
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)

        return sell2

# TC: O(n) | SC: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        leftToRight = [0] * n
        minPrice = prices[0]
        mp = 0
        for x in range(n):
            mp = max(mp, prices[x] - minPrice)
            leftToRight[x] = mp
            minPrice = min(minPrice, prices[x])
        
        
        rightToLeft = [0] * n
        maxPrice = prices[-1]
        mp = 0
        for x in range(n-1,-1,-1):
            mp = max(mp, maxPrice - prices[x])
            rightToLeft[x] = mp
            maxPrice = max(maxPrice, prices[x])

        mp = 0
        for x in range(n):
            profit = leftToRight[x]
            if x+1 < n: profit +=  rightToLeft[x+1]
            mp = max(mp, profit)
        
        return mp