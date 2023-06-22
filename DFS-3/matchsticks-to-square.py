# TC: O(4^N) | SC: O(N)
class Solution:
    def makesquare(self, m: List[int]) -> bool:
        perimeter = sum(m)
        if perimeter % 4 != 0: return False
        possibleSide = perimeter / 4

        sums = [0] * 4
        m.sort(reverse=True)
        def f(i):
            nonlocal sums
            if i == len(m):
                return sums[0] == sums[1] == sums[2] == sums[3]
            for j in range(len(sums)): 
                if sums[j] + m[i] <= possibleSide:
                    sums[j] += m[i]
                    if f(i+1): return True
                    sums[j] -= m[i]
            return False

        return f(0)