# TC : O(n^2) | SC : O(n)
from collections import deque
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x : (-x[0],x[1]))
        ans = deque()
        for height, frontNum in people:
            ans.insert(frontNum, [height, frontNum])
        return list(ans)