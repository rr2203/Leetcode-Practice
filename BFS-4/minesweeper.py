# TC: O(m*n) | SC: O(m*n)
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        if board[click[0]][click[1]] == 'M':
                board[click[0]][click[1]] = 'X'
                return board
        
        dirs = [(0, 1),(0, -1),(1, 1),(1, -1),(-1, 1),(-1, -1),(1, 0),(-1, 0)]

        def dfs(i, j):
            nonlocal board
            
            numOfMines = 0
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if 0<=ni<len(board) and 0<=nj<len(board[0]) and board[ni][nj][0] == 'M':    numOfMines += 1
            
            if numOfMines>0:
                board[i][j] = str(numOfMines)
            else:
                board[i][j] = 'B'
                for di, dj in dirs:
                    ni, nj = i+di, j+dj
                    if 0<=ni<len(board) and 0<=nj<len(board[0]) and board[ni][nj] == 'E':    dfs(ni, nj)

        dfs(click[0], click[1])
        return board