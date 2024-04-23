from collections import deque
from typing import List


class Solution:
    # dfs - TLE O(n**2) time
    # def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    #     graph = defaultdict(list)
    #     for u, v in edges:
    #         graph[u].append(v)
    #         graph[v].append(u)

    #     def height(root):
    #         tree_height = 1
    #         for child in graph[root]:
    #             if child not in visited:
    #                 visited.add(child)
    #                 tree_height = max(tree_height, 1 + height(child))
    #         return tree_height
    #     min_height = float('inf')
    #     min_tree_roots = []
    #     for node in range(n):
    #         visited = set([node])
    #         curr_height = height(node)
    #         # print(curr_height)
    #         if curr_height > min_height:
    #             continue
    #         if curr_height < min_height:
    #             min_height = curr_height
    #             min_tree_roots = []

    #         min_tree_roots.append(node)

    #     return min_tree_roots


    # moving from leaves to the center of tree - wrong(almost correct)
    # def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    #     if n == 1:
    #         return [0]
    #     graph = defaultdict(list)
    #     for u, v in edges:
    #         graph[u].append(v)
    #         graph[v].append(u)
    #     visited = []
    #     for u in graph:
    #         if len(graph[u]) == 1:
    #             visited.append(u)
    #     queue = deque(visited)
    #     visited = set(visited)
    #     seen = len(queue)
    #     while seen != n:
    #         q_len = len(queue)
    #         for i in range(q_len):
    #             node = queue.popleft()
    #             for child in graph[node]:
    #                 if child not in visited:
    #                     visited.add(child)
    #                     seen += 1
    #                     queue.append(child)
    #     return list(queue)


    # reverse traversal from leaf to center - O(n) time
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # Initialize the adjacency list and degree of each node
        adjacency_list = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        # Initialize leaves queue
        leaves = deque([i for i in range(n) if degree[i] == 1])

        # Trim leaves until 2 or fewer nodes remain
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbour in adjacency_list[leaf]:
                    degree[neighbour] -= 1
                    if degree[neighbour] == 1:
                        leaves.append(neighbour)
        return list(leaves)