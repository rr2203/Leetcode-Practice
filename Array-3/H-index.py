# TC: O(n) | SC: O(1)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        freq = [0] * (n+1)
        for c in citations: freq[min(c, n)] += 1
        
        curTotal = 0
        for i in range(n, -1, -1):
            curTotal += freq[i]
            if curTotal >= i:
                return i

        return -1