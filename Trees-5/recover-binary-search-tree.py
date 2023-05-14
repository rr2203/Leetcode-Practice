# DFS Inorder
# TC: O(n) | SC: O(h)
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev, first, second = None, None, None

        def inorderDFS(r):
            nonlocal prev,first,second
            if not r: return

            inorderDFS(r.left)

            if prev and prev.val > r.val:
                if not first: first = prev
                second = r
            prev = r

            inorderDFS(r.right)

        inorderDFS(root)
        if first and second: first.val, second.val = second.val, first.val

# DFS using stack
# TC: O(n) | SC: O(h)
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        prev, first, second = None, None, None

        stack = []
        while root or stack:
            while(root): 
                stack.append(root)
                root = root.left

            root = stack[-1]
            stack.pop()

            if prev and prev.val > root.val:
                if not first: first = prev
                second = root
            prev = root


            root = root.right
            


        if first and second: first.val, second.val = second.val, first.val