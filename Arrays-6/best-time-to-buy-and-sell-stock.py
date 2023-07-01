# TC: O(n) | SC: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        ans = 0
        for price in prices[1:]:
            ans = max(ans, price - minPrice)
            minPrice = min(minPrice, price)
        return ans