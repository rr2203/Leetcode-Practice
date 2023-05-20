# Optimized by using 1D array
# TC: O(m*n) , SC: O(n)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)
        maxLen = 0
        prev = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                    maxLen = max(maxLen, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return maxLen ** 2


# TC: O(m*n) , SC: O(m*n)
# 2D Dynamic Programming
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        maxLen = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    maxLen = max(maxLen, dp[i][j])

        return maxLen ** 2

