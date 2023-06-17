# TC: O(V+E) | SC: O(V+E)
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        # Create Adjacency List
        neighbours = defaultdict(list)
        for u,v in connections:
            neighbours[u].append(v)
            neighbours[v].append(u)

        # print(neighbours)
        
        # Tarjans Algo
        time = 0
        disc = [-1] * n
        low = [n] * n
        bridges = []

        def dfs(parent, curNode):
            nonlocal time, disc, low, bridges, neighbours
            if disc[curNode] != -1: return
            
            disc[curNode] = time
            low[curNode] = time
            
            time += 1

            for neighbour in neighbours[curNode]:
                if disc[neighbour] == -1:
                    dfs(curNode, neighbour)
                    low[curNode] = min(low[curNode], low[neighbour])
                    if low[neighbour] > disc[curNode]:
                        bridges.append([curNode, neighbour])
                elif neighbour != parent:
                    low[curNode] = min(low[curNode], low[neighbour])


        dfs(-1, 0)
        # print(disc, low, neighbours)
        return bridges