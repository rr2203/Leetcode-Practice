# TC: O(m*n) | SC: O(m*n)
from functools import lru_cache
class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:

        @lru_cache(maxsize=None)
        def dfs(t, p):
            if p == len(pattern): return t == len(text)

            isMatch = t < len(text) and (text[t] == pattern[p] or pattern[p] == '.')
            if p+1 < len(pattern) and pattern[p+1] == '*':
                return dfs(t, p+2) or (isMatch and dfs(t+1, p))
            elif isMatch:
                return dfs(t+1, p+1)
            else:
                return False

        return dfs(0, 0)