from collections import deque, defaultdict
from typing import List


class Solution:
    #Bellmen-Ford Shortest Path - Algorithm ( it is DP)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''This algorithms keeps track of the cheapest 
            price from src to every other nodes'''
        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k + 1): # for atmost k stops
            temp = prices.copy()
            for sr, dt, p in flights: # source, destination, price
                if prices[sr] == float('inf'): # source is not reachable
                    continue
                if prices[sr] + p < temp[dt]:
                    temp[dt] = prices[sr] + p
            prices = temp
        return -1 if prices[dst] == float('inf') else prices[dst]

    # BFS
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for sc, dt, price in flights:
            adj[sc].append((dt, price))
        
        dist = [float('inf')] * n
        dist[src] = 0

        q = deque()
        q.append((src, 0))
        stops = 0

        while q and stops <= k:
            sz = len(q)
            for _ in range(sz):
                node, distance = q.popleft()
                if node not in adj: 
                    continue
                for neighbour, price in adj[node]:
                    if price + distance >= dist[neighbour]:
                        continue
                    dist[neighbour] = price + distance
                    q.append((neighbour, dist[neighbour]))
            stops += 1
        return dist[dst] if dist[dst] != float('inf') else -1
        