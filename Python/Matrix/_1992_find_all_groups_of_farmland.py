from typing import List
from collections import deque


class Solution:
    # dfs - recursive - (n*m) time; O(n*m) space
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(land), len(land[0])
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                or (r, c) in visited or land[r][c] == 0):
                return
            visited.add((r, c))
            # update the top left and bottom right borders
            farmland[0] = min(farmland[0], r)
            farmland[1] = min(farmland[1], c)
            farmland[2] = max(farmland[2], r)
            farmland[3] = max(farmland[3], c)
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        farmlands = []
        for r in range(ROWS):
            for c in range(COLS):
                if land[r][c] == 1 and (r, c) not in visited:
                    farmland = [r, c, r, c]
                    dfs(r, c)
                    farmlands.append(farmland)
        return farmlands


    # dfs - iterative - (n*m) time; O(n*m) space
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(land), len(land[0])
        visited = set()
        directions = [(1, 0), (0, 1)]
        farmlands = []
        stack = []
        def dfs():
            while stack:
                r, c = stack.pop()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS
                        or (nr, nc) in visited or land[nr][nc] == 0):
                        continue
                    visited.add((nr, nc))
                    farmland[2] = max(farmland[2], nr)
                    farmland[3] = max(farmland[3], nc)
                    stack.append((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if land[r][c] == 1 and (r, c) not in visited:
                    stack.append((r, c))
                    visited.add((r, c))
                    farmland = [r, c, r, c]
                    dfs()
                    farmlands.append(farmland)
        return farmlands


    # bfs - (n*m) time; O(n*m) space
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(land), len(land[0])
        visited = set()
        directions = [(1, 0), (0, 1)]
        farmlands = []
        queue = deque()
        def bfs():
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nr == ROWS or nc < 0 or nc == COLS
                        or (nr, nc) in visited or land[nr][nc] == 0):
                        continue
                    visited.add((nr, nc))
                    farmland[2] = max(farmland[2], nr)
                    farmland[3] = max(farmland[3], nc)
                    queue.append((nr, nc))
        for r in range(ROWS):
            for c in range(COLS):
                if land[r][c] and (r, c) not in visited:
                    queue.append((r, c))
                    visited.add((r, c))
                    farmland = [r, c, r, c]
                    bfs()
                    farmlands.append(farmland)
        return farmlands


    # greedy - (n*m) time; (n*m) space
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(land), len(land[0])
        farmlands = []
        for r in range(ROWS):
            for c in range(COLS):
                if (land[r][c] and (r == 0 or land[r - 1][c] == 0) 
                    and (c == 0 or land[r][c - 1] == 0)):
                    nc = c + 1
                    while nc < COLS and land[r][nc] == 1:
                        nc += 1
                    nc -= 1
                    nr = r + 1
                    while nr < ROWS and land[nr][c] == 1:
                        nr += 1
                    nr -= 1
                    farmlands.append([r, c, nr, nc])
        return farmlands

