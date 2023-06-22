# TC: O(k*(n+m)) | SC: O(1)
class Solution:
    def camelMatch(self, q: List[str], p: str) -> List[bool]:
        for i in range(len(q)):
            s = q[i]

            sp = pp = 0
            match = True
            while pp < len(p):
                if sp < len(s) and s[sp] == p[pp]:
                    sp +=1 
                    pp += 1
                elif sp < len(s) and s[sp].islower():
                    sp += 1
                else:
                    match = False
                    break

            match &= all(c.islower() for c in s[sp:])
            q[i] = match

        return q