from typing import List


class Solution:
    # simulation - O(r*c) time; O(1) space
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        maxLocal = [[-1] * (cols - 2) for _ in range(rows - 2)]


        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                cur_max = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        cur_max = max(cur_max, grid[r + dr][c + dc])
                maxLocal[r - 1][c - 1] = cur_max
        return maxLocal


    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]
        for r in range(n - 2):
            for c in range(n - 2):
                maxLocal[r][c] = max(grid[r][c], grid[r][c + 1], grid[r][c + 2],
                                    grid[r + 1][c], grid[r + 1][c + 1], grid[r + 1][c + 2],
                                    grid[r + 2][c], grid[r + 2][c + 1], grid[r + 2][c + 2])
        return maxLocal