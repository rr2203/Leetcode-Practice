# TC: O(2^N) | SC: O(N)
from collections import deque

def isValid(s):
    if not s: return True

    openBrackets = 0
    for c in s:
        if c == '(':
            openBrackets += 1
        elif c == ')':
            openBrackets -= 1
            if openBrackets < 0: return False

    return openBrackets == 0

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        bfsq = deque()
        memo = set()
        ans = []

        bfsq.append(s)
        while bfsq:
            curStr = bfsq.popleft()
            if isValid(curStr):
                ans.append(curStr)

            if not ans:
                for i in range(len(curStr)):
                    if not curStr[i].isalpha(): 
                        childStr = curStr[:i]+curStr[i+1:]
                        if childStr not in memo:
                            memo.add(childStr)
                            bfsq.append(childStr)

        return ans