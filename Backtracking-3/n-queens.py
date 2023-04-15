#TC: O(n!)
#SC: O(n^2)
def is_valid(board,n,row,col):
    for j in range(col,-1,-1):
        if board[row][j] == 'Q': return False
    i,j=row,col
    while i>=0 and j>=0:
        if board[i][j] == 'Q': return False
        i-=1; j-=1
    i,j=row,col
    while i<n and j>=0:
        if board[i][j] == 'Q': return False
        i+=1; j-=1

    return True

ans=[]    
def backtrack(col,board,n):
    global ans
    if col==n:
        ans.append(["".join(r) for r in board])
        return

    for i in range(n):
        if is_valid(board,n,i,col): 
            board[i][col]='Q'
            backtrack(col+1,board,n)
            board[i][col]='.'

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n)]
        global ans
        ans=[]
        backtrack(0,board,n)
        return ans