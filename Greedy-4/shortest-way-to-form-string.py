# TC: O(MlogN) where M is length of target and N is length of source | SC: O(N)
from bisect import bisect_left
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sourceIdx = defaultdict(list)
        for i in range(len(source)):
            sourceIdx[source[i]].append(i)

        count = 1
        sp, tp = 0, 0
        while tp < len(target):
            c = target[tp]
            if c not in sourceIdx: return -1
            expectedIndex = bisect_left(sourceIdx[c], sp)
            if expectedIndex == len(sourceIdx[c]): 
                sp = sourceIdx[c][0]
                count += 1
            else:
                sp = sourceIdx[c][expectedIndex]
            tp += 1
            sp += 1


        return count