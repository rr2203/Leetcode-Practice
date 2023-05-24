# BFS
# Time Complexity: O(m*n) | Space Complexity: O(m*n)
from collections import deque
class Solution:
    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        dirs = [(0,1),(1,0), (0, -1), (-1, 0)]
        q = deque([start])
        maze[start[0]][start[1]] = 2

        while q:
            r, c = q.popleft()
            if [r,c] == destination: return True

            for dx, dy in dirs:
                i, j = r, c
                # roll the ball
                while 0 <= i < m and 0 <= j < n and maze[i][j] != 1:
                    i += dx
                    j += dy
                # bring back to stop point
                i -= dx
                j -= dy

                if maze[i][j] != 2:
                    q.append([i, j])
                    maze[i][j] = 2

        return False

# DFS
# TC: O(m*n) | SC: O(m*n)
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(x, y):
            nonlocal maze, m, n, start, destination, dirs
            if [x, y] == destination: 
                return True
            if maze[x][y] == 2: return False
            # mutated the input to use as visited array in order to save space
            maze[x][y] = 2

            for dx, dy in dirs:
                nx, ny = x, y
                while 0<=nx<m and 0<=ny<n and maze[nx][ny] != 1:
                    nx += dx
                    ny += dy
                nx -= dx
                ny -= dy
                if 0<=nx<m and 0<=ny<n and dfs(nx, ny): return True

            return False

        return dfs(start[0], start[1])