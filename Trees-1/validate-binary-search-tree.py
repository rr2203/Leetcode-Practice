#TC: O(n)
#SC: O(height of tree)
class Solution:

    def isValidBSTHelper(self, root,_min,_max):
        if root==None: return True
        if (root.val<=_min or root.val>=_max 
            or not self.isValidBSTHelper(root.left,_min,root.val) 
                or not self.isValidBSTHelper(root.right,root.val,_max)): 
            return False

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root,-2**31-1,2**31+1)
