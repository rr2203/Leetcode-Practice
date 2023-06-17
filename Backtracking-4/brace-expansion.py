# TC: O(nlogn+k^m) | SC: O(n+k^m)
class Solution:
    def expand(self, s: str) -> List[str]:
        n = len(s)
        #preprocess
        s2 = []
        i = 0
        while i < n:
            if s[i].isalpha():
                s2.append(s[i])
                i+=1
            elif s[i] == '{':
                idx = s.find('}', i+1)
                substr = s[i+1:idx].split(',')
                s2.append(sorted(list(substr)))
                i = idx+1


        #backtrack
        curstr = []
        result = []
        def dfs(i):
            nonlocal curstr, result

            if i == len(s2):
                result.append("".join(curstr))
                return

            if str(s2[i]).isalpha():
                curstr.append(s2[i])
                dfs(i+1)
                curstr.pop()
            else:
                for c in s2[i]:
                    curstr.append(c)
                    dfs(i+1)
                    curstr.pop()

        dfs(0)
        return result