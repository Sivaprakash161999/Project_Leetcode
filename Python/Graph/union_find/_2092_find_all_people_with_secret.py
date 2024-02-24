from collections import defaultdict, deque
from typing import List


class Solution:
    # BFS - Time: O((M+N).M); Space: O(M+N)
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Fort every person, store the time and label of the person they meet.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))
        
        # Earliest time at which a person learned the secret
        # as per current state of knowledge. If due to some new info,
        # the earliest time of knowing the secret changes, we will update
        # it and again process all the people whom he/she meets after the 
        # time at which he/she learned the secret.
        earliest = [float('inf')] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        # Queue for BFS. It will store (person, time of knowing the secret)
        q = deque()
        q.append((0, 0))
        q.append((firstPerson, 0))

        # Do BFS
        while q:
            person, time = q.popleft()
            for t, next_person in graph[person]:
                if t >= time and earliest[next_person] > t:
                    earliest[next_person] = t
                    q.append((next_person, t))
        
        # Since we visited only those people who know the secret, 
        # we need to return the indices of all visited people.
        return [i for i in range(n) if earliest[i] != float('inf')]

    # DFS using stacks - Time: O((M+N).M); Space: O(M+N)
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        earliest = [float('inf')] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        # Stack for DFS. It will store (person, time of knowing the secret)
        stack = [(0, 0), (firstPerson, 0)]

        # Do DFS
        while stack:
            person, time = stack.pop()
            for t, next_person in graph[person]:
                if t >= time and earliest[next_person] > t:
                    earliest[next_person] = t
                    stack.append((next_person, t))
        return [i for i in range(n) if earliest[i] != float('inf')]
        