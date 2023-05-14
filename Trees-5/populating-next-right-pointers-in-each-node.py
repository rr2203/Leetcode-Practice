# Sol1: Optimized level order traversal
# TC: O(n) | SC: O(1)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head = root
        while root and root.left:
            levelRoot = root
            while levelRoot:
                levelRoot.left.next = levelRoot.right
                if levelRoot.next: levelRoot.right.next = levelRoot.next.left
                levelRoot = levelRoot.next
            root = root.left

        return head
    
# Sol2: DFS
# TC: O(n) | SC: O(h)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root

        def dfs(left, right):
            if not left: return
            left.next = right
            dfs(left.left, left.right)
            dfs(left.right, right.left)
            dfs(right.left, right.right)

        left, right = root.left, root.right
        dfs(left, right)
        return root