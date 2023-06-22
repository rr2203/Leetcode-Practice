from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        mp = defaultdict(list)
        bfsq = deque()
        bfsq.append((root, 0))
        minLoc, maxLoc = 100, -100
        while bfsq:
            curNode, loc = bfsq.popleft()
            minLoc = min(minLoc, loc)
            maxLoc = max(maxLoc, loc)
            mp[loc].append(curNode.val)
            if curNode.left: bfsq.append((curNode.left, loc-1))
            if curNode.right: bfsq.append((curNode.right, loc+1))

        return [mp[loc] for loc in range(minLoc, maxLoc+1)]