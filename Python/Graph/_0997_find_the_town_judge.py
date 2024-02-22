from typing import List


class Solution:
    # Graph - indegree vs outdegree; time - O(n) space - O(n)
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''The judge will have an indegree of n-1
            and out-degree of 0;
            so cummulative in-out degree is n-1'''
        in_out_bound = [0] * (n + 1)
        for f, t in trust:
            in_out_bound[f] -= 1
            in_out_bound[t] += 1
        for i in range(1, n + 1):
            if in_out_bound[i] == n - 1:
                return i
        return -1
        