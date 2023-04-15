#TC: O(m*n)
#SC: O(m*n)
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        bfsq=collections.deque()
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2: bfsq.append((i,j))
                elif grid[i][j]==1: fresh+=1
        if fresh==0: return 0

        time=0
        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        while bfsq:
            level_size=len(bfsq)
            while level_size:
                x,y=bfsq.popleft()
                for dir in dirs:
                    nx,ny=x+dir[0],y+dir[1]
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1: 
                        fresh-=1
                        grid[nx][ny]=2
                        bfsq.append((nx,ny))
                level_size-=1
            if bfsq: time+=1
        
        return -1 if fresh>0 else time