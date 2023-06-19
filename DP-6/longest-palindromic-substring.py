# TC: O(n^2) , SC: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        bestX = bestY = 0
        
        for L in range(n):
            for i in range(n - L):
                j = i + L
                if L < 2:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
                
                if dp[i][j] and (j - i + 1) > (bestY-bestX+1):
                    bestX,bestY = i,j
        return s[bestX:bestY+1]

# TC: O(n^2) , SC: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0
        for i in range(len(s)):

            # odd
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > reslen:
                    reslen = r-l+1
                    res = s[l : r+1]
                l-=1
                r+=1

            # even
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1 > reslen:
                    reslen = r-l+1
                    res = s[l : r+1]
                l-=1
                r+=1

        return res