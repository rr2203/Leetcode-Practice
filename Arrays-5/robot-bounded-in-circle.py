# TC: O(n) | SC: O(1)
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        idx = 0
        x,y = 0,0
        for i in instructions:
            if i == "L":
                idx = (idx + 1) % 4
            elif i == "R":
                idx = (idx - 1) % 4
            else:
                dx, dy = dirs[idx]
                x += dx
                y += dy
        return (x == 0 and y == 0) or idx != 0