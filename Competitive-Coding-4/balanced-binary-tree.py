#TC: O(n)
#SC: O(height of tree)
class Solution:
    def isBalancedHelper(self, root):
        if not root:
            return True, 0

        is_bal_left,h_left=self.isBalancedHelper(root.left)
        is_bal_right,h_right=self.isBalancedHelper(root.right)
        is_bal=is_bal_left and is_bal_right and abs(h_left-h_right)<=1
        h = 1 + max(h_left,h_right)
        return is_bal,h

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root)[0]