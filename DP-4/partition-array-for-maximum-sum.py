# TC: O(n*k) , SC: O(n)
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0]*len(arr)
        for i in range(len(arr)):
            curMax = arr[i]
            for j in range(i, max(i-k, -1), -1):
                curMax = max(curMax, arr[j])
                curSum = curMax * (i-j+1)
                if j-1>=0: curSum += dp[j-1]
                dp[i] = max(dp[i], curSum)

        return dp[-1]