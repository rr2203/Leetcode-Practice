#TC: O(n)
#SC: O(n)
class Solution:
    def countArrangement(self, n: int) -> int:

        def backtrack(i):
            nonlocal n,vis
            if i == n+1:
                return 1

            count = 0
            for j in range(1,n+1):
                if vis[j]!=True and (i%j==0 or j%i==0):
                    vis[j] = True
                    count += backtrack(i+1)
                    vis[j] = False
            return count

        vis = [False]*(n+1)
        return backtrack(1)