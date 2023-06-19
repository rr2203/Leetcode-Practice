# Two Pointers Greedy Approach
# TC: O(m+n) | SC: O(1)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sp = pp = 0
        sstar = pstar = -1

        while sp < len(s):
            if pp < len(p) and p[pp] in [s[sp], '?']:
                sp += 1
                pp += 1
            elif pp < len(p) and p[pp] == '*':
                pstar = pp
                sstar = sp
                pp += 1
            elif sstar == -1:
                return False
            else:
                pp = pstar
                sstar += 1
                sp = sstar
        
        return all(c == '*' for c in p[pp:])

# TC: O(m*n) | SC: O(m*n)
# Bottom up approach
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        dp = [[False] * (len(p)+1) for _ in range(len(s)+1)]

        for sp in range(len(s), -1, -1):
            for pp in range(len(p), -1, -1):
                if pp == len(p): 
                    dp[sp][pp] = sp == len(s)
                elif sp == len(s): 
                    dp[sp][pp] =  all(c=='*' for c in p[pp:])
                elif p[pp] in ['?', s[sp]]:   
                    dp[sp][pp] =  dp[sp+1][pp+1]
                elif p[pp] == '*':  
                    dp[sp][pp] = dp[sp+1][pp] or dp[sp][pp+1]

        return dp[0][0]

# TC: O(m*n) | SC: O(m*n)
# Top down approach
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(maxsize=None)
        def f(sp, pp):
            if pp == len(p): return sp == len(s)
            if sp == len(s): return all(c=='*' for c in p[pp:])

            if p[pp] in ['?', s[sp]]:   return f(sp+1, pp+1)
            elif p[pp] == '*':  return f(sp+1, pp) or f(sp, pp+1)
            else:   return False

        return f(0,0)