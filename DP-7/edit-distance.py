# TC: O(m*n) | SC: O(m*n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        dp = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]
        dp[-1][-1] = 0

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m:  dp[i][j] = n-j
                elif j == n:    dp[i][j] = m-i
                elif word1[i] != word2[j]:    dp[i][j] = 1+min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                else: dp[i][j] = dp[i+1][j+1]

        return dp[0][0]
