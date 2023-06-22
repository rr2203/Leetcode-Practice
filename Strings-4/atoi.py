# TC: O(n) | SC: O(1)
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        isNeg = s[0] == '-'
        if s[0] in ['+', '-']: s = s[1:]

        num = 0
        for c in s:
            if not c.isnumeric(): break
            num = 10*num + int(c)
            if num > (2**31):
                break
            
        if isNeg: return max(-2**31, -num)
        else: return min(2**31 - 1, num)