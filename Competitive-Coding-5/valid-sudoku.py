#TC: O(1) - since size of sudoku is fixed
#SC: O(1) - since size of sudoku is fixed
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=9

        for i in range(n):
            setr=set()
            for j in range(n):
                if board[i][j].isdigit():
                    if board[i][j] in setr: 
                        return False
                    setr.add(board[i][j])

        for j in range(n):
            setc=set()
            for i in range(n):
                if board[i][j].isdigit():
                    if board[i][j] in setc: 
                        return False
                    setc.add(board[i][j])

        for si in range(0,n,3):
            for sj in range(0,n,3):
                setg=set()
                for i in range(si,si+3):
                    for j in range(sj,sj+3):
                        if board[i][j].isdigit() and board[i][j] in setg: 
                            return False
                        setg.add(board[i][j])

        return True