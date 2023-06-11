# TC: O(N^2) | SC: O(N^2)

from collections import deque

class Solution:
    def __init__(self):
        self.flattenedBoard = []
        self.q = deque([0])
        self.min_moves = 0

    def transform_board(self, board):
        rows, cols = len(board), len(board[0])
        total_cells = rows * cols
        self.flattenedBoard = [0]*total_cells

        i, j, even, counter = rows - 1, 0, 0, 0

        while i >= 0 and j >= 0:
            self.flattenedBoard[counter] = board[i][j] - 1 if board[i][j] != -1 else -1
            counter += 1
            j += 1 if even % 2 == 0 else -1

            if j >= cols or j < 0:
                i -= 1; even += 1
                j = cols - 1 if j >= cols else 0

        self.flattenedBoard[0] = -2

    def bfs(self, total_cells):
        while self.q:
            for _ in range(len(self.q)):
                curr = self.q.popleft()

                if curr == total_cells - 1:
                    return self.min_moves

                for step in range(1, 7):
                    child = step + curr
                    if child < total_cells and self.flattenedBoard[child] != -2:
                        next_move = self.flattenedBoard[child] if self.flattenedBoard[child] > -1 else child
                        self.q.append(next_move)
                        self.flattenedBoard[child] = -2

            self.min_moves += 1

        return -1

    def snakesAndLadders(self, board):
        if board is None or len(board) == 0:
            return 0

        self.transform_board(board)
        total_cells = len(board) * len(board[0])

        return self.bfs(total_cells)
