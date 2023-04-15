#TC: O(m*n*(3^l))
#SC: O(l)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        boardset=set()
        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                boardset.add(board[i][j])
        for c in word: 
            if c not in boardset: return False

        def backtrack(i,j,k):
            nonlocal board,word,dirs,m,n
            if k==len(word): return True
            if i<0 or j<0 or i>=m or j>=n: return False

            if board[i][j]==word[k]:
                cur=board[i][j]
                board[i][j]='.'
                for dr,dc in dirs:
                    if backtrack(i+dr,j+dc,k+1):
                        return True
                board[i][j]=cur

            return False

        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0): return True

        return False