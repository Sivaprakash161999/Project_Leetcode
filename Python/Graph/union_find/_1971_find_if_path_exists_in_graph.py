from typing import List
from collections import defaultdict, deque
import heapq


class Solution:

    # dfs - O(n+e)
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(u):
            if u == destination:
                return True
            visited.add(u)
            path = False
            for v in graph[u]:
                if v not in visited:
                    path |= dfs(v)
                    if path:
                        return True
            return False
        return dfs(source)


    # bfs
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        queue = deque([source])
        visited = set([source])
        while queue:
            u = queue.popleft()
            if u == destination:
                return True
            for v in graph[u]:
                if v in visited:
                    continue
                visited.add(v)
                queue.append(v)
        return False
                
                
    # Union Find
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        rank = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx != rooty:
                if rank[rootx] > rank[rooty]:
                    parent[rooty] = rootx
                elif rank[rootx] < rank[rooty]:
                    parent[rootx] = rooty
                else:
                    parent[rooty] = rootx
                    rank[rootx] += 1
        for u, v in edges:
            union(u, v) 
        return find(source) == find(destination)


    # Djikstra's shortes path
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        distances = {node: float('inf') for node in range(n)}
        distances[source] = 0
        priority_queue = [(0, source)]
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_node == destination:
                return True
            if current_distance > distances[current_node]:
                continue
            for neighbour in graph[current_node]:
                distance = current_distance + 1
                if distance < distances[neighbour]:
                    distances[neighbour] = distance
                    heapq.heappush(priority_queue, (distance, neighbour))
        return False
        





        