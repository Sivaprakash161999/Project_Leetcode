from collections import deque
from typing import List


class Solution:
    # bfs
    def openLock(self, deadends: List[str], target: str) -> int:
        nums = '0123456789'
        graph = {num:[] for num in nums}
        for i in range(10):
            graph[nums[i]].append(nums[(i + 1) % 10])
            graph[nums[i]].append(nums[i - 1])
        # print(graph)
        q = deque()
        q.append('0000')
        visit = set()
        visit.add('0000')
        dead_ends = set(deadends)
        if '0000' in dead_ends:
            return -1
        moves = 0
        while q:
            level = len(q)
            for _ in range(level):
                cur = q.popleft()
                if cur == target:
                    return moves
                for i in range(4):
                    for nei in graph[cur[i]]:
                        new = cur[:i] + nei + cur[i + 1:]
                        if new not in visit and new not in dead_ends:
                            q.append(new)
                            visit.add(new)
            moves += 1
        return -1

    # bfs
    def openLock(self, deadends: List[str], target: str) -> int:
        def children(comb):
            res = []
            for i in range(4):
                c = str((int(comb[i]) + 1) % 10)
                new = comb[:i] + c + comb[i + 1:]
                res.append(new)
                c = str((int(comb[i]) - 1 + 10) % 10)
                new = comb[:i] + c + comb[i + 1:]
                res.append(new)
            return res

        q = deque()
        q.append(['0000', 0]) # [combination, moves(or)level in bfs]
        visit = [0] * 10000
        for end in deadends:
            visit[int(end)] = 1 # we can add the deadends in visit as well
        if visit[0]: # edge case where '0000' is in deadend
            return -1
        visit[0] = 1
        while q:
            comb, moves = q.popleft()
            if comb == target:
                return moves
            for child in children(comb):
                if not visit[int(child)]: # not visited
                    visit[int(child)] = 1 # mark as visited
                    q.append([child, moves + 1])
        return -1

            

