#DFS Solution
#TC: O(n)
#SC: O(n)
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(cur_root, level, parent_val):
            if not cur_root: return
            nonlocal x,y,hx,hy,px,py
            if cur_root.val==x: 
                hx=level; px=parent_val
            if cur_root.val==y: 
                hy=level; py=parent_val
            if px==-1 or py==-1:
                dfs(cur_root.left,level+1,cur_root.val)
                dfs(cur_root.right,level+1,cur_root.val)

        hx,px,hy,py=-1,-1,-1,-1
        dfs(root,0,-1)
        print(hx,hy,px,py)
        return hx==hy and px!=py

#BFS Solution
#TC: O(n)
#SC: O(n)
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root: return False
        bfsq=deque()
        bfsq.append(root)
        while bfsq:
            level_size=len(bfsq)
            x_found,y_found=False,False
            while level_size:
                curnode=bfsq.popleft()
                if curnode.val==x: x_found=True
                if curnode.val==y: y_found=True
                if curnode.left and curnode.right:
                    if (curnode.left.val==x and curnode.right.val==y) or (curnode.left.val==y and curnode.right.val==x):
                        return False
                if curnode.left: bfsq.append(curnode.left)
                if curnode.right: bfsq.append(curnode.right)
                level_size-=1
            if x_found and y_found: return True
            elif x_found or y_found: return False
        
        return False