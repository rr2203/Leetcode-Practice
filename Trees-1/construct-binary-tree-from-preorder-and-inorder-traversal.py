#TC: O(n)
#SC: O(n)
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def recurse(in_st,in_end):
            if in_st>in_end: return None

            nonlocal preorder,inorder,root_idx
            root_idx+=1
            cur_root_val=preorder[root_idx]
            inorder_idx=inorder_index_mp[cur_root_val]

            return TreeNode(cur_root_val,
                recurse(in_st,inorder_idx-1),
                recurse(inorder_idx+1,in_end))


        root_idx=-1
        inorder_index_mp={val:i for i,val in enumerate(inorder)}
        return recurse(0,len(inorder)-1)