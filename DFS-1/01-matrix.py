#TC: O(m*n)
#SC: O(1)
import collections
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        bfsq=collections.deque()
        onecount=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0: bfsq.append((i,j))
                elif mat[i][j]==1: 
                    mat[i][j]=-1
                    onecount+=1

        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        level=1
        while bfsq:
            x,y=bfsq.popleft()
            for dir in dirs:
                nx,ny=x+dir[0],y+dir[1]
                if 0<=nx<m and 0<=ny<n and mat[nx][ny]==-1:
                    mat[nx][ny]=mat[x][y]+1
                    onecount-=1
                    if onecount==0: return mat
                    bfsq.append((nx,ny))
            level+=1

        return mat