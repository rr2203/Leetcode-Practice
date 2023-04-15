#TC: O(n)
#SC: O(n)

#BFS Solution (can be done via DFS as well)
import collections
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        bfsq = collections.deque()
        bfsq.append(root)

        ans=[]
        while bfsq:
            level_size=len(bfsq)
            curmax = -float('inf')
            while level_size:

                cur_node = bfsq.popleft()
                
                curmax = max(curmax, cur_node.val)

                if cur_node.left: bfsq.append(cur_node.left)
                if cur_node.right: bfsq.append(cur_node.right)
                level_size-=1
            ans.append(curmax)
        return ans