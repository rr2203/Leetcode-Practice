# TC: O(N) | SC: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root: return ""

        bfsq = deque()
        bfsq.append(root)
        ans = ""
        while bfsq:
            curNode = bfsq.popleft()
            if not curNode: 
                ans += "null,"
                continue

            ans += str(curNode.val) + ","
            bfsq.append(curNode.left)
            bfsq.append(curNode.right)

        return ans
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if not data: return None

        data = data.split(',')
        i = 0
        bfsq = deque()
        root = TreeNode(int(data[0]))
        bfsq.append(root)
        while bfsq and i < len(data)-2:
            curNode = data[i]
            curNode = bfsq.popleft()

            i+=1
            if data[i] != 'null':   
                curNode.left = TreeNode(int(data[i]))
                bfsq.append(curNode.left)

            i+=1
            if data[i] != 'null':   
                curNode.right = TreeNode(int(data[i]))
                bfsq.append(curNode.right)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))