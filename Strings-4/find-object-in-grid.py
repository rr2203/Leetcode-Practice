# TC: O(log(m) + log(n))
class GFG:
    def __init__(self):
        print("GfG!")

    def get_response(self, grid, row, col):
        # Black box
        pass

    def find_object(self, grid):
        m = len(grid)
        n = len(grid[0])
        top = 0
        left = 0
        bottom = m - 1
        right = n - 1
        column_index = self.binary_search_column(grid, left, right)
        row_index = self.binary_search_row(grid, top, bottom)
        return [row_index, column_index]

    def binary_search_column(self, grid, left, right):
        while left <= right:
            mid = left + (right - left) // 2
            i, j = 0, mid
            if self.get_response(grid, i, j) == 'Exact' or (
                    self.get_response(grid, i, j + 1) != 'Hotter' and self.get_response(grid, i, j - 1) != 'Hotter'):
                return mid
            elif self.get_response(grid, i, j) == 'Hotter':
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def binary_search_row(self, grid, top, bottom):
        while top <= bottom:
            mid = top + (bottom - top) // 2
            i, j = mid, 0
            if self.get_response(grid, i, j) == 'Exact' or (
                    self.get_response(grid, i + 1, j) != 'Hotter' and self.get_response(grid, i - 1, j) != 'Hotter'):
                return mid
            elif self.get_response(grid, i, j) == 'Hotter':
                top = mid + 1
            else:
                bottom = mid - 1
        return -1


gfg = GFG()
