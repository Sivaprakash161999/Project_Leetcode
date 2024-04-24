


class Solution:
    # dp - O(n) time; O(1) space
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        n_3, n_2, n_1 = 0, 1, 1
        for _ in range(n - 2):
            n_3, n_2, n_1 = n_2, n_1, (n_3 + n_2 + n_1)
        return n_1


    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n <= 2:
            return t[n]
        for _ in range(n - 2):
            t[0], t[1], t[2] = t[1], t[2], sum(t)
        return t[2]
        