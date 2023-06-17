# TC: O(N) | SC: O(1)
class Solution:
    def check(self, x, a, b, n):
        arot, brot = 0, 0
        for i in range(n):
            if a[i] != x and b[i] != x: return -1
            elif a[i] != x: arot += 1
            elif b[i] != x: brot += 1
        return min(arot, brot)

    def minDominoRotations(self, A, B):
        rot = self.check(A[0], A, B, len(A))
        if rot != -1 or A[0] == B[0]:   return rot
        else:   return self.check(B[0], A, B, len(A))