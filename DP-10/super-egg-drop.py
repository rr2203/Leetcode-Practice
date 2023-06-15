# We basically modelled the problem differently than usual such that we didn't need to worry about "which floor exactly" unlike the original dp[i][j] definition as "number of moves", instead we considered the number of floors
# TC: O(nk)
# SC: O(nk)
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,k+1):
                dp[i][j] = 1 + dp[i-1][j-1] + dp[i-1][j]
                if dp[i][j] >= n: return i

        return -1

# Here we just optimized memoized recursion by using binary search to find the optimal floor to drop the egg
# TC: O((n * k) * logn ) | SC: O(nk)
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        
        @lru_cache(maxsize=None)
        def find(k: int, n: int) -> int:
            if n == 0 or n == 1:    return n
            if k == 1:  return n
            
            minMoves = float('inf')
            l, h = 1, n
            while l <= h:
                mid = (l + h) // 2
                left = find(k - 1, mid - 1)
                right = find(k, n - mid)     
                if left < right: l = mid + 1
                else: h = mid - 1
                minMoves = min(minMoves, 1 + max(left, right))         

            return minMoves
        
        return find(K, N)