from typing import List
from collections import deque


class Solution:
    # dfs - (m*n) time; O(m*n) space
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                or grid[r][c] == 0):
                return 1
            if (r, c) in visited:
                return 0
            
            visited.add((r, c))
            walls = 0    
            walls += dfs(r + 1, c)
            walls += dfs(r - 1, c)
            walls += dfs(r, c + 1)
            walls += dfs(r, c - 1)
            return walls
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)
                

    # dfs - recursive
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        stack = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    stack.append((r, c))
                    visited.add((r, c))
                    break
        inrange = lambda x, y: x < 0 or x >= ROWS or y < 0 or y >= COLS
        walls = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while stack:
            r, c = stack.pop()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inrange(nr, nc):
                    walls += 1
                elif grid[nr][nc] == 0:
                    walls += 1
                elif (nr, nc) in visited:
                    continue
                else:
                    visited.add((nr, nc))
                    stack.append((nr, nc))
        return walls
    

    # bfs
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        perimeter = 0
        visited = set()
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    queue.append((r, c))
                    visited.add((r, c))
                    break
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited:
                    continue
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or not grid[nr][nc]:
                    perimeter += 1
                else:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return perimeter
    

    # optimized - O(n*m) time; O(1) space
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        perimeter = 0
        for i, row in enumerate(grid):
            for j, cl in enumerate(row):
                if not cl:
                    continue
                if not j or not row[j - 1]:
                    perimeter += 2
                if not i or not grid[i - 1][j]:
                    perimeter += 2
        return perimeter
                
                


        