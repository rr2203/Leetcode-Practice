#TC: O(n)
#SC: O(n)
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        bfsq=collections.deque()
        if root: bfsq.append(root)
        ans=[]
        while bfsq:
            cur_level_nodes=[]
            cur_level_size=len(bfsq)
            while cur_level_size:
                cur_node=bfsq.popleft()
                cur_level_nodes.append(cur_node.val)
                if cur_node.left: bfsq.append(cur_node.left)
                if cur_node.right: bfsq.append(cur_node.right)
                cur_level_size-=1
            ans.append(cur_level_nodes)

        return ans

#DFS
#TC: O(n)
#SC: O(lgn)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(cur_root, level):
            if not cur_root: return
            nonlocal ans
            if level+1>len(ans): ans.append([])
            ans[level].append(cur_root.val)
            dfs(cur_root.left, level+1)
            dfs(cur_root.right, level+1)
        ans=[]
        dfs(root,0)
        return ans

        