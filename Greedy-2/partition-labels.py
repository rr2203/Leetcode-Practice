# TC: O(n) | SC: O(1)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOcc = {}
        for i in range(len(s)):
            lastOcc[s[i]] = i

        partSize = 0
        maxEnd = -1
        ans = []
        for i in range(len(s)):
            maxEnd = max(maxEnd, lastOcc[s[i]])
            partSize += 1
            if i == maxEnd:
                ans.append(partSize)
                partSize = 0
        
        return ans