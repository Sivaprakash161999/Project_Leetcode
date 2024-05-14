from typing import List


class Solution:
    # backtracking - O(m, n)
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def backtrack(r, c):
            if (r < 0 or c < 0 
                or r >= rows or c >= cols
                or grid[r][c] == 0
                or (r, c) in visited):
                return 0
            
            visited.add((r, c))
            golds = grid[r][c] + max(backtrack(r - 1, c),
                                    backtrack(r + 1, c),
                                    backtrack(r, c - 1),
                                    backtrack(r, c + 1))
            visited.remove((r, c))
            return golds

        max_gold = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    visited = set()
                    max_gold = max(max_gold, backtrack(r, c))
        return max_gold


    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def backtrack(r, c):
            if (r < 0 or c < 0 
                or r >= rows or c >= cols
                or grid[r][c] == 0):
                return 0
            
            origin = grid[r][c]
            grid[r][c] = 0
            golds = origin + max(backtrack(r - 1, c),
                                    backtrack(r + 1, c),
                                    backtrack(r, c - 1),
                                    backtrack(r, c + 1))
            grid[r][c] = origin
            return golds

        max_gold = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    max_gold = max(max_gold, backtrack(r, c))
        return max_gold

        