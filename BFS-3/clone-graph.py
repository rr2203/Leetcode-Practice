# TC: O(V+E) | SC: O(V+E)
class Solution:
    def cloneGraph(self, firstNode: 'Node') -> 'Node':
        if not firstNode: return None

        nodeMap = {}
        def dfs(originalNode, cloneNode):
            nonlocal nodeMap

            nodeMap[originalNode.val] = cloneNode
            for neighbor in originalNode.neighbors:
                if neighbor.val in nodeMap:
                    cloneNode.neighbors.append(nodeMap[neighbor.val])
                else:
                    newCloneNode = Node(neighbor.val)
                    cloneNode.neighbors.append(newCloneNode)
                    dfs(neighbor, newCloneNode)


        firstCloneNode = Node(1)
        dfs(firstNode, firstCloneNode)

        return firstCloneNode