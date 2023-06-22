# TC: O(log(N)) | SC: O(logN)
class Solution:
    def confusingNumberII(self, n: int) -> int:

        options = ['0', '1', '6', '8', '9']
        ans = set()

        def isConfusingNumber(x):
            if not x: return False
            x = str(int(x))
            rotatedX = ""
            for c in x:
                if c == '6': rotatedX += '9'
                elif c == '9': rotatedX += '6'
                else: rotatedX += c
            rotatedX = rotatedX[::-1]
            
            return int(x) != int(rotatedX)

        def dfs(x):
            nonlocal ans
            if x and (int(x) > n or len(x) > 10): return
            if isConfusingNumber(x):    
                ans.add(int(x))

            for digit in options:   
                dfs(x+digit)

        for i in options[1:]:
            dfs(str(i))
        return len(ans)