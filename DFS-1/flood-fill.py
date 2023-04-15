#TC: O(m*n)
#SC: O(m*n)

dirs=[(0,1),(1,0),(0,-1),(-1,0)]

def dfs(src,color,grid):
    print(src)
    x,y=src
    original_color=grid[x][y]
    grid[x][y]=color
    for dir in dirs:
        nx,ny=x+dir[0],y+dir[1]
        if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==original_color:
            dfs((nx,ny),color,grid)
    grid[x][y]=color

class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if grid[sr][sc]==color: return grid
        src=(sr,sc)
        dfs(src,color,grid)
        return grid