# TC: O(n) | SC: O(n)
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1: return -1
        indegree, outdegree = [0] * (n + 1), [0] * (n + 1)
        
        for whoTrusts, getsTrusted in trust:
            outdegree[whoTrusts] += 1
            indegree[getsTrusted] += 1
            
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        return -1
    
    