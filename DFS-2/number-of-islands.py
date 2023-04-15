#DFS: O(m*n)
#BFS: O(m*n)
dirs=[(0,-1),(-1,0),(1,0),(0,1)]
def dfs(grid, i, j, m, n):
    grid[i][j]="0"
    for dir in dirs:
        ni,nj=i+dir[0],j+dir[1]
        if 0<=ni<m and 0<=nj<n and grid[ni][nj]=="1":
            dfs(grid,ni,nj,m,n)
    

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        islands=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    islands+=1
                    dfs(grid,i,j,m,n)
        return islands