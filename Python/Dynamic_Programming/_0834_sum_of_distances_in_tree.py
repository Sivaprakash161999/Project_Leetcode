from typing import List
from collections import defaultdict


class Solution:
    # DFS - O(n) time; O(n) space
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 1. do a dfs from any arbitrary node
        # lets say 0, dfs will return 
        # (number of nodes in the subtree, sum of distance of the subtree)
        visited = set()
        number_of_subtrees = [0] * n
        sum_of_distance_of_node0 = [0]
        def dfs1(node, curr_distance):
            visited.add(node)
            sum_of_distance_of_node0[0] += curr_distance
            nodes_in_subtree = 1 # current_node
            for neighbour in graph[node]:
                if neighbour not in visited: 
                    nodes_in_subtree += dfs1(neighbour, curr_distance + 1)
            number_of_subtrees[node] = nodes_in_subtree
            return nodes_in_subtree

        # this will give us the number of nodes in subtrees of each node
        # and the sum of distance for node 0
        dfs1(0, 0)

        # array to keep track of our results
        sum_of_distances = [0] * n
        # we will use the sum of distance of node 0,
        # to calculate the sum of distance of other nodes
        # formula:
        # sum of distance of child = (sum of distance of parent) - 
        #                               (number of nodes in subtree of child) +
        #                               (number of nodes other than the subtree of child)

        # this dfs will take 2 parameters,
        # (curr node, sum of distance of current node)
        visited = set()
        def dfs2(node, sum_of_distance):
            visited.add(node)
            # update the sum of distances of the current node
            # in result
            sum_of_distances[node] = sum_of_distance

            for neighbour in graph[node]:
                if neighbour not in visited:
                    # calculate the sum of distance of the neighoubr using
                    # the formula
                    sum_of_distance_of_neighbour = (sum_of_distance
                                                    - number_of_subtrees[neighbour]
                                                    + (n - number_of_subtrees[neighbour]))
                    # recursively call the neighbour
                    # with its sum_of_distance
                    dfs2(neighbour, sum_of_distance_of_neighbour)
        
        dfs2(0, sum_of_distance_of_node0[0])

        return sum_of_distances



        