class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count=0

        for row in grid:
            for value in row:
                if value < 0:
                    count+=1
        return count