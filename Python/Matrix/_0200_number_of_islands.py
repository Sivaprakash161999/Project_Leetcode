from typing import List
from collections import deque


class Solution:
    # dfs recursive - O(n*m) time; O(n*m) space
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS
                or (r, c) in visited or grid[r][c] == "0"):
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands


    # dfs iterative - O(n*m) time; O(n*m) space
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        stack = []
        def dfs():
            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr == ROWS or nc < 0 or nc == COLS
                        or grid[nr][nc] == "0" or (nr, nc) in visited):
                        continue
                    visited.add((nr, nc))
                    stack.append((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    stack.append((r, c))
                    dfs()
        return islands


    # bfs - O(n*m) time; O(n*m) space
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        def bfs():
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr == ROWS or nc < 0 or nc == COLS
                        or (nr, nc) in visited or grid[nr][nc] == "0"):
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    queue.append((r, c))
                    bfs()
        return islands


    # Union Find - O(n*m) time; (n*m) space
    def numIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cell_map = {}
        idx = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    cell_map[(r, c)] = idx
                    idx += 1

        uf = UnionFind(idx) # initiate the Union Find with idx number of "1"
        for r in range(ROWS):
            for c in range(COLS):
                # if 2 consecutive horizontal or vertical cells have
                # "1", union them into single island and reduce the
                # total islands count by 1
                if r > 0 and grid[r][c] == "1" and grid[r - 1][c] == "1":
                    uf.union(cell_map[(r, c)], cell_map[(r - 1, c)])
                if c > 0 and grid[r][c] == "1" and grid[r][c - 1] == "1":
                    uf.union(cell_map[(r, c)], cell_map[(r, c - 1)])

        return uf.size



class UnionFind:
    def __init__(self, n):
        self.size = n # initially consider there are n islands each representing "1"
        self.parent = [i for i in range(n)] # each island is the parent of their own

    def union(self, x, y):
        # find the parent of two islands
        p1, p2 = self.find(x), self.find(y)
        if p1 != p2: # combine them into a single island, if the parents are different
            self.parent[p2] = p1
            self.size -= 1 # reduce the total count of islands by 1
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x




        