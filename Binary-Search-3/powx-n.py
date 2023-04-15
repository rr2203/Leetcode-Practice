#TC: O(lgn)
#SC: O(lgn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        print(n)
        if n==0: return 1
        result = self.myPow(x, int(n/2))
        if n%2==0: return result*result
        elif n<0: return result*result*(1/x)
        else: return result*result*x