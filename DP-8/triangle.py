# TC: O(n^2) | SC: O(n^2)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(maxsize = None)
        def recurse(i, r):
            if r == len(triangle):  return 0
            return triangle[r][i] + min(recurse(i, r+1), recurse(i+1, r+1))

        return recurse(0, 0)