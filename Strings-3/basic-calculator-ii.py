"""
TC: O(n)
SC: O(1)
"""
class Solution:
    def calculate(self, s: str) -> int:
        calc,num,tail,lastSign = 0,0,0,'+'

        for i,c in enumerate(s):
            if c.isdigit():
                num = num*10 + int(c)
            if not (c.isdigit() or c==' ') or i==len(s)-1:
                if lastSign == '+':
                    calc += num
                    tail = num
                elif lastSign == '-':
                    calc += -num
                    tail = -num
                elif lastSign == '*':
                    calc -= tail    #revert previous action
                    calc += tail*num    #use previous module to handle operator precedence
                    tail = tail*num
                elif lastSign == '/':
                    calc -= tail
                    calc += int(tail/num)
                    tail = int(tail/num)
                
                num = 0
                lastSign = c

        return calc