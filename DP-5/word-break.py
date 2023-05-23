# Bottom Up
# TC : O(n^3) | SC: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ws = set(wordDict)

        dp = [False] * (len(s)+1)
        dp[-1] = True
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)+1):
                if s[i:j] in ws:
                    dp[i] |= dp[j] 

        return dp[0]
    
# Top Down
# TC : O(n^3) | SC: O(n)
from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ws = set(wordDict)
        
        @lru_cache(maxsize = None)
        def f(i):
            nonlocal ws, s

            if i == len(s): return True

            flag = False
            for j in range(i+1, len(s)+1):
                if s[i:j] in ws:
                    flag |= f(j)
            return flag

        return f(0)