#Iterative Solution
#TC: O(len of output string)
#SC: O(depth of brackets)
from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        s=list(s)
        numstack,curstrstack = deque(),deque()
        num,curstr=0,[]
        i=0
        while i<len(s):
            if s[i].isalpha():
                curstr.append(s[i])
            elif s[i].isdigit():
                num=num*10 + (int(s[i]))
            elif s[i]=='[':
                numstack.append(num); curstrstack.append(curstr)
                num=0; curstr=[]
            elif s[i]==']':
                freq=numstack.pop()
                curstr=(curstrstack.pop()) + freq*curstr
            i+=1

        return "".join(curstr)
        
#Recursive Solution
#TC: O(len of output string)
#SC: O(depth of brackets)from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:

        def decodeStringHelper(s):
            num,curstr=0,[]
            nonlocal i
            while i<len(s):
                if s[i].isalpha():
                    curstr.append(s[i])
                elif s[i].isdigit():
                    num=num*10 + (int(s[i]))
                elif s[i]=='[':
                    i+=1
                    decoded_s=decodeStringHelper(s)
                    curstr=curstr+num*decoded_s
                    num=0
                elif s[i]==']':
                    return curstr
                i+=1

            return curstr
        
        i=0
        s=list(s)
        return "".join(decodeStringHelper(s))
                

