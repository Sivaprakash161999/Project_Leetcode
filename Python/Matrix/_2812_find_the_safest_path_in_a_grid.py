from collections import deque
import heapq
from typing import List


class Solution:

    # multisource bfs + backtracking - TLE
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        safe = [[0] * cols for _ in range(rows)]
        queue = deque()
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    visited.add((r, c))
                    queue.append((r, c))
        step = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                safe[cr][cc] = step
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if (nr < 0 or nc < 0 
                        or nr >= rows or nc >= cols
                        or (nr, nc) in visited):
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
            step += 1

        if safe[0][0] == 0 or safe[rows - 1][cols - 1] == 0:
            return 0

        res = [0]
        def dfs(r, c, mi):
            if (r, c) == (rows - 1, cols - 1):
                res[0] = max(res[0], min(mi, safe[r][c]))
                return
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or safe[r][c] == -1):
                return
            cell = safe[r][c]
            safe[r][c] = -1
            mi = min(mi, cell)
            for dr, dc in directions:
                dfs(r + dr, c + dc, mi)
            safe[r][c] = cell
        dfs(0, 0, safe[0][0])
        return res[0]


    # multi-source bfs + binary search - O(n^2logn) time; O(n^2) space
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def is_valid_cell(r: int, c:int) -> bool:
            return 0 <= r < n and 0 <= c < n

        # bfs for finding the minimum manhattan distance for 
        # each cell from a thief
        queue = deque()
        for r in range(n):
            for c in range(n):
                # if a thief is present in the cell
                # add the cell to the queue
                # set the distance as zero for that cell
                if grid[r][c] == 1:
                    queue.append((r, c))
                    grid[r][c] = 0
                # else make the cell as unvisited for bfs
                else:
                    grid[r][c] = -1
        # calculate the safeness factor using multi-source bfs
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    val = grid[r][c]
                    # check if the cell is valid and unvisited
                    if is_valid_cell(nr, nc) and grid[nr][nc] == -1:
                        grid[nr][nc] = val + 1
                        queue.append((nr, nc))

        def is_valid_safeness(val: int) -> bool:
            # Check if the source and destination cells satisfy mimimum safeness
            if grid[0][0] < val or grid[n-1][n-1] < val:
                return False
            
            # bfs to find path between source and destination
            # which has a minimum safeness >= val
            queue = deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            while queue:
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return True # valid path
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    # check if neighbour cell is valid and unvisited
                    if (is_valid_cell(nr, nc) 
                        and not visited[nr][nc] and grid[nr][nc] >= val):
                        visited[nr][nc] = True
                        queue.append((nr, nc))
            return False # not valid path

        
        # Binary Search for maximum safeness factor
        start, end, res = 0, 0, -1
        for i in range(n):
            for j in range(n):
                # set end as the maximum safeness factor possible
                end = max(end, grid[i][j])

        # Binary Search
        while start <= end:
            mid = start + (end - start) // 2
            if is_valid_safeness(mid):
                res = max(res, mid)
                start = mid + 1
            else:
                end = mid - 1
        return res


    # multi-source bfs + greedy (Dijkstra's)
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def is_valid_cell(r: int, c: int) -> bool:
            return 0 <= r < n and 0 <= c < n

        # multi-source bfs to find the safeness factor of each cell
        queue = deque()
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    grid[r][c] = 0
                else:
                    grid[r][c] = -1
        
        # bfs
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for d in directions:
                    nr, nc = r + d[0], c + d[1]
                    val = grid[r][c]
                    if is_valid_cell(nr, nc) and grid[nr][nc] == -1:
                        grid[nr][nc] = val + 1
                        queue.append((nr, nc))

        # Dijkstra's to greedily select the next cell
        # in the path with highest 'safeness';
        # so the overall minimum of the path will be highest

        # pq -> [maximum_safeness_till_now, x-coordinate, y-coordinate]
        pq = [(-grid[0][0], 0, 0)]
        grid[0][0] = -1 # Mark the source cell as visited

        # BFS to find the path with maximum safeness factor
        while pq:
            safeness, i, j = heapq.heappop(pq)
            # If reached the destination, return the safeness factor
            if i == n - 1 and j == n - 1:
                return -safeness
            
            # check neighbour cells
            for d in directions:
                di,  dj = i + d[0], j + d[1]
                # check if neighbour cell is valid and unvisited
                if is_valid_cell(di, dj) and grid[di][dj] != -1:
                    heapq.heappush(pq, (-min(-safeness, grid[di][dj]), di, dj))
                    grid[di][dj] = -1
        return -1
        



                
        