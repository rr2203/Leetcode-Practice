#DFS Solution:
# TC: O(n)
# SC: O(n)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(curroot,level):
            if not curroot: return
            nonlocal ans
            if len(ans)==level: ans.append(curroot.val)
            dfs(curroot.right,level+1)
            dfs(curroot.left,level+1)
        ans=[]
        dfs(root,0)
        return ans
        
#BFS Solution:
# TC: O(n)
# SC: O(n)
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        bfsq=deque()
        bfsq.append(root)
        ans=[]
        while bfsq:
            level_size=len(bfsq)
            while level_size:
                cur_node=bfsq.popleft()
                if level_size==1: ans.append(cur_node.val)
                if cur_node.left: bfsq.append(cur_node.left)
                if cur_node.right: bfsq.append(cur_node.right)
                level_size-=1
        return ans