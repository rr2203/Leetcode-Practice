# TC: O(n^3) | SC: O(n^2)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @lru_cache(maxsize=None)
        def f(l, r):
            if l>r: return 0
            coins = 0
            for i in range(l, r+1):
                coins = max(coins, nums[l-1]*nums[i]*nums[r+1] + f(l,i-1) + f(i+1, r))
            return coins

        return f(1, len(nums)-2)